# Anthropic — Demystifying evals for AI agents

Anthropic's engineering post on agent evaluation: defines the eval harness as the test infrastructure that closes the verify loop. Covers offline benchmarks (held-out scenarios), online evaluation (production telemetry), LLM-as-judge patterns, and how to avoid "self-congratulation machines" where the agent grades its own work.

Critical for the Dark Factory pattern: without trusted evals, removing the human reviewer is unsafe. The post is one of the more rigorous vendor-side treatments and explicitly discusses isolation between code-generation context and validation context — a load-bearing requirement for StrongDM-style holdout scenarios. Central reference for the validation aspect of any tools stack.
