# anthropics/claude-agent-sdk-python

Claude Agent SDK (Python) exposes the Claude Code agent loop as a library: ClaudeSDKClient enables custom tools and hooks defined as Python functions, in-process MCP servers, and programmatic control over context, tool permissions, and conversation state. Mirrors a TypeScript SDK.

The Claude Agent SDK is the most direct OSS-callable surface for the Anthropic harness — what you import when you want to embed a coding agent inside a larger orchestrator (e.g. agent-orchestrator above) rather than shelling out. In Dark Factory pipelines it is the glue between the orchestration layer and the inner agent.
