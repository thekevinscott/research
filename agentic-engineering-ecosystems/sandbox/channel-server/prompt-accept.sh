#!/usr/bin/env bash
# Runs in background, polls tmux pane, auto-accepts interactive prompts
TMUX_SESSION="claude"

for i in $(seq 1 60); do
  sleep 2
  PANE=$(tmux capture-pane -t "$TMUX_SESSION" -p 2>/dev/null || true)

  # Trust folder prompt: "Yes, I trust" is default (option 1) — just Enter
  if echo "$PANE" | grep -q "trust this folder"; then
    echo "[prompt-accept] Trust folder prompt — accepting" >&2
    tmux send-keys -t "$TMUX_SESSION" Enter
    continue
  fi

  # Bypass permissions prompt: "No, exit" is default — need Down then Enter
  if echo "$PANE" | grep -q "Bypass Permissions mode"; then
    echo "[prompt-accept] Bypass permissions — selecting Yes" >&2
    tmux send-keys -t "$TMUX_SESSION" Down
    sleep 1
    tmux send-keys -t "$TMUX_SESSION" Enter
    continue
  fi

  # Settings error prompt: select "Continue without these settings" (option 3)
  if echo "$PANE" | grep -q "Settings Error"; then
    echo "[prompt-accept] Settings error — selecting Continue" >&2
    tmux send-keys -t "$TMUX_SESSION" Down
    sleep 0.5
    tmux send-keys -t "$TMUX_SESSION" Down
    sleep 0.5
    tmux send-keys -t "$TMUX_SESSION" Enter
    continue
  fi

  # Claude ready
  if echo "$PANE" | grep -q "What can I help"; then
    echo "[prompt-accept] Claude ready!" >&2
    break
  fi
done
