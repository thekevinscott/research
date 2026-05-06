# LLM as a Judge — Primer and Pre-Built Evaluators

**URL:** https://arize.com/llm-as-a-judge/
**Publisher:** Arize AI

## Reconstructed content

> "LLM-as-a-Judge uses large language models themselves to evaluate outputs from other models."

> "LLM as a judge is useful across a raft of use cases, including detecting hallucination, accuracy, relevancy, toxicity, and more."

## Arize's empirical claim

> "The Arize AI team has tested and assembled a list of simple evaluation templates that use an LLM-as-a-judge and achieve target precision and F-scores above 70%."

> "Arize's Phoenix Evals library is a practical starting point before you build anything custom. It has pre-built, benchmarked templates for everything listed above, tested against golden datasets targeting 70-90% precision."

## Practical patterns

Arize emphasizes:

- **Templates over freeform prompts.** Each evaluator (hallucination, relevance, toxicity, code correctness, etc.) ships as a tested template with known precision/F-score against a golden dataset.
- **Calibrate before deploying.** Without measurement against gold labels, you cannot trust the judge.
- **Brief reasoning + criteria boost correlation with human preference.** Asking the judge to articulate the rubric pushes agreement up.

> "Strong models already correlate well with human preferences in open-ended evaluation, and structured prompts that elicit brief reasoning and criteria often push correlations higher."

## Phoenix prompt-optimization

Arize Phoenix supports an explicit LLM-as-a-Judge prompt-optimization workflow: you collect labeled examples, search prompt variants, and pick the variant with the highest agreement against your gold. This is the operationalization of "treat your judge prompt like a model."

## Why it matters

Arize is the source of the most widely-deployed library of pre-built, calibrated judge templates. For Dark Factory builders, Phoenix Evals is the easiest way to bootstrap a verification harness without writing every judge from scratch — and the public precision numbers (70-90%) are roughly the bar a custom judge has to beat to be worth building.
