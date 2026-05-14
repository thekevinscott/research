#!/usr/bin/env bash
set -euo pipefail

APP_NAME="${1:-agent-sandbox}"

fly ssh console --app "$APP_NAME"
