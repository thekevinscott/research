#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

APP_NAME="${1:-agent-sandbox}"

echo "==> Copying ~/.claude into build context..."
rm -rf .claude
cp -rf "$HOME/.claude" .claude

echo "==> Creating app: $APP_NAME"
fly apps create "$APP_NAME" --org personal 2>/dev/null || true

echo "==> Deploying..."
fly deploy --app "$APP_NAME" --yes

echo "==> Cleaning up build context..."
rm -rf .claude

echo "==> Machine running. Connect with:"
echo "    fly ssh console --app $APP_NAME"
echo ""
echo "==> Destroy with:"
echo "    fly apps destroy $APP_NAME --yes"
