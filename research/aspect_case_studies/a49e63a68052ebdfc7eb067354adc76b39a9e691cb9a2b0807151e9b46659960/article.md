# Dark Factory: "No Humans Should Write Code" (and what it taught me)

- URL: https://world.hey.com/johnnybutler/dark-factory-no-humans-should-write-code-and-what-it-taught-me-3f1a06f0
- Author: Johnny Butler (tech lead, ex-startup engineer)
- Published: February 2026
- Reconstructed from WebSearch snippets - direct quotes are flagged.

## Summary of the experience

Johnny Butler ran his own small dark-factory experiment after reading the StrongDM/Simon Willison writeup. He built a personal website as a fully spec-driven "dark factory" project, in order to feel "the full dark-factory loop of specs going in and software coming out" first-hand (paraphrase).

He then tried to apply the same pattern at his day job, where the codebase is a large legacy Rails monolith.

## Key first-hand findings (paraphrased from snippets)

- In greenfield, isolated areas, agents can do a lot of implementation with tight prompts.
- It's much harder to achieve a true dark-factory loop in a large legacy Rails monolith because of technical debt and operational complexity.
- The realistic goal isn't to replace an entire monolith with a dark factory. Instead, carve out boundaries where a factory can operate with full autonomy - he calls these "micro-factories" inside the monolith.

## Direct quotes (from search snippets)

> "Dark Factory isn't 'no humans'. It's 'humans move up the stack'."

> "humans stop spending time on mechanical implementation and diff-reading"

(Paraphrase, repeated across snippets) The experiment provided a practical pathway back into the monolith: not a rewrite or big-bang transformation, but a set of factory lines with shared rules, each responsible for a bounded part of the system - producing software from specs, and proving it with harnesses instead of opinions.

## Takeaway

For working engineers in legacy codebases, the dark factory pattern is most plausible as a series of "micro-factories" - bounded sub-systems with their own specs/scenarios/harnesses - rather than as a wholesale replacement of human coding.
