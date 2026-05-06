# huggingface/smolagents

smolagents is Hugging Face's barebones agent library: ~1k LoC core, agents that 'think in code' (CodeAgent emits Python snippets executed in a sandbox) and a classic ToolCallingAgent that uses model-native tool calls. It includes a webagent built on helium for browsing, MCP tool integration, and a security model emphasizing isolated execution.

smolagents is a minimal coding-agent / tool-calling-agent harness — useful in Dark Factory builds as a lightweight inner agent for narrow scenarios where Cline/Aider/OpenHands are over-kill. Its emphasis on code-as-action is conceptually adjacent to StrongDM's natural-language-spec approach: both use generated artifacts (code or NLSpec) as the agent's action representation.
