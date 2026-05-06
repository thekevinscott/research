# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

URL: https://arxiv.org/abs/2310.06770

Authors: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan (Princeton Language and Intelligence). ICLR 2024.

## Reconstructed from snippets

The original SWE-bench paper — the benchmark that defined "can a language model fix a real GitHub issue end-to-end" and that every subsequent autonomous-agent claim is calibrated against.

### Quoted core claim

> "SWE-bench is an evaluation framework consisting of 2,294 software engineering problems drawn from real GitHub issues and corresponding pull requests across 12 popular Python repositories."

> "Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue."

> "Resolving issues in SWE-bench frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation."

### Why it matters for the Dark Factory thesis

SWE-bench is the metrological backbone of the entire conversation. Devin's debut number (13.86%), the SWE-bench Verified subset created with OpenAI, the SWE-Bench Pro extension, and the SWE-RL self-play work all start here. Without SWE-bench there is no shared ruler to argue that agents have crossed the threshold where Dark Factory operation is plausible.

### Lineage

- ICLR 2024 paper, original 2,294 issues across 12 Python repos.
- Spawned SWE-bench Verified (OpenAI partnership, 500 human-vetted issues), SWE-bench Lite, SWE-Bench-CL, and SWE-Bench Pro.

---

## Two-paragraph summary

The original SWE-bench paper (Jimenez et al., Princeton, ICLR 2024) is the foundational benchmark of the autonomous-coding-agent era. It evaluates whether language models can resolve real-world GitHub issues end-to-end across 2,294 problems from 12 popular Python repos, requiring multi-file edits, execution-environment interaction, and long-context reasoning — far beyond the function-completion benchmarks that preceded it.

For Dark-Factory researchers, SWE-bench is the metrological precondition: it is the ruler against which every subsequent claim — from Devin's 13.86% to GPT-5's 75% on SWE-bench Verified — is measured. The benchmark's evolution into Verified, Lite, CL, and Pro variants tracks the field's growing confidence that agents can carry production tasks autonomously. Highly relevant (3) as the methodological foundation.
