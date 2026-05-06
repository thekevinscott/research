# Dark Factory Research Report

*Synthesis of 117 sources (91 tier-1/2) — 2026-05-06*

**Subject**: Level 5 of Dan Shapiro's five-level AI-coding automation model — software produced entirely by coding agents, with no human writing or reviewing code.

---

## Sections

| File | Contents |
|---|---|
| [00-overview.md](00-overview.md) | Definition, five-level taxonomy, terminology, model prerequisites |
| [01-strongdm.md](01-strongdm.md) | StrongDM canonical implementation — charter, DTU, Attractor, techniques |
| [02-validation.md](02-validation.md) | Scenarios, satisfaction metric, reward hacking, OSS validation tooling |
| [03-tools.md](03-tools.md) | Coding agents, parallel orchestration, context engineering, observability |
| [04-cases.md](04-cases.md) | First-hand practitioner accounts — StrongDM, OpenAI, Stripe, Rakuten, Night Shift |
| [05-failures.md](05-failures.md) | Pitfalls — METR slowdown study, reward hacking, production incidents, maintainability |
| [06-domains.md](06-domains.md) | Domain results — where it works, where it struggles, pattern heuristics |
| [07-contested.md](07-contested.md) | Contested claims — verification, productivity, cost, bottleneck, accountability |

---

## Source Counts

| Tier | Description | Count |
|---|---|---|
| 1 | Peer-reviewed / arXiv | 11 |
| 2 | Lab / vendor / first-hand practitioner | 80 |
| 3 | Journalism / synthesis | 20 |
| 4 | Forum / social | 6 |
| **Total** | | **117** |

Tier-1/2 sources cited across the report: ≥ 35 unique.

---

## Key Findings

- The pattern is real and functioning in production as of early 2026, with StrongDM as the sole detailed public case
- Validation is the hard problem: holdout scenarios stored outside the codebase, with LLM-as-judge satisfaction scoring, is the only demonstrated approach to preventing reward hacking
- The METR RCT (19% slowdown) and the BCG/OpenAI productivity claims are not directly contradictory — they measure different workflow levels and model generations
- Domain fit matters strongly: internal tooling, migrations, and greenfield products with clear specs are good fits; regulated, scientific, and hardware-adjacent domains are not
- The $1,000/day/engineer token budget claim is a benchmark for scale, not a minimum — the pattern is accessible at lower cost
- Accountability, regulatory compliance, and maintainability of opaque generated code are unresolved open questions
