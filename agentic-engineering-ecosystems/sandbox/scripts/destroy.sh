#!/usr/bin/env bash
set -euo pipefail

APP_NAME="${1:-agent-sandbox}"

echo "==> Destroying app: $APP_NAME"
fly apps destroy "$APP_NAME" --yes

echo "==> Done. No longer billing."
