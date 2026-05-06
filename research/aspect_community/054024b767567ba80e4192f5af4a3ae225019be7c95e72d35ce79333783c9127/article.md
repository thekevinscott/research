# Simon Willison: "How StrongDM's AI team build serious software without even looking at the code"

**URL:** https://simonwillison.net/2026/Feb/7/software-factory/
**Author:** Simon Willison
**Date:** February 7, 2026

## Reconstructed content (from search snippets)

This is the canonical post that named the pattern in the engineering press. Willison opens by recalling a demo he saw in October from a three-person StrongDM AI team — Justin McCarthy, Jay Taylor, and Navan Chauhan — formed only three months earlier.

Direct quotes recovered from snippets:

> "I wrote about the most ambitious form of AI-assisted software development I've seen yet — Strong DM's 'Software Factory' approach, where two of the guiding principles are 'Code must not be written by humans' and 'Code must not be reviewed by humans'."

> "How could that possibly be a sensible strategy when we all know how prone LLMs are to making inhuman mistakes?"

The piece introduces several artefacts that the rest of the discourse refers back to:

- **Attractor** — StrongDM's non-interactive coding agent (open-sourced).
- **cxdb** — an "AI Context Store" using an immutable DAG of conversations and tool outputs (16,000 lines Rust + 9,500 Go + 6,700 TypeScript).
- **Digital Twin Universe** — behavioural clones of third-party services StrongDM depends on, "including Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, replicating their APIs, edge cases, and observable behaviors."
- **Scenarios** — repurposed from QA literature to mean LLM-validated end-to-end user stories.

Willison frames the core unsolved problem:

> "How can you prove that software you are producing works if both the implementation and the tests are being written for you by coding agents?"

His provisional answer: validation infrastructure (digital twins + scenario engines) replaces human review.

## Strategic framing

Willison places the StrongDM model at Dan Shapiro's Level 5 — "the dark software factory" — and treats it as the first real-world existence proof. He is markedly more optimistic in this post than in the surrounding HN comments.

---

## Summary (2 paragraphs)

Simon Willison's Feb 7 2026 post is the canonical write-up that linked Dan Shapiro's "Dark Factory" framing to a working real-world implementation, StrongDM's three-person AI team. The post lays out the four moving parts — Attractor (the agent), cxdb (the context store), the Digital Twin Universe (cloned third-party APIs), and Scenarios (LLM-validated user stories) — and identifies the core unsolved question: how to prove software works when both code and tests are written by agents.

Willison's tone is admiring but careful, repeatedly noting the riskiness of "code must not be reviewed by humans." His framing — that validation infrastructure now bears the burden review used to bear — became the central argument the rest of the community (BCG, Citrix, Stanford Law, Pragmatic CTO, Lenny's Newsletter) responded to.
