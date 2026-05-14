#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.fly/bin:$PATH"

cd "$(dirname "$0")/.."

APP_NAME="${1:-$(grep "^app" fly.toml 2>/dev/null | head -1 | sed "s/.*= *['\"]//;s/['\"]//")}"

fly ssh console --app "$APP_NAME" --command "tmux attach -t agent || tmux new-session -s agent"
