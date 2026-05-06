# The Dark Factory Pattern — Summary

The **Dark Factory** (also "Software Factory", "Level 5 of AI-assisted
programming", "lights-out coding") is a pattern of software development in
which **no human writes or reviews any production code**. Instead, AI
coding agents are driven by human-authored *specifications* and
*scenarios*, run inside an end-to-end *validation harness*, and converge
on shippable code through a *feedback loop*. The metaphor is borrowed
from Fanuc's "lights-out" robotic factory in Japan, which runs in the
dark because no humans are inside who would need light.

## Provenance

| Source                         | Contribution                              |
|---|---|
| Dan Shapiro, "The Five Levels: from Spicy Autocomplete to the Dark Factory" (Jan 2026) | Coined the term *dark factory* as Level 5 of a SAE-style autonomy ladder for coding |
| Simon Willison, "How StrongDM's AI team build serious software without even looking at the code" (7 Feb 2026) | First publicly documented production deployment, at StrongDM |
| StrongDM, factory.strongdm.ai | Charter, principles, and the Digital Twin Universe |

## The core equation

> Seed → Validation harness → Feedback loop. **Tokens are the fuel.**

* **Seed** – PRD, spec, sentence, screenshot, or existing codebase.
* **Validation harness** – end-to-end and as close to production as
  possible: customers, integrations, economics.
* **Feedback loop** – outputs are fed back into inputs to drive
  self-correction and compound correctness.

## StrongDM's three cardinal rules

1. Code must not be written by humans.
2. Code must not be reviewed by humans.
3. If you haven't spent at least $1,000 on tokens today per human
   engineer, your software factory has room for improvement.

## Key concepts

* **Scenario** – end-to-end user story stored *outside* the codebase
  (treated like an ML "holdout" set), graded by an LLM.
* **Satisfaction** – fraction of agent trajectories across all scenarios
  that an LLM judge considers to satisfy the user. Probabilistic, not
  deterministic.
* **Digital Twin Universe (DTU)** – behavioural clones of third-party
  SaaS (Okta, Jira, Slack, Google Workspace) that let the harness run
  thousands of scenarios per hour without hitting rate limits or
  triggering abuse detection.
* **Long-horizon agentic coding** – per StrongDM, the inflection point
  came with Claude Sonnet 3.5 (October 2024 revision), at which point
  agent loops began *compounding correctness rather than error*.

## Dan Shapiro's six levels (zero-indexed)

| Level | Driving analogy | Coding analogy |
|---|---|---|
| 0 | Volvo with manual transmission | vi/Visual Studio, no AI |
| 1 | Lane-keeping & cruise control | AI fills small tasks (tests, docstrings) |
| 2 | Tesla Autopilot on highway | AI handles boring stuff; "AI-native" baseline today |
| 3 | Waymo with a safety driver | Human is the manager / reviewer of agent PRs |
| 4 | Robotaxi (you can do something else) | Human is the PM, not even reviewing |
| 5 | **Dark factory** (lights out) | Implementation loop is autonomous; the factory is the product |

## Why now?

* Long-context, long-horizon agentic models (Claude Sonnet 3.5+, Claude
  Opus 4+, GPT-5) finally produce loops that converge.
* Cheap virtualised and headless validation environments make end-to-end
  scenario execution at thousands per hour feasible.
* Scenario-based testing (and probabilistic LLM-as-judge grading) lets
  teams measure correctness without writing assertions for everything.

## Where it appears to work

* High-leverage, well-bounded backend systems (security/access control at
  StrongDM, accounting glue, internal tooling, refactors).
* Domains where a digital twin or sandbox is achievable.
* Organisations that can absorb >$1k/day/engineer in token spend.

## Where it tends to fail

* Open-ended UX/UI work where "satisfaction" is hard to score.
* Codebases without strong test coverage to seed the harness.
* Teams that try to flatten coordination across many agents at once
  (agent sprawl, lock contention, risk-aversion).
* Anywhere the generator is also the judge.

## The open question

Can the dark factory be made economical at lower budgets, generalised
beyond well-bounded backends, and made safe against cascading failures
before the next big incident? That is the question Willison and most
commentators leave open.
