# Anthropic Ecosystem Baseline

This document establishes the reference against which all competitors are measured. Everything described here is what the user currently has access to and finds best-in-class but expensive.

---

## Claude Code CLI

**What it is**: A terminal-based agentic coding assistant that can read/write files, execute shell commands, manage git operations, and orchestrate complex multi-step software engineering tasks.

**Distribution**: Proprietary binary, available via `npm install -g @anthropic-ai/claude-code`. Supported on macOS and Linux. Available as CLI, desktop app (Mac/Windows), web app (claude.ai/code), and IDE extensions (VS Code, JetBrains).

### Core Capabilities

- **File operations**: Read, write, and edit files with a diff-based editing tool
- **Shell execution**: Run arbitrary terminal commands with a permission system
- **Git integration**: Stage, commit, create branches, resolve merge conflicts, create PRs via `gh`
- **Multi-agent**: Can spawn sub-agents for parallel task execution within a session
- **Extended thinking**: Visible chain-of-thought reasoning for complex problems
- **Context management**: Automatic compaction when approaching context limits, with summarization that preserves continuity

### MCP (Model Context Protocol)

[MCP](https://modelcontextprotocol.io) is Anthropic's open standard for connecting AI agents to external tools and data sources. Claude Code is a first-class MCP client.

**What MCP enables**:
- Connect to databases, APIs, file systems, and custom tools via MCP servers
- Ecosystem of community-built servers (PostgreSQL, GitHub, Slack, Jira, etc.)
- Configure in project or user settings — persists across sessions
- Any tool can expose itself to Claude Code without modifying Claude Code

**Significance**: MCP is arguably Anthropic's most important strategic contribution beyond model quality. It's been adopted by VS Code, JetBrains, Cursor, Cline, Roo Code, Goose, and many other tools. It creates an ecosystem moat — tools that speak MCP work with Claude Code, and vice versa.

### Hooks System

User-defined shell commands that execute at lifecycle points:
- Before/after tool calls (e.g., run linter after every file edit)
- On session start/end
- On prompt submission
- Configured in `settings.json`

### Slash Commands

Both built-in and custom:
- Built-in: `/init`, `/compact`, `/clear`, `/review`, `/remote-control`
- Custom: Define in `.claude/commands/` directories (project or user level)
- Markdown templates with parameters

### /remote-control

Syncs a local Claude Code CLI session to the Claude web/desktop app. The terminal session appears in the app interface, allowing visual interaction, sharing with others, and richer display. This is the "bridge" between CLI power and app UX.

### IDE Integrations

- **VS Code**: Extension with Claude Code panel, inline diff preview
- **JetBrains**: Extension for IntelliJ-family IDEs
- Both provide the same core capabilities as the CLI, wrapped in IDE UX

---

## Claude App (claude.ai)

**Platforms**: Web (claude.ai), macOS desktop, Windows desktop, iOS, Android

### Key Features

- **Projects**: Persistent workspaces with custom system prompts, knowledge files, and conversation history
- **Artifacts**: Side-panel for generated content (code, documents, diagrams) that persists and can be iterated
- **File uploads**: PDFs, images, code files, spreadsheets for analysis
- **Vision**: Image understanding for screenshots, diagrams, UI mockups
- **Code execution**: JavaScript sandbox for running generated code (limited compared to full terminal access)
- **Extended thinking**: Available on Opus and Sonnet for complex reasoning tasks

### App + CLI Synergy

The `/remote-control` feature is what makes Anthropic's offering uniquely cohesive: you get the power of a terminal agent with the visual polish of an app interface. No competitor offers this bidirectional sync between CLI and GUI.

---

## Managed Agents (Background Agents)

### claude-code-action (GitHub Action)

**Repository**: [github.com/anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)

Enables Claude Code to run autonomously on Anthropic's servers, triggered by GitHub events:

```yaml
on:
  issues:
    types: [opened, labeled]
  pull_request_review_comment:
    types: [created]

jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

**Capabilities**:
- Triggered by issue creation, PR comments, review comments
- Creates branches, writes code, opens PRs
- Responds to review feedback and iterates
- Runs tests and linters to verify its own work
- Full shell access within the Action runner
- Can install dependencies, build projects

**Pricing**: No additional cost beyond API token usage. The Action runner is GitHub's (or self-hosted). You pay Anthropic for input/output tokens consumed.

### Background Agents (Anthropic-hosted)

Anthropic also offers fully-hosted background agents that run on Anthropic's infrastructure (not GitHub Actions runners). These provide:
- Longer execution time than GitHub Actions limits
- Anthropic-managed compute
- Available via API for programmatic triggering
- Accessible from claude.ai interface

---

## API Pricing (May 2026)

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Context Window |
|-------|----------------------|------------------------|----------------|
| Claude Opus 4 | $15.00 | $75.00 | 200K |
| Claude Sonnet 4 | $3.00 | $15.00 | 200K |
| Claude Haiku 3.5 | $0.80 | $4.00 | 200K |

### Prompt Caching

Automatic 90% discount on repeated context (cache hits). When Claude Code maintains a long conversation, previously-sent context is cached. Cached input reads cost 10% of fresh input. This significantly reduces costs for iterative coding sessions where the system prompt + project context remain stable.

### Batch API

50% discount on standard pricing for asynchronous, non-time-sensitive requests. Processed within 24 hours.

---

## Subscription Plans

| Plan | Price | Usage Level |
|------|-------|-------------|
| Free | $0 | Limited messages, Sonnet only |
| Pro | $20/month | Higher limits, all models |
| Max 5x | $100/month | 5x Pro usage |
| Max 20x | $200/month | 20x Pro usage |
| Team | $25-30/seat/month | Collaborative features |
| Enterprise | Custom | SSO, audit, admin controls |

**Max plans** were introduced to address power users hitting Pro caps. At $200/month (20x), heavy Claude Code users get substantial usage before hitting limits. However, with agentic coding consuming 50-200K+ tokens per complex task, even Max 20x has limits during intensive use.

### API vs. Subscription Economics

For individual power users, the economics depend on usage patterns:
- **Light use** (< $50 API/month): Pro subscription is better value
- **Moderate use** ($50-200 API/month): Max 5x likely comparable to API
- **Heavy use** (> $200 API/month): API pay-as-you-go may be cheaper than Max 20x depending on specific patterns
- **Automated agents**: API is the only option (subscriptions don't cover programmatic use)

---

## Agent SDK / Multi-Agent

Anthropic's approach to multi-agent differs from OpenAI's explicit SDK:

- **Claude Code sub-agents**: Built into Claude Code — the agent can spawn child agents for parallel tasks
- **Tool use in API**: The Messages API supports tool definitions, allowing custom agent loops
- **No standalone orchestration SDK**: Unlike OpenAI's Agents SDK, Anthropic doesn't publish a framework for building multi-agent systems. The expectation is that Claude Code itself, or MCP, handles orchestration needs.

This is both a strength (simplicity — one powerful agent vs. many coordinated ones) and a weakness (less flexibility for custom multi-agent architectures).

---

## What Makes This Best-in-Class

1. **Model quality**: Claude Opus 4 and Sonnet 4 are among the strongest coding models available
2. **CLI+App synergy**: /remote-control bridge is unique in the market
3. **MCP ecosystem**: Open protocol with broad adoption creates network effects
4. **Prompt caching**: 90% discount on repeated context is a significant cost advantage for long sessions
5. **Context engineering**: Claude Code has sophisticated built-in heuristics for what to show the model
6. **Managed agents**: Turnkey GitHub integration via Actions with strong iteration capability
7. **Extended thinking**: Transparent reasoning visible to the user

---

## What It Costs (Practically)

A typical power user running Claude Code for 4-6 hours/day of active coding:
- **Subscription**: $100-200/month (Max tier)
- **API equivalent**: Roughly $300-600/month depending on model mix and task complexity
- **Managed agents**: Additional $50-200/month depending on how many issues are delegated

The expense complaint is valid. An active user spending $400-800/month on Anthropic is the scenario driving this research.

---

## Sources

- [Anthropic API Pricing](https://www.anthropic.com/pricing) — Official pricing page
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) — Official docs
- [MCP Specification](https://modelcontextprotocol.io) — Protocol documentation
- [claude-code-action](https://github.com/anthropics/claude-code-action) — GitHub Action
- [Claude Subscription Plans](https://claude.ai/pricing) — Consumer pricing
