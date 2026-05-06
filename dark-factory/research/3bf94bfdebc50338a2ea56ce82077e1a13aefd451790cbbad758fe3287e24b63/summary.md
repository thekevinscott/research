# Aider-AI/aider

Aider is a terminal-native AI coding agent that works directly against a git repository, scoring consistently on SWE-bench. It supports Claude, GPT, DeepSeek, local models via Ollama, and uses repo-map summarization to fit large codebases into context. Releases are frequent (93 releases / 13k+ commits as of March 2026).

Aider is one of the canonical OSS coding-agent harnesses; in the Dark Factory pattern it is the kind of CLI agent that an orchestrator spawns N copies of in parallel git worktrees. Aider is also one of the small set of agents that pi-builder / vibe-tools / agent-orchestrator wrap as a backend, which makes it foundational infrastructure rather than a leaf tool.
