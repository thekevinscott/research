#!/usr/bin/env bash
set -e

REPO_URL="${REPO_URL:-}"
WORKDIR="/home/agent/work"

if [ -n "$REPO_URL" ]; then
  if [ -n "$GH_TOKEN" ]; then
    git clone "https://x-access-token:${GH_TOKEN}@github.com/${REPO_URL}" "$WORKDIR" 2>&1 || true
  else
    git clone "https://github.com/${REPO_URL}" "$WORKDIR" 2>&1 || true
  fi
  [ -d "$WORKDIR" ] && chown -R agent:agent "$WORKDIR"
fi

AGENT_WORKDIR="$WORKDIR"
[ -d "$AGENT_WORKDIR" ] || AGENT_WORKDIR="/home/agent"

# Write env for agent user
cat > /home/agent/.env.sandbox <<ENVEOF
export GH_TOKEN='${GH_TOKEN:-}'
export AGENT_WORKDIR='${AGENT_WORKDIR}'
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
ENVEOF
chown agent:agent /home/agent/.env.sandbox

# Start channel server as agent user (it spawns Claude Code internally)
su - agent -c "
  source /home/agent/.env.sandbox
  cd $AGENT_WORKDIR
  exec node /home/agent/channel-server/server.cjs
"
