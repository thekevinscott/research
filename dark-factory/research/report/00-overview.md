# Dark Factory: Definition and Taxonomy

*Section 1 of 8 — synthesis report, 2026-05-06*

---

## Scope and Disambiguation

This report covers **Level 5 of Dan Shapiro's five-level AI-coding automation model**: a software development pattern where coding agents write, test, and ship code with no human writing or reviewing any of it.[^5f951b] The term borrows from manufacturing — Fanuc's lights-out robot factory where "humans are neither needed nor welcome"[^5f951b] — and applies that metaphor to software production.

Two prior uses of similar terms are out of scope:

- *Lights-out / dark factory* in manufacturing (automated production facilities, predating AI coding)
- *Software factory* in the 1960s–2000s sense (Cusumano's industrialized-SE research)

All sources cited are post-2024-06 unless flagged otherwise.

[^5f951b]: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ — "It's dark, because it's a place where humans are neither needed nor welcome." — sha256:5f951b03c05299d2171805ebe171c0c4e754acb82c430436e872a1ce0ce2cd4c

---

## The Five-Level Model

Dan Shapiro introduced the taxonomy in January 2026, drawing explicit analogy to the NHTSA's five levels of driving automation.[^5f951b]

| Level | Analogy | Human role |
|---|---|---|
| 0 | Manual car | Writes every character |
| 1 | Lane-keeping | Offloads discrete tasks, reviews everything |
| 2 | Autopilot | Pair-programs with AI, reviews every line |
| 3 | Waymo + safety driver | Full-time code reviewer |
| 4 | Robotaxi | Writes specs, reviews plans, checks test results |
| 5 | **Dark Factory** | Designs the factory; never reads the code |

Shapiro described Level 5 as "a black box that turns specs into software."[^5f951b] He placed himself at Level 4 at time of writing and noted Level 5 was being practiced by "a handful of people... small teams, less than five people."[^5f951b]

Simon Willison's January 28 link-blog added key nuance from a team he had seen demo the pattern: the humans' role is not to review code but to "find new patterns that can help the agents work more effectively and demonstrate that the software they are building is robust and effective."[^9459392b]

[^9459392b]: https://simonwillison.net/2026/Jan/28/the-five-levels/ — "Nobody reviews AI-produced code, ever. They don't even look at it." — sha256:9459392bc03c0a8a2fa622aa6396bc2a4f19b36a1eba37ffa7014e04edc0b1ea

---

## Contested Terminology

The pattern carries at least four names in active use:

- **Dark Factory** (Shapiro, Willison) — emphasizes the lights-out manufacturing analogy
- **Software Factory** (StrongDM, BCG Platinion) — emphasizes industrialized production
- **Non-interactive development** (StrongDM internal) — emphasizes the absence of human interaction in the coding loop
- **Grown software** (StrongDM internal) — frames code as an artifact that emerges from a process rather than being authored

BCG Platinion uses "Dark Software Factory" as a distinct compound to signal the lights-out analogy while separating from the historical SE "software factory" term.[^1223500b] The overlap creates confusion: StrongDM's public site uses "Software Factory" throughout, which is why this report uses "Dark Factory" as the canonical term.

[^1223500b]: https://www.bcgplatinion.com/insights/the-dark-software-factory — "fully automated production facilities that run with the lights off (because no human is on the floor)" — sha256:1223500beed9dad3c0289732aa941183900a39c9ea88012924ba83ab4794a258

---

## What Makes Level 5 Different from Level 4

The distinction between levels 4 and 5 is frequently misunderstood. At Level 4, humans still read code — they review plans, check that tests pass, and inspect diffs before shipping. At Level 5, code is treated as **opaque output**: its internal structure is irrelevant, correctness is inferred exclusively from externally observable behavior.[^bb419cf4]

StrongDM frames this explicitly: "Code was treated analogously to an ML model snapshot: opaque weights whose correctness is inferred exclusively from externally observable behavior. Internal structure is treated as opaque."[^bb419cf4]

This is not merely a workflow choice. It is a claim about what matters: if the system demonstrably does what the spec says under adversarial testing, the implementation details are irrelevant to ship/no-ship decisions.

[^bb419cf4]: https://factory.strongdm.ai/techniques — "Code was treated analogously to an ML model snapshot: opaque weights whose correctness is inferred exclusively from externally observable behavior." — sha256:bb419cf4713c2ffb0ae2c03e5c07ddea7dee5b90ddabd679b6dedbc4fe9c2e90

---

## Model Capability as Prerequisite

The Dark Factory is not a technique that works on any model. StrongDM's founding insight was a specific model transition: Claude 3.5 Sonnet (October 2024 revision) was the first model where "long-horizon agentic coding workflows began to compound correctness rather than error."[^d5099378] Before that inflection, iterative application of LLMs accumulated errors until the codebase "collapsed."

A second inflection Willison identified: November 2025 releases from Anthropic and OpenAI made agentic coding "significantly more reliable" — shifting the question from "can agents write code?" to "why are humans still writing code?"[^78862ac8]

This dependency on frontier model capability is a hard constraint: teams attempting the pattern on sub-frontier models or earlier checkpoints report the compounding-error failure mode rather than compounding correctness.

[^d5099378]: https://factory.strongdm.ai/ — "with the second revision of Claude 3.5 (October 2024), long-horizon agentic coding workflows began to compound correctness rather than error." — sha256:d5099378349485a70d738ac8d266b249ca6442f1a3c78fdda294691da3b125d3

[^78862ac8]: https://simonwillison.net/2026/Feb/7/software-factory/ — "StrongDM's AI team was founded in July 2025 based on an earlier inflection point relating to Claude Sonnet 3.5" — sha256:78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3
