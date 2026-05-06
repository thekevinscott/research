# Introducing Open SWE: An Open-Source Asynchronous Coding Agent

URL: https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/
Source: LangChain

## Reconstructed content (from search snippets)

> "Open SWE is an open-source, cloud-native, asynchronous coding agent designed to act like a real teammate: it plans, writes, tests, reviews code, and opens pull requests directly from GitHub issues or a web UI."

Architecture:

> "Open SWE operates using three specialized LangGraph agents that work in sequence: a Manager, a Planner, and a Programmer (which contains a sub-agent Reviewer)."

Sandbox isolation:

> "Every run occurs in a secure, isolated Daytona sandbox, allowing the agent to execute shell commands freely without risking the host environment."

Human-in-the-loop:

> "When Open SWE generates a plan, it interrupts and gives you the chance to accept, edit, delete, or request changes to the plan. You can interrupt the agent when you want to review work or nudge it back on track without restarting."

> "'Double texting' - the ability to send new requests while the agent is already working, something most coding assistants can not do."

Integrations:

> "Slack - Mention the bot in any thread. Linear - Comment @openswe on any issue. GitHub - Tag @openswe in PR comments on agent-created PRs to have it address review feedback and push fixes to the same branch."

Hosted/self-hosted:

> "Teams can try the hosted UI at swe.langchain.com by connecting GitHub and supplying a model API key (e.g., Anthropic). The codebase is fully open source on GitHub, and LangChain notes enterprises can self-host via their own LangGraph API server."

Inspiration:

> "The project draws inspiration from architectural patterns that Stripe, Coinbase, and Ramp independently developed for their internal AI coding agents."

Repository: https://github.com/langchain-ai/open-swe

## Relevance to dark factories

Open SWE is essentially a dark-factory reference architecture: Manager + Planner + Programmer + Reviewer running in Daytona sandboxes, triggered from Slack/Linear/GitHub. Its explicit framing as a "real teammate" that a human-on-the-loop can interrupt aligns directly with Martin Fowler's harness-engineering recommendation.
