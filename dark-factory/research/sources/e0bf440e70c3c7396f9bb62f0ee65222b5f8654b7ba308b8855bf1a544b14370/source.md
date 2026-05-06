# emdash

Emdash is the Open-Source Agentic Development Environment (🧡 YC W26). Run multiple coding agents in parallel. Use any provider.

Download Emdash v1
Stable v1 is now available for macOS, Windows, and Linux ·
Read the launch post
Emdash is a provider-agnostic desktop app that lets you run multiple coding agents in parallel, each isolated in its own git worktree, either locally or over SSH on a remote machine. We call it an Agentic Development Environment (ADE).
Emdash supports 24 CLI agents, including Claude Code, Codex, OpenCode, Gemini and Amp. Users can directly pass Linear, GitHub, or Jira tickets to an agent, review diffs, test changes, create PRs, see CI/CD checks, and merge.
Develop on remote servers via SSH
Connect to remote machines via SSH/SFTP to work with remote codebases. Emdash supports SSH agent and key authentication, with secure credential storage in your OS keychain. Run agents on remote projects using the same parallel workflow as local development.
Learn more
Installation
•
Providers
•
Contributing
•
FAQ
Installation
macOS
Apple Silicon:
https://releases.emdash.sh/emdash-arm64.dmg
Intel x64:
https://releases.emdash.sh/emdash-x64.dmg
Windows
Installer (x64):
https://releases.emdash.sh/emdash-x64.msi
Portable (x64):
https://releases.emdash.sh/emdash-x64.exe
Linux
AppImage (x64):
https://releases.emdash.sh/emdash-x86_64.AppImage
Debian package (x64):
https://releases.emdash.sh/emdash-amd64.deb
Release Overview
Latest Releases (macOS • Windows • Linux)
Providers
Supported CLI Providers
Emdash currently supports 24 CLI providers, and we are adding new ones regularly. If you miss one, let us know or create a PR.
CLI Provider
Status
Install
Amp
✅ Supported
npm install -g @sourcegraph/amp@latest
Auggie
✅ Supported
npm install -g @augmentcode/auggie
Autohand Code
✅ Supported
npm install -g autohand-cli
Charm
✅ Supported
npm install -g @charmland/crush
Claude Code
✅ Supported
curl -fsSL
https://claude.ai/install.sh
| bash
Cline
✅ Supported
npm install -g cline
Codebuff
✅ Supported
npm install -g codebuff
Codex
✅ Supported
npm install -g @openai/codex
Continue
✅ Supported
npm i -g @continuedev/cli
Cursor
✅ Supported
curl
https://cursor.com/install
-fsS | bash
Devin
✅ Supported
curl -fsSL
https://cli.devin.ai/install.sh
| bash
Droid
✅ Supported
curl -fsSL
https://app.factory.ai/cli
| sh
Gemini
✅ Supported
npm install -g @google/gemini-cli
GitHub Copilot
✅ Supported
npm install -g @github/copilot
Goose
✅ Supported
curl -fsSL
https://github.com/block/goose/releases/download/stable/download_cli.sh
| bash
Kilocode
✅ Supported
npm install -g @kilocode/cli
Kimi
✅ Supported
uv tool install kimi-cli
Kiro (AWS)
✅ Supported
curl -fsSL
https://cli.kiro.dev/install
| bash
Mistral Vibe
✅ Supported
curl -LsSf
https://mistral.ai/vibe/install.sh
| bash
OpenCode
✅ Supported
npm install -g opencode-ai
Pi
✅ Supported
npm install -g @mariozechner/pi-coding-agent
Qwen Code
✅ Supported
npm install -g @qwen-code/qwen-code
Rovo Dev
✅ Supported
acli rovodev auth login
Issues
Emdash allows you to pass issues, tickets, and support threads straight to your coding agent.
Tool
Status
Authentication
Linear
✅ Supported
Connect with a Linear API key.
Jira
✅ Supported
Provide your site URL, email, and Atlassian API token.
GitHub Issues
✅ Supported
Connect your GitHub account or authenticate via GitHub CLI (
gh auth login
).
GitLab Issues
✅ Supported
Provide your GitLab instance URL and a personal access token with
read_api
scope.
Forgejo Issues
✅ Supported
Provide your Forgejo instance URL and API token.
Plain Threads
✅ Supported
Connect with a Plain API key.
Contributing
Contributions welcome! See the
Contributing Guide
to get started, and join our
Discord
to discuss.
FAQ
What telemetry do you collect and can I disable it?
We send
anonymous, allow‑listed events
(app start/close, feature usage names, app/platform versions) to PostHog.
We
do not
send code, file paths, repo names, prompts, or PII.
Disable telemetry:
In the app:
Settings → General → Privacy & Telemetry
(toggle off)
Or via env var before launch:
TELEMETRY_ENABLED=false
Full details: see
Telemetry
.
Where is my data stored?
App data is local‑first
. We store app state in a local
SQLite
database:
macOS: ~/Library/Application Support/emdash/emdash.db
Windows: %APPDATA%\emdash\emdash.db
Linux: ~/.config/emdash/emdash.db
Privacy Note:
While Emdash itself stores data locally,
when you use any coding agent (Claude Code, Codex, Qwen, etc.), your code and prompts are sent to that provider's cloud API servers
for processing. Each provider has their own data handling and retention policies.
You can reset the local DB by deleting it (quit the app first). The file is recreated on next launch.
How do I add a new provider?
Emdash is
provider‑agnostic
and built to add CLIs quickly.
Open a PR following the
Contributing Guide
(
CONTRIBUTING.md
).
Include: provider name, how it’s invoked (CLI command), auth notes, and minimal setup steps.
We’ll add it to the
Providers table
and wire up provider selection in the UI.
If you’re unsure where to start, open an issue with the CLI’s link and typical commands.
What permissions does Emdash need?
Filesystem/Git:
to read/write your repo and create
Git worktrees
for isolation.
Network:
only for provider CLIs you choose to use (e.g., Codex, Claude) and optional GitHub actions.
Local DB:
to store your app state in SQLite on your machine.
Emdash itself does
not
send your code or chats to any servers. Third‑party CLIs may transmit data per their policies.
Can I work with remote projects over SSH?
Yes!
Emdash supports remote development via SSH.
Setup:
Go to
Settings → SSH Connections
and add your server details
Choose authentication: SSH agent (recommended), private key, or password
Add a remote project and specify the path on the server
Requirements:
SSH access to the remote server
Git installed on the remote server
For agent auth: SSH agent running with your key loaded (
ssh-add -l
)
See
Remote Projects
for detailed setup instructions and
Bring Your Own Infrastructure
for technical details.
