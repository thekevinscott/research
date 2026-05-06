# Tools and Infrastructure

*Section 4 of 8 — synthesis report, 2026-05-06*

---

## Coding Agents

**Claude Code** (Anthropic) is the most-cited implementation backbone in Dark Factory builds in 2026.[^claude_code] Shapiro noted that "most folks at level 4 seem to find their way to Claude Code" — it provides an agentic CLI with hooks, sub-agents, MCP servers, and a skill system that serves as the harness-building surface teams build on.[^5f951b]

**Aider** — terminal-native, git-aware coding agent with strong SWE-bench scores. Suited for parallel worktree spawning: you can run N copies against N isolated branches simultaneously.[^aider]

**Cline** and its fork **Roo Code** — IDE-embedded, multi-mode agents (Code/Architect/Ask/Debug modes constrain agent capabilities per phase; closest OSS analog to Attractor's multi-phase node graph).[^cline][^roocode]

**OpenHands** (formerly OpenDevin) — most mature OSS coding-agent platform with a full software agent SDK, sandboxed execution, and GUI/CLI/API surface.[^openhands] MLSys 2026 paper documents the redesigned production toolkit.[^openhands_paper]

**GitHub Copilot coding agent** — asynchronous PR-generating agent announced by GitHub; complements the IDE assistant with autonomous background execution.[^github_copilot_agent]

[^claude_code]: https://github.com/anthropics/claude-code — "the most-cited closed-implementation coding-agent harness powering Dark Factory builds in 2026" — sha256:e0374fa253eeca68f0ca025c60e0b2d7638a5cfbc12efa63b22fb3c22e6cdd1d

[^5f951b]: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ — "most folks at level 4 seem to find their way to Claude Code" — sha256:5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c

[^aider]: https://github.com/aider-ai/aider — "terminal-native git-aware coding agent with strong SWE-bench scores; the kind of CLI agent parallel orchestrators spawn N copies of in worktrees." — sha256:3b836785e1677f1477d304f401f850dfa68c55a2551af34ddace36dc7caf5897

[^cline]: https://github.com/cline/cline — "model-agnostic" — sha256:635cd09b88e4b69ca8ae01aa814b54c60a5345219247ff38a2835bc5bef444e9

[^roocode]: https://github.com/roocodeinc/roo-code — "Cline fork with custom modes that constrain agent capabilities per phase" — sha256:7bb313f91beda310b802bcf09f0265bb6f3958b06dbd8a0e8cbbea2048a6a816

[^openhands]: https://github.com/openhands/openhands — "most mature OSS replacement for the proprietary inner loop in a Dark Factory build" — sha256:6038ae0c15e5e15313c60a62a17758722db92efea644723d954e83d525d08233

[^openhands_paper]: https://arxiv.org/abs/2511.03690 — "OpenHands Software Agent SDK paper (MLSys 2026): redesigned production agent toolkit with sandboxed execution" — sha256:a955e8c00a1b8419ff9fe9c163481ee2d0cbef9c4ffbda430ba0ec1d63664bea

[^github_copilot_agent]: https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/ — "GitHub announces the Copilot coding agent (asynchronous)" — sha256:7e8be62f29158f638138fba1006c4f9f4fee685067c20ce64717a40edf92b289

---

## Parallel Orchestration

Scaling a Dark Factory means running many agents concurrently. The dominant pattern: spawn agents in isolated git worktrees, one per task.

**Composio Agent Orchestrator** — spawns parallel Claude Code/Codex/Aider/OpenCode agents on git worktrees with a coordination layer.[^composio]

**Emdash** (YC W26) — desktop multi-agent orchestrator running 24+ CLI agents in worktrees simultaneously; provides supervised-mode oversight without blocking the agents.[^emdash]

**Cursor** found that scaling to hundreds of concurrent agents required rethinking coordination. Flat coordination with locking failed due to deadlock; their research blog documents the architectural changes required.[^cursor_scale]

[^composio]: https://github.com/composiohq/agent-orchestrator — "spawns parallel Claude Code/Codex/Aider/OpenCode agents on git worktrees" — sha256:d275ba4fb0a49a49d04978966d1743103af0321e69c4affe974f8bf027564ff3

[^emdash]: https://github.com/generalaction/emdash — "desktop multi-agent orchestrator running 24+ CLI agents in worktrees" — sha256:5689d6a404d1711b82d659c7de1ef235d1d94fd60ae1328cc87638801276e4de

[^cursor_scale]: https://cursor.com/blog/scaling-agents — "flat coordination + locking failed (deadlock)" — sha256:c7f1c8f877ed55a6e104a6675e18ab8c00d21cd5a35163f626e41691a2252033

---

## Context Engineering

**Repomix** — packs an entire repo into AI-friendly bundles using tree-sitter compression and an MCP server; the context-packing utility agents use to fit codebases into context windows.[^repomix]

**Claude Agent SDK** (Python) — exposes the Claude Code agent loop as a library with custom tools/hooks and in-process MCP servers; the glue between orchestration and inner agent.[^agent_sdk]

**Codex CLI 0.128.0 `/goal` command** — built-in autonomous loop equivalent for long-horizon objectives that persist across sessions.[^codex_goal]

[^repomix]: https://github.com/yamadashy/repomix — "packs an entire repo into AI-friendly bundles with tree-sitter compression and an MCP server" — sha256:f8ec743018ff82a36855302b642fca9d26bc2f99f8c20f004436fb64e2ecfc98

[^agent_sdk]: https://github.com/anthropics/claude-agent-sdk-python — "exposes the Claude Code agent loop as a library with custom tools/hooks and in-process MCP servers" — sha256:5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c

[^codex_goal]: https://simonwillison.net/2026/Apr/30/codex-goals/ — "Codex CLI 0.128.0 /goal command — built-in autonomous loop equivalent for long-horizon objectives that persist across sessions." — sha256:e08f4d5ae736788c2b41e8bebd1dda6c6b9b85ed758621b06c64eebe4c53f1c4

---

## Observability and Tracing

**CXDB** (StrongDM) — self-hosted AI Context Store. Content-addressed Turn DAG; p50 append < 1ms for 10KB; branching is O(1); 70%+ storage reduction via BLAKE3.[^cxdb]

**Langfuse** — OSS LLM observability, evals, and prompt management; eval/observability substrate complementing CXDB for post-hoc agent-fleet debugging.[^langfuse]

**Anthropic's eval guidance** warns explicitly against "self-congratulation machines" — eval harnesses that produce high scores by gaming the metric rather than solving the problem. The guidance distinguishes offline benchmarks from online telemetry and recommends LLM-as-judge patterns with adversarial probing.[^anthropic_evals]

[^cxdb]: https://github.com/strongdm/cxdb — "content-addressed Turn DAG plus Blob CAS for immutable agent conversation/tool-output traces" — sha256:4bcac8b1d85cbcc8a9960d654265b2f60efe4b1621489b474fd19cceddcd1acf

[^langfuse]: https://github.com/langfuse/langfuse — "OSS LLM observability + evals + prompt management" — sha256:d00858c7d4547b9a459b6e4973c71b083f58de6bc93e2022dfc3f7a6731311b9

[^anthropic_evals]: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — "explicit warning against self-congratulation machines" — sha256:b05a471aaaba3c48dd19b3305d0e16b0a14603e0a42c6336451d698f401eab2c

---

## Infrastructure-as-Code Adaptation

Pulumi adapted the Dark Factory pattern to IaC: a four-layer architecture where AI agents generate, validate, and apply infrastructure changes with human oversight at the policy gate rather than the code level.[^pulumi_dark] Their Agent Skills feature uses markdown skill files to encode org standards, IaC patterns, and policy gates for Claude Code/Cursor/Codex.[^pulumi_skills]

[^pulumi_dark]: https://www.pulumi.com/blog/dark-factory-pattern-pulumi-autonomous-iac/ — "four-layer architecture" — sha256:121b5b1e2999f2923f667f510e2ec3665cbf05368249ef351ea4f74aeb203e7b

[^pulumi_skills]: https://www.pulumi.com/blog/pulumi-agent-skills/ — "markdown skill files encode org standards/IaC patterns/policy gates for Claude Code/Cursor/Codex" — sha256:099f3c42a82d5db68817da96a4f838e8ec1df85e8b94d6f6de3f96f79f7f935b
