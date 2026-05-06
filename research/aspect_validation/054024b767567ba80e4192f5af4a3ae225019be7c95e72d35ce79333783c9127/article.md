# How StrongDM's AI team build serious software without even looking at the code

**URL:** https://simonwillison.net/2026/Feb/7/software-factory/
**Author:** Simon Willison
**Date:** Feb 7, 2026

## Reconstructed content (from search snippets)

Simon Willison visited the StrongDM AI team in October 2025 as part of a small group of invited guests. He characterized what he saw as:

> "a glimpse of one potential future of software development, where software engineers move from building the code to building and then semi-monitoring the systems that build the code. The Dark Factory."

The three-person team — Justin McCarthy, Jay Taylor, and Navan Chauhan — had formed only three months earlier, and they already had:

- A working coding-agent harness
- "Digital Twin Universe" clones of half a dozen third-party services
- A swarm of simulated test agents running through scenarios

## The three cardinal rules of the Software Factory

> "Rule one, code must not be written by humans. Rule two, code must not be reviewed by humans. Rule three, if you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement."

## Scenarios as out-of-codebase user stories (holdout set)

> "StrongDM repurposed the word *scenario* to represent an end-to-end 'user story', often stored outside the codebase (similar to a 'holdout' set in model training), which could be intuitively understood and flexibly validated by an LLM."

This is the core validation primitive of the Dark Factory: the spec lives outside the repo so an agent cannot overfit by silently editing it; an LLM judge interprets and grades behavior against the scenario.

## Digital Twin Universe

Behavioral clones of third-party services (Okta, Jira, Slack, Google Docs/Drive/Sheets, etc.) replicate APIs, edge cases, and observable behaviors. Per the article (paraphrased from snippets): creating a high-fidelity clone of a major SaaS application was previously possible but not economically feasible — the dark-factory economics make it viable because the twin is the test environment for swarms of simulated agents.

## On X (Simon's posted summary)

> "I wrote about the most ambitious form of AI-assisted software development I've seen yet — StrongDM's 'Software Factory' approach, where two of the guiding principles are 'Code must not be written by humans' and 'Code must not be reviewed by humans.'"

## Significance

The post is broadly cited as the canonical introduction of the "Dark Factory" (a term coined by Dan Shapiro) to the software-development discourse, and ties together several validation primitives — scenarios, LLM judges, digital twins, harness loops — into one coherent stack.
