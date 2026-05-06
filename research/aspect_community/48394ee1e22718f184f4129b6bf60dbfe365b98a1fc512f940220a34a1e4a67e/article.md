# Hacker News: "StrongDM's AI team build serious software without even looking at the code"

**URL:** https://news.ycombinator.com/item?id=46924711
**Posted:** ~Feb 7-8, 2026 (front-paged after Simon Willison's blog post)

## Submission context

The submission points to Simon Willison's Feb 7 2026 write-up at simonwillison.net/2026/Feb/7/software-factory/. Willison summarises StrongDM's two charter rules:

> "Code must not be written by humans"
> "Code must not be reviewed by humans"

He calls this "the most ambitious form of AI-assisted software development I've seen yet."

## Reconstructed key comments (from snippets)

A widely-quoted skeptical reply (HN item 46926133):

> "I was looking for some code, or a product they made, or anything really on their..."

Several commenters reportedly cloned the open-sourced strongdm/attractor and strongdm/cxdb repos and "carefully read the documentation in the Attractor repository and strictly followed the specifications provided by StrongDM to have Claude build a complete project. As soon as the code was released, developers on Hacker News quickly examined it and pointed out suspected bugs, Rust anti-patterns, and relatively lenient error handling methods."

A commenter linked to the StrongDM landing page:

> "I'd encourage you to read this post: https://factory.strongdm.ai — it hit the front..." (HN 47196509)

## Themes raised

- Doubt about whether the open-sourced agent harness actually represents production output.
- Concern over Rust anti-patterns and lenient error handling in the released code.
- Discussion of the Digital Twin Universe (clones of Okta, Jira, Slack, Google Docs/Drive/Sheets) as the real moat.
- Recurring worry: "How could 'code must not be reviewed by humans' possibly be a sensible strategy when we all know how prone LLMs are to making inhuman mistakes?" (echoing Willison).

---

## Summary (2 paragraphs)

This Hacker News thread is the most-cited community discussion of StrongDM's announcement, surfacing right after Simon Willison's Feb 7 2026 endorsement. Commenters dug into the open-sourced strongdm/attractor and strongdm/cxdb repos and quickly flagged Rust anti-patterns, lenient error handling, and the absence of a visible end-product. The dominant tone is "interesting but unproven," with the audience treating StrongDM's two charter rules as either a stunt or a leap of faith.

The thread also crystallised the field's central technical question: the Digital Twin Universe (behavioural clones of Okta, Jira, Slack, Google Docs/Drive/Sheets) appears to be the actual hard part, not the agents themselves. HN's verdict reads as cautiously curious: respect for the engineering, scepticism about generalisability, and explicit concern that LLMs' "inhuman" failure modes are not well covered by even sophisticated test harnesses.
