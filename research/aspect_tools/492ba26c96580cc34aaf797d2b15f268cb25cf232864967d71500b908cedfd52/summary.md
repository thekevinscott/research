# Summary

GitHub Copilot's cloud (coding) agent, GA in 2026, runs autonomously in a GitHub Actions-powered ephemeral environment and turns assigned GitHub issues directly into pull requests. The agent researches the repo, drafts a plan, edits code on a branch, runs tests, performs self-review and security scanning, and opens a draft PR - all without leaving the GitHub UI.

This is arguably the most mainstream dark-factory worker pattern: it lives directly in the repo, uses Actions-minute billing, and integrates with existing CODEOWNERS and branch protection. For organizations already on GitHub it is the path of least resistance to dark-factory adoption, and is heavily used in combination with Cursor/Claude/Codex agents that hand off to it for the merge step.
