# How StrongDM's AI team build serious software without even looking at the code

URL: https://simonwillison.net/2026/Feb/7/software-factory/
Author: Simon Willison
Date: Feb 7, 2026

## Reconstructed content (from search snippets)

This is the canonical reference post defining the "Dark Factory" pattern for AI-driven software development. Simon Willison documents StrongDM's "Software Factory" approach.

> "I wrote about the most ambitious form of AI-assisted software development I've seen yet - Strong DM's 'Software Factory' approach, where two of the guiding principles are 'Code must not be written by humans' and 'Code must not be reviewed by humans'." (Simon Willison on X)

The piece describes how StrongDM repurposed key concepts to make this work:

> "StrongDM repurposed the word scenario to represent an end-to-end 'user story', often stored outside the codebase (similar to a 'holdout' set in model training), which could be intuitively understood and flexibly validated by an LLM."

> "StrongDM uses the term satisfaction to quantify this validation: of all the observed trajectories through all the scenarios, what fraction of them likely satisfy the user?"

The Digital Twin Universe is described:

> "StrongDM built twins of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, replicating their APIs, edge cases, and observable behaviors."

Reward-hacking observation:

> "Their agents wrote return true, which passes any test beautifully and does nothing useful, so they kept these descriptions hidden from the agents, so the agents could not simply memorize the answers."

By October 2025, when Willison visited StrongDM, the team already had working demos of the system that manages their coding agents, their Digital Twin Universe, and their satisfaction testing framework.

## Key tools / patterns referenced

- Seed -> validation harness -> feedback loop pipeline
- Coding agents (StrongDM does not name vendor-specific agents in this post but uses commercial coding agents)
- Digital Twin Universe (in-house behavioral clones of SaaS APIs)
- Scenario-based validation (held-out user stories scored by LLM judges)
- Satisfaction metric across observed trajectories
