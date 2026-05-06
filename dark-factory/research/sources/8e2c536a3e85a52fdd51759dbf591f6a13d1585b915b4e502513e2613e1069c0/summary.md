# strongdm/cxdb

CXDB is StrongDM's open-source AI Context Store: a content-addressed Turn-DAG + Blob CAS that stores agent conversation histories and tool outputs as immutable nodes with BLAKE3 hashes and parent pointers. It supports branch-from-any-turn (fork a conversation without copying history), fast append for the common case, and msgpack/JSON typed projections for UIs. It ships a binary protocol on :9009, an HTTP API on :9010, a React UI, and a first-party `cxtx` CLI that wraps `codex` and `claude` sessions to capture them as canonical turns.

CXDB is the immutable conversation/tool-output store layer of the Dark Factory — the substrate that lets an agent fleet branch, replay, dedupe, and audit long-horizon agentic-coding traces. It is the second of the two StrongDM repos cited in Willison's Feb 2026 case study and is actively maintained (Rust + Go + TypeScript codebase, ~30k LoC as of search snapshots).
