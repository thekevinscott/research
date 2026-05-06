# Code That Nobody Reads, Running Tests That Nobody Wrote

Source: Marco Kotrotsos / Medium
URL: https://kotrotsos.medium.com/code-that-nobody-reads-running-tests-that-nobody-wrote-1855837ee9a8

## Summary

Marco Kotrotsos's essay distills the Dark Factory critique into the title slogan: a system where no human reads the source code AND no human writes the tests. The article surveys the StrongDM manifesto and Dan Shapiro's five-level taxonomy that places "the Dark Factory" at Level 5 (above "spicy autocomplete," "AI pair programming," etc.). It documents that StrongDM spends roughly $1,000/month per engineer on AI tokens (StrongDM's CTO actually says $1,000/day, suggesting a citation drift in the popular narrative) on a system that ships production code without human review or testing.

This article is a frequently-cited entry-point critique because the title is sticky and the framing crystallizes the structural concern: when nobody reads the code AND nobody writes the tests, every layer of the trust pipeline rests on the same model class, and the ostensible independence of "the agent that writes" vs "the agent that tests" is largely fiction. For pitfalls research the piece anchors the Dark Factory discourse in concrete dollar figures and operational detail rather than abstract principle.

## Reconstructed from search snippets

The article's two operating rules (StrongDM's): "Code must not be written by humans" and "Code must not be reviewed by humans."

> "No human reads the source code and no human writes the tests."

The five-level taxonomy from Dan Shapiro:
- Level 1: Spicy autocomplete
- Level 2: AI pair programming
- ...
- Level 5: The Dark Factory — fully autonomous; "robots work in unlit facilities because robots do not need to see."

### Token economics

The article notes the $1,000-per-engineer-per-day spend at StrongDM (sometimes mis-quoted as per month) and frames it through the lens of: at this price point, what is the engineer for?

## Why this matters

Kotrotsos provides the rhetorical handle for the entire critique: "Code That Nobody Reads, Running Tests That Nobody Wrote." That phrase has become the de-facto skeptic shorthand for the Dark Factory pattern. For pitfalls research the article is one of the most popular gateway critiques and is heavily referenced by downstream commentators.
