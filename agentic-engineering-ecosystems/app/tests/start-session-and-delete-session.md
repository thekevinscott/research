# Start session and delete session

## Steps

1. Navigate to `http://localhost:9091/auth/dev` to authenticate
2. Navigate to `http://localhost:9091`
3. Click a repo from the left panel (e.g., "putitoutthere")
4. Click the "+" button in the Sessions panel to create a new session
5. Wait for the session to appear in the sessions list (green dot)
6. Note the session name (e.g., "blue-dawn-9300")
7. Click the "x" button next to the session in the sessions panel
8. Verify the session disappears from the list
9. Verify the main pane returns to "Start a session" empty state
10. Wait one poll cycle (~5s) and confirm the session does not reappear

## Expected

- Session is destroyed on Fly.io (machine terminated)
- Session removed from the sessions list immediately
- If the terminal was open, it disconnects cleanly
- The destroyed machine does not reappear on the next poll

## Failure modes

- Session reappears after deletion — Fly machine not actually destroyed, or destroy API call failed
- "x" button unresponsive — event handler not wired or session ID mismatch
- 500 on destroy — Fly API token expired or machine already gone
- Terminal stays connected after deletion — WebSocket not cleaned up
