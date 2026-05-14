# Start session skips trust prompts

## Steps

1. Navigate to `http://localhost:9091/auth/dev` to authenticate
2. Navigate to `http://localhost:9091`
3. Click a repo from the left panel (e.g., "putitoutthere")
4. Click the "+" button in the Sessions panel to create a new session
5. Wait for the session to appear with green dot
6. Click the session to open the terminal
7. Wait for Claude Code TUI to load (may take 5-10s after SSH connects)
8. Observe that Claude Code skips directly to the idle prompt — no trust dialog, no external imports dialog, no permission prompts

## Expected

- Claude Code starts inside the container
- NO "Do you trust this folder?" prompt (handled by `trustedDirectories` in settings.json)
- NO "Allow external imports?" prompt (handled by auto mode)
- NO permission prompts (handled by `permissions.allow` wildcard rules)
- Claude Code reaches idle input prompt automatically
- No "not logged in" or credential errors

## Failure modes

- Trust prompt appears — `trustedDirectories` in sandbox settings.json doesn't include `/home/agent/work`, or sandbox image is stale
- Permission prompts appear — `defaultMode` not set to "auto" or `permissions.allow` missing wildcard
- "Not logged in" error — `.credentials.json` not present or expired in sandbox image
- Claude hangs on startup — PTY resize not sent, or tmux session not created

## Config dependencies

Sandbox image must include `/home/agent/.claude/settings.json` with:
```json
{
  "permissions": {
    "allow": ["Bash(*)", "Read(*)", "Write(*)", "Edit(*)"],
    "deny": [],
    "defaultMode": "auto"
  },
  "trustedDirectories": ["/home/agent", "/home/agent/work"]
}
```
