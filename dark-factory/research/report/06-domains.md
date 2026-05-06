# Domain Results

*Section 7 of 8 — synthesis report, 2026-05-06*

---

## Where It Works

### Internal Tooling and Migration

The clearest wins are in **bounded, well-specified internal work** where the integration surface is controlled and the cost of a bug is low. Stripe's Minions system generates 1,000+ PRs/week for internal tooling — the pattern scales when the scope is narrow and the validation harness can be tightly constructed.[^stripe]

Spotify reported 60–90% time savings on large-scale code migrations using agentic patterns.[^bcg] Cognition's 2025 Devin review documents Visma (fintech) using agentic coding for large migration tasks.[^devin] Migrations are particularly well-suited: they have a clear before/after, the correctness criterion is behavioral equivalence, and the holdout-scenario structure maps naturally to regression testing.

[^stripe]: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — "Stripe's Minions ship 1000+ PRs/week of one-shot" — sha256:5af13a18d374026eb8f292635c140bcbb084e12e4c51d2cbc098556815b512a3

[^bcg]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "Spotify has reported time savings of 60 to 90% on large-scale code migrations" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258

[^devin]: https://cognition.ai/blog/devin-annual-performance-review-2025 — "Cognition's 2025 Devin review documents Visma (fintech)" — sha256:7bf45c0eca71eb0c3c25b65cd4ee3348dc749657e392ce7b878fcbaa9d4eab1f

### Infrastructure-as-Code

Pulumi's adaptation of the Dark Factory pattern to IaC targets infrastructure provisioning — a domain with well-defined APIs, testable state, and high repetition.[^pulumi] The human oversight point shifts to policy gates (does this change comply with security policy?) rather than code review. This is a natural fit: IaC correctness is largely verifiable by applying it to a staging environment.

[^pulumi]: https://www.pulumi.com/blog/dark-factory-pattern-pulumi-autonomous-iac/ — "four-layer architecture" — sha256:121b5b1e2999f2923f667f510e2ec3665cbf05368249ef351ea4f74aeb203e7b

### Security Software (Contested)

StrongDM's case is the most provocative: access management software built with no human code review. BCG Platinion and practitioners who have seen the demos report it works. Stanford's CodeX argues the accountability inversion this creates is not prepared for by current regulatory frameworks.[^stanford] The claim that behavioral verification is stronger than code review is contested but not obviously wrong — the question is whether the scenario set is comprehensive enough to catch the vulnerabilities that code review would catch.

[^stanford]: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ — "Existing regulatory frameworks are not prepared for it." — sha256:099f3c42a82d5db68817da96a4f838e8ec1df85e8b94d6f6de3f96f79f7f935b

---

## Where It Struggles

### Regulated Domains

Databricks Genie Code (April 2026) targets data-engineering pipelines but **explicitly keeps humans in the loop on every change**; full autonomy is positioned as future work.[^databricks] For ML/data pipelines, the validation problem is particularly hard: correctness depends on data distributions that may not be captured in scenario tests.

Retool's analysis: agentic coding is fine for prototypes and simple CRUD but "breaks in production systems handling real data."[^retool] The threshold they identify is roughly where data integrity guarantees, audit trails, and rollback requirements kick in.

[^databricks]: https://www.databricks.com/blog/agentic-data-engineering-genie-code-and-lakeflow — "explicitly keeps human-in-the-loop on every change; full autonomy positioned as future work" — sha256:a72f5fd263cefb3e46ffe33af4c907c6a1b24c0e128f152f76457de5f6cdd88d

[^retool]: https://retool.com/blog/vibe-coding-risks — "vibe/dark-factory coding is fine for prototypes and simple CRUD but breaks in production systems handling real data" — sha256:5b5dcc81daef3e7b713e95b4f92dd11cf9f595b21075c29e7a795171a212f96c

### Scientific Computing

AutoMat benchmark (2026) of 85 SME-curated claims in computational materials science: the best agent succeeds only 54.1% end-to-end.[^automat] Scientific computing requires domain-specific correctness criteria that are hard to encode in general scenario tests, and where errors may not manifest as failures but as subtly wrong numerical results.

[^automat]: https://arxiv.org/abs/2605.00803 — "AutoMat benchmark of 85 SME-curated claims finds best agent succeeds only 54.1% end-to-end" — sha256:b94c29df9c6e8a970da4c94881c41ffde232ae3b9d8d2364d797d6e3b91a93dd

### Embedded and Firmware

Sun and Staron (Chalmers, 2026) found embedded/firmware development poses particular challenges for agentic coding: hardware simulation fidelity, real-time constraints, and certification requirements (DO-178C, IEC 61508) create validation problems that holdout scenarios cannot fully address.[^embedded]

[^embedded]: https://arxiv.org/html/2601.10220v1 — "embedded/firmware: Sun & Staron (Chalmers)" — sha256:f60924ba8a744d164ba9452032657ca3358e61153e82f4a8b5d7d6c20d88c545

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
