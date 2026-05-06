@AGENTS.md

# Research project instructions

## Fetching web content

Use `./scripts/safe-fetch <url> [output_path]` for all web fetches.

- Saves verbatim raw bytes to `/tmp/` (default) or specified path under `/tmp/`.
- Required when audit/citation needs byte-exact source — `WebFetch` summarizes and is not suitable for verbatim quoting.
- HTTPS only; private/loopback/metadata IPs blocked (SSRF guard); 20 MB / 30 s caps; max 3 redirects.
- Output path must be under `/tmp/`.

Raw `curl` and `wget` are denied by project settings. Do not attempt to bypass — extend `safe-fetch` instead if a real need arises.

For quick summaries where verbatim text is not needed, `WebFetch` is fine and cheaper.

## Tracking work across sessions

Use **bd (beads)** for any work that needs to persist between sessions. Built-in `TaskCreate`/`TaskList` are scoped to a single conversation; bd survives compactions, restarts, and handoffs.

- `bd ready` — find unblocked work at session start
- `bd create "title" --description "context" -p <0-4>` — file new work as you discover it
- `bd update <id> --claim` — atomically claim before working
- `bd close <id> --reason "done"` — complete

In-conversation todos still belong in `TaskCreate`; cross-session work belongs in bd. See `AGENTS.md` for the full bd workflow.
