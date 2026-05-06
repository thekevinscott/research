# Claude Code docs — Sub-agents

Anthropic's Claude Code documentation for sub-agents: each sub-agent runs in its own context window with a custom system prompt, specific tool access, and independent permissions. The parent agent delegates to a sub-agent based on the sub-agent's description; the sub-agent works independently and returns results.

Sub-agents are the primary mechanism Claude Code offers for parallel work and context isolation in long-horizon runs. Combined with managed sub-agents (organization-deployed) and the parallel-agent orchestrator pattern, they form the Anthropic-native answer to multi-agent Dark Factory operation. The page enumerates configuration syntax, tool whitelisting, and the description-as-router contract.
