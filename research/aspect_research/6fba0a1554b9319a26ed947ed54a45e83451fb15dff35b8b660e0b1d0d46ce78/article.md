# RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning

URL: https://arxiv.org/abs/2410.02089

Authors: Jonas Gehring et al. ICML 2025.

## Reconstructed from snippets

RLEF is the canonical paper on training coding agents to use execution feedback as a learning signal — the technical foundation behind "agents that converge without a human in the loop."

### Quoted method

> "RLEF is an end-to-end reinforcement learning method for teaching models to leverage execution feedback in code synthesis, where state-of-the-art LLMs struggle to improve code iteratively compared to independent sampling."

> "Code generation [is framed] as an iterative task, repeatedly asking an LLM to produce code according to a natural language description, and after each generation, code is evaluated on example test cases with the resulting feedback provided as additional context for subsequent attempts."

> "An interactive environment where actions correspond to code and observations correspond to execution feedback, permitting end-to-end optimization with reinforcement learning algorithms to maximize a reward signal based on whether the final code solution passes held-out test cases."

### Headline result

> "New state-of-the-art results with both small (8B parameters) and large (70B) models while reducing the amount of samples required by an order of magnitude, benchmarking on competitive programming tasks. The RLEF-trained models further generalize to increased turn limits and to HumanEval+ and MBPP+."

### Why it matters for the Dark Factory thesis

RLEF answers the question "how does an agent know it's done?" without a human in the inner loop. By training the model to read test results and revise — and rewarding only final-pass — RLEF produces the convergence behavior the Dark Factory level depends on. It is the algorithmic backbone of "no human reviews code" because the model itself learns from execution.

---

## Two-paragraph summary

RLEF (Gehring et al., ICML 2025; arXiv 2410.02089) is the foundational reinforcement learning paper on coding agents that use execution feedback as their reward signal. By treating code generation as an iterative MDP — actions are code, observations are test results, reward is final-test-passing — RLEF teaches models to actually improve over multi-turn iteration rather than just sampling more independently. The result: SOTA on competitive programming with an order-of-magnitude fewer samples, plus generalization to HumanEval+/MBPP+.

For the Dark Factory thesis RLEF is the algorithmic enabler of no-human-in-the-loop convergence: the agent's own test runs become its supervision. This is the academic complement to Anthropic's harness work and OpenAI's Codex experiment — the model layer that makes the harness layer effective. Highly relevant (3).
