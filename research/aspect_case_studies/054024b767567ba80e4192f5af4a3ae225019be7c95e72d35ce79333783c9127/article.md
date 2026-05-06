# How StrongDM's AI team build serious software without even looking at the code

- URL: https://simonwillison.net/2026/Feb/7/software-factory/
- Author: Simon Willison
- Published: 2026-02-07
- Reconstructed from WebSearch snippets.

## What this is

The canonical reference write-up for the Dark Factory pattern. Simon Willison reports first-hand on visiting the StrongDM AI team in October 2025 and seeing the system live. This post is what introduced the term "Dark Factory" / "Software Factory" to the broader AI coding discourse.

## Direct quotes / near-quotes from snippets

> "the most ambitious form of AI-assisted software development I've seen yet"

> Two of the guiding principles are: "Code must not be written by humans" and "Code must not be reviewed by humans."

> "If you haven't spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement." - Justin McCarthy, StrongDM CTO

> "By October, when Simon Willison visited, they already had working demos of the system that manages their coding agents, their Digital Twin Universe, and their satisfaction testing framework."

> "the three person team of Justin McCarthy, Jay Taylor and Navan Chauhan had formed just three months earlier, and they already had working demos of their coding agent harness, their Digital Twin Universe clones of half a dozen services and a swarm of simulated test agents running through scenarios"

> "The Digital Twin Universe was notable as the part of the demo that made the strongest impression, since the software they were building helped manage user permissions across a suite of connected services - and security software is the last thing you would expect to be built using unreviewed LLM code!"

## What StrongDM showed Simon

- A coding agent harness (the Attractor loop).
- A Digital Twin Universe with clones of Okta, Jira, Slack, Google Docs, Google Drive, Google Sheets.
- A satisfaction-testing framework (LLM-as-judge over scenario trajectories).
- A swarm of simulated test agents running through scenarios.

## The framing Simon coined

- Five-level spectrum from "spicy autocomplete" to "the Dark Factory" - fully agentic development where humans don't write code and don't review it.
- Treats StrongDM as the first publicly-documented company operating at level 5.
- Notes the irony that StrongDM's product is *security* software (access management across SaaS platforms) - "the last thing you would expect to be built using unreviewed LLM code."

## Takeaway

This post is the origin of widespread interest in the Dark Factory pattern. Almost every other piece reviewed in this folder is a direct response to it.
