# A Survey on LLM-as-a-Judge

URL: https://arxiv.org/abs/2411.15594

## Reconstructed from snippets

The most-cited survey of the LLM-as-a-judge paradigm — relevant because Dark Factory pipelines depend on AI evaluating AI output (and the StrongDM critique that this creates a circularity).

### Quoted framing

> "How can reliable LLM-as-a-Judge systems be built?"

> "It explores strategies to enhance reliability, including improving consistency, mitigating biases, and adapting to diverse assessment scenarios, and proposes methodologies for evaluating the reliability of LLM-as-a-Judge systems, supported by a novel benchmark."

The paper has been updated multiple times, with the most recent version dated October 19, 2025.

### Companion / related work

- "LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods" (arXiv 2412.05579) — five-perspective analysis (Functionality, Methodology, Applications, Meta-evaluation, Limitations).
- "Preference Leakage: A Contamination Problem in LLM-as-a-judge" — accepted to ICLR 2026, exposes risks when generator and evaluator are related models.
- "How to Correctly Report LLM-as-a-Judge Evaluations" (arXiv 2511.21140) — addresses bias from imperfect judge sensitivity/specificity.

### Why it matters for the Dark Factory thesis

The Dark Factory's foundational assumption is that AI can grade AI work well enough to close the loop without humans. This survey is the academic field's reckoning with that assumption. Preference leakage in particular is the technical formalization of the worry Stanford CodeX raises in "Built by Agents, Tested by Agents, Trusted by Whom?" — when builder and judge share the same blind spots, the loop is not actually closed.

---

## Two-paragraph summary

The LLM-as-a-Judge survey (arXiv 2411.15594) is the central academic reference for the practice that makes Dark Factory pipelines possible at all: using LLMs to evaluate LLM output as a substitute for human review. It catalogs methods to improve consistency, mitigate bias, and meta-evaluate judges, and is the launching point for a fast-growing literature on judge reliability.

The most consequential follow-ups for the Dark Factory thesis are the contamination/preference-leakage and reporting-bias papers, which formalize the circularity worry: when builder and judge come from the same model family, agreement does not guarantee correctness. This is the academic counterpart to Stanford CodeX's "Trusted by Whom?" essay. Highly relevant (3).
