# Dark Factory: "No Humans Should Write Code" (and what it taught me)

Source: Johnny Butler / hey.com (world.hey.com)
URL: https://world.hey.com/johnnybutler/dark-factory-no-humans-should-write-code-and-what-it-taught-me-3f1a06f0

## Summary

Johnny Butler's piece is a hands-on practitioner's mixed verdict on Dark Factory after attempting to apply it to a monolithic codebase. His core finding: "the path back into the monolith is through boundaries." Replacing an entire monolith with a Dark Factory is unrealistic, but creating multiple "factory lines" inside the monolith — each owning a bounded area, running autonomously, with shared guardrails and tailored acceptance checks — is feasible. He also reframes the rhetoric: "Dark Factory isn't 'no humans' — it's 'humans move up the stack,' where humans stop spending time on mechanical implementation and diff-reading."

For Dark Factory pitfalls research this article is valuable because Butler is sympathetic, not hostile, but his lessons quietly catalogue what doesn't work. The article documents that Dark Factory cannot be retrofitted onto an existing codebase wholesale; that the pattern requires architectural pre-work (bounded contexts, factory-line boundaries) that most companies do not have; and that the headline framing ("no humans should write code") is misleading — what's actually being claimed is "no humans implement; humans validate at a higher level." That framing is much weaker than the StrongDM marketing suggests.

## Reconstructed from search snippets

### Core lessons

1. "What a Dark Factory actually is": validation replaces code review, not "AI writes code."
2. "Practical implementation": multiple factory lines inside a monolith, each bounded.
3. "The human role": humans move up the stack, not out.
4. "End goal": factory lines with shared rules; software produced from specs and proven via harnesses.

### The "isn't 'no humans'" framing

> "Dark Factory isn't 'no humans' — it's 'humans move up the stack,' where humans stop spending time on mechanical implementation and diff-reading."

This rhetorical move undercuts the StrongDM marketing line. Butler's lived experience suggests the "no human writes code, no human reviews code" rules are aspirational rather than literal — humans still write specs, design factory boundaries, and curate acceptance scenarios.

### Architectural prerequisites

Butler discovered that Dark Factory requires:
- Bounded context boundaries.
- Factory line ownership.
- Shared guardrails.
- Tailored acceptance checks per line.

Most monoliths do not have these. Adopting Dark Factory therefore requires a substantial up-front architectural investment that the marketing rarely mentions.

## Why this matters

Butler's article is one of the more honest practitioner accounts and is therefore widely cited by Dark Factory skeptics as evidence that the pattern doesn't apply at the headline-stated strength. The pitfalls he documents — needs bounded contexts, requires significant architectural prep, the "no humans" framing is rhetorical not literal — show up across other practitioner critiques.
