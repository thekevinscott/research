# Tools and Infrastructure

*Section 4 of 8 — synthesis report, 2026-05-06*

---

## Coding Agents

**Claude Code** (Anthropic) is the most-cited implementation backbone in Dark Factory builds in 2026.[^claude_code] Shapiro noted that "most folks at level 4 seem to find their way to Claude Code" — it provides an agentic CLI with hooks, sub-agents, MCP servers, and a skill system that serves as the harness-building surface teams build on.[^5f951b]

**Aider** — terminal-native, git-aware coding agent with strong SWE-bench scores. Suited for parallel worktree spawning: you can run N copies against N isolated branches simultaneously.

**Cline** and its fork **Roo Code** — IDE-embedded, multi-mode agents (Code/Architect/Ask/Debug modes constrain agent capabilities per phase; closest OSS analog to Attractor's multi-phase node graph).[^cline]

**OpenHands** (formerly OpenDevin) — most mature OSS coding-agent platform with a full software agent SDK, sandboxed execution, and GUI/CLI/API surface. MLSys 2026 paper documents the redesigned production toolkit.[^openhands_paper]

**GitHub Copilot coding agent** — asynchronous PR-generating agent announced by GitHub; complements the IDE assistant with autonomous background execution.[^github_copilot_agent]

[^claude_code]: https://github.com/anthropics/claude-code — "ough natural language commands. Claude Code Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps" — sha256:d109d50f7af9cd6c407bf80d469af01d25e1d53c5bd356c50a010008f3219f07
[^5f951b]: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ — "most folks at level 4 seem to find their way to Claude Code" — sha256:5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c

[^cline]: https://github.com/cline/cline — "rmission every step of the way. English | Español | Deutsch | 日本語 | 简体中文 | 繁體中文 | 한국어 Cline Download on VS Marketplace Discord r/cline Feature" — sha256:535d0fb765dc65e140c27d8401b2b9ca4692f84816e9cb049c57d9ffed569e8c
[^openhands_paper]: https://arxiv.org/abs/2511.03690 — "dev # The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents Xingyao Wang Simon" — sha256:c66594b2aca9d2e2bea9e5a5eba95ed364dcb7b2c97de31e1b40f29b2c371baa
[^github_copilot_agent]: https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/ — "t the new coding agent - The GitHub Blog" — sha256:e421f4fb6e4fb7cc20313dc200691508a5a57de44b22750125db30e3985fe862
---

## Parallel Orchestration

Scaling a Dark Factory means running many agents concurrently. The dominant pattern: spawn agents in isolated git worktrees, one per task.

**Composio Agent Orchestrator** — spawns parallel Claude Code/Codex/Aider/OpenCode agents on git worktrees with a coordination layer.

**Emdash** (YC W26) — desktop multi-agent orchestrator running 24+ CLI agents in worktrees simultaneously; provides supervised-mode oversight without blocking the agents.[^emdash]

**Cursor** found that scaling to hundreds of concurrent agents required rethinking coordination. Flat coordination with locking failed due to deadlock; their research blog documents the architectural changes required.[^cursor_scale]

[^emdash]: https://github.com/generalaction/emdash — "pports 24 CLI agents, including Claude Code, Codex, OpenCode, Gemini and Amp. Users can directly pass Linear, GitHub," — sha256:e0bf440e70c3c7396f9bb62f0ee65222b5f8654b7ba308b8855bf1a544b14370
[^cursor_scale]: https://cursor.com/blog/scaling-agents — "agents autonomously for weeks. Our goal is to understand how far we can push the frontier of agentic coding for projects that typically take human" — sha256:729f057d79f93e9d475e208c21ac66ded88377ddb6502c7036c1787cb20721a5
---

## Context Engineering

**Repomix** — packs an entire repo into AI-friendly bundles using tree-sitter compression and an MCP server; the context-packing utility agents use to fit codebases into context windows.[^repomix]

**Claude Agent SDK** (Python) — exposes the Claude Code agent loop as a library with custom tools/hooks and in-process MCP servers; the glue between orchestration and inner agent.[^agent_sdk]

**Codex CLI 0.128.0 `/goal` command** — built-in autonomous loop equivalent for long-horizon objectives that persist across sessions.[^codex_goal]

[^repomix]: https://github.com/yamadashy/repomix — "acks your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large" — sha256:c593b7f4cf71e1a1c7fec84ab5999b535e13fa0d2cb144b87a346f70101c3ac4
[^agent_sdk]: https://github.com/anthropics/claude-agent-sdk-python — "tion that the Claude Code application ( not Claude) invokes at specific points of the Claude agent loop. Hooks can" — sha256:87b3edde4ef9fef8732d74f812bd872e49e4299468ffd6878deb678676966aab
[^codex_goal]: https://simonwillison.net/2026/Apr/30/codex-goals/ — "k Blog **[Codex CLI 0.128.0 adds /goal](https://github.com/openai/codex/releases/tag/rust-v0.128.0" — sha256:988993f64825cb53547e67b12a6b2786bbdbb14f5d771d37fa08c9f8948afb61
---

## Observability and Tracing

**CXDB** (StrongDM) — self-hosted AI Context Store. Content-addressed Turn DAG; p50 append < 1ms for 10KB; branching is O(1); 70%+ storage reduction via BLAKE3.[^cxdb]

**Langfuse** — OSS LLM observability, evals, and prompt management; eval/observability substrate complementing CXDB for post-hoc agent-fleet debugging.[^langfuse]

**Anthropic's eval guidance** warns explicitly against "self-congratulation machines" — eval harnesses that produce high scores by gaming the metric rather than solving the problem. The guidance distinguishes offline benchmarks from online telemetry and recommends LLM-as-judge patterns with adversarial probing.[^anthropic_evals]

[^cxdb]: https://github.com/strongdm/cxdb — "uilt on a Turn DAG + Blob CAS architecture, CXDB gives you: - **Branch-from-any-turn**: Fork conversations at any point" — sha256:9dd9d7c5ff97ec700755c7d9c3eceb81dd797effad3c23236523ee84a72cf7ae
[^langfuse]: https://github.com/langfuse/langfuse — "s, evals, prompt management, playground, datasets. Integrates with OpenTelemetry, Langchain, OpenAI SDK, LiteLLM, and" — sha256:24fa67a403347072585bfa0116fc4eee216f7ddf06105effc4b006c64f2d432c
[^anthropic_evals]: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — "ake them difficult to evaluate. The strategies that work across deployments combine techniques to match the complexity of the systems they measure." — sha256:94e59d0e1b4e5bf46533bcfc9854cb28a58e55e2fe8f2cb18de887ff4e1e2553
---

## Infrastructure-as-Code Adaptation

Pulumi adapted the Dark Factory pattern to IaC: a four-layer architecture where AI agents generate, validate, and apply infrastructure changes with human oversight at the policy gate rather than the code level.[^pulumi_dark] Their Agent Skills feature uses markdown skill files to encode org standards, IaC patterns, and policy gates for Claude Code/Cursor/Codex.[^pulumi_skills]

[^pulumi_dark]: https://www.pulumi.com/blog/dark-factory-pattern-pulumi-autonomous-iac/ — "e using your favorite language. [Get started →](/docs/get-started/ "/docs/get-started/") --- ##### Recent Posts * [The Dark Factory Pattern for" — sha256:121b5b1e2999f2923f667f510e2ec3665cbf05368249ef351ea4f74aeb203e7b
[^pulumi_skills]: https://www.pulumi.com/blog/pulumi-agent-skills/ — "including infrastructure code. Tools like Claude Code, Cursor, and GitHub Copilot can generate code, explain complex systems, and automate tedious" — sha256:fd4b0c8f67f6c6f91ae759619a77ece85c2bc985cfe9b8aeeeb9e9c3fb59d56a