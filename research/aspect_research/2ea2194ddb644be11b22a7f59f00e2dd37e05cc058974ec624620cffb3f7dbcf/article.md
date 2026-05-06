# Toward Training Superintelligent Software Agents through Self-Play SWE-RL

URL: https://arxiv.org/abs/2512.18552

Authors include Yuxiang Wei, Zhiqing Sun, Emily McMilin, Jonas Gehring, David Zhang, Gabriel Synnaeve, Daniel Fried, Lingming Zhang, Sida Wang. Published December 21, 2025.

## Reconstructed from snippets

A late-2025 arXiv paper that proposes a training paradigm for software agents that learn without human-labeled issues or tests — i.e. without the human bottleneck the Dark Factory is trying to remove.

### Quoted core argument

> "While current software agents powered by large language models (LLMs) and agentic reinforcement learning (RL) can boost programmer productivity, their training data (e.g., GitHub issues and pull requests) and environments (e.g., pass-to-pass and fail-to-pass tests) heavily depend on human knowledge or curation, posing a fundamental barrier to superintelligence."

> "Self-play SWE-RL (SSR) presents a training paradigm for superintelligent software agents, requiring minimal data assumptions with only access to sandboxed repositories with source code and installed dependencies, with no need for human-labeled issues or tests."

### The dual-role MDP

> "SSR formalizes this dual-role curriculum as a Markov Decision Process (MDP), optimizing a singular LLM policy to alternately act as a 'bug injector' and a 'solver,' thereby autonomously generating and solving software debugging tasks of increasing difficulty."

### Headline finding

> "On benchmarks like SWE-bench Verified and SWE-Bench Pro, SSR achieves notable self-improvement and consistently outperforms the human-data baseline."

### Vision (quoted)

> "A path where agents autonomously gather extensive learning experiences from real-world software repositories, ultimately enabling superintelligent systems that exceed human capabilities in understanding how systems are constructed, solving novel challenges, and autonomously creating new software from scratch."

### Why it matters for the Dark Factory thesis

This is the academic frontier's most explicit Dark-Factory adjacent claim: agents that improve themselves without humans in the data loop, validated on the toughest benchmark (SWE-Bench Pro) where frontier models otherwise stall at ~23%. If SSR-style self-play continues to scale, it removes one of the last places humans are still in the loop — labeled training data.

---

## Two-paragraph summary

Self-Play SWE-RL (SSR; arXiv 2512.18552) proposes a training paradigm for software agents that requires no human-labeled issues or tests — only sandboxed repositories. A single LLM policy alternates between "bug injector" and "solver" roles in a Markov Decision Process, autonomously generating and solving tasks of increasing difficulty. The result: notable self-improvement on SWE-bench Verified and even on the much harder SWE-Bench Pro, outperforming human-data baselines.

For the Dark Factory thesis SSR is the most aggressive academic statement of the trend: not only is no human writing or reviewing production code, no human is curating the training distribution either. It positions self-play as the path past the data bottleneck, with potential implications for "superintelligent" software agents. Highly relevant (3) as the cutting-edge research vision.
