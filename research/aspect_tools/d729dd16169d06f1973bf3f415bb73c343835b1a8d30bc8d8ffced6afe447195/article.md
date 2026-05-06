# Best practices for coding with agents (Cursor)

URL: https://cursor.com/blog/agent-best-practices
Source: Cursor / Anysphere

## Reconstructed content (from search snippets)

Cursor's Cloud Agents (formerly Background Agents):

> "On February 24, 2026, Cursor launched fully autonomous AI coding agents running on isolated virtual machines that can build software, test it themselves, record video demos of their work, and produce merge-ready pull requests."

> "Cursor background agents are autonomous AI-powered assistants built into the Cursor IDE that execute coding tasks independently while you continue working on other aspects of your project. Background agents run autonomously - building, testing, and iterating without requiring approval for every command."

Capabilities:

> "Cursor's cloud agents are AI coders running on isolated VMs that self-test their code, record video demos, and produce merge-ready PRs. Cursor automatically creates and manages git worktrees for parallel agents. Each agent runs in its own worktree with isolated files and changes, so agents can edit, build, and test code without stepping on each other."

Self-PR adoption:

> "30% of Cursor's own PRs are now made by agents."

Cursor 3 / TypeScript SDK:

> "Anysphere released Cursor 3, a redesigned interface built from scratch that shifts the primary model from file editing to managing parallel coding agents. The new workspace supports local-to-cloud agent handoff, multi-repo parallel execution, and a plugin marketplace."

> "Cursor Introduces a TypeScript SDK for Building Programmatic Coding Agents With Sandboxed Cloud VMs, Subagents, Hooks, and Token-Based Pricing." (MarkTechPost, April 29 2026)

Self-hosted: https://cursor.com/blog/self-hosted-cloud-agents - Run cloud agents in your own infrastructure.

## Relevance to dark factories

Cursor Cloud agents - VM-isolated, self-testing, video-demo-recording, merge-ready PR producers - are one of the closest off-the-shelf packages of the dark-factory pattern. The TypeScript SDK with subagents and hooks lets teams build custom dark-factory orchestrations on top.
