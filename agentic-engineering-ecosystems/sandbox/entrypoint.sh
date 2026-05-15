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

cat > /home/agent/.env.sandbox <<ENVEOF
export GH_TOKEN='${GH_TOKEN:-}'
export AGENT_WORKDIR='${AGENT_WORKDIR}'
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
ENVEOF
chown agent:agent /home/agent/.env.sandbox

# Start tmux + claude + prompt-accept + channel server all as agent user
exec su - agent -c "
  source /home/agent/.env.sandbox
  cd $AGENT_WORKDIR

  # Start tmux with claude
  tmux new-session -d -s claude -c '$AGENT_WORKDIR'
  tmux send-keys -t claude 'source /home/agent/.env.sandbox && cd $AGENT_WORKDIR && claude --permission-mode bypassPermissions' Enter

  # Background prompt acceptor (runs as agent, same tmux server)
  /home/agent/channel-server/prompt-accept.sh &

  # Channel server in foreground (keeps container alive)
  exec node /home/agent/channel-server/server.cjs
"
