# Overview

`langwatch/scenario` is an open-source library that implements the StrongDM-style scenario primitive: an AI user-simulator agent drives the system-under-test through a declarative user-story (persona + goal + success conditions), and a judge agent verifies whether the journey satisfied the acceptance criteria. Scenarios run alongside conventional unit tests in CI but are explicitly designed for the nondeterminism of LLM-backed systems, where assertion-based testing is too brittle.

For Dark Factory teams without StrongDM's bespoke harness, this is the most accessible operational template. It supports importing user stories, BDD/Gherkin specs, or manual test cases as scenario sources, and it preserves the central design choice that makes scenarios powerful: they live outside the codebase as a holdout-style spec, so the agent cannot pass the test by silently editing the test.
