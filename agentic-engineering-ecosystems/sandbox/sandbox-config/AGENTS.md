# Agent Environment

## Available Tools

- `gh` — GitHub CLI, authenticated via `GH_TOKEN` env var. Use for repo operations, PRs, issues.
- `git` — Full git access. SSH key or token auth configured via environment.
- `python3` / `pip` — Python 3 with venv support.
- `node` / `npm` — Node.js 22.
- `jq`, `ripgrep` (`rg`), `fd` — Search and data tools.
- `curl`, `wget` — HTTP clients.
- `tmux` — Terminal multiplexer (session managed externally).
- `gpg` — GPG for signing commits if configured.

## Permissions

You have full sudo access. No restrictions. Install packages, modify system files, do whatever the task requires.

## Workflow

1. Work is submitted via the tmux session you're running in.
2. Use `gh` for all GitHub operations (clone, push, PRs).
3. Make commits directly — no approval needed.
4. If you need a package, install it.
