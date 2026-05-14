package handlers

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"sync"
	"time"
)

type MachineSession struct {
	ID        string `json:"id"`
	MachineID string `json:"machine_id"`
	AppName   string `json:"app_name"`
	RepoName  string `json:"repo_name"`
	Status    string `json:"status"`
}

var (
	sessionsMu sync.RWMutex
	sessions   = map[string]*MachineSession{}
	sessionSeq int
)

func flyCmd(args ...string) (string, error) {
	flyPath := os.Getenv("FLY_PATH")
	if flyPath == "" {
		home, _ := os.UserHomeDir()
		flyPath = home + "/.fly/bin/fly"
	}
	cmd := exec.Command(flyPath, args...)
	out, err := cmd.CombinedOutput()
	return strings.TrimSpace(string(out)), err
}

func getAPIToken() (string, error) {
	tok := os.Getenv("FLY_API_TOKEN")
	if tok != "" {
		return strings.TrimSpace(tok), nil
	}
	out, err := flyCmd("auth", "token")
	if err != nil {
		return "", fmt.Errorf("no FLY_API_TOKEN and flyctl auth failed: %w", err)
	}
	return strings.TrimSpace(out), nil
}
func createMachine(appName, image string) (string, error) {
	apiToken, err := getAPIToken()
	if err != nil {
		return "", err
	}

	body := map[string]interface{}{
		"region": env("FLY_REGION", "iad"),
		"config": map[string]interface{}{
			"image": image,
			"guest": map[string]interface{}{
				"cpu_kind":  "shared",
				"cpus":      4,
				"memory_mb": 4096,
			},
			"auto_destroy": true,
		},
	}

	jsonBody, _ := json.Marshal(body)
	url := fmt.Sprintf("https://api.machines.dev/v1/apps/%s/machines", appName)

	req, _ := http.NewRequest("POST", url, bytes.NewReader(jsonBody))
	req.Header.Set("Authorization", "Bearer "+apiToken)
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		b, _ := io.ReadAll(resp.Body)
		return "", fmt.Errorf("create machine failed (%d): %s", resp.StatusCode, string(b))
	}

	var result struct {
		ID string `json:"id"`
	}
	json.NewDecoder(resp.Body).Decode(&result)
	return result.ID, nil
}

func waitMachineStarted(appName, machineID string) error {
	apiToken, err := getAPIToken()
	if err != nil {
		return err
	}

	url := fmt.Sprintf("https://api.machines.dev/v1/apps/%s/machines/%s/wait?state=started&timeout=60", appName, machineID)
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("Authorization", "Bearer "+apiToken)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		b, _ := io.ReadAll(resp.Body)
		return fmt.Errorf("wait failed (%d): %s", resp.StatusCode, string(b))
	}
	return nil
}

func destroyMachine(appName, machineID string) error {
	apiToken, err := getAPIToken()
	if err != nil {
		return err
	}

	url := fmt.Sprintf("https://api.machines.dev/v1/apps/%s/machines/%s?force=true", appName, machineID)
	req, _ := http.NewRequest("DELETE", url, nil)
	req.Header.Set("Authorization", "Bearer "+apiToken)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	return nil
}

func CreateSession(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	var req struct {
		RepoName string `json:"repo_name"`
	}
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}

	appName := env("FLY_APP", "agent-sandbox-lively-leaf-9253")
	image := env("FLY_IMAGE", "registry.fly.io/"+appName+":latest")

	// Create a new machine
	machineID, err := createMachine(appName, image)
	if err != nil {
		http.Error(w, "failed to create machine: "+err.Error(), http.StatusInternalServerError)
		return
	}

	// Wait for it to start
	if err := waitMachineStarted(appName, machineID); err != nil {
		http.Error(w, "machine failed to start: "+err.Error(), http.StatusInternalServerError)
		return
	}

	// Give it a moment to fully boot
	time.Sleep(2 * time.Second)

	// Start tmux with claude
	_, err = flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
		"--command", "bash -c 'tmux new-session -d -s agent claude'")
	if err != nil {
		http.Error(w, "failed to start claude: "+err.Error(), http.StatusInternalServerError)
		return
	}

	sessionsMu.Lock()
	sessionSeq++
	session := &MachineSession{
		ID:        fmt.Sprintf("sess-%d", sessionSeq),
		MachineID: machineID,
		AppName:   appName,
		RepoName:  req.RepoName,
		Status:    "active",
	}
	sessions[session.ID] = session
	sessionsMu.Unlock()

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(session)
}

func GetSessionOutput(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	sessionID := r.PathValue("id")
	sessionsMu.RLock()
	session, ok := sessions[sessionID]
	sessionsMu.RUnlock()

	if !ok {
		http.Error(w, "session not found", http.StatusNotFound)
		return
	}

	output, err := flyCmd("ssh", "console", "--app", session.AppName,
		"--machine", session.MachineID,
		"--command", "tmux capture-pane -t agent -p -S -50")
	if err != nil {
		http.Error(w, "failed to capture output: "+err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"output": output,
	})
}

func SendSessionInput(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	sessionID := r.PathValue("id")
	sessionsMu.RLock()
	session, ok := sessions[sessionID]
	sessionsMu.RUnlock()

	if !ok {
		http.Error(w, "session not found", http.StatusNotFound)
		return
	}

	var body struct {
		Input string `json:"input"`
	}
	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}

	_, err = flyCmd("ssh", "console", "--app", session.AppName,
		"--machine", session.MachineID,
		"--command", fmt.Sprintf("tmux send-keys -t agent %q Enter", body.Input))
	if err != nil {
		http.Error(w, "failed to send input: "+err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "sent"})
}

func DestroySession(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	sessionID := r.PathValue("id")
	sessionsMu.Lock()
	session, ok := sessions[sessionID]
	if ok {
		session.Status = "done"
	}
	sessionsMu.Unlock()

	if !ok {
		http.Error(w, "session not found", http.StatusNotFound)
		return
	}

	// Destroy the machine entirely
	destroyMachine(session.AppName, session.MachineID)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "destroyed"})
}
