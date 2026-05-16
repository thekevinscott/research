#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)

RESPONSE=$(echo "$INPUT" | jq -r '.last_assistant_message // empty')

if [ -z "$RESPONSE" ]; then
  exit 0
fi

SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

jq -n --arg text "$RESPONSE" --arg sid "$SESSION_ID" '{text:$text,session_id:$sid}' | \
  curl -s -X POST http://localhost:8788/hook/stop -H "Content-Type: application/json" -d @-
