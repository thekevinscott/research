# SWE-bench Verified

**URL:** https://www.swebench.com/verified.html
**Publisher:** SWE-bench team / OpenAI

## Reconstructed content

> "SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI, where human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information."

The motivation: the original SWE-bench had quality issues — under-specified problem descriptions, brittle test patches, sometimes unsolvable instances — that produced noisy comparisons across agents. Verified is the cleaned holdout.

## Apples-to-apples evaluation

> "The Verified leaderboard features results from a wide variety of AI coding systems, and to make an apples-to-apples comparison of language models easier, all LMs are evaluated using mini-SWE-agent in a minimal bash environment with no tools and no special scaffold structure, just a simple ReAct agent loop."

The mini-SWE-agent constraint is critical: it isolates the *model's* contribution from clever scaffolding so the leaderboard reflects underlying coding capability rather than tool wrapping.

## Grading mechanism

A solution passes only if:

1. The previously failing test(s) now pass (issue resolution).
2. All previously passing tests still pass (no regressions).

This is the cleanest example of "deterministic grader" in Anthropic's taxonomy — there is no LLM judge in the loop, just `pytest`.

## Progress curve

> "LLMs have progressed from 40% to >80% on this eval in just one year." (Anthropic, 2025)

The rapid saturation is part of why SWE-bench Pro was created.

## Why it matters

SWE-bench Verified is the gold standard for "the harness can be the test suite itself." Dark Factories essentially scale this principle: every scenario is a fail-to-pass / pass-to-pass test plan, and the agent iterates until both conditions are satisfied.
