# yamadashy/repomix

Repomix packs an entire repository into a single AI-friendly file (XML, markdown, or plain text) for feeding to LLMs and coding agents. It supports tree-sitter-based intelligent compression (~70% token reduction), per-file token counting, .gitignore-aware filtering, and an MCP server so coding agents can pull packed views of a repo on demand.

Repomix is a context-packing utility — the prompt-engineering / context-management leg of the Dark Factory pipeline. It is what an autonomous agent uses to fit a large codebase into a model context window without human curation, and the MCP-server form means it composes cleanly with Claude Code / Cursor / Codex CLIs that orchestrators spawn in parallel.
