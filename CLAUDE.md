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

## Always persist expensive artifacts

If a script trains, fits, downloads, scrapes, or otherwise produces a non-trivial-cost artifact (model weights, fitted vectors, embeddings, fetched corpora, expensive intermediate caches), **save the artifact to disk before the script exits**. Do not assume the in-process object will be reused — script exits drop in-memory state and reproducing the work costs time and GPU.

Rules:
- Save the artifact to a stable on-disk path before any eval / sweep / generation step that uses it. If the eval errors, the artifact is still there.
- Include a tiny metadata sidecar (or embed metadata in the saved file): training inputs, hyperparameters, substrate identifier, training timestamp. Re-derivable from git, but the friction kills reuse.
- Prefer canonical formats: `torch.save` for tensors / pickled torch objects, `.json` for structured data, `.npy` for numpy arrays.
- Commit small artifacts to git (KB–low-MB). Gitignore large ones (>10 MB) and document where they live in a README.
- When you write a new training/fitting script, the question is not "should we save?" but "what's the save path?". Default to yes.
