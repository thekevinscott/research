# Contested Claims and Open Questions

*Section 8 of 8 — synthesis report, 2026-05-06*

---

## The Verification Claim

**Claim**: Behavioral verification via adversarial holdout scenarios is a stronger correctness guarantee than human code review.

**For**: Human reviewers miss bugs. Code review is slow, expensive, and scales linearly with codebase size. An adversarial agent running thousands of scenarios per hour covers more surface area than any human reviewer.

**Against**: Scenario tests cover only scenarios the spec-writer could imagine. Human code review catches structural problems — unintended API surface, data leaks, subtle authentication logic errors — that behavioral tests may not exercise. Security researchers have documented cases where AI-generated code introduces auth-bypass vulnerabilities that pass functional tests.[^base44] Stanford's CodeX argues the accountability inversion (who is responsible when the factory ships a bug?) is unresolved.[^stanford]

**Status**: Genuinely contested. StrongDM's domain choice (security software) is either the strongest possible proof or the most reckless possible gamble, depending on whether the scenario coverage is actually comprehensive. No independent audit of their coverage has been published.

[^base44]: https://www.wiz.io/blog/critical-vulnerability-base44 — "eplace traditional programming. This shift has empowered millions of users with little to no technical background to build fully functional" — sha256:32ae935a9a38012f15a4d99b34106451fe9340f8c2577aec9cb995043deb33e5
[^stanford]: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ — "It inverts how we assign responsibility for software behavior. Existing regulatory frameworks are not prepared for it." — sha256:099f3c42a82d5db68817da96a4f838e8ec1df85e8b94d6f6de3f96f79f7f935b

---

## The Productivity Claim

**Claim**: Dark Factory delivers 3–5x productivity gains (BCG Platinion) or 10x gains (OpenAI case).

**For**: BCG Platinion documents 3–5x productivity gains "on average" for organizations operating at this level.[^bcg] The OpenAI case (1M LOC, 3 engineers, 5 months) represents a ratio that is difficult to explain without substantial automation leverage.

**Against**: The METR RCT found a 19% slowdown for experienced developers on early-2025 tools.[^metr] BCG and OpenAI figures are self-reported, not RCT-measured. The methodology for measuring "productivity" varies: BCG may be measuring throughput (features shipped), METR measured time-per-task. These are not the same thing.

**Status**: The contradiction is partly explained by model vintage (early-2025 vs post-November-2025 frontier) and workflow level (METR tested Level 2–3, BCG/OpenAI report Level 4–5). A controlled study of Level 5 workflows with post-2025 models has not been published.

[^bcg]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "utcomes - organizations operating at this level report **productivity gains of 3 to 5x** on average. OpenAI was able to" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258
[^metr]: https://arxiv.org/abs/2507.09089 — "allowing AI actually increases completion time by 19%" — sha256:0c7700afa99c5d14a3c2b745eb2c0208b72e3092c413786974b32ed9e55a30b9

---

## The Cost Claim

**Claim**: $1,000/day/engineer in token costs is a benchmark for a productive factory.

**For**: At that spend, agents are genuinely running at scale — thousands of scenarios, continuous harness iteration, parallel execution. The spend correlates with leverage.

**Against**: Willison's challenge is direct: $20,000/month in additional costs "becomes more of a business model exercise."[^willison] At that cost structure, Dark Factory is accessible to funded startups and large enterprises but not to individuals, small teams, or most open-source projects.

**Status**: The cost floor is a genuine access barrier. Community implementations (OctopusGarden) demonstrate the pattern works at lower spend; Willison experiments on $200/month. The $1,000/day figure may describe a fully productionized factory, not the minimum viable version.

[^willison]: https://simonwillison.net/2026/Feb/7/software-factory/ — "If these patterns really do add $20,000/month per engineer to your budget they're far less interesting to me." — sha256:78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3

---

## The Bottleneck Question

**Claim**: Automating code generation meaningfully accelerates software delivery.

**Counter-claim** (Elliott-McCrea): Code was never the bottleneck. The value has always been "the system, the value is human-technology hybrid that allows a product to be delivered" — and that is not what a Dark Factory automates. Elliott-McCrea explicitly plans to "incorporate humans rather than exclude them" — he is not running a dark factory, but finds the pattern worth engaging with.[^kellan]

**Status**: Probably both true, in different contexts. For greenfield products with clear specs and small teams (the StrongDM case), code generation may indeed be the bottleneck. For large organizations with multiple stakeholders and complex integration dependencies, the bottleneck is upstream of code. The Dark Factory is not a solution to organizational dysfunction.

[^kellan]: https://laughingmeme.org/2026/02/09/code-has-always-been-the-easy-part.html — "ys* known that the value is the system, the value is human-technology hybrid that allows a product to be delivered," — sha256:e835240967b666293fea7d47aac204cc50739a34f2ac35227b3944599e9a0cb5
---

## Accountability and Regulation

Stanford CodeX raises the sharpest unresolved question: who is responsible when unreviewed agent code ships a bug that causes harm?[^stanford] Current software liability frameworks assume humans made code decisions and can be held accountable. A factory where no human ever reads the code creates a liability vacuum — the organization that deployed the factory is responsible for outcomes, but not in the way existing frameworks contemplate.

This is not a hypothetical. StrongDM ships security software this way. If their access management software has an auth bypass, the question of whether the bug is a "product defect" or a "failure of the development process" matters for insurance, litigation, and regulatory compliance.

No regulatory framework as of May 2026 specifically addresses this. The EU AI Act's provisions on high-risk AI systems may reach some deployments, but software development tooling is not clearly in scope.

---

## Open Questions

1. **Scenario coverage**: How do you know your holdout scenarios cover the attack surface that matters? No methodology for measuring scenario coverage completeness has been published.

2. **Model dependency**: The pattern works on frontier models. What happens when those models change or are deprecated? Agent behavior on re-runs is non-deterministic; a factory's output may change across model versions.

3. **Maintainability**: Generated code is disposable by design. But disposal requires regeneration, which requires a working factory. What is the recovery path if the factory itself breaks?

4. **Regulatory compliance**: SOC 2, ISO 27001, and similar frameworks assume human review points. Compliant Dark Factories require either different compliance frameworks or new mappings from scenario-based validation to existing controls.

5. **Talent transition**: Moving humans from code-writers to factory-designers is a skills transition, not a headcount reduction. The supply of people who can design and debug agentic harnesses is currently small.
