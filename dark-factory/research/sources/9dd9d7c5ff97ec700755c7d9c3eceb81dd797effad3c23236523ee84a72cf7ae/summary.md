# GitHub — strongdm/cxdb README

CXDB's README documents the full architecture: a Rust server exposing a binary protocol (port 9009) and HTTP gateway (9010), Go client SDK, React/Next.js frontend, BLAKE3 content addressing, msgpack storage with typed JSON projections, and a sandboxed renderer plug-in system. Forks are O(1); typical use is appending turns from Claude/Codex sessions via the cxtx CLI wrapper.

The README emphasizes CXDB as the storage substrate for production agent runs: append every turn, fork at any point, dedupe identical payloads automatically. Type registry supports forward-compatible schema evolution. Apache 2.0. This is the most concrete artifact of the "AI Context Store" category referenced in the StrongDM Software Factory writeup, and the only one with full code.
