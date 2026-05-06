# Introducing Codex

URL: https://openai.com/index/introducing-codex/
Source: OpenAI

## Reconstructed content (from search snippets)

> "Codex is a cloud-based software engineering agent that can work on many tasks in parallel."

> "Codex can perform tasks such as writing features, answering questions about your codebase, fixing bugs, and proposing pull requests for review; each task runs in its own cloud sandbox environment, preloaded with your repository."

Model:

> "Codex is powered by codex-1, a version of OpenAI o3 optimized for software engineering. It was trained using reinforcement learning on real-world coding tasks to generate code that closely mirrors human style and PR preferences, adheres precisely to instructions, and can iteratively run tests until it receives a passing result."

2026 status:

> "Codex in 2026 has become production-ready infrastructure that fundamentally changed how developers build software. OpenAI claimed they were using Codex itself to improve Codex, and the improvement curve has been steep and consistent in a way that suggests systematic, automated refinement rather than just periodic model updates."

Features:

> "Multi-agent parallel execution, GPT-5.4 as the core model, reusable agent workflows (Skills), scheduled background work (Automations), and AI-powered vulnerability detection (Codex Security)."

OpenAI also publishes the harness-engineering pattern at https://openai.com/index/harness-engineering/ - using Codex in an agent-first world.

## Relevance to dark factories

Codex Cloud is the per-task sandbox + parallel-PR pattern productized. It directly enables non-interactive seed -> harness -> feedback loops at scale, with Skills/Automations as primitives for assembling dark-factory pipelines.
