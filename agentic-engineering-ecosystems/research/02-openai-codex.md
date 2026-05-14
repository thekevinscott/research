# OpenAI / Codex Ecosystem

OpenAI offers the broadest product surface in the agentic engineering space — spanning open-source CLI tools, cloud-hosted autonomous agents, a multi-agent SDK, and consumer subscription tiers. Their strategy is platform breadth rather than single-product depth.

---

## Codex CLI

**Repository**: [github.com/openai/codex](https://github.com/openai/codex)  
**Stars**: 82,000+  
**License**: Apache 2.0  
**Language**: Rust (96.2% of codebase)  
**Distribution**: Single binary, also available via `npm install -g @openai/codex` or Homebrew

### Architecture

Unlike Claude Code (proprietary), Codex CLI is fully open source. The Rust implementation means it ships as a single binary with no runtime dependencies — no Node.js required at execution time.

### Capabilities

- File reading, writing, and editing across entire codebases
- Shell command execution
- Git operations (staging, committing, branch management)
- Multimodal input — accepts screenshots and diagrams
- Network-disabled sandboxed execution by default (OS-level sandboxing)

### Three Autonomy Modes

| Mode | File Edits | Commands | Use Case |
|------|-----------|----------|----------|
| `suggest` | Requires approval | Requires approval | Learning, reviewing |
| `auto-edit` | Auto-applied | Requires approval | Day-to-day coding |
| `full-auto` | Auto-applied | Auto-applied | Automated pipelines |

### Models

Configurable: o3, o4-mini, GPT-4.1 (default varies by task). Can authenticate via "Sign in with ChatGPT" (uses subscription quota) or via API key.

### Key Differences from Claude Code

| Dimension | Codex CLI | Claude Code |
|-----------|-----------|-------------|
| Source | Open source (Apache 2.0) | Proprietary |
| Sandboxing | Network-disabled by default (OS-level) | Permission system, no sandbox |
| MCP support | Yes (added May 2025) | Yes (core feature) |
| Extended thinking | Hidden (o-series CoT) | Visible and inspectable |
| Git depth | Basic operations | Deep (merge conflicts, PR workflows) |
| IDE extensions | VS Code, Cursor, Windsurf | VS Code, JetBrains |
| App sync | No equivalent to /remote-control | /remote-control to claude.ai |

### Assessment

Codex CLI is a competent terminal agent but trades depth for openness. Its lack of MCP support means it can't be extended with custom tools the way Claude Code can. The sandboxing approach (network disabled by default) is more conservative — good for security, limiting for tasks requiring internet access (installing packages, fetching docs).

---

## Codex Cloud (chatgpt.com/codex)

A separate product from the CLI — fully autonomous cloud agents.

### Architecture

- Powered by **codex-1** (o3 fine-tuned for software engineering)
- Each task runs in an isolated cloud microVM
- Pre-loaded with repository code and environment
- **No internet access** during execution (security/reproducibility constraint)
- Tasks typically take 1-30 minutes

### Capabilities

- Connects directly to GitHub repositories
- Creates branches and pull requests automatically
- Runs tests, linters, and type checkers to verify its own work
- Multiple tasks can run in parallel
- Provides full terminal logs and citations for every step
- Handles: features, bug fixes, refactoring, codebase Q&A

### Availability

ChatGPT Pro ($200/month), Enterprise, and Team users. Available at chatgpt.com/codex.

### Key Limitation: No Internet

The deliberate choice to block internet access during agent execution is a meaningful constraint. The agent cannot:
- Install new packages from registries during execution
- Fetch documentation from the web
- Hit external APIs for testing

This is a security/reproducibility decision, but it limits the range of tasks the agent can handle compared to Anthropic's managed agents (which have full internet access).

---

## OpenAI API

### Model Pricing (per 1M tokens)

| Model | Input | Cached Input | Output | Context |
|-------|-------|-------------|--------|---------|
| GPT-4.1 | $2.00 | $0.50 | $8.00 | 1,000,000 |
| GPT-4.1 Mini | $0.40 | $0.10 | $1.60 | 1,000,000 |
| GPT-4.1 Nano | $0.10 | $0.025 | $0.40 | 1,000,000 |
| o3 | $10.00 | $2.50 | $40.00 | 200,000 |
| o4-mini | $1.10 | $0.275 | $4.40 | 200,000 |

### Notable Features

- **1M token context window** (GPT-4.1 family) — 5x Claude's 200K
- **Batch API**: 50% discount for async processing (24-hour window)
- **Structured Outputs**: Guaranteed JSON schema adherence
- **Responses API**: Newer API with built-in tool support, web search, file search
- **Reasoning models** (o3, o4-mini): Chain-of-thought reasoning, though tokens are hidden (not inspectable like Claude's extended thinking)

### Context Window Advantage

GPT-4.1's 1M token context is a genuine advantage for large codebases. Where Claude Code must carefully manage what fits in 200K tokens (using repo maps, selective file reading, compaction), GPT-4.1 can theoretically hold an entire medium-sized codebase in context. In practice, latency and cost scale with context size, but the option exists.

---

## Agents SDK

**Repository**: [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)  
**Stars**: ~26,000  
**License**: MIT  
**Language**: Python 3.10+

### Core Concepts

1. **Agents**: LLMs configured with instructions, tools, guardrails, and handoffs
2. **Handoffs**: Delegation mechanisms for multi-agent orchestration
3. **Tools**: Function tools, MCP tools, hosted tools (code interpreter, file search)
4. **Guardrails**: Input/output validation running in parallel
5. **Sessions**: Automatic conversation history management
6. **Tracing**: Built-in debugging and optimization tracking
7. **Realtime Agents**: Voice agent support

### Provider Agnostic

Despite being OpenAI's SDK, it supports 100+ LLMs via LiteLLM integration — including Claude. This makes it usable as a general-purpose agent framework regardless of model preference.

### vs. Anthropic's Approach

Anthropic has no equivalent SDK. Their philosophy is "one powerful agent" (Claude Code) rather than "many coordinated agents." For users wanting multi-agent orchestration (e.g., one agent writes code while another reviews it), OpenAI's SDK is the most mature first-party option.

---

## GitHub Copilot Relationship

OpenAI models power GitHub Copilot, creating a massive distribution channel:

- **Copilot coding agent**: Assign issues to `@copilot`, agent works in Codespaces
- **Copilot Pro+**: $39/month, includes ~1,500 premium requests
- **Multi-model**: Copilot now supports Claude, Gemini alongside GPT models

This means OpenAI's models reach developers through GitHub without them explicitly choosing OpenAI. The agent capability is bundled with existing Copilot subscriptions.

---

## Subscription Tiers

| Tier | Price | Key Features |
|------|-------|--------------|
| Free | $0 | GPT-4o mini, limited access |
| Plus | $20/month | GPT-4o, o4-mini, limited o3, DALL-E |
| Pro | $200/month | Unlimited o3, Codex cloud, Operator |
| Team | $25-30/user/month | Everything in Plus + admin |
| Enterprise | Custom | Unlimited, SSO, audit |

### Pro Tier ($200/month)

The most relevant comparison to Claude Max. Includes:
- **Unlimited o3** reasoning (no usage caps on most powerful model)
- **Codex cloud agent** access
- **Operator** (browser automation)
- Priority access to new features

This is more generous than Claude Max 20x ($200/month) — "unlimited" vs. "20x base rate." However, o3's reasoning quality for coding specifically may not match Claude Opus 4.

---

## Operator (Browser Automation)

- Autonomous web browser agent at operator.chatgpt.com
- Powered by CUA (Computer-Using Agent) model
- Can click, fill forms, navigate, scroll
- Browser-only (not full desktop like Anthropic's computer use)
- Currently Pro tier only ($200/month)

---

## Key Gaps: OpenAI vs. Anthropic

### OpenAI offers, Anthropic doesn't:
1. **Open-source agent tooling** (Codex CLI, Agents SDK)
2. **1M token context** (GPT-4.1)
3. **Multi-agent orchestration SDK** (production-ready framework)
4. **Consumer browser automation** (Operator — ready to use)
5. **More pricing tiers** (Nano at $0.10/$0.40 through o3 at $10/$40)
6. **Image generation** (DALL-E integrated)
7. **$200/month unlimited reasoning** (no caps)
8. **Voice/realtime agents** (GPT-4o realtime API)

### Anthropic offers, OpenAI doesn't:
1. **MCP** (open protocol, ecosystem adoption)
2. **Transparent extended thinking** (visible reasoning tokens)
3. **CLI agent depth** (deeper git integration, more mature)
4. **Full desktop computer use** (not just browser)
5. **Prompt caching** (automatic 90% discount)
6. **CLI↔App sync** (/remote-control — unique)
7. **Simpler API surface** (one endpoint, clear versioning)
8. **Internet access during managed agent execution**

---

## Sources

- [OpenAI Codex CLI](https://github.com/openai/codex) — GitHub repository
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — GitHub repository
- [OpenAI API Pricing](https://openai.com/api/pricing) — Official pricing
- [ChatGPT Pricing](https://openai.com/chatgpt/pricing) — Subscription tiers
- [Codex Cloud](https://chatgpt.com/codex) — Product page
- [GitHub Copilot](https://github.com/features/copilot) — Features and pricing
- [Operator](https://operator.chatgpt.com) — Browser automation
