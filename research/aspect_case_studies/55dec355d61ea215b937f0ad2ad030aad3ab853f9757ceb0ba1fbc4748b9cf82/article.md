# Show HN: OctopusGarden - An autonomous software factory (specs in, code out)

- URL: https://news.ycombinator.com/item?id=47226107
- Project: foundatron/octopusgarden (GitHub)
- Reconstructed from WebSearch snippets.

## What this is

A first-hand "I built my own dark factory" Show HN. The author open-sourced an end-to-end implementation of the StrongDM-style pattern (specs + scenarios + attractor + satisfaction) so other developers can run a dark factory locally.

## Direct quotes / near-quotes from snippets

> "OctopusGarden is an autonomous software development system where you describe what you want (specs) and how to verify it works (scenarios), and OctopusGarden orchestrates AI coding agents that generate, test, and iterate on the code until it converges on a working implementation - without any human code review."

> "The key insight is that scenarios are a holdout set - the coding agent never sees them during generation."

> "An LLM judge scores satisfaction probabilistically (0-100), not with boolean pass/fail, which prevents reward hacking and produces genuinely correct software."

> In the dark factory model, "a spec goes in, code gets generated, built in Docker, validated against scenarios the agent never saw, scored, and failures feed back until it converges."

## Components (from snippets)

- **Specs**: Markdown files describing what the software should do.
- **Scenarios**: YAML files describing user journeys, used as a holdout set.
- **Attractor**: convergence loop - generate -> test -> score -> feedback -> regenerate.
- **Satisfaction**: LLM-as-judge probabilistic scoring (0-100).
- **Preflight**: LLM-based assessment of spec clarity and scenario quality.
- **Wonder/Reflect**: two-phase stall recovery - high-temperature diagnosis, then low-temperature surgical generation.
- **Model Escalation**: switches to stronger models when stuck.
- **Gene Transfusion**: extracts coding patterns from exemplar codebases.
- **Stratified Validation**: layered validation across scenarios.

## What works (from snippets)

- The system "works with mostly standard CRUD/REST API apps."
- Sample specs ship with the repo demonstrating REST APIs, todo apps with authentication, and terminal UI applications.

## Takeaway

OctopusGarden is the most concrete "you can run a dark factory yourself today" artifact. It transparently re-implements StrongDM's core ideas - including the holdout-scenario insight that is widely seen as the technically hardest piece - in open source.
