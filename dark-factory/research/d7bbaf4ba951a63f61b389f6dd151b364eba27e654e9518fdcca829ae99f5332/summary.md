# Anthropic — Building agents with the Claude Agent SDK

Anthropic's engineering post on the Claude Agent SDK introduces the agent loop primitives — gather context, take action, verify results — and how the SDK exposes them: tools, sub-agents, hooks, MCP servers, file operations, and bash. The SDK is positioned as the harness layer of choice for production deployments, with explicit support for parallel sub-agents and managed sandboxing.

The post argues the verify step is the lever that distinguishes Level 4 (assisted) from Level 5 (Dark Factory) operation: harness quality, not model quality, decides whether long-horizon runs converge. Concrete examples cover code review, documentation generation, and incident response. Anthropic later launched Claude Managed Agents (April 2026) as the hosted form of this stack.
