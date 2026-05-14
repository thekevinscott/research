# Recommendations and Self-Critique

---

## Recommended Strategy

### For the User's Specific Situation

Profile: Power user, 4-6 hours/day coding with Claude Code, $400-800/month Anthropic spend, interested in self-hostable managed agents, not interested in local LLMs or pure API cost optimization.

**Recommended approach: Hybrid stack.**

Keep Claude Code as primary interactive tool. Supplement with self-hosted managed agents and cheaper models for delegated tasks.

### Tier 1: Immediate (this week)

**Deploy OpenHands for managed agents.** Docker Compose on any server with 8GB+ RAM. Configure GitHub App on your repos. Route issue-fixing tasks to OpenHands instead of Anthropic's managed agents.

- Same model quality (OpenHands can call Claude API)
- No subscription overhead — pay only API tokens
- Full control over execution environment
- Estimated savings: $50-200/month on managed agent costs

**Install PR-Agent for automated review.** Self-hosted, runs on every PR. Use Claude Sonnet via API. Catches issues before human review, reduces iteration cycles.

### Tier 2: This month

**Set up Aider in CI for simple issues.** GitHub Actions workflow triggered by label. For well-scoped bugs and small features. Use architect mode: Claude Sonnet plans, DeepSeek edits. Costs roughly 60-80% less than all-Claude.

**Add Cline to VS Code as secondary agent.** Model-flexible. When a task doesn't need Claude Opus-level reasoning, route through Cline with Gemini Flash or GPT-4.1 Mini. Keep Claude Code for complex architectural work.

### Tier 3: If spend exceeds $600/month

**Evaluate Cursor Pro ($20/month)** as partial Claude Code replacement for day-to-day coding. Background agents for async work. Codebase indexing for faster context retrieval. Multi-model support.

**Consider model routing**: Claude Opus for planning/architecture, Claude Sonnet for implementation, Gemini 2.5 Flash ($0.15/$0.60/M) for routine tasks (formatting, simple refactors, boilerplate). OpenRouter or LiteLLM can automate routing.

---

## Cost Modeling

### Current state (estimated)

| Category | Monthly Cost |
|----------|-------------|
| Claude Max subscription | $100-200 |
| API for managed agents | $50-200 |
| Total Anthropic | $150-400+ |

### Hybrid stack (estimated)

| Category | Monthly Cost |
|----------|-------------|
| Claude Code (keep for complex work) | $100-200 |
| OpenHands managed agents (Claude API) | $30-100 |
| Aider-in-CI (DeepSeek for editing) | $5-20 |
| PR-Agent (Claude Sonnet for review) | $10-30 |
| Server for OpenHands | $20-40 |
| Total | $165-390 |

Savings are modest at the low end (~10%) but significant at the high end (~40-50%). The real value is flexibility — ability to route tasks to appropriate models rather than paying Opus pricing for everything.

### Break-even analysis

Self-hosting only saves money if managed agent volume is high enough to offset server costs. At fewer than ~5 agent tasks/week, Anthropic's managed agents (pay-per-token, no infra) may be cheaper despite higher per-token cost.

---

## What This Report Gets Right

1. **Market landscape is accurately mapped.** Major players covered, pricing verified from official sources, capabilities described from documentation and user reports.

2. **Self-hostable options are real.** OpenHands at 50K+ stars with GitHub resolver is genuinely production-viable for managed agent workflows. Not a research prototype.

3. **Parity framing is honest.** No tool fully replaces Anthropic. The report doesn't pretend otherwise.

4. **Cost analysis is grounded.** Based on published pricing, not theoretical savings.

---

## What This Report Gets Wrong (or Might)

### Systematic biases

1. **Benchmark bias.** SWE-bench scores are referenced but overweighted in the ecosystem. Real-world agent performance depends on codebase size, language, framework, test infrastructure — none captured by benchmarks. An agent scoring 40% on SWE-bench Verified might handle 80% of your specific tasks or 10% of them.

2. **Documentation-as-capability bias.** Features documented don't always work as described. OpenHands' GitHub resolver, for example, is documented as turnkey — but deployment friction, edge cases in webhook handling, and container resource management aren't captured by feature lists. Production experience would change some ratings.

3. **Recency bias.** Information gathered May 2026. This field changes monthly. Specific risks:
   - Windsurf's OpenAI acquisition could restructure the competitive landscape
   - Cursor's background agents are still rolling out — maturity assessment may be premature
   - OpenAI could release a Claude Code competitor with MCP support
   - Anthropic could slash pricing, eliminating the cost motivation for alternatives
   - Google could ship a mature Jules, changing the managed agent picture

4. **Survivorship bias.** Report covers existing tools. Tools that failed or pivoted (Sweep shut down, Windsurf acquired) are mentioned but not analyzed deeply. The failure modes of dead products are informative — they suggest that managed agent products with weak underlying models or poor UX don't survive regardless of first-mover advantage.

