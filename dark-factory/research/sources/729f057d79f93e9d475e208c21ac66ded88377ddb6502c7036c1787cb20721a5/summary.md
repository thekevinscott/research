# Cursor — Scaling long-running autonomous coding

Cursor's research blog (Wilson Lin, Jan 14 2026) reports on running hundreds of concurrent coding agents on a single project, generating over a million lines of code and trillions of tokens. Initial flat-coordination approaches with shared state and locking failed: agents held locks too long, forgot to release them, and became risk-averse, churning on small safe changes.

Cursor's working architecture: planner/worker separation. A planner decomposes work, workers execute, both run with a shared coordination protocol that uses optimistic concurrency rather than locks. This is one of the most concrete primary writeups on the actual mechanics of running a Dark Factory at industrial scale, with explicit failure modes and counter-designs.
