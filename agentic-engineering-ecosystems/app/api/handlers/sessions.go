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
			"services": []map[string]interface{}{
				{
					"ports": []map[string]interface{}{
						{"port": 8788, "handlers": []string{"http"}},
					},
					"internal_port":      8788,
					"protocol":           "tcp",
					"auto_stop_machines": false,
					"auto_start_machines": false,
				},
			},
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

// channelURL returns the URL to reach a machine's channel server via Fly proxy
func channelURL(appName, machineID, path string) string {
	return fmt.Sprintf("https://%s.fly.dev%s", appName, path)
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

	machineID, err := createMachine(appName, image)
	if err != nil {
		http.Error(w, "failed to create machine: "+err.Error(), http.StatusInternalServerError)
		return
	}

	if err := waitMachineStarted(appName, machineID); err != nil {
		http.Error(w, "machine failed to start: "+err.Error(), http.StatusInternalServerError)
		return
	}

	// Give it a moment to fully boot
	time.Sleep(2 * time.Second)

	// Clone repo and fix ownership
	repoDir := "/home/agent/work"
	cloneCmd := fmt.Sprintf("bash -c 'git clone https://github.com/%s %s 2>&1; chown -R agent:agent %s'", req.RepoName, repoDir, repoDir)
	flyCmd("ssh", "console", "--app", appName, "--machine", machineID, "--command", cloneCmd)

	// Start Claude Code with channels enabled (as agent user)
	startCmd := fmt.Sprintf(
		"su - agent -c 'cd %s 2>/dev/null; claude --dangerously-skip-permissions --dangerously-load-development-channels server:blunderdome'",
		repoDir,
	)
	// Run in background — claude will keep running
	flyCmd("ssh", "console", "--app", appName, "--machine", machineID,
		"--command", fmt.Sprintf("nohup %s > /tmp/claude.log 2>&1 &", startCmd))

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

// SendMessage proxies a message to the channel server on the Fly machine
func SendMessage(w http.ResponseWriter, r *http.Request) {
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

	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}

	// Proxy to channel server via fly ssh
	var input struct {
		Message string `json:"message"`
	}
	json.Unmarshal(body, &input)

	out, err := flyCmd("ssh", "console", "--app", session.AppName,
		"--machine", session.MachineID,
		"--command", fmt.Sprintf("curl -s -X POST http://localhost:8788/message -d %q", input.Message))
	if err != nil {
		http.Error(w, "failed to send message: "+err.Error()+"\n"+out, http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(out))
}

// StreamEvents proxies SSE events from the channel server on the Fly machine
func StreamEvents(w http.ResponseWriter, r *http.Request) {
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

	// Connect to channel server's SSE endpoint via Fly proxy
	appName := session.AppName
	machineID := session.MachineID
	targetURL := channelURL(appName, machineID, "/events")

	apiToken, err := getAPIToken()
	if err != nil {
		http.Error(w, "failed to get fly token", http.StatusInternalServerError)
		return
	}

	proxyReq, _ := http.NewRequest("GET", targetURL, nil)
	proxyReq.Header.Set("fly-force-instance-id", machineID)
	proxyReq.Header.Set("Authorization", "Bearer "+apiToken)

	client := &http.Client{Timeout: 0}
	resp, err := client.Do(proxyReq)
	if err != nil {
		http.Error(w, "failed to connect to channel server: "+err.Error(), http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()

	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")

	flusher, ok := w.(http.Flusher)
	if !ok {
		http.Error(w, "streaming not supported", http.StatusInternalServerError)
		return
	}

	buf := make([]byte, 4096)
	for {
		n, err := resp.Body.Read(buf)
		if n > 0 {
			w.Write(buf[:n])
			flusher.Flush()
		}
		if err != nil {
			break
		}
	}
}

// ChannelHealth checks if the channel server is running on a machine
func ChannelHealth(w http.ResponseWriter, r *http.Request) {
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

	out, err := flyCmd("ssh", "console", "--app", session.AppName,
		"--machine", session.MachineID,
		"--command", "curl -s http://localhost:8788/health")
	if err != nil {
		http.Error(w, "channel server not ready", http.StatusServiceUnavailable)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(out))
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
