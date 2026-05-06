# StrongDM Software Factory (factory.strongdm.ai)

- URL: https://factory.strongdm.ai/
- Authors: Justin McCarthy (CTO), Jay Taylor, Navan Chauhan
- Published: 2026-02-06
- Reconstructed from WebSearch snippets.

## What this is

The canonical first-party site for StrongDM's Dark Factory. Includes the manifesto, the principles page (factory.strongdm.ai/principles), a techniques page (factory.strongdm.ai/techniques) and a products page (factory.strongdm.ai/products). This is the team's own first-hand account.

## Team and timeline

- The AI team was founded on July 14, 2025 by Justin McCarthy (CTO), Jay Taylor and Navan Chauhan (a "new hire less than a year out of school").
- By October 2025 they had a working agent harness, a Digital Twin Universe, a satisfaction-testing framework, and demos.
- The catalyst was Anthropic's Claude 3.5 October 2024 revision, which enabled "compounding correctness" in long-horizon agentic workflows.
- The manifesto and supporting site were published February 6, 2026.

## The three rules (paraphrased + quoted)

> "Code must not be written by humans."

> "Code must not be reviewed by humans."

> "If you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement."

## Core technical pieces (from snippets)

- **Specs + Scenarios**: Markdown specs describe what the software should do; scenarios are end-to-end user-story behaviors stored *outside* the codebase so coding agents never see them. Scenarios act as a "holdout set."
- **Attractor**: the convergence loop - generate -> test -> score -> feedback -> regenerate.
- **Satisfaction**: a probabilistic LLM-as-judge score (0-100) over observed trajectories through scenarios. Avoids boolean pass/fail and discourages reward hacking.
- **Digital Twin Universe (DTU)**: behavioral clones of Okta, Jira, Slack, Google Docs, Google Drive, Google Sheets - replicating their APIs, edge cases, and observable behaviors. Allows running thousands of scenarios per hour without rate-limit or safety constraints.
- **Humans' role**: write specs, design scenarios, architect systems. They do not program.

## Direct quotes (from snippets)

> "non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review"

> "Code is treated as opaque weights - correctness is inferred from behavior, not inspection."

> "the humans in a Software Factory write specifications, design scenarios, and architect systems. They do not program."

> "treating scenarios as holdout sets - used to evaluate the software but not stored where the coding agents can see them - imitates aggressive testing by an external QA team"

## Takeaway

The first-party site is the canonical reference for what StrongDM actually built. It establishes the three rules, the Specs/Scenarios/Attractor/Satisfaction/DTU vocabulary, and frames code as opaque weights validated only by external behavioral evidence.
