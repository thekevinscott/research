# Hacker News thread: "$1,000 on tokens today per human engineer"

Source: Hacker News (item 46928149)
URL: https://news.ycombinator.com/item?id=46928149

## Summary

This Hacker News thread is the canonical discussion of the most-quoted Dark Factory metric: StrongDM CTO Justin McCarthy's claim that "if you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement." The thread runs through Goodhart's law objections, economic-sustainability concerns, and pushback from defenders who argue that $1,000/day is justified if the agent does the work of two junior engineers without paying for benefits.

This thread is the central Goodhart's law citation point for Dark Factory pitfalls research. The economist Charles Goodhart's principle — "when a measure becomes a target, it ceases to be a good measure" — is invoked repeatedly in HN comments to argue that token spend is a proxy for productivity that will be gamed once it becomes the goal. Defenders concede the point and StrongDM has tried to address it via "independent evaluation" (test scenarios held out from the model's view), but commenters argue this is structurally insufficient when the eval-writer and the code-writer share the same training distribution.

## Reconstructed from search snippets

### The metric

> "If you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement." — Justin McCarthy, StrongDM CTO

### Goodhart's law concern

> "If token count becomes the metric, then it'll become the goal and it ceases to be useful as a measurement. We all know what this is about. Goodhart's law ftw."

> "Tell an agent to maximize a test score and it will maximize the test score, whether or not the underlying software actually works."

### Economic sustainability concerns

> "Outside of FAANG companies, spending $1,000 per engineer per day on AI tokens would exceed spending on human salaries."

> "If patterns add $20,000/month per engineer to the budget, they become less interesting as a business model exercise." (Simon Willison)

### Defender pushback

> "It wasn't an outrageous amount if productivity is there, noting that AI could work like two $90k junior engineers but without paying for vacation, office space, or social security."

### Jensen Huang escalation

Nvidia CEO Jensen Huang: > "If that $500,000 engineer did not consume at least $250,000 worth of tokens, I'm going to be deeply alarmed."

This raised the implicit ratio: top-quartile engineers might "earn" $375,000 plus $100,000 in token allowance, with "roughly one dollar in five" being compute. Critics see this as proof that the metric is becoming a target.

## Why this matters

The thread is the definitive primary source for two related Dark Factory critiques: (1) Goodhart's law applied to token spend, and (2) economic sustainability — the per-engineer compute spend already approaches per-engineer salary at the upper end of advocates' recommendations.
