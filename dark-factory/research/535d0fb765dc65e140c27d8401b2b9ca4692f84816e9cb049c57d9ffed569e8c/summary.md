# cline/cline

Cline is a fully open-source, model-agnostic coding agent that runs as a VS Code extension. It executes a plan-then-act loop: read the workspace, propose changes, apply diffs, run commands, and pause for human confirmation at each step. As of 2026 it has 50k+ GitHub stars and is widely cited as the most popular OSS coding agent inside an IDE.

Cline is a coding-agent harness with a deliberate review-first workflow — the opposite end of Shapiro's spectrum from Dark Factory, but useful as a reference implementation for the inner agentic loop (tool calls, file diffs, terminal use). In Dark Factory pipelines Cline is the harness teams downgrade from when they remove the human-confirmation step.
