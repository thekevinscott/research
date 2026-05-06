# GitHub — strongdm/attractor README

The Attractor repository contains no implementation code — only NLSpecs (Natural Language Specs): three markdown files describing the Attractor pipeline, Coding Agent Loop, and Unified LLM Client. Users are expected to feed the spec to a coding agent (Claude Code, Codex, OpenCode, Amp, Cursor) with the prompt "Implement Attractor as described by https://github.com/strongdm/attractor" and have the agent generate the working system.

This is a load-bearing artifact for the Dark Factory pattern: the spec-as-source approach lets Attractor be re-implemented in any language while the canonical reference stays in natural language. NLSpec is positioned as a primary unit of distribution — not a description of code, but the actual source from which code is generated.
