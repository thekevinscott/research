# Overview

Arize's LLM-as-a-Judge primer is the most-cited industry articulation of the pattern, anchored by Arize's own Phoenix Evals library — a set of pre-built, benchmarked judge templates (hallucination, relevance, toxicity, code correctness) calibrated to 70-90% precision against golden datasets. The page makes the case that judges are an engineering artifact: they require templates, calibration runs, and prompt optimization (Phoenix supports an explicit prompt-search workflow that picks the variant with the highest agreement against gold labels).

For Dark Factory designers it sets a quantitative floor: a judge that beats 70-90% precision against a domain-specific gold set is "production-ready," and templates that already meet that bar are downloadable. It is the pragmatic complement to academic work like J1 and Agent-as-a-Judge — fewer SOTA claims, more deployment recipes.
