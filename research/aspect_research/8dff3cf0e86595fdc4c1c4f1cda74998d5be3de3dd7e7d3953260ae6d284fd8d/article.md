# Agent-as-a-Judge: Evaluate Agents with Agents

URL: https://arxiv.org/abs/2410.10934

## Reconstructed from snippets

The arXiv paper that extends LLM-as-a-judge into the agentic regime — directly relevant to the Dark Factory question of who decides whether agent-produced code is acceptable.

### Quoted framing

> "The Agent-as-a-Judge framework enables agentic systems to evaluate agentic systems as an organic extension of the LLM-as-a-Judge framework, incorporating agentic features that enable intermediate feedback for the entire task-solving process."

> "The researchers presented DevAI, a new benchmark of 55 realistic automated AI development tasks."

### Headline finding

> "The judge agent does not require a human in the loop for intermediate checking, yet its judgments were found to be as reliable as human evaluations in identifying the better agent solution, and it dramatically outperformed a standard LLM-as-a-judge that only saw final outputs."

### Companion: When AIs Judge AIs (arXiv 2508.02994)

> "An 'agent judge' is an autonomous LLM-based agent endowed with similar abilities as the agents it evaluates – it can observe intermediate steps, utilize tools (if needed), and perform reasoning over the agent's action log. Crucially, it can give granular feedback: not only a final score, but also pinpoint which requirements were satisfied or which steps were efficient/correct."

### Why it matters for the Dark Factory thesis

Agent-as-a-Judge addresses the central question raised by Stanford CodeX about Dark Factories: if no human reviews the code, who does? The paper's empirical claim — judge agents matching human evaluations and outperforming output-only LLM judges — is the academic basis on which Dark Factory operators justify the closed loop. It also surfaces the limitation: shared blind spots between builder and judge.

---

## Two-paragraph summary

Agent-as-a-Judge (arXiv 2410.10934) extends LLM-as-a-judge into the agentic regime: a judge agent observes intermediate steps, uses tools, and reasons over the action log, rather than scoring only final outputs. On the DevAI benchmark of 55 realistic AI development tasks the judge agent matches human evaluations in identifying the better agent solution and dramatically outperforms output-only LLM judges.

This is the academic answer to the Stanford CodeX "Trusted by Whom?" question. It operationalizes how a Dark Factory closes its quality loop without humans — and, in the limitations its successor paper (When AIs Judge AIs, arXiv 2508.02994) acknowledges, where that loop can fail when builder and judge share architecture and biases. Highly relevant (3).
