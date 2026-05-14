# Agentic Engineering Ecosystems: Landscape Survey

A comprehensive analysis of the agentic software engineering tool landscape as of May 2026. Evaluates alternatives to Anthropic's Claude Code ecosystem with emphasis on self-hostable managed agent infrastructure.

---

## How to Read This Report

Start with your primary interest:

- **"What exists?"** — Read sections 01-05 for a market overview
- **"Can I self-host managed agents?"** — Start with [06-self-hostable-agents.md](research/06-self-hostable-agents.md)
- **"What should I use?"** — Jump to [08-parity-matrix.md](research/08-parity-matrix.md) and [09-recommendations.md](research/09-recommendations.md)
- **"I want to build custom agents"** — See [07-agent-frameworks.md](research/07-agent-frameworks.md)

Each section is self-contained (~1500-2000 words). Cross-references are inline.

---

## Table of Contents

| # | File | Topic | Key Finding |
|---|------|-------|-------------|
| 01 | [anthropic-baseline.md](research/01-anthropic-baseline.md) | Anthropic reference | The benchmark: CLI + App sync + managed agents + MCP ecosystem |
| 02 | [openai-codex.md](research/02-openai-codex.md) | OpenAI ecosystem | Broadest surface area; open-source CLI, no-internet cloud agents, Agents SDK |
| 03 | [google-gemini.md](research/03-google-gemini.md) | Google/Gemini | 1M context window, aggressive free tier, less mature agent tooling |
| 04 | [indie-cli-tools.md](research/04-indie-cli-tools.md) | Independent CLI/IDE tools | Aider (best open-source CLI), Cursor (best IDE), Cline (best VS Code extension) |
| 05 | [managed-cloud-agents.md](research/05-managed-cloud-agents.md) | Cloud agent platforms | GitHub Copilot Agent is closest competitor; market pricing collapsed to $20-80/mo |
| 06 | [self-hostable-agents.md](research/06-self-hostable-agents.md) | Self-hostable infrastructure | OpenHands achieves ~85% parity; turnkey Docker deployment with GitHub resolver |
| 07 | [agent-frameworks.md](research/07-agent-frameworks.md) | Agent-building SDKs | Construction kits, not finished products; LangGraph most viable for custom managed agents |
| 08 | [parity-matrix.md](research/08-parity-matrix.md) | Feature comparison | No single tool replaces Anthropic; best composite stacks reach ~80% parity |
| 09 | [recommendations.md](research/09-recommendations.md) | Strategy and self-critique | Hybrid stack recommended; honest gaps and research opportunities identified |
| 10 | [audit.md](research/10-audit.md) | Report audit | Factual corrections, structural weaknesses, prioritized research opportunities |
| 11 | [amazon-q-sourcegraph.md](research/11-amazon-q-sourcegraph.md) | Coverage gaps | Amazon Q Developer (~75% parity at $19/mo); Sourcegraph Cody (enterprise context layer) |
| 12 | [mcp-deep-dive.md](research/12-mcp-deep-dive.md) | MCP ecosystem | Near-universal adoption (70+ clients); no longer an Anthropic differentiator; security vulnerabilities documented |
| 13 | [caching-economics.md](research/13-caching-economics.md) | Prompt caching | 90% discount not unique (Google matches); Anthropic's real advantage is 68% hit rate in practice |
| 14 | [openhands-deep-dive.md](research/14-openhands-deep-dive.md) | OpenHands architecture | 73K stars, $23.8M raised, 64% SWE-bench, 6 git platforms, Enterprise product May 2026 |

---

## Methodology

- **Scope**: Tools that achieve or approach parity with Anthropic's agentic coding capabilities (Claude Code CLI + managed agents + MCP ecosystem)
- **Exclusions**: Local LLMs, API cost optimization strategies, non-coding AI tools
- **Sources**: Official documentation, GitHub repositories, published pricing, user reports (Reddit, HN), benchmark results
- **Verification**: Pricing verified from official sources where available. Capabilities described from documentation; production experience notes are flagged as such.
- **Bias disclosure**: Author is an Anthropic power user. Report attempts steel-man of competitors but may underweight UX polish of tools not personally used.

---

## Key Findings

1. **Self-hosted managed agents are viable.** OpenHands (50K+ GitHub stars, MIT license) provides near-parity with Anthropic's managed agents. Deploy via Docker, configure GitHub App, route issues to agent. Uses any model via API.

2. **No single tool replaces Anthropic's integrated experience.** The /remote-control CLI↔App sync and prompt caching economics have no equivalent. Multi-tool stacks achieve 75-85% parity.

3. **Market is commoditizing.** Managed agent pricing collapsed from $500/month (Devin early access) to $20-80/month across providers. Differentiation is execution quality and integration depth, not having an agent.

4. **GitHub is Anthropic's strongest competitor.** Native platform integration + bundled pricing + multi-model support makes Copilot coding agent the most accessible alternative.

5. **Hybrid strategy is optimal.** Keep Claude Code for complex interactive work. Deploy OpenHands for managed agents. Use model routing (expensive model for planning, cheap for editing) for cost control.

6. **Amazon Q Developer is underrated.** CLI + IDE + managed agents + MCP at $19/month fixed price. For AWS-native teams, highest value per dollar in the survey.

---

## Research Date

May 2026. This field moves monthly. Pricing, features, and competitive positioning may shift significantly within 3-6 months of this writing.
