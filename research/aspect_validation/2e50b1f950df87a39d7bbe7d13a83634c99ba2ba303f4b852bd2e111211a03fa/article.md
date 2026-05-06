# J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning

**URL:** https://arxiv.org/abs/2505.10320
**Authors:** Meta researchers (Whitehouse et al.), May 2025

## Reconstructed content

> "J1 is a reinforcement learning framework for teaching LLM judges to think before making decisions."

> "The core contribution lies in converting all judgment tasks for non-verifiable and verifiable prompts into a unified format with verifiable rewards, enabling direct optimization of evaluation quality while mitigating positional bias."

## Method

> "J1 is a generalist LLM-as-a-Judge trained to assess the quality of model-generated responses. Unlike scalar reward models that produce a single score, it uses chain-of-thought reasoning and makes judgments through verdicts or scores."

The unified verifiable-reward formulation is the trick: even subjective ("non-verifiable") evaluation prompts are recast so the judge can be RL-trained against an automatically-checkable signal (e.g., consistency under swap, agreement with synthetic gold).

## Variants and results

> "J1 was trained at scales of 8B, 32B, and 70B and achieved state-of-the-art performance across multiple benchmarks. In particular, J1-Qwen-32B, the multitasked pointwise and pairwise judge, also outperforms o1-mini, o3, and a much larger 671B DeepSeek-R1 on some benchmarks, while only training on synthetic data."

> "J1 achieved strong performance across PPE, RewardBench, JudgeBench, RM-Bench, and FollowBenchEval benchmarks."

## Emergent behaviors

> "Qualitative analysis reveals that J1 develops systematic evaluation strategies, including dynamic criteria generation, reference answer creation, iterative self-correction of initial assessments, and feedback generation for low-quality responses."

## Why it matters

J1 is the most prominent example of "judge-as-first-class artifact" — a model trained specifically to be the verifier in a generator-judge loop. Two implications for Dark Factories: (1) you can reach o3-level judgment quality at 32B with synthetic data, making in-house judges economically feasible; (2) judges that explicitly reason and self-correct are a better fit for the long-horizon, multi-criteria scenario validation StrongDM-style harnesses require.
