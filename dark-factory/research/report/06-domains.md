# Domain Results

*Section 7 of 8 — synthesis report, 2026-05-06*

---

## Where It Works

### Internal Tooling and Migration

The clearest wins are in **bounded, well-specified internal work** where the integration surface is controlled and the cost of a bug is low. Stripe's Minions system generates 1,000+ PRs/week for internal tooling — the pattern scales when the scope is narrow and the validation harness can be tightly constructed.[^stripe]

Spotify reported 60–90% time savings on large-scale code migrations using agentic patterns.[^bcg] Cognition's 2025 Devin review documents Visma (fintech) using agentic coding for large migration tasks.[^devin] Migrations are particularly well-suited: they have a clear before/after, the correctness criterion is behavioral equivalence, and the holdout-scenario structure maps naturally to regression testing.

[^stripe]: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — "0and%20how%20we%20built%20them." — sha256:58e6a45811ed3bb0d2aa50d8c4d749889e27f219014cb15ad3be83d9b7c848d3
[^bcg]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "f 10x2**. Spotify has reported time savings of **60 to 90%** on large-scale code migrations3 when using the same" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258
[^devin]: https://cognition.ai/blog/devin-annual-performance-review-2025 — "ember 14, 2025 Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work" — sha256:573e8d583289caefb981bc48b70260cf7ddd6bd38660bdb85909f085c3bda60b
### Infrastructure-as-Code

Pulumi's adaptation of the Dark Factory pattern to IaC targets infrastructure provisioning — a domain with well-defined APIs, testable state, and high repetition.[^pulumi] The human oversight point shifts to policy gates (does this change comply with security policy?) rather than code review. This is a natural fit: IaC correctness is largely verifiable by applying it to a staging environment.

[^pulumi]: https://www.pulumi.com/blog/dark-factory-pattern-pulumi-autonomous-iac/ — "e using your favorite language. [Get started →](/docs/get-started/ "/docs/get-started/") --- ##### Recent Posts * [The Dark Factory Pattern for" — sha256:121b5b1e2999f2923f667f510e2ec3665cbf05368249ef351ea4f74aeb203e7b
### Security Software (Contested)

StrongDM's case is the most provocative: access management software built with no human code review. BCG Platinion and practitioners who have seen the demos report it works. Stanford's CodeX argues the accountability inversion this creates is not prepared for by current regulatory frameworks.[^stanford] The claim that behavioral verification is stronger than code review is contested but not obviously wrong — the question is whether the scenario set is comprehensive enough to catch the vulnerabilities that code review would catch.

[^stanford]: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ — "Existing regulatory frameworks are not prepared for it." — sha256:099f3c42a82d5db68817da96a4f838e8ec1df85e8b94d6f6de3f96f79f7f935b

---

## Where It Struggles

### Regulated Domains

Databricks Genie Code (April 2026) targets data-engineering pipelines but **explicitly keeps humans in the loop on every change**; full autonomy is positioned as future work.[^databricks] For ML/data pipelines, the validation problem is particularly hard: correctness depends on data distributions that may not be captured in scenario tests.

Retool's analysis: agentic coding is fine for prototypes and simple CRUD but "breaks in production systems handling real data."[^retool] The threshold they identify is roughly where data integrity guarantees, audit trails, and rollback requirements kick in.

[^databricks]: https://www.databricks.com/blog/agentic-data-engineering-genie-code-and-lakeflow — "argest data, apps and AI event." — sha256:42c8c5aa1397347a052ef38148ba472d264cdcdc97931dd10c21a79c27723d47
[^retool]: https://retool.com/blog/vibe-coding-risks — "t of vibe coding is that these vulnerabilities can be introduced through the prompts themselves. If your prompt" — sha256:3c494aceaf9e95863efbee0a97de11515a1056fde961c62157736d7e8b296e88
### Scientific Computing

AutoMat benchmark (2026) of 85 SME-curated claims in computational materials science: the best agent succeeds only 54.1% end-to-end.[^automat] Scientific computing requires domain-specific correctness criteria that are hard to encode in general scenario tests, and where errors may not manifest as failures but as subtly wrong numerical results.

[^automat]: https://arxiv.org/abs/2605.00803 — "s.html"), and all contributors. [Donate](https://info.arxiv.org/about/donate.html "https://info.arxiv.org/about/donate.html") [![arxiv" — sha256:4bf41f4473c7aee000d08433afd52aa2d8a1feaa55db81bb6c327af44cae0a2b
### Embedded and Firmware

Sun and Staron (Chalmers, 2026) found embedded/firmware development poses particular challenges for agentic coding: hardware simulation fidelity, real-time constraints, and certification requirements (DO-178C, IEC 61508) create validation problems that holdout scenarios cannot fully address.[^embedded]

[^embedded]: https://arxiv.org/html/2601.10220v1 — "f Gothenburg, and 17 companies. 1. [I Introduction](https://arxiv.org/html/2601.10220v1#S1 "In Agentic Pipelines in Embedded Software Engineering:" — sha256:e141d2ead39d27464b6cd66fafd1a7af4cd02470dde936259fa277ea134b0866
---

## The Domain Pattern

A rough heuristic emerges from the evidence:

**Dark Factory works better when:**
- The correctness criterion is behavioral (does it do what a user would want?)
- The integration surface is controllable (can be simulated or tested in isolation)
- The codebase is greenfield or migration-bounded (not a legacy system with undocumented invariants)
- Failure modes are observable and recoverable (not silent data corruption or regulatory violation)

**Dark Factory struggles when:**
- Correctness requires domain expertise to verify (scientific, medical, regulated)
- Audit trails and code provenance are legally required
- Real-time or hardware-in-the-loop constraints apply
- The scenario set cannot represent the long tail of production inputs
