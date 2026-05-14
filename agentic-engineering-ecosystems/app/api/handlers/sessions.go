package handlers

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"sync"
)

type MachineSession struct {
	ID       string `json:"id"`
	AppName  string `json:"app_name"`
	RepoName string `json:"repo_name"`
	Status   string `json:"status"`
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

	// Start tmux with claude inside
	_, err = flyCmd("ssh", "console", "--app", appName, "--command",
		"bash -c 'tmux new-session -d -s agent claude'")
	if err != nil {
		http.Error(w, "failed to start session: "+err.Error(), http.StatusInternalServerError)
		return
	}

	session := &MachineSession{
		ID:       fmt.Sprintf("sess-%d", len(sessions)+1),
		AppName:  appName,
		RepoName: req.RepoName,
		Status:   "active",
	}

	sessionsMu.Lock()
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

	output, err := flyCmd("ssh", "console", "--app", session.AppName, "--command",
		"tmux capture-pane -t agent -p")
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

	var req struct {
		Input string `json:"input"`
	}
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}

	_, err = flyCmd("ssh", "console", "--app", session.AppName, "--command",
		fmt.Sprintf("tmux send-keys -t agent %q Enter", req.Input))
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

	// Kill tmux session
	flyCmd("ssh", "console", "--app", session.AppName, "--command",
		"tmux kill-session -t agent")

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "destroyed"})
}
