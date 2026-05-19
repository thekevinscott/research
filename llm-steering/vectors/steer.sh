#!/usr/bin/env bash
# Fire up an interactive llama.cpp chat with a steering vector applied.
#
# Usage:
#   ./steer.sh <substrate> <trait> [coeff]
#
#   substrate : qwen | mistral
#   trait     : vector name (see tables below)
#   coeff     : steering strength; optional, defaults per trait.
#               Positive steers TOWARD the trait, negative steers away.
#
# Examples:
#   ./steer.sh qwen trippy            # qwen, trippy vector at default +6
#   ./steer.sh qwen sycophancy -6     # steer AWAY from sycophancy (toward honest)
#   ./steer.sh mistral honesty 3      # mistral honesty at +3
#
# Runs on tower (the GGUF models live there). Override the llama-cli path
# with LLAMA_CLI=/path/to/llama-cli if it is built elsewhere.
set -euo pipefail

LLAMA_CLI="${LLAMA_CLI:-/home/tower/code/llama.cpp/build/bin/llama-cli}"

VECTORS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STEERING_DIR="$(dirname "$VECTORS_DIR")"
GGUF_DIR="$STEERING_DIR/models/gguf"

usage() {
    sed -n '2,18p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 1
}

[ $# -ge 2 ] || usage
substrate="$1"
trait="$2"
coeff="${3:-}"

case "$substrate" in
    qwen)    model="$GGUF_DIR/qwen2.5-7b-instruct-q8_0.gguf" ;;
    mistral) model="$GGUF_DIR/mistral-7b-instruct-v0.1-q8_0.gguf" ;;
    *) echo "error: unknown substrate '$substrate' (expected qwen|mistral)" >&2; exit 1 ;;
esac

vector="$VECTORS_DIR/$substrate/$trait.gguf"
[ -f "$vector" ] || { echo "error: no vector at $vector" >&2; exit 1; }
[ -f "$model" ]  || { echo "error: no GGUF model at $model" >&2
                      echo "  convert it first (convert_hf_to_gguf.py --outtype q8_0)" >&2; exit 1; }
[ -x "$LLAMA_CLI" ] || { echo "error: llama-cli not found at $LLAMA_CLI (set LLAMA_CLI=)" >&2; exit 1; }

# Default coefficient per substrate/trait, from vectors/README.md status table.
if [ -z "$coeff" ]; then
    case "$substrate/$trait" in
        qwen/happy)       coeff=4 ;;
        mistral/honesty)  coeff=2 ;;
        mistral/trippy)   coeff=2.2 ;;
        *)                coeff=6 ;;
    esac
fi

# Traits that did not reliably install in the research — warn but still run.
case "$substrate/$trait" in
    qwen/golden_gate|qwen/paranoia|qwen/hedge|qwen/clarify)
        echo "note: '$trait' was a null/weak result in testing — steering may not show." >&2 ;;
esac

cmd=("$LLAMA_CLI" -m "$model"
     --control-vector-scaled "$vector:$coeff"
     -ngl 99 -c 4096 -cnv --color)

echo "+ ${cmd[*]}" >&2
exec "${cmd[@]}"
