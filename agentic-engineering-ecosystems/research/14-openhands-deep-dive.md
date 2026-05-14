# OpenHands Architecture Deep Dive

The original report (06-self-hostable-agents.md) covers OpenHands at surface level. This section goes deeper on architecture, real-world performance, security model, and the Enterprise product launched May 2026.

---

## Updated Stats

| Metric | Original Report | Updated |
|--------|----------------|---------|
| GitHub Stars | 50,000+ | **73,410** |
| Funding | Not mentioned | **$23.8M** ($5M seed + $18.8M Series A) |
| Valuation | Not mentioned | **$100M-500M** range |
| SWE-bench Verified | "Top scores" | **64%** (#1 among open-source, March 2025) |
| Git Platform Support | GitHub only mentioned | **6 platforms**: GitHub, GitLab, Bitbucket, Azure DevOps, Forgejo, Jira/Linear/Slack |
| Enterprise Product | None | **OpenHands Enterprise** (May 2026, self-hosted) |

The 85% parity rating from the original report may be conservative. With Enterprise features, OpenHands approaches 90%+ for organizations willing to run it.

---

## Architecture

### Event-Driven Agent Loop

Three layers:

```
┌──────────────────────────────────────────┐
│  Agent (CodeActAgent)                    │
│  - Converse mode (chat) or CodeAct mode  │
│  - Bash, IPython, Browser, Editor tools  │
│  - 27 built-in skills + repo-specific    │
├──────────────────────────────────────────┤
│  Controller (AgentController)            │
│  - EventStream: Actions ↔ Observations   │
│  - Budget enforcement, iteration limits   │
│  - max_iterations=500, concurrent_convos=3│
├──────────────────────────────────────────┤
│  Runtime (multiple backends)             │
│  - Docker (primary)                      │
│  - Kubernetes (configurable resources)   │
│  - Remote, E2B, Modal, Local             │
└──────────────────────────────────────────┘
```

### CodeActAgent

Primary agent implementation, based on ICLR 2025 paper. Operates in two modes per turn:

- **Converse**: Natural language interaction with user
- **CodeAct**: Task execution via bash commands or IPython cells

Configurable tools: `enable_browsing`, `enable_editor` (str_replace_editor), `enable_jupyter`, `enable_cmd` (bash), `enable_think`, `enable_finish`.

### Context Management (Condensers)

Six strategies for managing context window overflow:

| Strategy | Approach | Key Config |
|----------|----------|------------|
| `noop` | No condensing (default) | — |
| `observation_masking` | Mask older observations, keep events | `attention_window = 100` |
| `recent` | Keep only N recent events | `max_events = 100` |
| `llm` | LLM summarizes conversation history | Uses configured model |
| `amortized` | Intelligent forgetting | Preserves important context |
| `llm_attention` | LLM scores relevance of each event | Priority-based retention |

This is more sophisticated than what the original report described. The condenser system directly addresses context engineering — one of Anthropic's claimed advantages.

### Skills/Microagents

27 built-in skills covering GitHub, Docker, Kubernetes, security, code review. Repository-specific skills loadable from `.openhands/skills/` directory. Similar in concept to Claude Code's CLAUDE.md but more structured.

### Runtime Backends

| Backend | Use Case | Isolation |
|---------|----------|-----------|
| Docker | Primary, single-server | Container-level |
| Kubernetes | Scalable, multi-node | Pod-level with resource limits |
| Remote | Managed sandbox on remote servers | Full VM isolation |
| E2B | Specialized secure execution | E2B's security model |
| Modal | Distributed scaling | Modal's infrastructure |
| Local | Development/testing only | None |

Kubernetes config: `resource_cpu_request = "1"`, `resource_memory_request = "1Gi"`, `resource_memory_limit = "2Gi"`, `pvc_storage_size = "2Gi"`.

---

## GitHub Resolver (Updated)

### Multi-Platform Support

The resolver now supports **six git platforms** (not just GitHub):
- GitHub, GitLab, Bitbucket (Cloud), Bitbucket Data Center, Azure DevOps, Forgejo

Plus issue tracker integrations: Jira, Jira Data Center, Linear, Slack.

This is a significant expansion from what the original report described.

### Trigger Mechanisms

Two invocation methods:
1. **Label-based (`fix-me`)**: Apply label → agent addresses entire issue/PR
2. **Macro-based (`@openhands-agent`)**: Mention in comment → agent focuses on that comment + context

### PR Review Iteration

Fully supported. The resolver:
- Receives branch name and PR context
- Fetches diff against main
- Processes PR body and linked issue
- Distinguishes questions (answers without code changes) from update requests (modifies code, commits, pushes)
- Handles general comments, review comments, and inline thread comments
- Uses GraphQL to traverse review thread reply chains

This matches Anthropic's managed agent capability for PR review iteration.

---

## Real-World Performance

### SWE-bench Verified Progression

| Date | Score | Method |
|------|-------|--------|
| Early 2025 | 53% | Standard |
| Feb 2025 | 61% | #1 open-source |
| Mar/Apr 2025 | **64%** | Inference-time scaling with critic model |

The 64% used best-of-N sampling: generate multiple solution trajectories, use critic/reward model to select best. Computationally expensive but demonstrates ceiling.

For comparison: SWE-agent achieved 12.47% on full SWE-bench at launch. Current gap between platforms is substantial.

### Enterprise Deployment: C3 AI

"Eight billion tokens in two weeks" (Dec 2025). C3 AI deployed OpenHands across their engineering team, processing 8B tokens in a 2-week period. One of the few public enterprise-scale reports.

### Task Types That Work

From blog posts and community reports:
- Bug fixes (well-defined, isolated)
- Test generation and coverage improvement
- Dependency upgrades and CVE remediation
- Documentation changes
- Small feature implementations
- Code review feedback processing

### Common Failure Modes

- Context window exhaustion on complex multi-file changes
- Looping behavior — agent repeats similar actions without progress
- Incorrect file edits in large codebases
- Environment setup issues with complex dependencies
- Over-engineering (more changes than necessary)
- Hallucinating APIs/functions that don't exist

---

## Resource Requirements

### Minimum (Single User)

- 4+ CPU cores, 16GB RAM
- Docker socket access required
- Port 3000 (uvicorn)
- Python 3.12+

### Concurrency

- Default `max_concurrent_conversations = 3` per user
- Each conversation spawns its own sandbox container
- Idle runtimes close after 300 seconds
- Conversation TTL: 10 days default

### Token Consumption Per Task

| Task Complexity | Iterations | Estimated Cost |
|----------------|-----------|----------------|
| Simple (typo, config) | 5-20 | $0.50-$2 |
| Medium (bug fix, small feature) | 20-50 | $2-$5 |
| Complex (multi-file, architectural) | 50-100+ | $5-$15+ |

Budget enforcement available: `max_budget_per_task` caps spending in USD.

### Cloud Deployment (Helm)

Full stack includes: PostgreSQL, Redis, Keycloak (auth), LiteLLM (model proxy), MinIO (file store), Runtime API, Automation service, Plugin directory. Requires Kubernetes 1.19+, Helm 3.2.0+.

**Licensing note**: The cloud Helm charts (OpenHands-Cloud repo) use **Polyform Free Trial License 1.0.0** — limited to 30 days per year without commercial license. Core OpenHands remains MIT.

---

## Security Model

### Container Isolation

- Default: bridge (isolated) network. Host network is opt-in.
- Not privileged by default (except for DinD use cases)
- Runs as UID 42420 (`openhands` user) with sudo inside container
- Configurable volume mounts
- Security analyzer: `llm` or `invariant` mode, enabled by default
- Confirmation mode available for headless/CLI execution

### Network Access

Sandbox containers have outbound internet by default (package install, API calls, browsing). No documented egress restrictions in OSS version. Enterprise adds containment and observability.

### Gaps

- Standard Docker isolation (no gVisor, Kata containers by default)
- No seccomp profiles or AppArmor documented
- `SANDBOX_USER_ID=0` (root) in some configurations
- No network policies in OSS documentation
- OSS version doesn't prescribe additional hardening

Enterprise version adds: "Code execution, file access, and external calls are contained and observable."

---

## OpenHands Enterprise (May 2026)

This is the major new development since the original report.

### What It Adds Over OSS

| Feature | OSS | Enterprise |
|---------|-----|-----------|
| Agent Control Plane | No | Centralized orchestration, observability, audit |
| Automations | Basic triggers | Scheduled/triggered across many repos in parallel |
| Plugin Marketplace | Repo-local skills | Organization-scoped skill sharing |
| Cost Attribution | Per-task budget | Per-org, per-user, per-conversation budgets |
| LLM Gateway | Direct API calls | Centralized model routing |
| Guardrails | Security analyzer | Default security policies across org |
| Platform Support | 6 git platforms | Same + enterprise SSO, audit logging |
| Deployment | Self-managed Docker/K8s | Self-hosted with commercial support |

### Implications

Enterprise OpenHands directly addresses the "enterprise governance gap" identified in the original report as Anthropic's unmet need. Factory AI was previously the only option; OpenHands Enterprise is now a self-hosted alternative.

For organizations needing SSO, audit trails, cost attribution, and centralized policies, OpenHands Enterprise fills the gap without vendor lock-in to a specific model provider.

---

## Comparison with SWE-agent (Detailed)

| Dimension | OpenHands (CodeActAgent) | SWE-agent (ACI) |
|-----------|------------------------|-----------------|
| Stars | 73,410 | 19,208 |
| Philosophy | Full OS access + good tools | Constrained, curated command set |
| Action space | Open-ended (any bash/Python) | Curated commands (`open`, `edit`, `search_dir`) |
| File editing | `str_replace_editor` | Custom `edit` with lint check |
| Navigation | Shell + code indexing (LocAgent) | Purpose-built `search_dir`, `find_file` |
| Runtime | Docker/K8s/Remote/E2B/Modal | Docker only |
| Browser | Full Chromium (BrowserGym) | Not core |
| Platform integrations | 6 git platforms + issue trackers | GitHub-focused |
| Web UI | Yes | No |
| PR creation | Native | Requires wrapper |
| SWE-bench Verified | 64% | Lower (varies by model) |
| Published at | ICLR 2025 | NeurIPS 2024 |

### Design Philosophy Difference

**SWE-agent**: Constrain the action space to prevent LLM errors. Provide lint-after-edit, windowed file viewing, structured search. The insight: interface design matters more than model capability.

**OpenHands**: Maximize flexibility with full OS access. Provide good tools as options. Add guardrails via security analyzer and budget limits. The insight: general-purpose execution with safety nets scales better than constrained interfaces.

Both approaches have merit. SWE-agent influenced the entire field (OpenHands' own ACI package is inspired by it). OpenHands has surpassed SWE-agent on benchmarks but uses more compute to do so.

---

## Revised Parity Assessment

| Dimension | Original (06) | Revised |
|-----------|--------------|---------|
| Overall parity | ~85% | **~90%** (OSS), **~95%** (Enterprise) |
| GitHub integration | Good | **Excellent** (6 platforms, full review iteration) |
| Enterprise governance | Gap | **Addressed** (Enterprise product) |
| Context engineering | "Less mature" | **Competitive** (6 condenser strategies) |
| Production readiness | Medium | **Medium-High** (C3 AI case study, $23.8M funding) |

The remaining gaps vs. Anthropic's offering:
1. No /remote-control equivalent (app sync)
2. Less mature context engineering heuristics (condensers exist but less battle-tested)
3. Anthropic continuously improves Claude Code's prompts; OpenHands relies on community + small team
4. Cloud deployment licensing is NOT open source (Polyform 30-day limit)

---

## Sources

- [OpenHands GitHub](https://github.com/All-Hands-AI/OpenHands) — 73,410 stars
- [OpenHands Blog](https://openhands.dev/blog) — Release notes, case studies
- [ArXiv Paper](https://arxiv.org/abs/2407.16741) — CodeAct architecture
- [SWE-bench Verified](https://www.swebench.com/verified) — Benchmark results
- [Series A Announcement](https://siliconangle.com/2025/03/04/yc-backed-hands-ai-lands-18-8-million-advance-ai-coding-agents/) — $18.8M raise
- [C3 AI Case Study](https://openhands.dev/blog) — 8B tokens in 2 weeks
- [OpenHands-Cloud Helm Charts](https://github.com/All-Hands-AI/OpenHands-Cloud) — Polyform license
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) — 19,208 stars