5. **Individual-user bias.** This analysis is from the perspective of one power user. Team dynamics change the calculus: a 10-person team might find GitHub Copilot Agent's bundled pricing ($390/month for the whole team) better than assembling a self-hosted stack.

### Specific uncertainties

- **OpenHands production reliability.** The 85% parity rating is based on documented features. Unknown: failure rate on real-world tasks, resource consumption, how well it handles large monorepos.

- **Model quality trajectory.** Claude Opus/Sonnet are currently strongest for coding. If GPT-5 or Gemini 2.5 Ultra close the gap, model flexibility becomes more valuable than model quality — shifting recommendations toward model-agnostic tools.

- **MCP trajectory.** If MCP becomes universal (adopted by all tools), MCP support stops being a differentiator. If it fragments or stalls, tools built on MCP carry risk.

- **Pricing stability.** All pricing here is current as of May 2026. The trend is downward (Devin from $500→$20-80, model inference costs dropping ~50%/year). Recommendations based on current pricing may be obsolete within 6 months.

---

## Research Gaps Identified

### Questions this report cannot answer from desk research

1. **Actual agent success rates.** How often does OpenHands/SWE-agent/Aider-in-CI successfully resolve a real issue end-to-end? Published benchmarks use curated datasets. Real repos have build systems, flaky tests, undocumented dependencies, and ambiguous issue descriptions.

2. **Infrastructure overhead.** What does it actually cost (time and money) to maintain a self-hosted OpenHands deployment? How often does it break? How much DevOps time does it consume?

3. **Context engineering quality.** Claude Code's secret weapon is context engineering — the heuristics for what to include in each prompt. How do competitors' context strategies compare? This requires controlled experiments, not documentation review.

4. **Team adoption friction.** How hard is it for a team of 5-10 engineers to adopt a self-hosted agent stack? What's the onboarding time? What breaks when the person who set it up leaves?

5. **Security posture.** Running AI agents that execute arbitrary code in containers connected to your repos has security implications. No systematic security analysis of these tools exists in public literature.

6. **Long-running task performance.** Managed agents sometimes need 30+ minutes for complex tasks. How do self-hosted solutions handle long-running execution? Timeouts, resource exhaustion, connection drops?

7. **Multi-repo workflows.** Most analysis assumes single-repo work. How do these tools handle tasks spanning multiple repositories?

8. **Enterprise governance.** For organizations needing audit trails, access controls, and compliance: what's the gap between Factory AI's enterprise offering and a self-hosted OpenHands + your own governance layer?

---

## Suggested Experiments

### Experiment 1: OpenHands Deployment Trial (2-3 hours)

Deploy OpenHands on a test server. Configure GitHub resolver on a non-critical repo. Create 10 issues of varying complexity (typo fix, simple bug, medium feature, complex refactor). Measure: success rate, time to PR, token cost, manual intervention needed.

### Experiment 2: Aider Architect Mode Cost Comparison (1 hour)

Run 10 identical tasks through:
- Claude Code (Sonnet)
- Aider with Claude Sonnet
- Aider architect mode (Claude Sonnet plans, DeepSeek edits)

Compare: output quality, total token cost, time to completion.

### Experiment 3: Model Routing Baseline (2 hours)

Categorize your last 50 Claude Code interactions by complexity (simple/medium/complex). Estimate how many could have used a cheaper model. Calculate theoretical savings with model routing.

### Experiment 4: Managed Agent Head-to-Head (4 hours)

Create identical issues on:
- Anthropic managed agents (claude-code-action)
- OpenHands resolver
- GitHub Copilot coding agent
- Aider-in-CI

Compare: success rate, PR quality, iteration handling, total cost.

---

## The Landscape in One Paragraph

Agentic engineering tooling is commoditizing rapidly. The basic capability — LLM reads code, writes code, runs tests, creates PRs — is available from a dozen providers at $20-200/month. What differentiates is integration depth (Anthropic), platform leverage (GitHub), open flexibility (Aider, OpenHands), and enterprise governance (Factory). For a power user spending $400-800/month on Anthropic, the viable path is a hybrid: keep Claude Code for complex interactive work, deploy OpenHands for managed agents, use model routing for cost control. Full parity without Anthropic is achievable at ~80% but requires accepting the loss of /remote-control, prompt caching economics, and single-vendor coherence. Whether that trade-off is worth $200-400/month depends on how much those features matter to your daily workflow.

---

## Sources

- Cost estimates based on published pricing from sections 01-07
- Strategy recommendations synthesized from parity analysis (section 08)
- Self-critique methodology: identifying systematic biases, specific uncertainties, and falsifiable predictions
