# Anthropic Engineering — Effective harnesses for long-running agents

URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## Reconstructed from snippets

A late-2025 Anthropic engineering post by Justin Young (with code-RL and Claude Code teams) on building harnesses that survive context-window boundaries — the operational underpinning of long-horizon, no-human-in-loop work.

### The core problem (quoted)

> "As AI agents become more capable, developers are increasingly asking them to take on complex tasks requiring work that spans hours or even days. However, getting agents to make consistent progress across multiple context windows remains an open problem."

> "The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before."

### The two-fold solution

> "An initializer agent that sets up the environment on the first run, and a coding agent that is tasked with making incremental progress in every session, while leaving clear artifacts."

> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with the claude-progress.txt file alongside the git history."

### Connection to Claude 4 prompting guide

> "A different prompt for the very first context window" — allowing the initializer to lay down the context that future coding agents will inherit.

### Why it matters for the Dark Factory thesis

This blog post is the Anthropic Engineering counterpart to OpenAI's harness essay. It exposes the actual techniques (claude-progress.txt, git artifacts as memory, distinct initializer prompts) that make hours-to-days autonomous runs possible — which is precisely what makes the Dark Factory level operable rather than aspirational.

---

## Two-paragraph summary

Anthropic's "Effective harnesses for long-running agents" post (Justin Young, late 2025) describes the practical patterns that turn a single coding agent into a multi-session worker capable of surviving the context-window boundary. The two-component pattern — an initializer agent that lays down environment state and a per-session coding agent that makes incremental progress while writing artifacts — solves the central problem of long-horizon autonomy: how to maintain continuity across discrete sessions with no shared memory.

The artifacts (claude-progress.txt, git history) become the cognitive substrate by which an agent can pick up its own work without a human re-priming it. This is the engineering substrate of the Dark Factory: it's not a research demo, it's the production technique behind "agents work overnight, humans review specs in the morning." Highly relevant (3).
