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
	// flyctl may print deprecation warnings before the token — take last line
	lines := strings.Split(strings.TrimSpace(out), "\n")
	return strings.TrimSpace(lines[len(lines)-1]), nil
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

func ListSessions(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	appName := env("FLY_APP", "dark-factory-sandbox")
	apiToken, err := getAPIToken()
	if err != nil {
		http.Error(w, "failed to get fly token: "+err.Error(), http.StatusInternalServerError)
		return
	}

	url := fmt.Sprintf("https://api.machines.dev/v1/apps/%s/machines", appName)
	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("Authorization", "Bearer "+apiToken)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		http.Error(w, "failed to list machines: "+err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		b, _ := io.ReadAll(resp.Body)
		http.Error(w, fmt.Sprintf("fly API error (%d): %s", resp.StatusCode, string(b)), http.StatusInternalServerError)
		return
	}

	var machines []struct {
		ID        string `json:"id"`
		Name      string `json:"name"`
		State     string `json:"state"`
		Region    string `json:"region"`
		CreatedAt string `json:"created_at"`
		UpdatedAt string `json:"updated_at"`
		ImageRef  struct {
			Tag string `json:"tag"`
		} `json:"image_ref"`
	}
	json.NewDecoder(resp.Body).Decode(&machines)

	type sessionResp struct {
		ID        string `json:"id"`
		MachineID string `json:"machine_id"`
		Name      string `json:"name"`
		State     string `json:"state"`
		Region    string `json:"region"`
		CreatedAt string `json:"created_at"`
		AppName   string `json:"app_name"`
	}

	var result []sessionResp
	for _, m := range machines {
		if m.State == "started" || m.State == "starting" {
			sessionsMu.Lock()
			if _, exists := sessions[m.ID]; !exists {
				sessions[m.ID] = &MachineSession{
					ID:        m.ID,
					MachineID: m.ID,
					AppName:   appName,
					Status:    "active",
				}
			}
			sessionsMu.Unlock()

			result = append(result, sessionResp{
				ID:        m.ID,
				MachineID: m.ID,
				Name:      m.Name,
				State:     m.State,
				Region:    m.Region,
				CreatedAt: m.CreatedAt,
				AppName:   appName,
			})
		}
	}

	if result == nil {
		result = []sessionResp{}
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(result)
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

	appName := env("FLY_APP", "dark-factory-sandbox")
	image := os.Getenv("FLY_IMAGE")
	if image == "" {
		http.Error(w, "FLY_IMAGE not configured", http.StatusInternalServerError)
		return
	}

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

	// Clone the repo and fix ownership so agent user can access it
	repoDir := "/home/agent/work"
	cloneCmd := fmt.Sprintf("bash -c 'git clone https://github.com/%s %s 2>&1; chown -R agent:agent %s'", req.RepoName, repoDir, repoDir)
	_, err = flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
		"--command", cloneCmd)
	if err != nil {
		// Non-fatal — clone might fail for private repos without token
	}

	// Start tmux with claude as agent user (claude rejects --dangerously-skip-permissions under root)
	startCmd := fmt.Sprintf("su - agent -c 'cd %s 2>/dev/null; tmux new-session -d -s agent claude --dangerously-skip-permissions'", repoDir)
	_, err = flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
		"--command", startCmd)
	if err != nil {
		http.Error(w, "failed to start claude: "+err.Error(), http.StatusInternalServerError)
		return
	}

	// Auto-accept Claude startup prompts by polling tmux output
	go func() {
		sendKey := func(key string) {
			flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
				"--command", fmt.Sprintf("su - agent -c 'tmux send-keys -t agent %s'", key))
		}
		capture := func() string {
			out, _ := flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
				"--command", "su - agent -c 'tmux capture-pane -t agent -p -S -50'")
			return out
		}

		for i := 0; i < 30; i++ {
			time.Sleep(2 * time.Second)
			screen := capture()
			switch {
			case strings.Contains(screen, "Yes, I trust this folder"):
				sendKey("Enter")
			case strings.Contains(screen, "Yes, allow external imports"):
				sendKey("Enter")
			case strings.Contains(screen, "Yes, I accept"):
				sendKey("Down")
				time.Sleep(500 * time.Millisecond)
				sendKey("Enter")
			case strings.Contains(screen, "Try \"how does"):
				return
			}
		}
	}()

	sessionsMu.Lock()
	session := &MachineSession{
		ID:        machineID,
		MachineID: machineID,
		AppName:   appName,
		RepoName:  req.RepoName,
		Status:    "active",
	}
	sessions[machineID] = session
	sessionsMu.Unlock()

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"id":         machineID,
		"machine_id": machineID,
		"name":       "new-session",
		"state":      "started",
		"region":     env("FLY_REGION", "iad"),
		"created_at": time.Now().UTC().Format(time.RFC3339),
		"app_name":   appName,
	})
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

	machineID := r.PathValue("id")
	appName := env("FLY_APP", "dark-factory-sandbox")

	sessionsMu.Lock()
	delete(sessions, machineID)
	sessionsMu.Unlock()

	destroyMachine(appName, machineID)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "destroyed"})
}
