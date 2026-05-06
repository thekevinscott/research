# Anthropic Engineering — Best practices for Claude Code

URL: https://www.anthropic.com/engineering/claude-code-best-practices

## Reconstructed from snippets

Anthropic's official "Best practices for Claude Code" engineering doc — the most widely cited operational reference for running coding agents with minimal supervision.

### Capability framing (quoted)

> "Claude Code is an agentic coding environment that can read files, run commands, make changes, and autonomously work through problems while you watch, redirect, or step away entirely."

### Context management

> "Claude Code on the web runs sessions on Anthropic-managed cloud infrastructure in isolated VMs, and agent teams enable automated coordination of multiple sessions with shared tasks, messaging, and a team lead."

> "Claude Code employs a hybrid model where CLAUDE.md files are included in context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time."

### Multi-session workflows

> "The best way to manage agent behavior is to ask the model to commit its progress to git with descriptive commit messages and write summaries of its progress in a progress file, which allows the model to use git to revert bad code changes and recover working states."

### Parallelism and review

> "Multiple sessions enable quality-focused workflows, and a fresh context improves code review since Claude won't be biased toward code it just wrote." — the canonical justification for "agent reviews agent" in the Dark Factory pattern.

### Sandboxing

> "Sandboxing safely reduces permission prompts by 84%, and by defining set boundaries within which Claude can work freely, they increase security and agency."

### Why it matters for the Dark Factory thesis

This is the most operational of Anthropic's documents. It explains how to actually run a Dark-Factory-style flow with Claude Code: agent teams + team lead coordinator, CLAUDE.md as harness substrate, git/progress files for persistence, fresh-context reviewer agents to avoid self-bias, and sandboxes to make autonomy safe.

---

## Two-paragraph summary

The Best Practices for Claude Code engineering doc is Anthropic's playbook for operating coding agents with as little human intervention as the Dark Factory level requires. Its key contribution is treating CLAUDE.md plus glob/grep navigation as a hybrid context strategy and codifying the multi-session pattern: commit progress to git, summarize in a progress file, run reviewer agents in fresh contexts so they're not biased toward code they just wrote.

The "fresh-context reviewer" pattern is particularly load-bearing for the Dark Factory thesis because it provides a defensible answer to the obvious objection that an agent can't be trusted to grade its own work — different invocation, different context, different tools. Combined with sandboxing (84% reduction in permission prompts), this is the inside-Anthropic blueprint for production agent autonomy. Highly relevant (3).
