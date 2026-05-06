# About GitHub Copilot cloud agent

URL: https://docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent
Source: GitHub Docs

## Reconstructed content (from search snippets)

Overview:

> "Copilot cloud agent works autonomously in a GitHub Actions-powered environment to complete development tasks assigned through GitHub issues or GitHub Copilot Chat prompts. It can research a repository, create a plan, make code changes on a branch, and optionally open a pull request."

PR generation:

> "The coding agent turns issues into pull requests: assign a GitHub issue to Copilot and it works autonomously in the background -- writing code, running tests, and opening a PR for your review. Copilot will open a draft pull request and work in the background in its own development environment through the power of GitHub Actions."

Workflow:

> "You can use the agents panel or other agents entry points on GitHub.com to have Copilot research, plan, and make code changes on a branch, then iterate before creating a pull request. Copilot automates branch creation, commit message writing, and pushing."

Security:

> "In 2026, assigning a GitHub issue to Copilot means that there is a pull request open, with tests passing, self-reviewed, and a security scan completed. The AI coding agents read the instruction file, explored the codebase, wrote the implementation, iterated through test failures, and tagged the developer for review."

GA status:

> "The coding agent is now generally available for all paid Copilot subscribers and represents a significant evolution in GitHub's AI-assisted development capabilities."

Note: Copilot code review starts consuming GitHub Actions minutes June 1 2026.

## Relevance to dark factories

Copilot's coding agent runs inside the GitHub Actions sandbox attached to the same repo where the dark factory ships. Issue-to-PR with self-review + security scan is a turnkey dark-factory unit at GitHub-account scope.
