# EPAM Insights: "From Figma to Production Code: Building a Dark Factory with AI Agents"

**URL:** https://www.epam.com/insights/ai/blogs/building-a-dark-factory-with-ai-agents

## Reconstructed content (from search snippets)

This is the canonical "where the dark factory fails" piece — EPAM ran an empirical attempt at a Figma-to-production dark factory and reported the negative results.

Key findings:

> "Agents are confidently, quietly bad at visual fidelity and unreliable on code quality. From their runs: the agent wrapped an entire page in a shadowed box with rounded corners the design never specified, included icons in a subtly wrong shade of gray compared to design, showed a download button with only one icon instead of two, and rendered a back-arrow navigation icon in blue instead of black."

On reproducibility:

> "Stability — how consistently the same task produces the same quality — is well below 95%. Different runs of identical input produce different decompositions, different implementation plans, different final output. One run nails icon placement and misses typography, while the next gets typography right and invents a wrapper element."

Failure-mode summary:

> "Dark factory automation works best for well-defined, repetitive tasks with testable acceptance criteria. It's poorly suited for ambiguous, novel, or high-stakes problems requiring real judgment."

## Domain-fit verdict

UI/UX is presented as a category-fail: the validation loop (visual fidelity to a design spec) is fundamentally hard for current LLMs, agent stability is sub-95%, and "looks right" is not a deterministic test. EPAM concludes the pattern works for backend/infra but not for visual front-end work as of mid-2026.

---

## Summary (2 paragraphs)

EPAM's "Figma to Production Code" report is the most-cited evidence that the dark factory does not generalise to UI/UX. Their empirical runs show sub-95% stability, confident-but-wrong visual fidelity (wrong gray, missing icons, wrong wrapper elements), and failure modes that are invisible to automated tests. The piece is the standard counter-example to the StrongDM-style success story.

The conclusion — that dark factories suit "well-defined, repetitive tasks with testable acceptance criteria" but fail on ambiguous/visual/novel work — is the most-quoted domain-fit framing in the discourse. It pairs with the StrongDM and BCG case studies to define the boundary: backend, security tooling, migrations, and accounting glue work; UI design, novel research code, and high-stakes judgment do not.
