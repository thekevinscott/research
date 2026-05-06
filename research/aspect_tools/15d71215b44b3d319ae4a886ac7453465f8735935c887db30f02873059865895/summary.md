# Summary

Augment Code's Context Engine is an enterprise-grade semantic indexer that maps relationships across hundreds of thousands of files, with a 200k-token effective context window and benchmarked 40% hallucination reduction on enterprise codebases. It powers Augment's own IDE Agents (VS Code/JetBrains), Auggie CLI, and Code Review product, but is increasingly consumed via MCP by other coding agents.

For dark factories, the Context Engine MCP is a force-multiplier rather than a worker: adding it lifts Claude Code, Cursor, and Codex agent performance by 70%+ in Augment's benchmarks. Because dark factories must scale across legacy enterprise codebases that exceed any single LLM's effective context, an Augment-style context layer is increasingly considered table stakes in real production deployments.
