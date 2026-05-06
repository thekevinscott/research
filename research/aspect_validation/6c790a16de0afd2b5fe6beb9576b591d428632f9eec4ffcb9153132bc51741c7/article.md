# Demystifying Evals for AI Agents

**URL:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
**Publisher:** Anthropic Engineering Blog (2025)

## Reconstructed content

> "An evaluation (eval) is a structured test where an AI agent is given a task and is graded on whether it succeeds. Evals help turn vague notions of 'agent quality' into measurable, repeatable signals."

## Grader taxonomy

Anthropic distinguishes among:

- **State and outcome checks** — deterministic predicates over final or intermediate state.
- **LLM-based rubrics** — flexible grading for open-ended dimensions where determinism fails.
- **Deterministic graders** — e.g., the SWE-bench Verified pattern of running the actual test suite.

> "For conversational agents, success can be multidimensional: is the ticket resolved (state check), did it finish in <10 turns (transcript constraint), and was the tone appropriate (LLM rubric)?"

## LLM-based rubric guidance

> "An LLM can flag unsupported claims and gaps in coverage but also verify the open-ended synthesis for coherence and completeness. Given the subjective nature of research quality, LLM-based rubrics should be frequently calibrated against expert human judgment to grade these agents effectively."

> "Create clear, structured rubrics to grade each dimension of a task, and then grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions."

(The "isolated judge per dimension" rule is the practical implementation of generator-judge separation.)

## SWE-bench Verified note

> "SWE-bench Verified gives agents GitHub issues from popular Python repositories and grades solutions by running the test suite; a solution passes only if it fixes the failing tests without breaking existing ones. LLMs have progressed from 40% to >80% on this eval in just one year."

## Key principles

- **Grade what the agent produced, not the path it took.** (Outcome > trajectory.)
- **20-50 simple tasks drawn from real failures** is enough to start.
- **A grader is logic that scores some aspect of the agent's performance. A task can have multiple graders, each containing multiple assertions (sometimes called checks).**
- **Calibrate LLM judges against humans regularly** to detect drift.

## Why it matters

This is the most cited "official" articulation of the eval discipline from a frontier lab. It supplies the vocabulary (task, grader, check, dimension, rubric) that subsequent dark-factory writeups (Datadog, OpenAI, StrongDM) build on, and it codifies "isolated judges per dimension" as best practice.
