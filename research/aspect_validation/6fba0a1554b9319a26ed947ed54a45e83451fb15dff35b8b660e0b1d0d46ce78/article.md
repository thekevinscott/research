# RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning

**URL:** https://arxiv.org/abs/2410.02089
**Authors:** Jonas Gehring et al. (Meta / FAIR), Oct 2024 (also at OpenReview / ICML 2025 poster)

## Reconstructed content (from search snippets)

> "RLEF is a fine-tuning method for LLMs that endows them with a crucial capability for autonomous operation: grounding future generations in environment feedback."

## Method

> "The LLM is repeatedly prompted to implement code according to a problem description. Each attempt is evaluated on a public test set; upon failure, feedback is inserted into the conversation. If public tests are passing, or a specified turn limit is reached, execution on additional, private tests determines the reward. The model is then updated with PPO."

This frames code generation as an interactive task: actions are code; observations are execution feedback (test outputs, errors, traces). End-to-end PPO fine-tuning teaches the model to actually use the feedback rather than ignoring it.

## Results

> "The paper achieves new state-of-the-art results with both small (8B parameters) and large (70B) models while reducing the amount of samples required by an order of magnitude on competitive programming tasks."

> "The improvements from RLEF on CodeContests generalize to HumanEval+ and MBPP+, two popular benchmarks for code synthesis, and to increased sample budgets compared to training time."

## Why it matters for Dark Factories

RLEF is the canonical paper showing that the validation harness can be more than a runtime safety net — it can be the *training signal*. Public tests give a per-turn shaping reward; private tests provide the terminal reward (which prevents the agent from gaming the public tests). This is the academic foundation for "the harness is the product" mindset Datadog and StrongDM espouse: better harnesses literally make better agents.

## Related lineage

The paper sits in a lineage with PPOCoder, CodeRL+, and RLVR (Reinforcement Learning with Verifiable Rewards), which all share the principle that executable code provides a uniquely cheap, dense, automatable reward signal compared to human preference labels.
