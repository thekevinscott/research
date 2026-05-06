# Datadog — Closing the verification loop: harness-first agents

Datadog's engineering post argues for harness-first agent design: the agent generates code, the harness verifies it deterministically, production telemetry validates it in the wild, and feedback updates the harness. The piece names four common harness verification mechanisms — deterministic simulation testing, formal specifications, shadow evaluation, and observability-driven feedback loops — and treats them as interchangeable tools selected by domain.

The framing matters because it inverts the usual model-first narrative: when models are good enough, the limit on Dark Factory operation is harness investment. Datadog presents observability (their own product space) as the third leg of the verification triangle, alongside spec and simulation. Cited widely as a 2026 reference for production harness architecture.
