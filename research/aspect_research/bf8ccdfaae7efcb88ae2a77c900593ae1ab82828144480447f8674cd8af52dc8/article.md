# Unified Software Engineering Agent (USEagent)

URL: https://arxiv.org/abs/2506.14683

Venue: ICSE 2026 (April 12–18, 2026, Rio de Janeiro). arXiv June 17, 2025; revised December 8, 2025.

## Reconstructed from snippets

USEagent is the academic answer to "what shape does a Dark Factory agent need to be?" — a single agent that orchestrates many SE capabilities (repair, regression testing, code generation, test generation) instead of a swarm of specialists.

### Quoted thesis

> "Unlike existing work which builds specialized agents for specific software tasks such as testing, debugging, and repair, USEagent's goal is to build a unified agent which can orchestrate and handle multiple capabilities, giving the agent the promise of handling complex scenarios in software development such as fixing an incomplete patch, adding new features, or taking over code written by others."

### Benchmark contribution

> "The authors built Unified Software Engineering Bench, or USEbench for short, as a unified dataset of challenging SE tasks to test unified agentic capabilities."

### Headline numbers

> "On USEbench consisting of 1,271 tasks including program repair, regression testing, code generation, and test generation, USEagent achieves an efficacy of 33.3%, which is higher than the 26.8% efficacy from the state-of-the-art general agent OpenHands CodeActAgent."

> "On software maintenance tasks in SWE-bench-verified, USEagent has an efficacy of 45.6% which is similar to the 46.2% efficacy of the specialized AutoCodeRover agent, while being applicable to more types of tasks."

### Why it matters for the Dark Factory thesis

USEagent provides academic evidence that one orchestrating agent can match specialists across heterogeneous SE tasks. That is the structural premise of a Dark Factory: a single autonomous agent (or a small team) handles spec-to-merge across many task types without a human routing each step.

---

## Two-paragraph summary

USEagent (arXiv 2506.14683, ICSE 2026) is the academic effort to consolidate software-engineering agent capabilities — repair, regression testing, code generation, test generation — into one unified agent. On the accompanying USEbench (1,271 tasks), USEagent reaches 33.3% efficacy, beating the prior best general agent (OpenHands CodeActAgent at 26.8%), and on SWE-bench-verified it nearly matches the specialized AutoCodeRover (45.6% vs 46.2%) while covering more task types.

For the Dark Factory thesis, USEagent supplies the structural argument: an autonomous SE pipeline can be staffed by a single orchestrating agent that flexibly handles spec-to-merge across heterogeneous tasks, rather than a brittle pipeline of specialists. It complements the engineering-side claims from Anthropic and OpenAI with an academic, peer-reviewed result. Highly relevant (3).
