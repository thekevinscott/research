# Scaling long-running autonomous coding (Cursor blog)

Source: Cursor Engineering Blog
URL: https://cursor.com/blog/scaling-agents

## Summary

Cursor's engineering team published a postmortem-style blog about their experiment running large numbers of coding agents in parallel. Their initial approach was a flat coordination model: agents would dynamically negotiate work amongst themselves through a shared coordination file, on the theory that planning ahead would be too rigid for ambiguous large codebases. The experiment failed in two distinct ways: (1) lock contention — 20 agents would slow to the throughput of 1-3, with most time spent waiting on locks, and agents could fail while holding locks or update the coordination file without acquiring locks at all; (2) risk-averse behavior — without hierarchy, no agent took responsibility for hard problems, so work churned on small safe changes for long periods without progress.

This article matters for Dark Factory pitfalls research because it is the strongest first-party documented evidence that "more agents in parallel" is not a free productivity multiplier. Cursor's solution was to abandon flat coordination for a hierarchical planner-worker pipeline. For Dark Factory advocates who imagine fleets of agents autonomously dividing work, the Cursor post is required reading: agent sprawl creates coordination overhead that can dominate output, and naive scaling produces churn rather than progress.

## Reconstructed from search snippets

> "Cursor's initial approach to multi-agent coordination was based on the assumption that planning ahead would be too rigid, since the path through a large project is ambiguous and the right division of work isn't obvious at the start. They began with dynamic coordination, where agents decide what to do based on what others are currently doing."

### Failure mode 1: Lock contention

> "The system was brittle: agents could fail while holding locks, try to acquire locks they already held, or update the coordination file without acquiring the lock at all. Locking also caused too much contention, where 20 agents would slow to the throughput of 1-3 with most time spent waiting on locks."

### Failure mode 2: Risk-averse behavior

> "With no hierarchy, agents became risk-averse. They avoided difficult tasks and made small, safe changes instead. No agent took responsibility for hard problems or end-to-end implementation. This led to work churning for long periods of time without progress."

### The pivot

Cursor moved from flat coordination to a planner-worker hierarchy:
- Planner agents continuously explore the codebase and create tasks.
- Worker agents execute tasks independently.
- Roles are separated rather than emergent.

This solution scaled to "hundreds of concurrent agents" but represents a structural admission: "let agents figure it out" does not work at scale.

## Implications for Dark Factory

The Cursor experiment is a direct refutation of one of the more aggressive Dark Factory framings: that you can simply spawn N agents per spec and let them collaborate. In practice:
- Coordination is non-trivial.
- Lock-free designs produce risk-averse behavior.
- Hierarchical control is necessary, which reintroduces the planner role that Dark Factory advocates often delegate to spec documents.
- The "right division of work" must be designed, not discovered at runtime by peers.
