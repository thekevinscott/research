# OpenAI — Introducing SWE-bench Verified

URL: https://openai.com/index/introducing-swe-bench-verified/

## Reconstructed from snippets

OpenAI's collaboration with the SWE-bench authors to produce a 500-instance human-verified subset — the cleanest benchmark for autonomous coding agents and the basis for nearly every public capability comparison cited in Dark Factory writeups.

### Quoted purpose

> "SWE-bench Verified is a human-filtered subset of 500 instances from SWE-bench, created in collaboration with OpenAI."

> "Human annotators reviewed each instance to ensure the problem descriptions are clear, the test patches are correct, and the tasks are solvable given the available information."

### Why a Verified subset

> "OpenAI collaborated with the authors of SWE-bench to address those issues in a new release of the benchmark that should provide more accurate evaluations."

### Current frontier scores (per coverage)

> "State-of-the-art models and agents have advanced to achieve scores up to 75% on variants like SWE-Bench-Verified (e.g., GPT-5) and around 40% on the full leaderboard."

### Benchmark mechanics

> "For each sample in SWE-bench, agents are provided with the original text from the GitHub issue, known as the problem statement, and are given access to the codebase. Given these, agents must edit the files in the codebase to resolve the issue."

### Why it matters for the Dark Factory thesis

SWE-bench Verified is the OpenAI-blessed measuring stick. When a frontier-lab announcement claims X% on coding, it almost always means X% on SWE-bench Verified. It is the bridge between the original Princeton academic benchmark and the operational claims big labs make about Dark-Factory readiness. Pairing this with SWE-Bench Pro (where the same models drop from ~70% to ~23%) is the most cited evidence of how cleanly the field separates "demo-ready" from "enterprise-ready."

---

## Two-paragraph summary

SWE-bench Verified is OpenAI's human-vetted 500-instance subset of the original Princeton SWE-bench, designed to remove ambiguous or unsolvable items so that progress on coding agents is measured on issues that humans confirm are actually resolvable. It has become the canonical scoreboard cited in big-lab capability announcements and the de facto gating benchmark for "is this model Dark-Factory-ready?"

Frontier scores around 75% on Verified — when paired with the much lower ~23% on the harder SWE-Bench Pro — give the field the clearest articulation of where agents are competent and where they still are not. OpenAI's curation work is the connective tissue between the academic SWE-bench tradition and the engineering claims that Dark Factory writeups make about real codebases. Highly relevant (3).
