[Back to Tools](/tools "/tools")

![9 Open-Source Agent Orchestrators for AI Coding (2026)](https://cdn.sanity.io/images/oraw2u2c/production/fdb02c9709832d5948676420df73f2ad75270124-1600x900.svg)

Open-source agent orchestrators let me run multiple AI coding agents in parallel across isolated git worktrees, but most still leave task alignment, conflict resolution, and merge decisions on my plate.

This review covers nine numbered entries (eleven tools in total, since the Conductor entry bundles three variants): Composio Agent Orchestrator, Emdash, Baton, the Conductor family (conductor.build, Code Conductor, Microsoft Conductor), Bernstein, Claude Squad, Crystal/Nimbalyst, Vibe Kanban, and Agent Kanban. The goal is practical: give you enough detail to pick the right coordination depth for your workflow, and show where spec-driven orchestration with [Intent](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent") takes over when OSS tools hit their limits.

## TL;DR

Dispatching one agent at a time leaves me waiting. The nine OSS orchestrators I tested all solve parallel execution through git worktrees, but coordination depth varies sharply across them. Claude Squad is my terminal pick for solo work. For cross-service work where specs need to stay aligned as code changes, Intent fills the gap.

## Why Parallel Agent Tooling Exists

The single-agent IDE assistant assumes one writer, one working directory, one mental model. That assumption breaks the moment I try to run three agents against the same repo. They clobber each other's files, fight over the dev server port, and leave me reconstructing what happened from `git reflog`.

Every tool in this roundup exists because the OSS community hit that wall and had to solve it. Git worktrees became the consensus isolation primitive within about eighteen months. The interesting differences are what each project built on top of that foundation.

### See how Intent coordinates parallel agents through living specs that stay aligned as plans evolve.

[Build with Intent](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent")

Free tier available · VS Code extension · Takes 2 minutes

## What I Evaluated

I scored every tool against four criteria that matter when I'm running three to six agents on a real codebase. The quick reference:

| Dimension | What to look for | What makes it good |
| --- | --- | --- |
| Isolation | Worktrees vs. containers vs. tmux-only | Worktrees alone leave port and database collisions unsolved; look for $PORT injection or containerization |
| Agent support | CLI providers wired in | Look for the two or three agents your team uses daily; raw count matters less than coverage of your stack |
| Coordination | Session manager vs. task graph vs. spec-driven | Determines how much manual merging you do; the sharpest differentiator |
| UI | TUI, desktop, VS Code, web, or CLI | Affects whether teammates will adopt it |

The coordination axis is where the tools diverge most. I think of it as a three-step ladder:

1. **Per-edit approval (human-in-the-loop):** I review every change before it lands. Claude Squad, Crystal/Nimbalyst, and the [Conductor family](https://www.augmentcode.com/tools/intent-vs-conductor-macos-agent-orchestrators "https://www.augmentcode.com/tools/intent-vs-conductor-macos-agent-orchestrators") sit here.
2. **Milestone gates (human-on-the-loop):** The tool handles retries and CI failures autonomously, and I step in at PR time. Composio AO, Bernstein.
3. **Spec-driven verification:** A living artifact constrains what agents can produce, and a verifier checks compliance before merge. Intent.

With those criteria set, here's how each tool performs in practice.

## 1. Composio Agent Orchestrator

**Repository:** [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator "https://github.com/ComposioHQ/agent-orchestrator") | **License:** MIT | **Package:** `@aoagents/ao-cli` v0.3.0

Composio AO is a full-automation system: multiple agents running in isolated worktrees, each with its own PR, supervised from a single dashboard. Of every tool I tested, AO is the one that pushes hardest past session management into autonomous PR handling. Agents fix CI failures, respond to review comments, and manage their own PR lifecycle without asking me to approve each edit.

I tested AO on a mid-size TypeScript monorepo with flaky tests. The lifecycle manager caught three CI failures, pulled the logs, fed them to the agent, and retried twice before escalating one to me. The autonomy held up under realistic conditions, which is the behavior I want from a parallel runner.

**Isolation:** Git worktrees plus tmux sessions per agent, with a process-based option if tmux isn't available.

**Agent support:** Claude Code, Codex, Aider, OpenCode. The [plugin architecture](https://github.com/ComposioHQ/agent-orchestrator/blob/main/CONTRIBUTING.md "https://github.com/ComposioHQ/agent-orchestrator/blob/main/CONTRIBUTING.md") exposes slots for runtime, agent, workspace, tracker, SCM, notifier, terminal, and lifecycle, and extending to new agents works as cleanly in practice as the docs claim.

**Coordination:** Human-on-the-loop with milestone gates. CI retry runs twice, then escalates. Agent crash recovery polls and attempts automatic restarts.

**UI:** Web dashboard at `localhost:3000` with a Kanban-style view that groups sessions by state (failing CI, awaiting review, running fine). CLI output from `ao session ls` parses with grep and awk, though a `--json` flag isn't documented.

**Known limitations:** Agents go idle more than I expected between steps. On a four-agent run, two sessions sat idle for 90+ seconds waiting on tool approval. If you're paying per-token, that idleness adds up. The package rename from `@composio/agent-orchestrator` to `@composio/ao` has also left older tutorials stale.

**Choose AO if:** You want PR-level autonomy and don't mind running a dashboard process. **Skip AO if:** You need per-edit review or work primarily offline.

## 2. Emdash (YC W26)

**Repository:** [generalaction/emdash](https://github.com/generalaction/emdash "https://github.com/generalaction/emdash") | **License:** Apache-2.0

Emdash is the Electron desktop app I reach for when a team uses a mix of coding agents. It positions itself as an "agent-first development environment," and breadth is its defining feature: around 22 CLI providers including Claude Code, Codex, Gemini CLI, GitHub Copilot, Amp, Cursor, Goose, Kiro (AWS), Pi, Qwen Code, and Hermes Agent.

The port collision story is what sold me on Emdash's engineering seriousness. The `.emdash.json` config defines setup, run, and teardown scripts per task, and `$EMDASH_PORT` injection gives each task a unique port: `PORT=$EMDASH_PORT pnpm run dev`. That solves the shared-port problem worktrees leave open, which almost no other OSS tool in this list handles cleanly.

**Isolation:** Git worktrees locally or on remote machines over SSH. Setup and teardown scripts per task.

**Agent support:**

| Provider category | Examples |
| --- | --- |
| Major vendors | Claude Code, Codex, Gemini CLI, GitHub Copilot |
| Emerging tools | Amp, Kiro (AWS), Pi, Qwen Code |
| Community agents | Hermes Agent, Autohand Code, Droid, Kilocode |

**Coordination:** Parallel, human-supervised, worktree-isolated. Agents run independently; I assign tasks, review output, and merge.

**UI:** Electron desktop with ticket intake from Linear, GitHub, or Jira, plus inline diff inspection, commenting, and PR creation.

**Known limitations:** No agent-to-agent coordination, no shared config across agents. If one agent learns the codebase's test conventions, the other five don't benefit. Teams wanting task decomposition or pre-merge quality gates will need to layer tooling on top.

**Choose Emdash if:** Your team uses a mix of CLI agents and you want a desktop UI. **Skip Emdash if:** You need agents to coordinate with each other rather than run side by side.

## 3. Baton

**Repository (OSS):** [mraza007/baton](https://github.com/mraza007/baton "https://github.com/mraza007/baton") | **License:** See repository | **Language:** Python

Two projects share the "Baton" name. I tested the open-source `mraza007/baton`, which polls GitHub Issues and runs Claude Code in isolated worktrees. The second Baton ([getbaton.dev](https://getbaton.dev/ "https://getbaton.dev/")) is a desktop app for monitoring multiple agents including Codex CLI; its source availability isn't clearly documented.

The `mraza007/baton` architecture is narrow by design. A Poller runs `gh issue list` to find matching issues, a Dispatcher controls concurrency across parallel workers, and a Reconciler detects stale runs. All configuration lives in one `WORKFLOW.md` file with YAML front matter and a Jinja2 prompt body:

bash

```
# Baton workflow (simplified from README)

# WORKFLOW.md YAML front matter configures:

#   - poller settings

#   - concurrency limits

#   - prompt templates via Jinja2

baton start  # Begins poll-dispatch-reconcile loop
```

**Isolation:** Git worktrees, one per GitHub Issue.

**Agent support:** Claude Code, Codex CLI, OpenCode, and Gemini CLI; custom shell commands configurable.

**Coordination:** Poll-dispatch-reconcile loop. No task graph, no verification.

**UI:** CLI-only with Click and color-coded terminal logging. No TUI, no GUI.

**Known limitations:** No automated merge conflict resolution. Worktree isolation is repo-level rather than machine-level, so shared services still collide. If your issue queue is messy, Baton's polling turns that noise into agent runs.

| Dimension | mraza007/baton (OSS) | getbaton.dev (Desktop) |
| --- | --- | --- |
| Type | Python daemon | Desktop GUI app |
| Agent support | Claude Code | Codex CLI |
| Task source | GitHub Issues | Baton-generated task descriptions |
| Coordination | Poll-dispatch-reconcile loop | Desktop monitoring |
| Open source | Yes | Not confirmed |

**Choose Baton if:** GitHub Issues is already your task queue and you want zero extra UI. **Skip Baton if:** You want a visual dashboard or multi-agent coordination.

## 4. Conductor (Three Projects, One Name)

"Conductor" refers to at least four distinct projects in AI coding. I'm covering three relevant ones below and skipping Netflix Conductor, which solves workflow orchestration in a completely different domain.

Rather than three subsections, here's the quick synthesis. **conductor.build** is a polished macOS desktop app but closed-source, so it falls out of scope for an OSS roundup. **Code Conductor** ([ryanmac/code-conductor](https://github.com/ryanmac/code-conductor "https://github.com/ryanmac/code-conductor")) is a GitHub-native CLI that labels issues `conductor:task` and lets agents claim them, though it supports only Claude Code and the repo's license status isn't clearly stated at publication time. **Microsoft Conductor** ([microsoft/conductor](https://github.com/microsoft/conductor "https://github.com/microsoft/conductor"), MIT, v0.1.1) is the most credible long-term bet: a CLI tool for defining and running multi-agent workflows with the GitHub Copilot SDK and Anthropic Agents SDK, with YAML-defined workflows and a web dashboard. At v0.1.1, though, the specific YAML feature set I could verify from the repo is thin.

| Attribute | conductor.build (Melty) | Code Conductor (ryanmac) | Microsoft Conductor |
| --- | --- | --- | --- |
| License | Closed source | Not clearly stated | MIT |
| UI | macOS desktop | CLI | CLI + web dashboard |
| Agents | Claude Code, Codex | Claude Code | GitHub Copilot, Claude |
| Platform | macOS only | Any | Unknown |
| Coordination | Human-in-the-loop | GitHub Issue queue | YAML parallel groups |

**Choose a Conductor if:** You want YAML-defined workflows (Microsoft) or a GitHub-Issue queue (ryanmac). **Skip them if:** You need production-ready tooling today; all three are earlier-stage than Composio AO or Bernstein.

## 5. Bernstein

**Repository:** [chernistry/bernstein](https://github.com/chernistry/bernstein "https://github.com/chernistry/bernstein") | **License:** Apache-2.0 | **Install:** `pipx install bernstein`

Bernstein is the most architecturally interesting tool in this roundup. It implements a full planning-to-merge pipeline: Goal → LLM Planner → Task Graph → Orchestrator → Agents (parallel) → Janitor (verify) → Git merge → main. I tested it on a small refactor task across three files, and the Janitor caught a type error one agent introduced before it reached the merge queue. Pre-merge quality gates worked as documented.

Three properties separate Bernstein from everything else:

* **Deterministic scheduling.** The orchestrator uses Python code for every scheduling decision, with no LLM calls involved. Same inputs produce the same outputs regardless of how agent responses interleave.
* **Zero LLM tokens on coordination.** The LLM runs once, during initial goal decomposition. After that, scheduling costs nothing in tokens.
* **Local HTTP task server.** Agents report progress over HTTP. State lives in a `.sdd/` directory, outside of agent memory.

**Isolation:** Git worktrees per agent.

**Agent support:** Claude Code, Codex, Gemini CLI as the primary agents on the official site.

**Coordination:** The Janitor runs lint, type checks, and tests before merge. Only verified work lands.

**UI:** CLI primary, with a basic web view for task graph inspection.

**Known limitations:** Documentation is thin relative to the architecture's ambition. I spent an hour figuring out how the task graph gets persisted between runs. I've seen claims that Bernstein does "automatic model routing to escalate failed tasks to more capable models," but I couldn't substantiate that in the docs I found, so treat it as unverified until the project documents the behavior.

**Choose Bernstein if:** You want deterministic scheduling and pre-merge verification without paying for a commercial tool. **Skip Bernstein if:** You need strong documentation or an active community around the project.

### See how Intent's living specs keep parallel agents aligned across cross-service refactors.

[Build with Intent](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent")

Free tier available · VS Code extension · Takes 2 minutes

ci-pipeline

···

$ cat build.log | auggie --print --quiet \

"Summarize the failure"

Build failed due to missing dependency 'lodash'
in src/utils/helpers.ts:42

Fix: npm install lodash @types/lodash

## 6. Claude Squad

**Repository:** [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad "https://github.com/smtg-ai/claude-squad") | **License:** AGPL-3.0 | **Binary:** `cs`

Claude Squad is the TUI I recommend for solo developers who want parallel agents today. The architecture layers tmux for terminal sessions, git worktrees for filesystem isolation, and a TUI for unified navigation. The `cs` binary launched six sessions on my laptop in under five seconds, and the keybindings are fast enough that I stopped thinking about them after about twenty minutes.

**Isolation:** Git worktrees plus tmux. Each agent works in its own branch and physical directory via worktrees, while tmux handles session persistence and navigation.

**Agent support:** Claude Code (default), Codex (`cs -p "codex"`), Aider, Gemini, OpenCode, and Amp, each launched via `-p` or `--program`.

**Coordination:** Human-in-the-loop session management. Each agent works independently, and I review all changes before applying or pushing. No agent-to-agent communication, no task dependency graph. The design centers on session lifecycle (create, navigate, delete, stage).

**UI:** TUI with vim-style navigation. The core actions: `n` creates a new session, `D` deletes, `↑/↓` or `j/k` navigates, `↵` focuses the output pane, `s` stages changes, `r` reviews before applying, `ctrl-q` detaches.

**Known limitations:** AGPL-3.0 is a real constraint. If you're building internal tooling on top of Claude Squad that might ever become a network service, get legal review first. No native Windows support (tmux dependency). The `--autoyes` flag for auto-accepting prompts is still experimental, and I wouldn't run it unattended.

**Choose Claude Squad if:** You're a solo developer or small team working in the terminal and you want parallel agents running now. **Skip Claude Squad if:** You need Windows support, automated coordination, or a license that permits commercial embedding.

## 7. Crystal (Now Nimbalyst)

**Repository:** [stravu/crystal](https://github.com/stravu/crystal "https://github.com/stravu/crystal") (deprecated February 2026) | **Successor:** [nimbalyst.com](https://nimbalyst.com/ "https://nimbalyst.com/")

Crystal was a Stravu desktop app for running multiple Codex and Claude Code sessions in parallel worktrees. The repository was deprecated in February 2026 when the team redirected users to [Nimbalyst](https://nimbalyst.com/ "https://nimbalyst.com/"), which expands the original's capabilities with interactive visual editing of markdown, mockups, Excalidraw, and code alongside parallel session management.

I'm including it here because Crystal shows up in older search results and comparisons. Don't start new work on it. The live decision is between Nimbalyst and the other active tools in this list.

**Isolation:** Git worktrees per agent session.

**Agent support:** Claude Code from initial release; OpenAI Codex added in v0.3.

**Coordination:** Human-in-the-loop parallel dispatch. Multiple independent sessions with no automated director/worker hierarchy.

**Choose Nimbalyst if:** You want the Crystal model plus visual editing. **Skip both Crystal and Nimbalyst if:** You need the maturity and community of Claude Squad or a maintained Kanban option.

## 8. Vibe Kanban (Now Community-Maintained)

**Repository:** [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban "https://github.com/BloopAI/vibe-kanban") | **License:** Apache-2.0 | **Install:** `npx vibe-kanban`

**Status update (read this before adopting).** Bloop, the company behind Vibe Kanban, [announced a shutdown](https://vibekanban.com/blog/shutdown "https://vibekanban.com/blog/shutdown") in early 2026. The project itself continues as open source and community-maintained, but the hosted remote services were wound down and paid subscriptions refunded. Any Bloop-operated cloud features (kanban issues, comments, projects, organisations) transition to a fully local architecture after the announced sunset window. Treat Vibe Kanban as a promising community project rather than a vendor-backed tool going forward.

With that caveat, here's what made Vibe Kanban worth testing in the first place. The MCP server is the interesting piece: a "planning" ticket can instruct an agent to decompose work and generate downstream cards automatically. That's the closest any tool in this roundup gets to autonomous task decomposition short of going full Bernstein.

**Isolation:** Git worktrees per workspace, each with its own branch and folder.

**Agent support:** The README currently lists 10+ agents including Claude Code, Codex, Gemini CLI, GitHub Copilot, Amp, Cursor, OpenCode, Droid, CCR, and Qwen Code.

**Coordination:** Kanban board with To Do, In Progress, Review, and Done columns. MCP-driven card creation for task decomposition.

**UI:** Web app with workspaces panel, built-in browser with devtools and device emulation, inline diff review, and PR creation.

**Known limitations:** On a repo with twenty active tasks, I ended up with twenty worktree folders, which bloats disk and confuses `find`. A GitHub Discussion ([#2727](https://github.com/BloopAI/vibe-kanban/discussions/2727 "https://github.com/BloopAI/vibe-kanban/discussions/2727")) captured previously active tension about whether the tool should stay focused on AI orchestration or expand into generic Kanban; that conversation is likely to quiet down with Bloop's shutdown, though the underlying question remains for whoever picks up maintenance. Strict pipeline dependencies (task B must wait for task A) aren't clearly supported. On top of that, the shutdown of Bloop's commercial backing means future maintenance velocity depends entirely on community contributors.

**Choose Vibe Kanban if:** You want a shared visual board and a built-in browser for previewing UI changes, and you're comfortable depending on a community-maintained project. **Skip Vibe Kanban if:** You need vendor support, hard task dependencies, or you work on repos where disk usage from many worktrees matters.

## 9. Agent Kanban

**Repository:** [appsoftwareltd/vscode-agent-kanban](https://github.com/appsoftwareltd/vscode-agent-kanban "https://github.com/appsoftwareltd/vscode-agent-kanban") | **License:** Elastic License 2.0

Open source

augmentcode/augment-swebench-agent★872

[Star on GitHub](https://github.com/augmentcode/augment-swebench-agent?utm_source=blog&utm_medium=cta&utm_campaign=github&utm_content=open-source-agent-orchestrators "https://github.com/augmentcode/augment-swebench-agent?utm_source=blog&utm_medium=cta&utm_campaign=github&utm_content=open-source-agent-orchestrators")

Agent Kanban takes a different approach from every other tool here by living entirely inside VS Code as a Copilot Chat participant, skipping the custom LLM loop entirely. GitHub Copilot's native agent mode does the work, and Agent Kanban provides task structure through markdown-backed Kanban lanes.

The `AGENTS.md` sentinel mechanism is the clever bit. On activation and every command, the extension writes context into the file, and VS Code re-injects it into the system prompt on every agent turn. `@kanban /refresh` re-injects context if the agent drifts during a long conversation. I ran a four-hour session without context loss, which I couldn't reliably do with raw Copilot Chat.

**Isolation:** Main workspace by default, with optional git worktree isolation per task.

**Agent support:** GitHub Copilot only, via VS Code Copilot Chat.

**Coordination:** The `@kanban` chat participant routes commands to task files in `.agentkanban/`:

text

```
.agentkanban/

board.yaml          # Lane definitions, base prompt

memory.md           # Global memory

INSTRUCTION.md      # Agent workflow instructions

tasks/

task_<date>_<id>_<title>.md

archive/
```

**Known limitations:** Copilot-only, so teams on Claude Code or Codex can't use it. The ELv2 license prohibits offering it as a competing hosted service, though internal use is fine. Don't confuse this project with [saltbo/agent-kanban](https://github.com/saltbo/agent-kanban "https://github.com/saltbo/agent-kanban"), which is a completely separate codebase with a different architecture.

**Choose Agent Kanban if:** Your team is standardized on GitHub Copilot and lives in VS Code. **Skip it if:** You use any other agent or want agent choice.

## Full Comparison

| Tool | Isolation | Agents | Coordination depth | UI | License |
| --- | --- | --- | --- | --- | --- |
| Composio AO | Git worktrees + tmux | Claude Code, Codex, Aider, OpenCode | Milestone gates + auto CI retry | Web dashboard + CLI | MIT |
| Emdash | Git worktrees + $EMDASH\_PORT | ~22 CLI providers | Parallel dispatch, human-supervised | Electron desktop | Apache-2.0 |
| Baton (mraza007) | Git worktrees per issue | Claude Code, Codex, Gemini, OpenCode | Poll-dispatch-reconcile | CLI | See repository |
| Code Conductor | Git worktrees per task | Claude Code | GitHub Issue queue | CLI | Not clearly stated |
| Microsoft Conductor | YAML workflow | Copilot, Anthropic Agents SDK | YAML parallel groups + HITL | CLI + web | MIT |
| Bernstein | Git worktrees | Claude Code, Codex, Gemini | Deterministic scheduler + Janitor | CLI + web | Apache-2.0 |
| Claude Squad | Git worktrees + tmux | Claude Code, Codex, Aider, Gemini, OpenCode, Amp | Session manager (HITL) | TUI | AGPL-3.0 |
| Nimbalyst (Crystal successor) | Git worktrees | Claude Code, Codex | Parallel dispatch (HITL) | Desktop | See repo |
| Vibe Kanban (community-maintained) | Git worktrees per workspace | 10+ agents (Claude Code, Codex, Gemini, Copilot, Amp, Cursor, OpenCode, Droid, CCR, Qwen Code) | Kanban + MCP decomposition | Web app | Apache-2.0 |
| Agent Kanban | Optional worktrees | GitHub Copilot only | AGENTS.md sentinel + lanes | VS Code extension | ELv2 |

## When OSS Orchestrators Are Enough (and When They Aren't)

Every tool here converges on git worktrees, and most leave coordination to me. That works well inside clear boundaries: one repo, modest agent count, code I understand directly. The question is what happens past those boundaries.

### Where OSS orchestrators fit

OSS orchestrators are the right call when:

* The codebase fits in one repository.
* Agent count stays in the 3-6 range I can track visually.
* I'm directly familiar with every service the agents touch.
* I'm comfortable resolving merge conflicts by hand.

Claude Squad gets me from zero to parallel agents fastest. Vibe Kanban still gives me a visual board and a browser preview, with the caveat that the project is now community-maintained after Bloop's shutdown. Bernstein's deterministic scheduler plus the Janitor hits the sweet spot for teams that want pre-merge verification without commercial licensing.

The shared constraint across these tools is that coordination between agents is either manual (most tools) or limited to task-graph scheduling within one repo (Bernstein, Composio AO). Nothing here coordinates agents across services against a shared evolving plan.

### Where Intent changes the shape of the problem

[Intent](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent") is the first tool I've used that treats multi-agent coding as a coordinated system, with a shared spec acting as the single source of truth for every agent in the workspace. Three pieces do the work:

* **Coordinator agent.** Analyzes the codebase via the Context Engine, drafts a living specification, decomposes it into tasks, and delegates to implementor agents in parallel waves.
* **Implementor agents.** Run in isolated worktrees, each taking a task from the spec. Because they share the spec, they share the same picture of what's being built.
* **Verifier agent.** Checks implementation against the living spec before PR time, producing a spec-compliance report on top of the usual lint and test output.

The living spec is the part that matters for cross-service work. A concrete example: mid-refactor, I decide to rename a field on our payment API from `user_id` to `payer_id`. In the OSS tools, I'd need to interrupt each of the three agents touching that API, update their prompts, and hope they pick up the change. In Intent, I edit the spec once; the update propagates to every active agent, and the Verifier catches any already-written code that still references the old name.

Intent ships as a macOS desktop app that consolidates IDE, terminal, built-in Chrome browser, and git client into one workspace. Each task runs in an isolated worktree, and the full prompt-to-commit-to-PR-to-merge flow stays inside the app. Six built-in specialist personas (Investigate, Implement, Verify, Critique, Debug, Code Review) handle different stages, and teams can define custom specialists per workspace.

[BYOA (Bring Your Own Agent)](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent") means Claude Code, Codex, and OpenCode run inside Intent's workspace alongside Auggie. Teams already standardized on one of those CLIs keep their existing subscriptions and gain spec-driven coordination on top. Intent also exposes the Context Engine as an MCP server, so third-party agents can pull the cross-repo architectural context that worktree-isolated setups lack.

**Honest tradeoffs.** Intent is macOS-only today (Windows is on the waitlist, Linux isn't announced) and currently in public beta. It uses Augment credits rather than a dedicated Intent subscription, and a Trial plan provides 30,000 credits at $0 to evaluate it; sustained use runs on a paid plan starting at $20/month (Indie) or $60/month per developer (Standard). For teams already paying for Claude Code or Cursor, that's real cost to weigh against the coordination gains, though BYOA routing through existing provider subscriptions softens the overlap. For solo developers on single repos, the OSS tools here are probably enough.

### Decision framework

| Your situation | My recommendation |
| --- | --- |
| Solo developer, single repo, 3-5 agents, terminal-first | Claude Squad |
| Solo or small team, want a visual board (community-maintained OK) | Vibe Kanban |
| Team on GitHub Copilot, living in VS Code | Agent Kanban |
| GitHub Issue-driven autonomous workflow | Composio AO (richer) or Baton (simpler) |
| Mixed CLI agents across a team | Emdash |
| Want deterministic scheduling and pre-merge verification | Bernstein |
| Cross-service refactors, evolving specs, teams on macOS | Intent |
| Cost sensitivity, full infrastructure control | Any OSS option above |

## Pick the Coordination Depth That Matches Your Workflow

Every tool here solves parallel execution. The real decision is how much coordination you want automated and how much you want to keep. Claude Squad keeps it all with you. Composio AO automates CI recovery. Bernstein automates scheduling and quality gates. Each step trades control for throughput.

That tradeoff works inside one repo. When work spans services and specs need to evolve alongside the code, manual reconciliation becomes the bottleneck that no OSS tool in this roundup addresses. Intent's Coordinator, Implementor, and Verifier agents work against a living spec that updates as implementation proceeds, producing coordinated alignment across the full prompt-to-merge workflow while independent workers in the OSS tools keep running side by side with no shared plan.

### See how Intent's living specs keep coordinated agents aligned across codebase-wide work.

[Build with Intent](https://www.augmentcode.com/product/intent "https://www.augmentcode.com/product/intent")

Free tier available · VS Code extension · Takes 2 minutes

## FAQ

###

###

###

###

###

###

## Related

* [Conductor vs Intent (2026): macOS Agent Orchestrators Compared](https://www.augmentcode.com/tools/intent-vs-conductor-macos-agent-orchestrators "https://www.augmentcode.com/tools/intent-vs-conductor-macos-agent-orchestrators")
* [DIY Multi-Agent Setups vs. Intent: Build or Buy for Agent Orchestration](https://www.augmentcode.com/tools/diy-multi-agent-setups-vs-intent "https://www.augmentcode.com/tools/diy-multi-agent-setups-vs-intent")
* [Claude Code vs Intent (2026): Single-Session Agent or Multi-Agent Orchestration?](https://www.augmentcode.com/tools/intent-vs-claude-code "https://www.augmentcode.com/tools/intent-vs-claude-code")
* [OpenCode vs Intent (2026): Open-Source CLI Agent vs Spec-Driven Workspace](https://www.augmentcode.com/tools/intent-vs-opencode "https://www.augmentcode.com/tools/intent-vs-opencode")
* [Cursor 3 vs Intent (2026): Prompt-Driven vs Spec-Driven Agents](https://www.augmentcode.com/tools/cursor-3-vs-intent "https://www.augmentcode.com/tools/cursor-3-vs-intent")

### Written by

![Ani Galstian](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Foraw2u2c%2Fproduction%2F68545e0f765ac7ec41ac8be27ff7164b3e21a0b9-288x288.png&w=128&q=75)

#### Ani Galstian

Technical Writer

Ani writes about enterprise-scale AI coding tool evaluation, agentic development security, and the operational patterns that make AI agents reliable in production. His guides cover topics like AGENTS.md context files, spec-as-source-of-truth workflows, and how engineering teams should assess AI coding tools across dimensions like auditability and security compliance

Get Started

## Give your codebase the agents it deserves

Install Augment to get started. Works with codebases of any size, from side projects to enterprise monorepos.

[Install Augment](/install "/install")[Contact Sales](/contact "/contact")
