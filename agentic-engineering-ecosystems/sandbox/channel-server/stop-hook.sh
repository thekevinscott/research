#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)
TRANSCRIPT=$(echo "$INPUT" | jq -r '.transcript_path // empty')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

if [ -z "$TRANSCRIPT" ] || [ ! -f "$TRANSCRIPT" ]; then
  echo "[stop-hook] no transcript at: $TRANSCRIPT" >&2
  exit 0
fi

RESPONSE=$(tac "$TRANSCRIPT" | while IFS= read -r line; do
  TYPE=$(echo "$line" | jq -r '.type // empty' 2>/dev/null)
  if [ "$TYPE" = "assistant" ]; then
    echo "$line" | jq -r '.message.content | map(select(.type == "text")) | map(.text) | join("")'
    break
  fi
done)

if [ -z "$RESPONSE" ]; then
  echo "[stop-hook] no assistant message found" >&2
  exit 0
fi

curl -s -X POST http://localhost:8788/hook/stop \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg text "$RESPONSE" --arg session_id "$SESSION_ID" '{text: $text, session_id: $session_id}')"
