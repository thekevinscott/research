# SWE-Bench Pro Leaderboard (Public Dataset)

**URL:** https://labs.scale.com/leaderboard/swe_bench_pro_public
**Publisher:** Scale AI

## Reconstructed content

> "SWE-Bench Pro is a software engineering benchmark by Scale AI that evaluates AI coding agents on 1,865 long-horizon tasks from 41 real repositories across Python, Go, TypeScript, and JavaScript."

> "SWE-Bench Pro tasks require coordinating changes across an average of 4.1 files, with tasks requiring an average of 107 lines of changes across 4.1 files."

This is a deliberate step up in difficulty from Verified, which is mostly single-file Python.

## Grading

> "A task is marked as 'resolved' only if a submitted code patch satisfies two strict conditions: Issue Resolution (the patch must fix the specific bug or implement the feature, verified when the new 'fail-to-pass' tests pass), and No Regressions (the patch must not break any existing functionality, verified when all pre-existing 'pass-to-pass' tests continue to pass)."

Same deterministic mechanism as Verified, just on harder, multi-language, multi-file tasks.

## Verified vs Pro comparison

> "SWE-Bench Verified has 500 Python-only tasks with small fixes (median 4 lines), while SWE-Bench Pro has 1,865 multi-language tasks requiring substantial, multi-file modifications. The drop from 80.9% (Verified) to 57-59% (Pro) reflects that SWE-Bench Verified is largely a single-file benchmark, with most fixes touching one file with a few lines changed."

## Why it matters

SWE-bench Pro is the current top-of-the-difficulty-curve deterministic-grader benchmark and a more honest proxy for the kind of work a Dark Factory has to do (multi-file, cross-language, real repos). The 57-59% ceiling on Pro vs 80%+ on Verified is the empirical reminder that the harness still has to absorb a lot of failure on realistic tasks.
