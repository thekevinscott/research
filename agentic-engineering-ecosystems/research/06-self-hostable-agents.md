# Self-Hostable Agentic Coding Infrastructure

This is the highest-priority section of this report. The question: **can you run managed coding agents on your own infrastructure, achieving parity with Anthropic's managed agents or OpenAI's Codex Cloud, without writing the platform yourself?**

The answer is yes — with caveats on maturity and integration depth.

---

## The Reference Target

Anthropic's managed agents (via [claude-code-action](https://github.com/anthropics/claude-code-action)) provide:

1. **Event-triggered execution**: GitHub issue created → agent runs autonomously
2. **Sandboxed environment**: Agent operates in isolated compute (Anthropic's servers)
3. **Repository access**: Full read/write to the repo, can install deps, run tests
4. **PR creation**: Agent creates branches, commits code, opens PRs
5. **Iteration**: Agent can respond to PR review comments, fix issues
6. **Multi-model**: Uses Claude Sonnet/Opus via API

A self-hosted alternative must replicate these properties. Below is a survey of what exists.

---

## 1. OpenHands (formerly OpenDevin)

**Repository**: [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)  
**Stars**: 50,000+ (as of May 2026)  
**License**: MIT  
**Language**: Python  

### What It Is

OpenHands is the most mature open-source platform for running autonomous AI software agents. It provides a complete runtime environment where AI agents can write code, execute shell commands, browse the web, and interact with development tools — all within sandboxed Docker containers.

### Architecture

```
┌─────────────────────────────────────────┐
│  Web UI / API / GitHub App              │
├─────────────────────────────────────────┤
│  Agent Controller                       │
│  (orchestrates LLM + tool calls)        │
├─────────────────────────────────────────┤
│  Sandboxed Runtime (Docker container)   │
│  - Shell access                         │
│  - File system                          │
│  - Browser (Playwright)                 │
│  - Code editing                         │
└─────────────────────────────────────────┘
```

Each agent task runs in an isolated Docker container. The container is pre-loaded with the target repository and any specified dependencies. The agent can execute arbitrary commands within the sandbox but cannot escape to the host.

### Key Capabilities

- **GitHub Resolver**: A dedicated component ([openhands-resolver](https://github.com/All-Hands-AI/openhands-resolver)) that acts as a GitHub bot. Configure it as a GitHub Action or webhook — when issues are created with a specific label, the resolver automatically attempts to fix them and opens a PR.
- **Multi-model support**: Works with Claude (Anthropic API), GPT-4/o3 (OpenAI API), Gemini, and any OpenAI-compatible endpoint (OpenRouter, Together, etc.)
- **Web UI**: Browser-based interface for monitoring agent progress, reviewing outputs, and intervening
- **SWE-bench performance**: Consistently ranks among top open-source solutions on SWE-bench Verified
- **Extensible agents**: Multiple agent implementations (CodeAct, Browsing, etc.) with ability to create custom agents

### Deployment

```bash
# Minimal deployment
docker pull docker.all-hands.dev/all-hands-ai/openhands:latest
docker run -p 3000:3000 \
  -e LLM_API_KEY=sk-... \
  -e LLM_MODEL=claude-sonnet-4-20250514 \
  docker.all-hands.dev/all-hands-ai/openhands:latest
```

Full deployment uses Docker Compose with separate containers for frontend, backend, and sandboxed runtime. Supports configuration via YAML for LLM providers, model selection, and agent behavior.

### GitHub Integration Depth

- **As GitHub Action**: Add to `.github/workflows/` — triggers on issue creation, PR comments
- **As GitHub App**: Install on repos for persistent bot presence
- **PR workflow**: Creates branches, commits, opens PRs, responds to review feedback
- **Label-based triggering**: Configure which issues the agent attempts (e.g., label `fix-me`)

### Maturity Assessment

| Dimension | Rating |
|-----------|--------|
| Stability | Medium-High — active development, occasional breaking changes |
| Documentation | Good — official docs at docs.all-hands.dev |
| Community | Very active — Discord, regular releases |
| Production readiness | Medium — used by some teams, but expect rough edges |
| Model flexibility | Excellent — any OpenAI-compatible API |

### Parity with Anthropic Managed Agents

OpenHands achieves **~85% parity** with Anthropic's managed agents:
- ✅ Event-triggered from GitHub issues/PRs
- ✅ Sandboxed execution in Docker
- ✅ Creates PRs, responds to reviews
- ✅ Multi-model (can use Claude itself, or cheaper alternatives)
- ✅ Self-hosted on your own infrastructure
- ⚠️ Requires more setup/maintenance than Anthropic's turnkey offering
- ⚠️ No built-in billing/usage management
- ❌ Less polished UX for non-technical team members

**This is the strongest candidate for "managed agents you run yourself."**

---

## 2. SWE-agent (Princeton NLP)

**Repository**: [github.com/princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent)  
**Stars**: ~15,000+  
**License**: MIT  
**Language**: Python  

### What It Is

SWE-agent is a research-grade autonomous coding agent developed by Princeton's NLP group. It turns LLMs into software engineering agents that can autonomously navigate repositories, understand code, make edits, and run tests. Its primary innovation is the **Agent-Computer Interface (ACI)** — a custom set of commands and file viewing tools designed specifically for LLMs (as opposed to human-designed tools like vim or grep).

### Architecture

SWE-agent runs tasks inside Docker containers. The agent receives a GitHub issue or bug description, then autonomously:
1. Navigates the repository structure
2. Identifies relevant files
3. Makes code changes using its custom editor
4. Runs tests to verify the fix
5. Outputs a patch/diff

### Key Capabilities

- **Custom ACI**: Purpose-built commands (`open`, `edit`, `search_dir`, `find_file`) that are more LLM-friendly than standard shell tools. This is a genuine innovation — agents perform significantly better with ACI than raw bash.
- **SWE-bench champion**: Achieved top scores on SWE-bench, the standard benchmark for automated program repair
- **Docker isolation**: Each task runs in a fresh container
- **Multi-model**: Works with GPT-4, Claude, and other models
- **Headless execution**: Designed to run without human interaction

### Deployment

```bash
# Clone and setup
git clone https://github.com/princeton-nlp/SWE-agent.git
cd SWE-agent
pip install -e .

# Run on a GitHub issue
python run.py \
  --model claude-sonnet-4-20250514 \
  --instance_id "repo__issue_123" \
  --data_path path/to/instance.json
```

SWE-agent is more of a library/tool than a platform. It requires wrapping with orchestration code to achieve the "managed agent" workflow (GitHub webhooks → SWE-agent → PR creation).

### GitHub Integration

SWE-agent does **not** natively integrate with GitHub events. It takes issue descriptions as input and produces patches as output. To achieve managed-agent behavior, you must build the glue:

1. GitHub webhook catches issue creation
2. Your orchestrator formats the issue for SWE-agent
3. SWE-agent runs in Docker, produces a patch
4. Your orchestrator applies the patch, creates a branch, opens a PR

Several community projects wrap SWE-agent with this orchestration, but none are as turnkey as OpenHands' resolver.

### Maturity Assessment

| Dimension | Rating |
|-----------|--------|
| Research quality | Excellent — peer-reviewed, reproducible |
| Production readiness | Low-Medium — research tool, not a product |
| Documentation | Good for researchers, sparse for operators |
| Community | Academic community, slower release cycle |
| Model flexibility | Good — configurable LLM backend |

### Parity with Anthropic Managed Agents

SWE-agent achieves **~50% parity** out of the box:
- ✅ Autonomous code editing and testing
- ✅ Docker-isolated execution
- ✅ Strong benchmark performance
- ⚠️ No native GitHub integration (must build webhook→agent→PR pipeline)
- ⚠️ No web UI for monitoring
- ❌ No PR review response capability
- ❌ More setup required than OpenHands

**Best for**: Users comfortable building orchestration who want the best-performing open-source agent core.

---

## 3. Goose (Block/Square)

**Repository**: [github.com/block/goose](https://github.com/block/goose)  
**License**: Apache 2.0  
**Language**: Rust  

### What It Is

Goose is Block's open-source AI agent that operates as a local CLI tool with deep extensibility via MCP (Model Context Protocol). It's designed as a general-purpose developer agent — not specifically for autonomous managed execution, but its architecture makes it adaptable.

### Key Capabilities

- **MCP-native**: First-class support for Model Context Protocol. Every tool Goose uses is an MCP server, making it trivially extensible.
- **Multi-model**: Supports Claude, GPT-4, Gemini, and other providers
- **CLI-first**: Runs in your terminal, operates on your local filesystem
- **Extensible**: Adding new capabilities means writing or connecting MCP servers
- **Shell execution**: Can run arbitrary commands

### As Self-Hosted Infrastructure

Goose is primarily a local tool (like Claude Code itself), not a managed agent platform. However, its MCP architecture means you could potentially:
1. Run Goose in a container triggered by webhooks
2. Connect GitHub MCP server for repo operations
3. Use filesystem MCP server for code editing

This requires building the orchestration layer — Goose itself doesn't provide event-triggered autonomous execution.

### Parity with Anthropic Managed Agents

Goose achieves **~30% parity** as a managed agent:
- ✅ Excellent code editing and shell capabilities
- ✅ MCP extensibility for any tool integration
- ✅ Multi-model support
- ❌ No GitHub event triggering
- ❌ No web UI or monitoring
- ❌ No built-in sandboxing (runs with your permissions)
- ❌ Designed for interactive use, not autonomous execution

**Best for**: Local agentic coding (Claude Code alternative), not managed agents.

---

## 4. Aider in CI/CD

**Repository**: [github.com/Aider-AI/aider](https://github.com/Aider-AI/aider)  
**Stars**: 30,000+  
**License**: Apache 2.0  

### The Pattern

Aider is designed as an interactive pair-programming tool, but it has a `--yes-always` flag and scriptable interface that enables automated use. The community has developed patterns for running Aider in GitHub Actions:

```yaml
# .github/workflows/aider-fix.yml
name: Aider Auto-Fix
on:
  issues:
    types: [labeled]
jobs:
  fix:
    if: contains(github.event.issue.labels.*.name, 'aider-fix')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install aider-chat
      - run: |
          aider --yes-always \
            --model claude-sonnet-4-20250514 \
            --message "${{ github.event.issue.body }}" \
            --auto-commits
      - uses: peter-evans/create-pull-request@v6
        with:
          title: "Fix: ${{ github.event.issue.title }}"
```

### Strengths of This Approach

- **Mature tool**: Aider is well-tested, stable, and handles git operations gracefully
- **Model agnostic**: Works with any model provider
- **Architect mode**: Can use a powerful model for planning and a cheap model for editing
- **Repo map**: Tree-sitter based understanding of repository structure
- **Cost control**: You choose the model and pay API costs directly
- **Simple**: No complex platform to deploy — just a pip install in CI

### Limitations

- **No iteration on PR feedback**: Basic pipeline can't respond to review comments
- **No sandboxing beyond CI runner**: Limited to what GitHub Actions provides
- **Single-shot**: Runs once per trigger, doesn't iteratively debug
- **No web UI**: Monitoring requires reading CI logs
- **Context limitations**: Large repos may exceed model context windows

### Parity with Anthropic Managed Agents

Aider-in-CI achieves **~60% parity**:
- ✅ Event-triggered via GitHub Actions
- ✅ Creates PRs automatically
- ✅ Multi-model, cost-controlled
- ✅ Simple deployment (pip install)
- ⚠️ Limited iteration (single-shot per trigger)
- ❌ No PR review response loop
- ❌ No web UI / monitoring dashboard

**Best for**: Teams wanting a lightweight, low-maintenance automated agent without deploying a full platform.

---

## 5. PR-Agent (Qodo Open Source)

**Repository**: [github.com/Codium-ai/pr-agent](https://github.com/Codium-ai/pr-agent)  
**Stars**: 10,000+  
**License**: Apache 2.0  

### What It Is

PR-Agent is the open-source core of Qodo Merge — an AI-powered code review and PR management tool. It's specifically designed to run as a self-hosted GitHub bot.

### Key Capabilities

- **Automated PR review**: Analyzes diffs, suggests improvements, identifies bugs
- **PR description generation**: Auto-generates PR descriptions from code changes
- **Code suggestions**: Inline code improvement suggestions
- **Test generation**: Can suggest tests for changed code
- **Multi-model**: Supports Claude, GPT-4, and other providers
- **Self-hosted**: Run on your own infrastructure as a GitHub App

### Deployment

```bash
# Docker deployment
docker run -e OPENAI_KEY=sk-... \
  -e GITHUB_TOKEN=ghp_... \
  codiumai/pr-agent:latest
```

Or as a GitHub Action:
```yaml
- uses: Codium-ai/pr-agent@main
  with:
    openai_key: ${{ secrets.OPENAI_KEY }}
```

### Scope

PR-Agent is **not** a general-purpose coding agent. It reviews and improves existing PRs but does not autonomously write features or fix bugs from issues. It's complementary to managed agents — use an agent to write code, use PR-Agent to review it.

### Parity with Anthropic Managed Agents

PR-Agent achieves **~25% parity** (different scope):
- ✅ Self-hosted, event-triggered
- ✅ GitHub-native (responds to PR events)
- ✅ Multi-model
- ❌ Does not write features or fix bugs from issues
- ❌ Review-only, not generative (with exceptions for suggestions)

**Best for**: Self-hosted code review automation. Pair with OpenHands or SWE-agent for full coverage.

---

## 6. Orchestration Patterns: Building Your Own Managed Agent Pipeline

For teams that want maximum control, the common pattern is:

```
GitHub Webhook → Orchestrator → Agent (in container) → Git operations → PR
```

### Components

1. **Webhook receiver**: n8n, Temporal worker, or a simple Express/FastAPI server
2. **Queue**: Redis, RabbitMQ, or cloud queue for handling multiple concurrent tasks
3. **Agent runtime**: Docker container with the agent tool (OpenHands, SWE-agent, Aider)
4. **Git operations**: Uses GitHub API to create branches, push commits, open PRs
5. **Monitoring**: Langfuse, OpenTelemetry, or custom logging

### n8n + AI Agent Pattern

[n8n](https://n8n.io) (open source, self-hostable workflow automation) has native AI agent nodes:

```
[GitHub Trigger] → [AI Agent Node] → [Execute Command] → [GitHub: Create PR]
```

- n8n handles the orchestration, retry logic, and monitoring
- AI Agent node connects to any LLM provider
- Self-hosted via Docker: `docker run -it n8n/n8n`
- Visual workflow builder for non-trivial pipelines

### Temporal + Agent Pattern

For more robust orchestration:
- [Temporal](https://temporal.io) provides durable execution, retries, and long-running workflow support
- Model the agent task as a Temporal workflow
- Each step (clone repo, run agent, create PR) is an activity with retry semantics
- Self-hosted: `docker compose up` with Temporal server

### Key Decisions

| Decision | Options |
|----------|---------|
| Orchestrator | n8n, Temporal, custom FastAPI |
| Agent tool | OpenHands, SWE-agent, Aider |
| Isolation | Docker-in-Docker, Kubernetes pods, Firecracker |
| Model provider | Anthropic API, OpenAI, OpenRouter, DeepSeek |
| Monitoring | Langfuse, OpenTelemetry, Grafana |
| Concurrency | Queue-based (Redis), k8s job queue |

---

## 7. Docker/Kubernetes Patterns for Agent Isolation

Running AI agents safely requires sandboxing — agents can execute arbitrary code and must not be able to escape to the host or access other tenants.

### Docker-in-Docker (DinD)

```yaml
# docker-compose.yml for agent execution
services:
  agent:
    image: openhands:latest
    privileged: false
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
    networks:
      - agent-network
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
```

### Kubernetes Job Pattern

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: agent-task-${ISSUE_ID}
spec:
  ttlSecondsAfterFinished: 3600
  template:
    spec:
      containers:
      - name: agent
        image: openhands:latest
        resources:
          limits:
            cpu: "2"
            memory: "4Gi"
        env:
        - name: LLM_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-credentials
              key: api-key
      restartPolicy: Never
  backoffLimit: 2
```

### Security Considerations

- **Network policy**: Agents should have outbound access only to LLM APIs and the target repo (git clone). Block access to internal services, metadata endpoints, etc.
- **Resource limits**: CPU, memory, disk, and time limits prevent runaway agents
- **Ephemeral**: Container is destroyed after task completion — no persistent state
- **Secrets management**: LLM API keys injected via secrets, not baked into images
- **Output validation**: Review agent-generated code before merging (automated CI checks + human review)

---

## 8. Comparison Matrix: Self-Hostable Options

| Tool | Deploy Complexity | GitHub Trigger | PR Creation | Review Loop | Model Flex | Sandboxing | Web UI | Maturity |
|------|-------------------|----------------|-------------|-------------|------------|------------|--------|----------|
| **OpenHands** | Medium (Docker Compose) | Yes (Action + App) | Yes | Yes | Excellent | Docker containers | Yes | Medium-High |
| **SWE-agent** | High (requires orchestration) | No (must build) | No (must build) | No | Good | Docker | No | Medium |
| **Aider in CI** | Low (pip install in Action) | Yes (native Actions) | Yes (with action) | No | Excellent | CI runner | No | High |
| **Goose** | Low (single binary) | No | No | No | Excellent | None (local) | No | Medium |
| **PR-Agent** | Low (Docker) | Yes | N/A (review only) | Yes | Good | N/A | No | High |
| **Custom (n8n+agent)** | Medium-High | Yes | Yes | Possible | Excellent | Configurable | Yes (n8n UI) | Varies |

---

## 9. Recommended Stack for Self-Hosted Managed Agents

### Tier 1: Quick Start (30 minutes)

**Aider in GitHub Actions** — for teams that want automated agent capabilities with minimal infrastructure:
- Add a workflow file, configure API key secret
- Label issues to trigger agent
- Agent creates PRs automatically
- Cost: API tokens only

### Tier 2: Full Platform (2-4 hours)

**OpenHands** — for teams wanting near-parity with Anthropic's managed agents:
- Deploy via Docker Compose on a server with 8GB+ RAM
- Configure GitHub App for webhook integration
- Set up LLM provider credentials
- Use GitHub resolver for automated issue fixing
- Web UI for monitoring and manual interaction

### Tier 3: Enterprise (days)

**OpenHands + Kubernetes + Temporal** — for teams needing robust, scalable agent infrastructure:
- Kubernetes for container orchestration and scaling
- Temporal for durable workflow execution
- OpenHands as the agent runtime
- Custom GitHub App for fine-grained trigger control
- Langfuse for observability and cost tracking
- Network policies for security isolation

---

## 10. Critical Gaps and Honest Assessment

### What self-hosted solutions still lack vs. Anthropic/OpenAI managed agents:

1. **Model quality**: Anthropic's managed agents use Claude, which remains among the strongest models for coding. Self-hosted tools can use Claude via API, but you're paying the same per-token cost — the savings come from avoiding subscription overhead and controlling infrastructure.

2. **Integrated experience**: Anthropic's offering is seamless — `/remote-control` syncs to the app, managed agents just work from GitHub. Self-hosted requires stitching together components.

3. **Reliability**: Anthropic manages uptime, scaling, and error handling. Self-hosted means you own the infrastructure failures.

4. **Context engineering**: Claude Code has extensive built-in heuristics for context management (what to include in the prompt, when to compact, how to search). OpenHands and SWE-agent have their own approaches but are less mature.

5. **Continuous improvement**: Anthropic continuously improves Claude Code's prompts, tool definitions, and agent behavior. Self-hosted tools improve at community pace.

### What self-hosted solutions offer that managed services don't:

1. **Model flexibility**: Use Claude for complex tasks, cheaper models (DeepSeek, Gemini Flash) for routine ones. Route dynamically based on task complexity.

2. **Cost control**: No subscription caps. Pay only for API tokens consumed. Use prompt caching aggressively.

3. **Data sovereignty**: Code never leaves your infrastructure (except to the LLM API, which you can also self-host if needed).

4. **Customization**: Modify agent behavior, add custom tools, integrate with internal systems.

5. **No vendor lock-in**: Switch LLM providers without changing your infrastructure.

---

## Sources

- [OpenHands (All-Hands-AI)](https://github.com/All-Hands-AI/OpenHands) — MIT licensed, 50K+ stars
- [OpenHands Resolver](https://github.com/All-Hands-AI/openhands-resolver) — GitHub bot component
- [OpenHands Docs](https://docs.all-hands.dev) — Official documentation
- [SWE-agent (Princeton NLP)](https://github.com/princeton-nlp/SWE-agent) — MIT licensed
- [SWE-bench](https://www.swebench.com/) — Standard benchmark for coding agents
- [Goose (Block)](https://github.com/block/goose) — Apache 2.0, MCP-native agent
- [Aider](https://github.com/Aider-AI/aider) — Apache 2.0, 30K+ stars
- [PR-Agent (Qodo)](https://github.com/Codium-ai/pr-agent) — Apache 2.0
- [n8n](https://github.com/n8n-io/n8n) — Workflow automation, self-hostable
- [Temporal](https://temporal.io) — Durable execution framework
- [Anthropic claude-code-action](https://github.com/anthropics/claude-code-action) — Reference implementation
