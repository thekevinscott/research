# langwatch/scenario — Agentic testing for agentic codebases

**URL:** https://github.com/langwatch/scenario
**Publisher:** LangWatch (open source)

## Reconstructed content

> "Scenario is an open-source testing library that uses an AI agent to test your AI agent, eliminating the tedious back-and-forth of manual testing and making sure your agent works in real-world scenarios."

## Core idea

> "Scenario enables you to modify agent prompts, tools, and structure without regressions, and the framework works with all AI agent frameworks and does not require datasets."

The library implements the StrongDM-style scenario pattern in OSS form: a *user-simulator agent* drives the system-under-test through a goal-driven journey, and a judge agent verifies whether the journey met the acceptance criteria. Scenarios are written declaratively (user persona + goal + success conditions) and executed alongside other tests in CI.

## User-story integration

> "You feed the agent a set of user stories or acceptance criteria, and it interprets the intent behind each requirement, then proposes a suite of test cases that cover the main path, alternative flows, and boundary scenarios."

> "AI can convert user stories, BDD specifications, or manual test cases from requirements documents into executable test scenarios automatically."

## Why it's needed

> "Systems running on LLMs are by their nature nondeterministic — the same input can produce different outputs, making traditional assertion-based testing unreliable, which is why Scenario was built to run in your CI alongside your existing tests with a new paradigm designed specifically for AI agents."

## Why it matters

`langwatch/scenario` is the most prominent open-source implementation of "scenarios as out-of-codebase user stories validated by an LLM judge" — i.e., the StrongDM primitive made available to every team. It also bridges to BDD: existing Gherkin specs can be mechanically lifted into scenarios.
