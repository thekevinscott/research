# Cursor's Research on Running 100 Agents in Parallel: Why Flat Agent Teams Fail Without an Issue Tracker

Source: MindStudio blog
URL: https://www.mindstudio.ai/blog/cursor-research-100-agents-parallel-flat-agent-teams-issue-tracker

## Summary

MindStudio's writeup unpacks Cursor's parallel-agent experiment and frames the lesson around coordination infrastructure: flat agent teams without an issue-tracker-like artifact for shared context cannot scale. The piece reinforces Cursor's findings that 20 agents on a shared coordination file run at the throughput of 1-3 due to lock contention, and that without a hierarchy, agents avoid hard problems. MindStudio extends this into a broader claim: the practical multi-agent stack is converging on simple, inspectable artifacts (markdown files, side workers, receipts, local-first coordination) rather than grand platform abstractions.

This article is useful for Dark Factory pitfalls research because it generalizes the Cursor finding: flat agent coordination is a known anti-pattern, and the entire industry is moving toward planner-worker hierarchies and persistent, inspectable artifacts. Dark Factory pitches that imagine "fleets of agents writing your codebase" must contend with the fact that such fleets need their own scheduling and arbitration, which is a substantial engineering problem in itself, often equivalent to building a miniature project-management system.

## Reconstructed from search snippets

The key claim: flat agent teams fail without an issue tracker.

Citing the original Cursor research:
- 20 agents → throughput of 1-3 in flat coordination.
- Brittle locking: agents fail while holding locks; agents skip lock acquisition entirely.
- Without hierarchy, agents are risk-averse: small safe changes, no end-to-end ownership.
- Hierarchical planner-worker scales to hundreds of concurrent agents.

> "Across communities, markdown files, side workers, receipts, and local-first coordination show up repeatedly, suggesting the practical AI-agent stack is converging around simple, inspectable artifacts instead of grand platform abstractions."

## Why this matters

For Dark Factory critics, the MindStudio writeup is useful because it documents that even successful multi-agent systems fall back to inspectable artifacts (issue trackers, markdown specs) — i.e., the very things human developers use. The "lights out" framing is misleading; what's actually happening at scale is "lights on, but for agents instead of humans." The infrastructure cost is real and the agent sprawl is bounded by the same coordination problems any engineering team faces.
