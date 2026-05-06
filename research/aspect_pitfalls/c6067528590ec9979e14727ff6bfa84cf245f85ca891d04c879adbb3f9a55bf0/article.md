# Built by Agents, Tested by Agents, Trusted by Whom?

Source: Stanford Law School / CodeX
URL: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/

## Summary

The Stanford Law CodeX piece is the canonical legal/accountability critique of the Dark Factory pattern. Written in response to StrongDM's February 2026 software factory manifesto, it argues that existing accountability frameworks — product liability, professional licensing, contractual warranties — were not designed for "software that no human has reviewed." The piece highlights the special concern that StrongDM is a security infrastructure company: a team building access management has decided that human code review is "an obstacle, not a safeguard," then sells the resulting product to enterprise customers.

For Dark Factory pitfalls research this is the indispensable accountability reference. The piece poses the question that gets asked in every critic thread: when an access management module written by an agent fails because of a subtle bug no human ever saw, who is liable? The architects, the AI vendor, or the company selling the product? It directly challenges the premise that "validation replaces code review" by pointing out that validation is also designed by humans who may not anticipate the very edge cases that cause harm.

## Reconstructed from search snippets

> "When customers ask how software is built in this model, the answer is: 'Coding agents wrote it. Other agents tested it against replicas of your services.'"

> "A team building security infrastructure has decided that human code review is an obstacle, not a safeguard."

### The accountability gap

> "Accountability in software has historically worked through product liability, professional licensing, and contractual warranties. None of these contemplate software that no human has reviewed."

> "If an access management system fails because an agent-written module contained a subtle error that no human ever saw, who is liable? The three engineers who designed the architecture? The AI provider whose model generated the code? The company that sold the product?"

### The "Dark Factory" terminology

The piece traces the term to manufacturing — fully automated plants that run "in the dark" because robots don't need lights. It then notes the critical disanalogy: in manufacturing, defects produce physical artifacts that fail visibly; in software, defects can lurk silently for years before triggering data breaches.

### Hallucination loop concern

A complementary concern flagged in the broader discussion: if the same model class reads documentation to build the code AND reads the same docs to build the digital twin test environment, they share the same blind spots. The product passes its tests but fails in production for the exact reason the test was inadequate.

## Why this matters

The Stanford piece is the most-cited "is this even legal?" critique of Dark Factory. It is referenced in nearly every long-form skeptical writeup. Its specific contribution is to push the conversation from "does it work?" to "who pays when it doesn't?"
