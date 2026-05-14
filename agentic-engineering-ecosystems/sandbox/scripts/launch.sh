#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.fly/bin:$PATH"

cd "$(dirname "$0")/.."

APP_NAME="${1:-$(grep "^app" fly.toml 2>/dev/null | head -1 | sed "s/.*= *['\"]//;s/['\"]//")}"
APP_NAME="${APP_NAME:-agent-sandbox}"

echo "==> Copying Claude credentials into build context..."
rm -rf .claude
mkdir -p .claude
cp -f "$HOME/.claude/.credentials.json" .claude/.credentials.json

if fly status --app "$APP_NAME" >/dev/null 2>&1; then
  echo "==> App exists, redeploying..."
  fly deploy --app "$APP_NAME" --yes
else
  echo "==> Launching new app..."
  fly launch --name "$APP_NAME" --region iad --yes --copy-config --no-public-ips
fi

echo "==> Cleaning up build context..."
rm -rf .claude
mkdir -p .claude
touch .claude/.keep

echo "==> Machine running. Connecting with tmux..."
fly ssh console --app "$APP_NAME" --command "tmux new-session -s agent"

echo "==> Disconnected. Destroying app..."
fly apps destroy "$APP_NAME" --yes
echo "==> Done. No longer billing."
