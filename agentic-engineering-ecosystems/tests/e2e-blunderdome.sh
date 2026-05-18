#!/usr/bin/env bash
set -euo pipefail

# End-to-end test for Blunderdome: creates a session, sends a message,
# verifies Claude responds via SSE.
#
# Prerequisites:
#   - Backend running on localhost:9090 with valid .env (CLAUDE_CREDENTIALS set)
#   - fly CLI authenticated
#
# Usage: ./tests/e2e-blunderdome.sh

API_URL="${API_URL:-http://localhost:9090}"
TIMEOUT_SESSION=120   # seconds to wait for machine to start
TIMEOUT_RESPONSE=60   # seconds to wait for Claude's reply

fail() { echo "FAIL: $1" >&2; exit 1; }
pass() { echo "PASS: $1"; }

cleanup() {
  if [ -n "${MACHINE_ID:-}" ]; then
    echo "Cleaning up machine $MACHINE_ID..."
    curl -s -b "$COOKIE" "$API_URL/api/sessions/$MACHINE_ID" -X DELETE > /dev/null 2>&1 || true
  fi
  rm -f /tmp/e2e-sse-$$.txt /tmp/e2e-cookie-$$.txt
}
trap cleanup EXIT

# --- Test 1: Auth ---
echo "--- Test 1: Auth (dev login) ---"
COOKIE_HEADER=$(curl -sv "$API_URL/auth/dev" 2>&1 | grep -i "< Set-Cookie:" | head -1 | sed 's/.*session=/session=/' | cut -d';' -f1)
[ -n "$COOKIE_HEADER" ] || fail "No session cookie from /auth/dev"
COOKIE="$COOKIE_HEADER"
pass "Got session cookie"

# --- Test 2: Auth/me ---
echo "--- Test 2: Auth/me ---"
ME=$(curl -s -b "$COOKIE" "$API_URL/auth/me")
LOGIN=$(echo "$ME" | python3 -c "import sys,json; print(json.load(sys.stdin).get('login',''))" 2>/dev/null)
[ -n "$LOGIN" ] || fail "/auth/me returned no login: $ME"
pass "Authenticated as $LOGIN"

# --- Test 3: Create session ---
echo "--- Test 3: Create session ---"
SESSION_RESP=$(curl -s -b "$COOKIE" "$API_URL/api/sessions" \
  -X POST -H "Content-Type: application/json" \
  -d '{"repo_name":"thekevinscott/putitoutthere"}')
MACHINE_ID=$(echo "$SESSION_RESP" | python3 -c "import sys,json; print(json.load(sys.stdin).get('id',''))" 2>/dev/null)
[ -n "$MACHINE_ID" ] || fail "No machine_id in response: $SESSION_RESP"
pass "Created session: $MACHINE_ID"

# --- Test 4: Health check (wait for channel server) ---
echo "--- Test 4: Health check ---"
HEALTH_OK=false
for i in $(seq 1 $((TIMEOUT_SESSION / 5))); do
  HEALTH=$(curl -s -b "$COOKIE" "$API_URL/api/sessions/$MACHINE_ID/health" 2>/dev/null || echo "")
  if echo "$HEALTH" | grep -q '"tmux_alive":true'; then
    HEALTH_OK=true
    break
  fi
  sleep 5
done
$HEALTH_OK || fail "Health check never passed (last: $HEALTH)"
pass "Channel server healthy, tmux alive"

# --- Test 5: Wait for Claude to be ready (past prompts) ---
echo "--- Test 5: Wait for Claude ready ---"
sleep 20  # prompt-accept.sh needs time to clear bypass prompt
pass "Waited for Claude startup"

# --- Test 6: Send message and receive reply via SSE ---
echo "--- Test 6: Send message + SSE reply ---"

# Start SSE listener in background
(timeout $TIMEOUT_RESPONSE curl -s -N -b "$COOKIE" "$API_URL/api/sessions/$MACHINE_ID/events" > /tmp/e2e-sse-$$.txt 2>&1) &
SSE_PID=$!
sleep 3  # let SSE connection establish

# Send message
SEND_RESP=$(curl -s -b "$COOKIE" "$API_URL/api/sessions/$MACHINE_ID/message" \
  -X POST -H "Content-Type: application/json" \
  -d '{"message":"What is 3+4? Reply with just the number."}')
echo "$SEND_RESP" | grep -q '"status":"sent"' || fail "Send failed: $SEND_RESP"

# Wait for reply event
wait $SSE_PID 2>/dev/null || true

# Check SSE output
if grep -q '"event":"reply"' /tmp/e2e-sse-$$.txt; then
  REPLY_TEXT=$(grep '"event":"reply"' /tmp/e2e-sse-$$.txt | python3 -c "
import sys, json
for line in sys.stdin:
  line = line.strip()
  if line.startswith('data: '):
    data = json.loads(line[6:])
    if data.get('event') == 'reply':
      print(data['data']['text'])
      break
" 2>/dev/null)
  if echo "$REPLY_TEXT" | grep -q "7"; then
    pass "Got correct reply: $REPLY_TEXT"
  else
    fail "Reply didn't contain '7': $REPLY_TEXT"
  fi
else
  echo "SSE output was:"
  cat /tmp/e2e-sse-$$.txt
  fail "No reply event in SSE stream"
fi

# --- Test 7: Destroy session ---
echo "--- Test 7: Destroy session ---"
DEL_RESP=$(curl -s -b "$COOKIE" "$API_URL/api/sessions/$MACHINE_ID" -X DELETE)
echo "$DEL_RESP" | grep -q '"status":"destroyed"' || fail "Destroy failed: $DEL_RESP"
MACHINE_ID=""  # prevent double-cleanup
pass "Session destroyed"

echo ""
echo "=== ALL TESTS PASSED ==="
