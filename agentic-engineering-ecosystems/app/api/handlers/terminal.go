package handlers

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
	"os/exec"
	"sync"

	"github.com/creack/pty"
	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool { return true },
}

type resizeMsg struct {
	Type string `json:"type"`
	Cols uint16 `json:"cols"`
	Rows uint16 `json:"rows"`
}

func Terminal(w http.ResponseWriter, r *http.Request) {
	_, err := getToken(r)
	if err != nil {
		http.Error(w, "unauthorized", http.StatusUnauthorized)
		return
	}

	machineID := r.PathValue("id")
	appName := env("FLY_APP", "dark-factory-sandbox")

	sessionsMu.RLock()
	session, ok := sessions[machineID]
	sessionsMu.RUnlock()

	if !ok {
		session = &MachineSession{
			ID:        machineID,
			MachineID: machineID,
			AppName:   appName,
			Status:    "active",
		}
		sessionsMu.Lock()
		sessions[machineID] = session
		sessionsMu.Unlock()
	}

	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Printf("websocket upgrade failed: %v", err)
		return
	}
	defer conn.Close()

	flyPath := os.Getenv("FLY_PATH")
	if flyPath == "" {
		home, _ := os.UserHomeDir()
		flyPath = home + "/.fly/bin/fly"
	}

	cmd := exec.Command(flyPath, "ssh", "console", "--app", session.AppName,
		"--machine", session.MachineID)
	cmd.Env = append(os.Environ(), "TERM=xterm-256color")

	ptmx, err := pty.Start(cmd)
	if err != nil {
		log.Printf("pty start failed: %v", err)
		conn.WriteMessage(websocket.TextMessage, []byte("Error: "+err.Error()))
		return
	}
	defer ptmx.Close()

	// Switch to agent user and attach to their tmux session
	ptmx.Write([]byte("su - agent -c 'tmux attach -t agent'\n"))

	var wg sync.WaitGroup
	done := make(chan struct{})

	// PTY → WebSocket
	wg.Add(1)
	go func() {
		defer wg.Done()
		buf := make([]byte, 4096)
		for {
			n, err := ptmx.Read(buf)
			if n > 0 {
				if writeErr := conn.WriteMessage(websocket.BinaryMessage, buf[:n]); writeErr != nil {
					break
				}
			}
			if err != nil {
				break
			}
		}
		close(done)
	}()

	// WebSocket → PTY (handles both input and resize)
	wg.Add(1)
	go func() {
		defer wg.Done()
		for {
			msgType, msg, err := conn.ReadMessage()
			if err != nil {
				break
			}
			if msgType == websocket.TextMessage {
				var resize resizeMsg
				if json.Unmarshal(msg, &resize) == nil && resize.Type == "resize" {
					pty.Setsize(ptmx, &pty.Winsize{
						Cols: resize.Cols,
						Rows: resize.Rows,
					})
					continue
				}
			}
			if _, err := ptmx.Write(msg); err != nil {
				break
			}
		}
	}()

	<-done
	cmd.Process.Kill()
	cmd.Wait()
	wg.Wait()
}
