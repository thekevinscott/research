# StrongDM Software Factory - Ry Walker Research

- URL: https://rywalker.com/research/strongdm-factory
- Author: Ry Walker (engineering leader / research notes site)
- Reconstructed from WebSearch snippets.

## What this is

A research-style writeup that compiles what StrongDM actually built and analyses it as an organisational case study, with explicit "recommended for / not recommended for" guidance. Walker also has a companion piece "In-House Coding Agents: Build vs Buy."

## Direct quotes / near-quotes from snippets

> "StrongDM's charter is 'Code must not be written by humans. Code must not be reviewed by humans.' Code is treated as opaque weights - correctness is inferred from behavior, not inspection."

> "A three-person team built the system in just three months."

> "The catalyst was Anthropic's Claude 3.5 October 2024 revision, which enabled 'compounding correctness' in long-horizon agentic workflows."

## Walker's analysis (from snippets)

**Advantages:**
- Clear success metric - "$1,000/day in tokens per engineer" is concrete and measurable.
- Behavioral clones (the DTU) handle integration complexity that would otherwise require fragile mocks.

**Challenges:**
- Validation infrastructure investment is heavy - building the DTU took significant engineering.
- Not every domain has clear third-party APIs to clone.
- Teams must accept *not* reading or understanding generated code - a cultural shift many organizations will resist.

**Recommended for:**
- Organizations exploring the limits of AI coding autonomy
- Teams building integration-heavy software
- Infrastructure engineers designing validation systems

**Not recommended for:**
- Regulated industries requiring audit trails
- Teams uncomfortable with opaque code
- Organizations without significant observability investment

## Takeaway

Walker's piece is the closest thing to a structured "should we adopt this?" analysis. He treats Dark Factory as domain-specific - powerful where you can clone integrations and tolerate opaque code, dangerous where audit trails or regulated workflows demand human review.
