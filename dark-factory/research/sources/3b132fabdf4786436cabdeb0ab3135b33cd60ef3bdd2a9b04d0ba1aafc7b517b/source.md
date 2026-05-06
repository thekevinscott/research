# agent-orchestrator

Agentic orchestrator for parallel coding agents — plans tasks, spawns agents, and autonomously handles CI fixes, merge conflicts, and code reviews.

Agent Orchestrator — The Orchestration Layer for Parallel AI Agents
Spawn parallel AI coding agents, each in its own git worktree. Agents autonomously fix CI failures, address review comments, and open PRs — you supervise from one dashboard.
Agent Orchestrator manages fleets of AI coding agents working in parallel on your codebase. Each agent gets its own git worktree, its own branch, and its own PR. When CI fails, the agent fixes it. When reviewers leave comments, the agent addresses them. You only get pulled in when human judgment is needed.
Agent-agnostic
(Claude Code, Codex, Aider) ·
Runtime-agnostic
(tmux, Docker) ·
Tracker-agnostic
(GitHub, Linear)
See it in action
Quick Start
Prerequisites:
Node.js 20+
,
Git 2.25+
,
tmux
,
gh
CLI
. Install tmux via
brew install tmux
(macOS) or
sudo apt install tmux
(Linux).
Install
npm install -g @aoagents/ao
Permission denied? Install from source?
If
npm install -g
fails with EACCES, prefix with
sudo
or
fix your npm permissions
.
To install from source (for contributors):
git clone https://github.com/ComposioHQ/agent-orchestrator.git
cd
agent-orchestrator
&&
bash scripts/setup.sh
Zsh Completion
Generate the completion file from the installed CLI:
mkdir -p
~
/.zsh/completions
ao completion zsh
>
~
/.zsh/completions/_ao
Then make sure the directory is on your
fpath
before
compinit
runs:
fpath=(~/.zsh/completions
$fpath
)
autoload -Uz compinit
compinit
For Oh My Zsh, install the same generated file into a custom plugin directory and add
ao
to your plugin list:
mkdir -p
"
${ZSH_CUSTOM
:-
~
/
.oh-my-zsh
/
custom}
/plugins/ao
"
ao completion zsh
>
"
${ZSH_CUSTOM
:-
~
/
.oh-my-zsh
/
custom}
/plugins/ao/_ao
"
If you are contributing from a source checkout, you can also symlink the repo copy at
completions/_ao
.
Start
Point it at any repo — it clones, configures, and launches the dashboard in one command:
ao start https://github.com/your-org/your-repo
Or from inside an existing local repo:
cd
~
/your-project
&&
ao start
That's it. The dashboard opens at
http://localhost:3000
and the orchestrator agent starts managing your project.
Add more projects
ao start
~
/path/to/another-repo
How It Works
You start
—
ao start
launches the dashboard and an orchestrator agent
Orchestrator spawns workers
— each issue gets its own agent in an isolated git worktree
Agents work autonomously
— they read code, write tests, create PRs
Reactions handle feedback
— CI failures and review comments are automatically routed back to the agent
You review and merge
— you only get pulled in when human judgment is needed
The orchestrator agent uses the
AO CLI
internally to manage sessions. You don't need to learn or use the CLI — the dashboard and orchestrator handle everything.
Configuration
ao start
auto-generates
agent-orchestrator.yaml
with sensible defaults. You can edit it afterwards to customize behavior:
#
agent-orchestrator.yaml
$schema
:
https://raw.githubusercontent.com/ComposioHQ/agent-orchestrator/main/schema/config.schema.json
#
Runtime data is auto-derived under ~/.agent-orchestrator/{hash}-{projectId}/
port
:
3000
defaults
:
runtime
:
tmux
agent
:
claude-code
workspace
:
worktree
notifiers
:
[desktop]
projects
:
my-app
:
repo
:
owner/my-app
path
:
~/my-app
defaultBranch
:
main
sessionPrefix
:
app
reactions
:
ci-failed
:
auto
:
true
action
:
send-to-agent
retries
:
2
changes-requested
:
auto
:
true
action
:
send-to-agent
escalateAfter
:
30m
approved-and-green
:
auto
:
false
#
flip to true for auto-merge
action
:
notify
CI fails → agent gets the logs and fixes it. Reviewer requests changes → agent addresses them. PR approved with green CI → you get a notification to merge.
Keep the
$schema
line so editors can autocomplete and validate against
schema/config.schema.json
.
See
agent-orchestrator.yaml.example
for the full reference, or run
ao config-help
for the complete schema.
Remote Access
AO keeps your Mac awake while running, so you can access the dashboard remotely (e.g., via Tailscale from your phone) without the machine going to sleep.
How it works:
On macOS, AO automatically holds an idle-sleep prevention assertion using
caffeinate
. When AO exits, the assertion is released.
#
agent-orchestrator.yaml
$schema
:
https://raw.githubusercontent.com/ComposioHQ/agent-orchestrator/main/schema/config.schema.json
power
:
preventIdleSleep
:
true
#
Default on macOS, no-op on Linux
Set to
false
if you want to allow idle sleep while AO runs.
Lid-close limitation:
macOS enforces lid-close sleep at the hardware level — no userspace assertion can override it. If you need remote access while traveling with the lid closed, use
clamshell mode
(external power + display + input device).
Plugin Architecture
Seven plugin slots. Lifecycle stays in core.
Slot
Default
Alternatives
Runtime
tmux
process
Agent
claude-code
codex, aider, cursor, opencode, kimicode
Workspace
worktree
clone
Tracker
github
linear, gitlab
SCM
github
gitlab
Notifier
desktop
slack, discord, composio, webhook, openclaw
Terminal
iterm2
web
All interfaces defined in
packages/core/src/types.ts
. A plugin implements one interface and exports a
PluginModule
. That's it.
Why Agent Orchestrator?
Running one AI agent in a terminal is easy. Running 30 across different issues, branches, and PRs is a coordination problem.
Without orchestration
, you manually: create branches, start agents, check if they're stuck, read CI failures, forward review comments, track which PRs are ready to merge, clean up when done.
With Agent Orchestrator
, you:
ao start
and walk away. The system handles isolation, feedback routing, and status tracking. You review PRs and make decisions — the rest is automated.
Documentation
Doc
What it covers
Setup Guide
Detailed installation, configuration, and troubleshooting
CLI Reference
All
ao
commands (mostly used by the orchestrator agent)
Examples
Config templates (GitHub, Linear, multi-project, auto-merge)
Development Guide
Architecture, conventions, plugin pattern
Contributing
How to contribute, build plugins, PR process
Development
pnpm install
&&
pnpm build
#
Install and build all packages
pnpm
test
#
Run tests (3,288 test cases)
pnpm dev
#
Start web dashboard dev server
See
docs/DEVELOPMENT.md
for code conventions and architecture details.
Contributing
Contributions welcome. The plugin system makes it straightforward to add support for new agents, runtimes, trackers, and notification channels. Every plugin is an implementation of a TypeScript interface — see
CONTRIBUTING.md
and the
Development Guide
for the pattern.
License
MIT
