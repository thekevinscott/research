# Summary

OpenAI's Codex (the 2026 cloud agent, distinct from the 2021 completion model) is a cloud-based software engineering agent that runs many tasks in parallel, each inside its own preloaded sandbox. Powered by codex-1 (an o3 derivative trained via RL on real-world coding tasks), it can iteratively run tests until they pass and proposes PRs that mirror human PR style.

For dark-factory pipelines, Codex Cloud is one of the most heavily used worker agents because of its parallelism, sandbox-per-task isolation, and built-in primitives like Skills (reusable workflows), Automations (scheduled background work), and Codex Security (vulnerability detection). OpenAI publicly endorses the "harness-engineering" frame, claiming it is using Codex itself to improve Codex - a reflexive dark-factory loop.
