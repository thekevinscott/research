# I blew through 24 million tokens in a day

- URL: https://blog.kronis.dev/blog/i-blew-through-24-million-tokens-in-a-day
- Author: kronis (independent developer blog)
- Reconstructed from WebSearch snippets.

## What this is

A first-hand "I tried it" account of what it actually feels like to operate at the StrongDM-recommended token budget ("$1,000/day per engineer"). The author runs an agent-driven workflow and tracks token throughput against rate limits and costs across providers.

## Headline numbers (from snippets)

- 24 million tokens consumed in a single day.
- Roughly 90 components, 40-60 utilities and project files.
- About 150 files touched -> ~160,000 tokens per file on average.
- Total cost on Cerebras: under $2 USD for the entire day.

## Direct quotes / near-quotes from snippets

> "An engineer running a swarm of agents can blow through millions of tokens in a day - automatically, in the background, without typing a word."

> "Cerebras allows 50 requests per second for agentic work without tight rate limiting."

> The author found Claude Code and other mainstream subscriptions "too restrictive regarding rate limits and token capacity for their scale of work."

## Key first-hand findings

- At dark-factory token throughputs, mainstream Claude/OpenAI subscription tiers are the bottleneck, not the model. The author moved to Cerebras specifically because of rate-limit and capacity headroom.
- Cost is no longer the limiting factor - 24 million tokens cost under $2 on Cerebras. The bottleneck is requests-per-second and orchestration.
- The numbers map cleanly onto a small dark-factory: ~150 files / day from a single human operator.

## Takeaway

A grounded, numbers-first counterpoint to the "$1,000/day in tokens" benchmark: at high-throughput inference providers, that benchmark may be the wrong metric - real factories may be RPS-limited, not dollar-limited.
