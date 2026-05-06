# drift: Detect architectural erosion from AI-generated code

Source: GitHub / sauremilk/drift
URL: https://github.com/sauremilk/drift

## Summary

`drift` is a static analyzer specifically designed to detect architectural erosion caused by AI-generated code. The tool's existence is itself evidence of a Dark Factory pitfall: enough engineering teams have observed "silent architectural drift" from AI-generated PRs that a dedicated tool category has emerged. The analyzer flags pattern fragmentation, architecture violations, and "mutant duplicates" — near-copies of existing code that the agent generated rather than reusing existing implementations.

For Dark Factory pitfalls research this repository is a useful citation because it concretizes a critique that is otherwise abstract. The "codebase coherence loss" concern that Waleson raises ("AI agents take the easiest path forward; systems get stuck in local maxima") is exactly what `drift` is designed to detect. The README and tool category formalize the failure mode: AI agents generate locally-correct code that violates global architecture, and over many PRs the architecture erodes silently. By the time a human notices, refactoring the way back is exponentially harder than preventing the drift.

## Reconstructed from search snippets

### Tool description

> "Detect architectural erosion from AI-generated code. Static analyzer for pattern fragmentation, architecture violations & mutant duplicates."

### Failure modes the tool detects

- **Pattern fragmentation**: the codebase loses consistent patterns (e.g., error-handling style varies wildly between modules).
- **Architecture violations**: dependency directions reverse; layers blur; abstractions leak.
- **Mutant duplicates**: near-identical code blocks generated independently rather than refactored into shared utilities.

### Connection to broader drift discourse

> "Each AI-generated PR moves the codebase slightly away from its intended architecture. After six months of AI-assisted development, the gap between 'how this system was designed' and 'how this system actually works' becomes a chasm, and refactoring your way back is exponentially harder than preventing the drift."

> "Detection of AI-generated code quality issues can happen through five signals: code duplication ratio, 30/90-day revert rates, complexity-adjusted analysis, architectural coherence scoring, and test behavior coverage."

### Task drift related concept

> "Without proper guardrails, agents drift from the original task, get stuck in infinite exploration cycles, or generate plausible-looking code that's fundamentally wrong."

## Why this matters

The existence of `drift` (and similar tools) is empirical evidence that Dark Factory's architectural-drift problem is real, observable, and serious enough to warrant dedicated tooling. For pitfalls research it is a citation that says: "this isn't theoretical; engineers in the wild have built measurement tools because they see the problem in their own codebases." The 30/90-day revert rate metric is particularly damning — if AI-generated code is being reverted at higher rates than human code, the productivity numbers Dark Factory advocates cite are inflated by counting code that later has to be undone.
