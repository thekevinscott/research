# Start session and type

## Steps

1. Navigate to `http://localhost:9091/auth/dev` to authenticate
2. Navigate to `http://localhost:9091`
3. Click a repo from the left panel (e.g., "putitoutthere")
4. Click the "+" button in the Sessions panel to create a new session
5. Wait for the session to appear in the sessions list with a green dot (started state)
6. Click the new session
7. Verify the terminal area loads with an xterm.js terminal (not a text input box)
8. Click into the terminal area
9. Type a command (e.g., `ls`) and press Enter
10. Verify the command executes and output appears in the terminal

## Expected

- Session creates successfully (no 500 errors)
- Terminal renders with colors, cursor, and monospace font
- Keystrokes are sent to the remote machine in real time
- Output streams back and renders correctly
- Claude Code TUI is visible and interactive if tmux session is running

## Failure modes

- Terminal shows a text input box instead of xterm.js — WebSocket connection failed
- Terminal shows "Connecting..." indefinitely — WebSocket upgrade rejected or SSH relay failed
- Session creation returns 500 — Fly machine creation or clone failed
- Garbled output — terminal resize not sent or PTY not allocated
