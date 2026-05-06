# Overview

OpenAI's "Harness Engineering" post is the company's own dark-factory case study: a three-person team starts from an empty repo in late August 2025 and for five months writes no human code — Codex generates everything, mediated by a harness of guides (orientation docs), sensors (automated environment checks), and structured constraint files. The post is widely credited as the moment "harness engineering" entered the lexicon as a discipline name.

The April 2026 follow-up adds native sandbox execution, configurable memory, and sandbox-aware orchestration to the Agents SDK under the banner of a "model-native harness" — execution patterns engineered around how frontier models actually behave. Combined with Anthropic's evals post and Datadog's harness-first piece, it establishes a near-consistent industry doctrine on validation: small focused tasks, isolated dimension graders, automated sensors, and tight feedback to the agent loop.
