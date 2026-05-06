Part 2 of Stripe's Minions writeup focuses on the harness architecture, mixing deterministic blueprint nodes (known-good steps with no LLM call) and agentic nodes (LLM with tool access). The deterministic backbone is what lets one-shot generation scale without runaway loops or unbounded retries.

From a domains perspective, this confirms the pattern is most production-ready for internal tooling and well-trodden payments-monorepo edits — bug fixes, migrations, flaky-test repair — rather than greenfield product work. Stripe positions this as supporting human reviewers, not replacing them.
