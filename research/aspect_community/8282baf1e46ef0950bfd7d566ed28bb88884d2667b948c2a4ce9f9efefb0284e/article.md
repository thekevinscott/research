# Hacker News: "Software factories and the agentic moment"

**URL:** https://news.ycombinator.com/item?id=46924426
**Posted:** Feb 7, 2026 (StrongDM blog post submission)

## Submission context

This thread points directly to StrongDM's own blog announcement at https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai. Key claims from the StrongDM piece (per snippets):

> "We built a Software Factory: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review."

> "Attractor is the non-interactive coding agent at the heart of their software factory."

> "cxdb [is] an AI Context Store - a system for storing conversation histories and tool outputs in an immutable DAG, with 16,000 lines of Rust, 9,500 of Go and 6,700 of TypeScript."

## Comment themes (reconstructed)

The thread predates the simonw-linked HN item 46924711 by hours and is more focused on technical mechanics than philosophy. Recurring themes from snippets:

- Discussion of "scenarios" — StrongDM repurposed the word "scenario" to mean an end-to-end "user story" intuitively understood and flexibly validated by an LLM.
- Engineers asked how the digital twins are kept in sync with real Okta/Jira/Slack APIs.
- Some commenters referenced Stripe's "Minions" program (≈1,300 AI-authored PRs/week) as a comparison point, distinguishing StrongDM's no-review stance from Stripe's still-human-merge model.
- Open-source skeptics noted that the Markdown-spec-only structure of the strongdm/attractor repo makes the claim hard to evaluate.

---

## Summary (2 paragraphs)

This Hacker News thread covers the StrongDM-authored blog post itself (as opposed to the simonw write-up), and the discussion centres on technical mechanics: the "scenarios" framing for end-to-end user stories, the Digital Twin Universe of cloned third-party APIs, and the immutable-DAG context store cxdb. Comments are notably more engineer-y than the parallel simonw-linked thread, with debate about how twins remain faithful to real services and whether spec-driven Markdown is a sufficient artefact.

Comparisons to Stripe's "Minions" pipeline (≈1,300 AI PRs/week, but humans still merge) frame StrongDM as the strict no-review extreme. Sentiment is curious but unsettled — most commenters treat the announcement as a credible existence proof for security-tooling-style domains while remaining unconvinced it generalises.
