# ComposioHQ/agent-orchestrator

Composio's Agent Orchestrator spawns parallel AI coding agents, each in its own git worktree with its own branch and PR. Agents autonomously fix CI failures, address review comments, and open PRs; the operator supervises from one dashboard. It is agent-agnostic (Claude Code, Codex, Aider), runtime-agnostic (tmux, Docker), and tracker-agnostic (GitHub, Linear).

Agent Orchestrator is a parallel-agent orchestrator — the layer above the inner coding-agent harness. In a Dark Factory pipeline this is what turns a single non-interactive agent into an N-way fleet that converges on the spec. The git-worktree-per-agent pattern is now the standard architecture (also seen in emdash, overstory, ccswarm).
