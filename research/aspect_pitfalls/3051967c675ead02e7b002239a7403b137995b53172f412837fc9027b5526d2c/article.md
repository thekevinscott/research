# Three Thoughts on Dark Code

Source: Jouke Waleson / blog.waleson.com (March 2026)
URL: https://blog.waleson.com/2026/03/three-thoughts-on-dark-code.html

## Summary

Jouke Waleson coined the term "Dark Code" — software that no human has written, read, or even reviewed — and offered a measured three-point critique. First, codebases will deteriorate without human review because "AI agents, like evolution, take the easiest path forward," and systems will get stuck in local maxima of complexity and brittleness. Second, programming languages may stop evolving because no one cares about the source's readability. Third, "darkness" is a continuum, not a binary state — code written a year ago is already darker than code written today, and most enterprise codebases are full of "dark" code by long-departed authors.

For Dark Factory pitfalls research, Waleson's piece is one of the more philosophically nuanced critiques. He grants that the dark-code direction is happening, and grants the relativist argument (humans don't fully read existing codebases either), while still landing on the conclusion that without human review and new architectural tools, codebases will become an unholy mess. His argument is structural, not anecdotal — making it complementary to the disaster-driven critiques (Replit, PocketOS).

## Reconstructed from search snippets

> "Dark code: lines of software that no human has written, read or even reviewed."

### Thought 1: Codebase deterioration

> "Without human review and new architectural tools, codebases will deteriorate. AI agents, like evolution, take the easiest path forward. Systems will become an unholy mess and get stuck in local maximums."

This is "an unsolved problem" in Waleson's framing. The agent's optimization gradient does not include "this is a clean architecture future engineers can extend"; it only includes "this passes the tests and matches the spec." Local maxima accumulate.

### Thought 2: Programming language evolution stops

If humans don't care about reading code, what drives language design? Improved syntax, better abstractions, ergonomics — all of these came from human readability concerns. When the audience is an LLM, those pressures relax. Waleson calls this "a shame."

### Thought 3: Dark is relative

> "Code he wrote a year ago is already darker than code he writes today, and enterprises are full of code written by teams that are no longer there."

This concession is rhetorically important: he is not pretending humans read every line of every codebase. The question is what happens at the margin when even fewer lines are read by anyone.

## Why this matters

Waleson is the source of the "Dark Code" terminology that complements StrongDM's "Software Factory" naming. His piece is heavily cited in skeptical writeups because it is principled rather than reactive. The architectural-drift argument it makes is mirrored in tools like the `drift` static analyzer and in critiques about Cross-Layer Edit Problems.
