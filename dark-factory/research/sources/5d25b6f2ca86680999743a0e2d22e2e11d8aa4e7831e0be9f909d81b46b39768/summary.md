# Aider — Usage docs

Aider's user docs describe the terminal-first pair-programming model: chat with the agent, it generates patches, applies edits via diffs, and commits with descriptive messages. Aider maps codebases automatically, supports many languages, and works with cloud and local models including GPT-5, Claude 4.x, and Gemini 2.5 Pro.

Aider's role in the Dark Factory landscape is as the minimal vendor-agnostic CLI: small, scriptable, atomic-commit-oriented. Often used inside loop frameworks (Ralphify, agent-orchestrator) where the wrapping orchestrator drives objectives and Aider executes single tasks. Treats Git as the source of truth and atomic commits as the unit of AI change.
