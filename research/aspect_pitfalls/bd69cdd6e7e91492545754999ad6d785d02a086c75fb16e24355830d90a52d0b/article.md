# 7 AI Agent Failure Modes and How to Prevent Them

Source: Galileo blog
URL: https://galileo.ai/blog/agent-failure-modes-guide

## Summary

Galileo's writeup catalogs seven distinct AI agent failure modes: context degradation, specification drift, sycophantic confirmation, tool call failures, cascading failure, silent failure, and a seventh in their taxonomy. The piece is most-cited for its treatment of cascading failures: "One agent produces a bad output. A second agent consumes that output as input. The error propagates and amplifies. Silent and cascading failures are the most dangerous because outputs look plausible while errors propagate undetected." The article recommends layered controls (zero-trust resilience, isolation boundaries, blast-radius guardrails, monitoring, forensic traceability).

For Dark Factory pitfalls research this is the canonical taxonomy citation for how multi-agent systems fail in ways that are different from traditional software bugs. Cascading failures are particularly relevant because Dark Factory pipelines chain together generator → tester → reviewer → deployer agents; if the generator hallucinates, the tester writes tests against the hallucination, and the reviewer approves. The whole pipeline confirms a wrong answer with confidence. This is the failure mode that makes Dark Factory disasters look "plausible" until production exposes them.

## Reconstructed from search snippets

### The seven failure modes

> "AI agents fail in structurally different ways than traditional software — the six core failure modes are context degradation, specification drift, sycophantic confirmation, tool call failures, cascading failure, and silent failure."

(Galileo's article extends to seven; the snippet retrieved six explicitly.)

### Cascading failures

> "Cascading errors are the failure mode that keeps production teams up at night. One agent produces a bad output. A second agent consumes that output as input. The error propagates and amplifies. Silent and cascading failures are the most dangerous because outputs look plausible while errors propagate undetected."

### Diagnosis

> "Most failures in multi-step pipelines originate earlier than they appear — trace backward from bad outputs, not forward from where they're noticed."

### Layered controls

The recommended defense stack:
1. Zero-trust fault tolerance (resilience handlers + structured errors + caching).
2. Isolation boundaries (API management + least-privilege identity + container sandbox).
3. Blast-radius guardrails (circuit breakers + input caps + resource limits).
4. Monitoring and detection (OpenTelemetry + health probes + structured logging).
5. Forensic traceability (conversation audit trail + distributed traces + diagnostic logs).

### The eval feedback loop

> "Turn that incident into an eval. Add the failed interaction to your regression suite, define what a good result looks like, and run it in CI/CD before the next release."

## Why this matters

Galileo's taxonomy is heavily cited in Dark Factory pitfalls writeups because it formalizes "cascading failure" as a named failure mode. This gives critics a shared vocabulary for the most damaging Dark Factory pattern: bad output from agent A becomes ground truth for agent B, and the pipeline ships confident wrong answers. Dark Factory advocates acknowledge this risk and try to address it via independent evaluation, but Galileo's piece argues the only reliable defense is layered controls plus forensic observability.
