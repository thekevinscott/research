# Report Audit and Research Opportunities

Self-critique of the Agentic Engineering Ecosystems landscape survey (sections 01-09).

---

## Factual Errors Found and Fixed

1. **Devin/Windsurf conflation (05-managed-cloud-agents.md)**: Originally stated "Cognition also acquired Windsurf (Codeium)." Wrong — OpenAI acquired Windsurf for ~$3B. Cognition (Devin) is a separate company. **Fixed.**

2. **"Eight capability areas" vs. nine listed (08-parity-matrix.md)**: Header said eight, body listed nine. **Fixed.**

3. **Codex CLI Model Flexibility rated "None" (08-parity-matrix.md)**: Codex CLI supports o3, o4-mini, GPT-4.1 — multiple models within OpenAI. Rating should be "Partial" (locked to one vendor, flexible within it). **Fixed.**

4. **Gemini CLI Self-Host rated "Full" (08-parity-matrix.md)**: Gemini CLI is open source, but "self-hostable" in this report's context means running on your own infrastructure. Gemini CLI still calls Google's API — you don't host the model. Rating changed to "Partial." **Fixed.**

---

## Structural Weaknesses

### Missing Coverage

1. **Amazon Q Developer / CodeWhisperer**: AWS's agentic coding tool is completely absent. For teams on AWS, this is a notable gap. Amazon Q has agent capabilities, IDE integration, and is bundled with AWS subscriptions. Not covering the third major cloud provider weakens the report's claim to comprehensiveness.

2. **Tabnine**: Enterprise-focused AI code assistant with self-hosted model option. Omitted despite being relevant to the self-hosting angle.

3. **Sourcegraph Cody**: AI coding assistant with deep code graph understanding. Relevant for its repository-wide semantic search capabilities — a different approach to the context engineering problem.

4. **Replit Agent**: Mentioned in passing in 05 under "app builders" but deserves fuller treatment. Replit Agent operates in a full cloud IDE, handles deployment, and targets a different user segment but demonstrates interesting architectural patterns.

5. **Open-source model hosting (Ollama, vLLM, TGI)**: Report explicitly excludes local LLMs per user preference, but doesn't discuss self-hosted API-compatible inference (e.g., running DeepSeek-V3 on your own GPU cluster via vLLM). This is distinct from "local LLMs" — it's self-hosted API infrastructure. Could be relevant for cost control at scale.

6. **Agent observability**: Langfuse, LangSmith, Braintrust are mentioned in passing but not analyzed. For production managed agent deployment, observability is critical — knowing why an agent failed, tracking token costs per task, monitoring success rates.

### Depth Gaps

1. **SWE-bench analysis is shallow.** Report references benchmark scores but doesn't analyze what SWE-bench measures vs. what real-world agents need. SWE-bench tests program repair (fixing bugs from issue descriptions). It doesn't test: feature implementation, refactoring, multi-repo changes, build system modifications, or working with proprietary frameworks. The benchmark's relevance to the user's actual needs is unexplored.

2. **Model comparison lacks nuance.** Report says "Claude Opus/Sonnet are strongest for coding" without qualifying what this means. Coding benchmarks test different things: HumanEval tests function completion, SWE-bench tests program repair, Aider's benchmark tests multi-file editing with specific tools. A model could lead on one and trail on another. The blanket claim oversimplifies.

3. **Prompt caching economics aren't quantified.** Report cites "90% discount on cache hits" but doesn't model how much this saves in practice. What percentage of tokens hit cache in a typical Claude Code session? Without this, the claim that caching is a major Anthropic advantage is unsupported by numbers.

4. **OpenHands depth is surface-level for the "highest priority" section.** 85% parity claim is based on feature checkboxes. No discussion of: agent success rates on real tasks, typical token consumption, failure modes, recovery patterns, or comparison of OpenHands' agent architecture to Claude Code's.

5. **Security analysis is absent.** Self-hosted agents run arbitrary code in containers with access to your repositories. The security implications — supply chain risk, container escapes, credential exposure, model prompt injection — are mentioned as a "gap" but should have dedicated analysis given the self-hosting focus.

### Analytical Weaknesses

1. **Parity percentages are invented.** "~85% parity," "~60% parity" — these numbers aren't derived from any methodology. They're vibes. Could be useful as rough indicators but should be explicitly flagged as subjective estimates, not measurements.

