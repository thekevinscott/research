# Closing the Verification Loop: Observability-Driven Harnesses for Building with Agents

**URL:** https://www.datadoghq.com/blog/ai/harness-first-agents/
**Publisher:** Datadog

## Reconstructed content

> "Datadog's approach is harness-first engineering: instead of reading every line of agent-generated code, they invest in automated checks that can tell them with high confidence, in seconds, whether the code is correct."

> "When the harness depends on observability to close the loop, the observability platform becomes the control layer for agent-built software."

## The closed loop

The piece's central diagram-in-prose:

> "The agent generates code, the harness verifies it, production telemetry validates it, and if something is wrong, the feedback updates the harness and the agent tries again."

This is the most explicit statement of the four-stage loop: **generate → static-verify → live-verify (telemetry) → harness-update**. Production observability is not an after-the-fact monitoring layer; it is the terminal verifier in the loop.

## The validation-cost argument

> "Without verification loops, the agent declares changes ready and pushes downstream, where validation gets picked up by human reviewers, integration tests, staging deploys, or production incidents, and the compounding cost of validation kicks in."

The economic argument is that the marginal cost of catching a bug rises by orders of magnitude per stage, so investments in upstream verification have outsized leverage.

## BitsEvolve case study

> "BitsEvolve, Datadog's LLM-guided evolutionary optimizer, uses production-driven feedback loops to keep evolved code honest and shipped 10x speedups on key ingestion functions, 1.53x on a DeBERTa encoder for sensitive data scanning, and 1.57x on Toto, their timeseries forecasting model — all verified against live traffic."

This is one of the few public examples of a closed loop that uses *live production traffic* as the validation signal — the observability angle in concrete form.

## Tools

- **MCP Server** that connects Claude Code, Cursor, Codex, Goose, Copilot, etc., to Datadog telemetry.
- **LLM Observability** product for end-to-end tracing of agents (inputs, outputs, latency, tokens, errors per step).
- **Agent Builder** for constructing custom agents on Datadog's hosted runtime.

## Why it matters

This post is the most-cited industry articulation of the harness-first engineering doctrine. Together with the StrongDM piece it forms the canonical pair: StrongDM shows what a Dark Factory looks like; Datadog shows how an existing observability vendor turns its product into the "control layer" for one.
