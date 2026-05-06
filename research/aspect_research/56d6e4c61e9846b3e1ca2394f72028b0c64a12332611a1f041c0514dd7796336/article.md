# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses (AHE)

URL: https://arxiv.org/abs/2604.25850

## Reconstructed from snippets

The arXiv paper that gives "harness engineering" its formal academic treatment — turning the OpenAI/Anthropic engineering blogs into a falsifiable framework with observability pillars and measured iterations on Terminal-Bench 2.

### Quoted definition

> "Agentic Harness Engineering (AHE) is a closed loop that addresses challenges through three matched observability pillars: (1) component observability gives every editable harness component a file-level representation so the action space is explicit and revertible; (2) experience observability distills millions of raw trajectory tokens into a layered, drill-down evidence corpus that an evolving agent can actually consume; and (3) decision observability pairs every edit with a self-declared prediction, later verified against the next round's task-level outcomes."

> "These pillars turn every edit into a falsifiable contract, so harness evolution proceeds autonomously without collapsing into trial-and-error."

### Empirical result

> "Ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed harness Codex-CLI (71.9%) and the self-evolving baselines ACE and TF-GRPO."

### Scope of "harness"

> "What evolves are the harness components — system prompts, tool descriptions, tool implementations, middleware, skills, sub-agents, and long-term memory."

The base model is held fixed; the harness evolves. AHE is described as "an open observability system for automatically evolving the harness around a coding agent."

### Why it matters for the Dark Factory thesis

AHE is the most direct academic operationalization of the Dark Factory's central claim that *the harness, not the model, is now the rate-limiter*. By demonstrating that an agentic process can autonomously evolve its own harness and beat human-designed harnesses (Codex-CLI), AHE provides a path where even harness engineering itself becomes a Dark Factory task — a recursion frontier-lab essays gesture at but academia has now begun to measure.

---

## Two-paragraph summary

AHE (arXiv 2604.25850) is the academic formalization of the harness-engineering practice OpenAI and Anthropic describe in their engineering blogs. It defines a closed loop with three observability pillars — component, experience, and decision — that turn every harness edit into a falsifiable contract, allowing the harness to evolve autonomously without collapsing into trial-and-error. Crucially, the base model is held fixed; what evolves are system prompts, tool definitions, middleware, skills, sub-agents, and memory.

Empirically, ten AHE iterations push pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed Codex-CLI harness (71.9%) and self-evolving baselines like ACE and TF-GRPO. This is the Dark Factory's recursion frontier: not just agents writing code, but agents evolving the very scaffolding that makes them autonomous. Highly relevant (3).
