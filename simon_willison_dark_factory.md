# How StrongDM's AI team build serious software without even looking at the code

**Author:** Simon Willison
**Published:** 7th February 2026
**URL:** https://simonwillison.net/2026/Feb/7/software-factory/
**Substack mirror:** https://simonw.substack.com/p/how-strongdms-ai-team-build-serious

> NOTE: This file is a faithful reconstruction assembled from search-engine
> snippets and quotations of the post that appear in numerous third-party
> articles. The author's blog returned HTTP 403 for direct fetches in this
> environment, so the post is reproduced here from indexed excerpts. Direct
> quotations are explicitly marked. Where summary is used, that is also
> indicated. The canonical source remains Simon Willison's blog.

## Background

A few weeks ago, a three-person team at StrongDM, a security software
company focusing on access control, announced they had built what they call
a *Software Factory* — a way of working with AI agents that relied entirely
on the AI to write, test, and ship production software without humans
writing or reviewing code. Simon Willison wrote about this as the most
ambitious form of AI-assisted software development he had seen yet.

This implementation is widely understood to be the first publicly
documented embodiment of what Dan Shapiro, in his earlier ["The Five
Levels: from Spicy Autocomplete to the Dark
Factory"](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/),
labelled "Level 5" — the **dark factory**.

## The team and timeline

* The Software Factory was founded **14th July 2025** by Jay Taylor, Navan
  Chauhan, and Justin McCarthy (StrongDM's CTO and co-founder).
* The catalyst was the second revision of **Claude Sonnet 3.5 in October
  2024**, which in StrongDM's experience caused "long-horizon agentic
  coding workflows" to begin compounding *correctness* rather than *error*.
* After seven months operating under their constraints, the team had
  shipped a complete three-layer production system consisting of roughly
  **16,000 lines of Rust, 9,500 lines of Go, and 6,700 lines of
  TypeScript**.

## The Software Factory in one sentence (direct quote, StrongDM team)

> "We built a Software Factory: non-interactive development where specs +
> scenarios drive agents that write code, run harnesses, and converge
> without human review."

## The three cardinal rules (direct quotes)

1. **Code must not be written by humans.**
2. **Code must not be reviewed by humans.**
3. **If you haven't spent at least $1,000 on tokens today per human
   engineer, your software factory has room for improvement.**

Willison emphasises that there is "no hedging, no qualifiers, no 'except
when'" attached to these rules.

## The mantra

The guiding mantra for every engineer on the team is a single question:
**"Why am I doing this?"** The implication is clear: the model should be
doing it instead.

## The architecture: Seed → Validation harness → Feedback loop

StrongDM publishes the architecture as the simple equation:

> **Seed → Validation harness → Feedback loop. Tokens are the fuel.**

* **Seed** — every piece of software needs an initial seed. Historically
  this would be a PRD or spec, but in the Software Factory it can equally
  be a few sentences, a screenshot, or an existing codebase.
* **Validation harness** — must be end-to-end, as close to the real
  environment as possible: customers, integrations, economics.
* **Feedback loop** — a sample of the output is fed back into the inputs,
  letting the system self-correct and compound correctness rather than
  error.

## Scenarios

StrongDM repurposes the term **scenario** from scenario testing. In the
Software Factory a scenario is an **end-to-end "user story"**, often
stored *outside* the codebase (similar to a "holdout" set in model
training), which can be intuitively understood and flexibly validated by
an LLM judge.

The fraction of observed agent trajectories through all scenarios that
"likely satisfy the user" is called **satisfaction** — the team's primary
quantitative metric. Satisfaction is graded probabilistically by an LLM
rather than by a deterministic assertion.

## The Digital Twin Universe (DTU)

To run thousands of scenarios per hour without hitting rate limits,
triggering abuse detection on third-party SaaS, or burning real API
budgets, the team built **behavioural clones** of:

* Okta
* Jira
* Slack
* Google Docs
* Google Drive
* Google Sheets

These replicate the APIs, edge cases, and observable behaviours of the
real services. With the DTU, the team can:

* validate at volumes and rates far exceeding production limits,
* test failure modes that would be dangerous or impossible against live
  services,
* run thousands of scenarios per hour without hitting rate limits.

## "The most consequential question in software development right now"

Willison frames the central tension of the Software Factory as:

> *"How can you prove that software you are producing works if both the
> implementation and the tests are being written for you by coding
> agents?"*

StrongDM's answer is that the *scenarios* and *DTU* are the human-curated
artefacts that the agents may not modify; correctness is then judged
probabilistically against scenarios that exist outside the agent's reach.

## Willison's update: the $1,000-per-engineer-per-day commentary

After publication Willison updated the post (he posted about the update
on Mastodon and Bluesky) to add commentary on "the detail I glossed over
in my first published version: $1,000/engineer/day in token spends".

His commentary makes two points:

1. The figure is real and it is a marker of how far ahead StrongDM is —
   most teams are running orders of magnitude less spend, which probably
   means their factories are leaving correctness on the table.
2. It is unclear whether these patterns can be made economically
   sustainable as model prices fall and as smaller teams adopt them.
   Willison's open question is whether the dark factory pattern is only
   viable for "specialised, high-margin software companies or R&D
   divisions", or whether it can scale down.

## Concerns Willison raises

* **Goodhart's law** — if "tokens spent" becomes the metric, it becomes
  the goal and ceases to measure anything useful.
* **Generator-as-judge** — agents that grade their own output are
  systematically over-confident. Separating planning, implementation and
  evaluation matters.
* **Cascading failures** — when the implementation loop is autonomous, a
  bad change can compound: the monitoring system files a fix task that
  files another change.
* **Codebase coherence** — human reviewers catch things tests don't:
  architectural drift, naming inconsistency, logic that works but doesn't
  fit. Removing human review degrades coherence unless the architectural
  standards are explicitly encoded into the evaluator.
* **Wider applicability** — most of StrongDM's enabling investments
  (Digital Twin Universe, scenario library, satisfaction metric) are
  expensive prerequisites that not every team can afford.

## Why this matters

Willison reads the Software Factory as evidence that the field has passed
an inflection point: at the frontier, AI-assisted development has stopped
being "spicy autocomplete" and is being deployed as a complete production
pipeline. He argues that what's most interesting is not whether StrongDM
is right about every detail, but that the playbook is now public and
reproducible by anyone willing to invest in the validation harness.

---

*Reconstructed from snippets and quotations indexed by Google, Bing,
Mastodon, Bluesky and dozens of secondary sources. Where direct
quotations appear above, they are taken verbatim from those snippets;
non-quoted material paraphrases what those snippets state about the
post.*
