# Cases: First-Hand Reports and Practitioner Accounts

*Section 5 of 8 — synthesis report, 2026-05-06*

---

## StrongDM: Security Software, Three Engineers

The canonical case. By October 2025 — three months after founding and before the November model inflection — a three-person team had working demos of their coding agent harness, Digital Twin Universe clones of six services, and a swarm of simulated test agents running through scenarios. Willison's assessment after seeing it: "It felt like a glimpse of one potential future of software development."[^78862ac8]

The product domain is notable: access management and security software. This is the last category most practitioners would choose for unreviewed LLM code. StrongDM's implicit argument is that behavioral verification via adversarial scenario testing is a *stronger* correctness guarantee than human code review — reviewers miss bugs, scenarios don't.

[^78862ac8]: https://simonwillison.net/2026/Feb/7/software-factory/ — "It felt like a glimpse of one potential future of software development, where software engineers move from building the code to building and then semi-monitoring the systems that build the code." — sha256:78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3

---

## OpenAI: Symphony and Harness Engineering

Ryan Lopopolo (OpenAI Frontier) published the most detailed account of OpenAI's Dark Factory practice in April 2026.[^latent_space] The constraint he started with: he refused to write any code himself, forcing the agent to do the job end-to-end. Result: a >1M-LOC codebase with 0% human-written and 0% human-reviewed code before merge, running at roughly 1 billion tokens per day (~$2–3k/day with caching).

The infrastructure he built to enable this is **Symphony** (`github.com/openai/symphony`): an Elixir-based orchestration layer for spinning up, supervising, reworking, and coordinating large numbers of Codex agents across tickets and repos.[^latent_space] A companion concept is **"ghost libraries"** — spec-driven reference implementations that set up a system of Codex agents "all extensively prompted with the specificity of a proper PRD spec, but without full implementation." The ghost library is the spec artifact; agents generate the actual code from it.

Lopopolo's framing — "harness engineering" — positions the harness, not the model, as the primary engineering surface. The key shift: from predefined scaffolds to reasoning-model-led workflows where the harness defines the box and the model chooses how to proceed. He called it borderline "negligent" if you aren't using >1B tokens/day.

BCG Platinion independently cites the same case: OpenAI building "a million-line product in five months with just three engineers and no manually written code whatsoever, representing speed improvement gains of 10x."[^bcg]

[^latent_space]: https://www.latent.space/p/harness-eng — "Symphony**, OpenAI's internal Elixir-based orchestration layer for spinning up, supervising, reworking, and coordinating large numbers of coding agents" — sha256:3eb41e9a5454c108bae1aa4b5a45d13cd3585b32b5a90fffa2ee8897afdd022c
[^bcg]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "average. OpenAI was able to build a million-line product in five months with just three engineers and no manually" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258
---

## Stripe: Minions at Scale

Stripe's internal "Minions" system generates 1,000+ pull requests per week autonomously — primarily for internal tooling. Their architecture mixes deterministic and agentic nodes in a blueprint pattern for high-volume PR generation.[^stripe_minions] This is Level 3–4 territory (humans still review PRs), but illustrates the scale achievable with agent automation applied to bounded domains.

[^stripe_minions]: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — "0and%20how%20we%20built%20them." — sha256:58e6a45811ed3bb0d2aa50d8c4d749889e27f219014cb15ad3be83d9b7c848d3
---

## Rakuten: 12.5M-Line vLLM Codebase

A Rakuten engineer ran Claude Code autonomously for 7 hours over a 12.5 million-line vLLM codebase.[^rakuten] This demonstrates the pattern's reach into large existing codebases — not just greenfield development — though it remains at the high end of what practitioners report attempting.

[^rakuten]: https://claude.com/customers/rakuten — "view") + [Claude Code](/product/claude-code "/product/claude-code") + [Claude Cowork](/product/cowork" — sha256:005d0202b7b01c3d5a63cd56381931e80ee277445988a401b4771faaa55bf9f1
---

## Jamon Holmgren: The Night Shift Workflow

Jamon Holmgren documents a practical hybrid pattern he calls the **Night Shift**:[^jamon] humans write specs during the day, agents execute autonomously overnight. His report: ~5x faster than prior workflows, better quality, and "I'm having fun again."

Key observations from his experience:
- Spec writing is the hard part: "Specs describe the feature, all the edge cases to cover, everything I can think of. They're well organized — not for the agent, but for ME."
- Human time and "human token usage" are the constrained, expensive resources. Agent tokens are cheap and practically unconstrained.
- He does not babysit agents or read their plans — he prepares the work, lets them run, and reviews outcomes.

This is closer to Level 4 than pure Level 5, but represents the practitioner-accessible version of the pattern.

[^jamon]: https://jamon.dev/night-shift — "too much. My current agentic workflow is about 5x faster, better quality, I understand the system better, and **I'm" — sha256:7c1f2bbc6d1a9bb214fabc47f5c4524a4b04574aaba6bce7ce63b3f005f104ab
---

## OctopusGarden: Community Implementation

OctopusGarden (`github.com/foundatron/octopusgarden`, CLI: `octog`) started as a weekend build after the StrongDM writeup and has since grown into the most complete open-source Dark Factory available. Brew-installable, written in Go, MIT licensed.[^octopus_readme]

The architecture matches StrongDM's pattern closely: spec + holdout scenarios in, Docker-built code out, LLM-as-judge satisfaction scoring, convergence loop. It adds several features beyond the minimal pattern: Preflight (spec/scenario quality check before running), Wonder/Reflect (stall recovery), Model Escalation (cheap model first, escalate on stalls), Gene Transfusion (`octog extract`), and Stratified Validation (tier scenarios by difficulty).

The builder's original HN post-mortem remains the most candid practitioner account in the corpus:[^octopus_hn]

- Generated code works behaviorally but is "pretty wild and messy" internally
- Debugging is harder; compliance boxes (SOC 2, ISO 27001) are "a nightmare"
- AI availability becomes an operational dependency (Claude outage blocked smoke tests)
- "The unit of responsibility keeps growing" — SRE teams managing meshes of factory-generated services

[^octopus_hn]: https://news.ycombinator.com/item?id=47226107 — "It works. The phenotype is (largely) correct, but the genotype is pretty wild and messy." — sha256:18f7206c7c967d28de86dcce51aa176110e10b1bf79a8286eec206f7a2cb329d
[^octopus_readme]: https://github.com/foundatron/octopusgarden — "scenarios are a **holdout set**. The coding agent never sees them during" — sha256:c421eb018c072a7bac1c0a398a63c578925b3f7388fb1c984a0c6a9fd4314d37
---

## Anthropic 2026 Trends Report

Anthropic's 2026 Agentic Coding Trends Report documents agent adoption spreading beyond engineering into sales, customer success, and legal — organizations running agent-generated code in production across more domains than the initial ML/infra early adopters.[^anthropic_trends] This suggests the Dark Factory pattern is diffusing beyond the technically sophisticated early teams.

[^anthropic_trends]: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf — "not certainties about tomorrow. We offer them as a framework for thinking about the year In 2025, coding agents moved from experimental tools to" — sha256:c0bad869f9e3e76484a0f06aad5c4015eaf5ad1d7286e684516d769f9988478a