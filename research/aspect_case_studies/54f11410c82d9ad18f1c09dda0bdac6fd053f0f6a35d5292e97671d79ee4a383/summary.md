# Summary

Kronis's blog post is a numbers-first account of what it actually takes to operate at dark-factory token budgets. He burned through 24 million tokens in a single day while running an agent swarm, touching ~150 files (about 160k tokens per file on average) and producing 90 components and 40-60 utility/project files. The total cost on Cerebras was under $2 USD for the day.

His key first-hand finding is that mainstream Claude Code and OpenAI subscription tiers are the bottleneck at this scale - he had to move to Cerebras specifically for the higher request-per-second ceiling and lighter rate limiting. This reframes StrongDM's "$1,000/day in tokens per engineer" benchmark: at high-throughput providers the limit is not money but RPS and orchestration, and a single operator can plausibly drive a small dark factory at trivial dollar cost.
