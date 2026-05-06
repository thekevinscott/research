# Cases: First-Hand Reports and Practitioner Accounts

*Section 5 of 8 — synthesis report, 2026-05-06*

---

## StrongDM: Security Software, Three Engineers

The canonical case. By October 2025 — three months after founding and before the November model inflection — a three-person team had working demos of their coding agent harness, Digital Twin Universe clones of six services, and a swarm of simulated test agents running through scenarios. Willison's assessment after seeing it: "It felt like a glimpse of one potential future of software development."[^78862ac8]

The product domain is notable: access management and security software. This is the last category most practitioners would choose for unreviewed LLM code. StrongDM's implicit argument is that behavioral verification via adversarial scenario testing is a *stronger* correctness guarantee than human code review — reviewers miss bugs, scenarios don't.

[^78862ac8]: https://simonwillison.net/2026/Feb/7/software-factory/ — "It felt like a glimpse of one potential future of software development, where software engineers move from building the code to building and then semi-monitoring the systems that build the code." — sha256:78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3

---

## OpenAI: 1M-LOC System, Three Engineers, Five Months

BCG Platinion cites OpenAI building "a million-line product in five months with just three engineers and no manually written code whatsoever, representing speed improvement gains of 10x."[^bcg] A more detailed account from Latent Space confirms: Ryan Lopopolo (OpenAI Frontier) shipped a 1M-LOC system with 0% human-written / 0% human-reviewed code via deterministic CI gates and dependency-direction enforcement.[^latent_space]

[^bcg]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "OpenAI was able to build a million-line product in five months with just three engineers and no manually written code whatsoever, representing speed improvement gains of 10x" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258

[^latent_space]: https://www.latent.space/p/harness-eng — "shipping a 1M-LOC system with 0% human-written / 0% human-reviewed code via deterministic CI gates and dependency-direction enforcement" — sha256:3eae0728ec4fb880f4a9415ffba5601f67c498fd8e5566ee277ae04448ebb87c

---

## Stripe: Minions at Scale

Stripe's internal "Minions" system generates 1,000+ pull requests per week autonomously — primarily for internal tooling. Their architecture mixes deterministic and agentic nodes in a blueprint pattern for high-volume PR generation.[^stripe_minions] This is Level 3–4 territory (humans still review PRs), but illustrates the scale achievable with agent automation applied to bounded domains.

[^stripe_minions]: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — "Stripe's Minions ship 1000+ PRs/week of one-shot" — sha256:5af13a18d374026eb8f292635c140bcbb084e12e4c51d2cbc098556815b512a3

---

## Rakuten: 12.5M-Line vLLM Codebase

A Rakuten engineer ran Claude Code autonomously for 7 hours over a 12.5 million-line vLLM codebase.[^rakuten] This demonstrates the pattern's reach into large existing codebases — not just greenfield development — though it remains at the high end of what practitioners report attempting.

[^rakuten]: https://claude.com/customers/rakuten — "Rakuten engineer ran Claude Code autonomously for 7 hours over a 12.5M-line vLLM codebase" — sha256:ad9bc036afd03b4699730dd2dbb2959c7d9dce201a12254a314738f5768de092

---

## Jamon Holmgren: The Night Shift Workflow

Jamon Holmgren documents a practical hybrid pattern he calls the **Night Shift**:[^jamon] humans write specs during the day, agents execute autonomously overnight. His report: ~5x faster than prior workflows, better quality, and "I'm having fun again."

Key observations from his experience:
- Spec writing is the hard part: "Specs describe the feature, all the edge cases to cover, everything I can think of. They're well organized — not for the agent, but for ME."
- Human time and "human token usage" are the constrained, expensive resources. Agent tokens are cheap and practically unconstrained.
- He does not babysit agents or read their plans — he prepares the work, lets them run, and reviews outcomes.

This is closer to Level 4 than pure Level 5, but represents the practitioner-accessible version of the pattern.

[^jamon]: https://jamon.dev/night-shift — "My current agentic workflow is about 5x faster, better quality, I understand the system better, and I'm having fun again." — sha256:7c1f2bbc6d1a9bb214fabc47f5c4524a4b04574aaba6bce7ce63b3f005f104ab

---

## OctopusGarden: Weekend Replication

One engineer built an open-source Dark Factory implementation (OctopusGarden) over a weekend after reading StrongDM's writeup. Results on CRUD/REST API apps: it works. The honest post-mortem from the builder:[^octopus]

- Generated code is behaviorally correct but internally messy
- Debugging is harder than with hand-written code
- Compliance (SOC 2, ISO 27001) is "a nightmare" with current tooling
- Dependency on AI availability is a new operational risk (Claude outage blocked smoke tests)
- The unit of responsibility is growing: "Most SRE teams manage 1-5 services at big companies. Will that number increase per team?"

This community replication confirms the pattern is accessible to individual practitioners, while surfacing the operational concerns that StrongDM's polished writeup elides.

[^octopus]: https://github.com/foundatron/octopusgarden — "working open-source Dark Factory with Docker-isolated build" — sha256:535d0fb765dc65e140c27d8401b2b9ca4692f84816e9cb049c57d9ffed569e8c

---

## Anthropic 2026 Trends Report

Anthropic's 2026 Agentic Coding Trends Report documents agent adoption spreading beyond engineering into sales, customer success, and legal — organizations running agent-generated code in production across more domains than the initial ML/infra early adopters.[^anthropic_trends] This suggests the Dark Factory pattern is diffusing beyond the technically sophisticated early teams.

[^anthropic_trends]: https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf — "cross-domain enterprise: Anthropic's 2026 trends report documents agent adoption beyond engineering (sales)" — sha256:5bbcd7582a9e557a5b57235b6f3912dd5876db4282ec604c7167ab9a7d434a8c
