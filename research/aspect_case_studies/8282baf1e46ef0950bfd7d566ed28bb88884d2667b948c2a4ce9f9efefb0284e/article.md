# Hacker News: "Software factories and the agentic moment"

- URL: https://news.ycombinator.com/item?id=46924426
- Date: ~2026-02-09
- Reconstructed from WebSearch snippets (the linked article was on the StrongDM Software Factory; this entry captures the discussion thread).

## What this is

The flagship Hacker News thread responding to Simon Willison's StrongDM Dark Factory writeup. Hundreds of practitioners weighed in with first-hand reactions and tried the open-sourced code.

## Direct quotes / near-quotes from snippets

> "specs + scenarios drive agents that write code, run harnesses, and converge without human review"

> "the most consequential question in software development right now: how can you prove that software you are producing works if both the implementation and the tests are being written for you by coding agents?"

> The "$1,000 on tokens today per human engineer" benchmark was repeatedly cited and debated.

## Discussion themes (from snippets)

- Practitioners on HN immediately downloaded the released Rust code and pointed out suspected bugs, Rust anti-patterns, and "relatively lenient error handling methods."
- Jay Taylor (StrongDM AI team) showed up in the thread and replied to those critiques.
- A widely upvoted concern: if the same model class writes both the implementation and the tests, the model's blind spots are baked into both - "if the model misunderstands an edge case, it will bake that misunderstanding into both the product and the test, causing the test to pass while the production system fails."
- A separate top-level cluster of comments criticised that StrongDM's marketing site lacked actual product/code at the time the manifesto was published.

## Why this counts as first-hand experience

The thread is a public, real-time peer review of the StrongDM artifacts by working engineers - including direct engagement from one of StrongDM's three core team members. It captures the first wave of practitioner reaction, including specific code-level critiques and counter-arguments from the StrongDM side.

## Takeaway

The HN discussion is the central place where the dark-factory pattern was stress-tested in public by working engineers, and it's where a number of the canonical critiques (shared blind spots between implementation and tests, code-quality of the released Rust, etc.) entered the conversation.