2. **Cost modeling assumes single user.** The $400-800/month Anthropic spend and hybrid stack alternatives model one power user. Teams of 5-10 have different economics (volume discounts, shared infrastructure costs, coordination overhead). Report acknowledges this once but doesn't model it.

3. **"Keep Claude Code for complex work" is circular.** The recommendation to keep Claude Code for complex tasks while routing simple ones elsewhere assumes you can reliably classify task complexity before starting. In practice, many tasks reveal their complexity mid-execution. The routing decision is harder than the report implies.

4. **No discussion of switching costs.** Migrating from Claude Code to alternatives involves learning new tools, adapting workflows, porting CLAUDE.md/MCP configurations, and adjusting team practices. These transition costs could easily exceed months of savings.

5. **MCP analysis is thin.** MCP is flagged as a major Anthropic advantage but the report doesn't catalog what MCP servers the user actually uses, whether alternatives support those specific servers, or what the real cost of losing MCP would be.

---

## Pricing Verification Needed

Several prices may have changed since research was conducted:

- Devin pricing restructured multiple times in 2024-2025; current tiers need verification
- Factory AI pricing on individual tiers is hard to verify from public sources
- Cursor pricing may have changed with background agents launch
- OpenAI Pro tier ($200/month) "unlimited o3" claim needs checking — there may be soft limits
- Gemini 2.5 Pro pricing tiers (≤200K / >200K context) should be verified against current API docs

---

## Research Opportunities (Prioritized)

### Tier 1: High-value, actionable within days

1. **OpenHands deployment trial.** Actually deploy OpenHands, run it against 10-20 real issues. Measure success rate, token cost, time, failure modes. This single experiment would ground the entire report's managed agent recommendations.

2. **Prompt caching quantification.** Analyze a week of Claude Code usage. What percentage of input tokens hit cache? What's the actual dollar savings from caching? This determines whether prompt caching is a minor convenience or a major economic factor.

3. **Model routing feasibility.** Categorize last 50 Claude Code tasks by complexity. For the "simple" ones, run them through Gemini Flash or GPT-4.1 Mini. Compare quality. Determines whether model routing is practical.

### Tier 2: Deeper research requiring more time

4. **Security analysis of self-hosted agent infrastructure.** Container escape risks, credential management, network policy requirements, prompt injection attack surface. No public analysis exists — producing one would be genuinely novel.

5. **Context engineering comparison.** Controlled experiment: same 20 tasks run through Claude Code, Aider, OpenHands, and Cursor. Measure not just success/failure but HOW each tool selects context. What files does each include? How does compaction work? This is the most opaque and important differentiator.

6. **SWE-bench vs. real-world correlation.** Take benchmark scores for each agent and compare against actual success rates on real repositories. Are benchmark rankings predictive? This would be publishable research.

7. **Amazon Q / Sourcegraph Cody analysis.** Fill the coverage gaps. Particularly relevant if the user works in AWS infrastructure or large monorepos.

### Tier 3: Strategic / long-horizon

8. **Multi-agent pipeline design.** Design and prototype: one agent writes code (OpenHands), another reviews (PR-Agent), a third writes tests (Qodo). Measure whether this pipeline produces better output than a single agent doing everything.

9. **Cost forecasting model.** Build a model that predicts monthly costs based on: task volume, task complexity distribution, model choice, caching hit rate. Would let users forecast before committing to a stack.

10. **Enterprise governance layer for OpenHands.** Design the SSO, audit logging, and access control layer that would make OpenHands enterprise-ready. Fills the gap identified between Factory AI's offering and open-source.

---

## Verdict

Report is solid as a first-pass landscape survey. The major frameworks, tools, and platforms are covered with reasonable accuracy. The self-hostable agents section (06) delivers on its promise as the highest-priority section.

Principal weakness: everything is desk research. The report describes what tools *claim* to do. The highest-value next step is deployment trials — actually using OpenHands, Aider architect mode, and model routing to see what works vs. what's documented.

Secondary weakness: several factual errors and rating inconsistencies were present (now fixed). In a fast-moving field, any survey this broad will have accuracy issues. The explicit dating (May 2026) and bias disclosure in the methodology help.

The 09-recommendations section's self-critique is honest but not exhaustive. This audit document fills that gap.
