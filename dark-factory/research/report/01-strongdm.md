# The StrongDM Implementation

*Section 2 of 8 — synthesis report, 2026-05-06*

---

## Background

The only detailed public first-hand account of a functioning Dark Factory as of early 2026 comes from **StrongDM's AI team**: Justin McCarthy (CTO), Jay Taylor, and Navan Chauhan. They published their methodology on February 6, 2026 at factory.strongdm.ai.[^d5099378] Simon Willison had previewed the work in January after an October 2025 visit, but withheld specifics until the team went public.[^78862ac8]

The team formed July 14, 2025 — notably, this was before the November 2025 model inflection Willison later identified. They were betting on a trajectory they had seen begin with Claude 3.5 Sonnet's October 2024 revision.

Crucially: StrongDM builds **access management and security software**. Stanford Law's CodeX blog flagged this as the most consequential aspect — a team building security infrastructure that decided human code review is an obstacle, not a safeguard.[^stanford_codex]

[^d5099378]: https://factory.strongdm.ai/ — "non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review." — sha256:b3342fee22542bfdce34015bd511e02c8f924dc5a6807dc638cf4b11fb029844
[^78862ac8]: https://simonwillison.net/2026/Feb/7/software-factory/ — "I visited the StrongDM AI team back in October as part of a small group of invited guests." — sha256:78862ac8ba43738ea2074832041a0945a21c651066722536ceb0eaad908551e3

[^stanford_codex]: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ — "tructure* has decided that human code review is an obstacle, not a safeguard. They are not alone. Dan Shapiro's" — sha256:099f3c42a82d5db68817da96a4f838e8ec1df85e8b94d6f6de3f96f79f7f935b
---

## Charter Rules

StrongDM's founding charter established two absolute rules:[^d5099378]

- **"Code must not be written by humans"**
- **"Code must not be reviewed by humans"**

A practical benchmark: "If you haven't spent at least **$1,000 on tokens today** per human engineer, your software factory has room for improvement."[^d5099378]

Willison challenged this figure directly: at $20,000/month per engineer in additional token costs, "this becomes more of a business model exercise: can you create a profitable enough line of products that you can afford the enormous overhead?"[^78862ac8] He noted he personally experiments with Dark Factory patterns on a $200/month Claude Max plan — but without running a swarm of QA testers 24/7.

---

## The Seed → Validation → Feedback Loop

StrongDM's published principles describe a three-stage loop:[^ba7eb647]

1. **Seed** — initial spec (could be a few sentences, a screenshot, or an existing codebase)
2. **Validation** — end-to-end harness, as close to real environment as possible: customers, integrations, economics
3. **Feedback** — a sample of output fed back as input, enabling self-correction

"The loop runs until the holdout scenarios pass (and stay passing)."[^ba7eb647] Tokens are the fuel: for every obstacle, convert it into a representation the model can understand.

[^ba7eb647]: https://factory.strongdm.ai/principles — "harness → Feedback loop. Tokens are the fuel. Entry Point Seed ---- Every piece of software needs an initial seed." — sha256:ba7eb647736fef2bbf8121d34d05ad2fd6476cea0cec9470a6ba95020da79fe6
---

## The Techniques

StrongDM documents six recurring patterns:[^bb419cf4]

**Digital Twin Universe (DTU)** — behavioral clones of third-party dependencies (Okta, Jira, Slack, Google Docs, Drive, Sheets). Built by coding agents from public API docs. Enables thousands of scenarios per hour without rate limits, production risk, or API costs. DTU creator Jay Taylor's key insight: "Use the top popular publicly available reference SDK client libraries as compatibility targets, with the goal always being 100% compatibility."[^78862ac8]

**Gene Transfusion** — extracting working patterns from existing codebases and reusing them elsewhere. Agents point at concrete exemplars; a solution paired with a good reference reproduces in new contexts.

**Filesystem as Memory** — models navigate repositories and adjust their own context by reading and writing files. Directories, indexes, on-disk state as practical memory substrate.

**Shift Work** — separate interactive work (spec-writing, scenario-curation by humans) from fully specified work (agent execution). When intent is complete, an agent runs end-to-end without back-and-forth.

**Semport** — semantically-aware automated ports between languages or frameworks, one-time or ongoing.

**Pyramid Summaries** — reversible summarization at multiple zoom levels: agent enumerates short summaries quickly and zooms into full detail as needed.

[^bb419cf4]: https://factory.strongdm.ai/techniques — "Patterns we return to frequently while building with the Software Factory" — sha256:bb419cf4713c2ffb0ae2c03e5c07ddea7dee5b90ddabd679b6dedbc4fe9c2e90

---

## Open-Source Releases

**Attractor** (`github.com/strongdm/attractor`) — published as three markdown NLSpec files with no runtime code. Users feed the specs to their coding agent of choice to generate the implementation.[^78862ac8] The release strategy demonstrates the Dark Factory principle: the artifact is the spec, not the code. The ~93KB `attractor-spec.md` is the canonical reference all community implementations target for compliance.[^attractor_spec]

**CXDB** (`github.com/strongdm/cxdb`) — 16,000 lines of Rust, 9,500 Go, 6,700 TypeScript. An AI Context Store: content-addressed Turn DAG for persisting agent conversation histories and tool outputs. Append performance p50 < 1ms for 10KB payloads; 70%+ storage reduction via BLAKE3 content addressing.[^cxdb]

[^attractor_spec]: https://github.com/strongdm/attractor/blob/main/attractor-spec.md — "e defines the canonical mapping: | Shape | Handler Type | Description |" — sha256:d94e091f4f532ca35f05040eb34b9f37739b63ec24cd02285226b27846214845
[^cxdb]: https://github.com/strongdm/cxdb — "uilt on a Turn DAG + Blob CAS architecture, CXDB gives you: - **Branch-from-any-turn**: Fork conversations at any point" — sha256:9dd9d7c5ff97ec700755c7d9c3eceb81dd797effad3c23236523ee84a72cf7ae
---

## Deliberate Naivete

StrongDM frames their methodology as requiring **deliberate naivete**: "finding and removing the habits, conventions, and constraints of Software 1.0."[^d5099378] The DTU example illustrates this — building full in-memory replicas of major SaaS services was "always possible, but never economically feasible" under old economics. Teams previously self-censored the proposal because they knew the answer would be no. Under Dark Factory economics, coding agents build the DTU components themselves, collapsing the cost.
