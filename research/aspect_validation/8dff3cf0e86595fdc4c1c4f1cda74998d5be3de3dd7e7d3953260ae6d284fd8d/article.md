# Agent-as-a-Judge: Evaluate Agents with Agents

**URL:** https://arxiv.org/abs/2410.10934
**Authors:** Mialon et al. (metauto-ai), Oct 2024

## Reconstructed content

> "Contemporary evaluation techniques are inadequate for agentic systems because these approaches either focus exclusively on final outcomes — ignoring the step-by-step nature of agentic systems — or require excessive manual labor."

The paper introduces **Agent-as-a-Judge**: extending LLM-as-a-Judge with agentic features so that the judge itself can step through, probe, and inspect intermediate states of the agent under test. This produces "intermediate feedback for the entire task-solving process" rather than only a final-outcome verdict.

## DevAI benchmark

> "The Agent-as-a-Judge framework was applied to code generation tasks using DevAI, a new benchmark of 55 realistic automated AI development tasks with 365 hierarchical user requirements."

## Results

> "The researchers benchmarked three popular agentic systems using Agent-as-a-Judge and found it dramatically outperforms LLM-as-a-Judge and is as reliable as human evaluation baseline."

This is the empirical claim that matters for Dark Factories: a sufficiently capable agentic judge approaches human-evaluation reliability — meaning the human grader can be removed from the loop without large quality loss, *if* the judge has enough scaffolding.

## Why it matters

The paper supplies the rigorous version of the "generator-judge separation" pattern: the judge is itself an agent (with tools, memory, multi-step reasoning), can verify intermediate steps (not just outputs), and can produce feedback that drives the next generation cycle. It is the natural complement to RLEF: RLEF tells you how to *use* a verifier signal; Agent-as-a-Judge tells you how to *build* a verifier rich enough to evaluate agentic work.
