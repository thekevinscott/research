# SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

URL: https://arxiv.org/abs/2509.16941

## Reconstructed from snippets

SWE-Bench Pro is the harder, contamination-resistant successor to SWE-bench Verified — explicitly designed for the long-horizon, multi-day enterprise tasks the Dark Factory pattern is supposed to solve.

### Quoted scope

> "SWE-Bench Pro is a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH."

> "SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools."

### Three-partition design

> "The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups."

### Task properties

> "Long-horizon tasks that may require hours to days for a professional software engineer to complete, often involving patches across multiple files and substantial code modifications. All tasks are human-verified and augmented with sufficient context to ensure resolvability."

### Headline result (snippet)

> "Top-tier models like Opus 4.1 and GPT-5 achieve a 23% success rate on SWE-Bench Pro compared to over 70% on benchmarks like SWE-Bench Verified, highlighting a critical gap between current agent capabilities and the demands of real-world development."

### Anti-contamination design

> "Exclusively selecting repositories distributed under strong copyleft licenses (GPL) to construct a public set and a held-out set, and acquiring commercial codebases from real startups to capture enterprise-grade problems in a commercial set."

### Why it matters for the Dark Factory thesis

SWE-Bench Pro is the most direct academic counter to over-claims about Dark Factory readiness. Frontier models drop from ~70% on Verified to ~23% on Pro, indicating that the multi-day, multi-file enterprise tasks the BCG/StrongDM/OpenAI essays claim victory on are still a research frontier on contamination-controlled data.

---

## Two-paragraph summary

SWE-Bench Pro (arXiv 2509.16941) is the harder, longer-horizon, contamination-resistant follow-up to SWE-bench Verified. With 1,865 human-verified tasks across 41 actively maintained repos — split into a public GPL-licensed set, a held-out set, and a commercial set drawn from real startups — it is explicitly designed to measure the kind of multi-file, hours-to-days enterprise work the Dark Factory is supposed to deliver.

The headline result is sobering: top models score ~23% on SWE-Bench Pro versus ~70% on SWE-bench Verified. This is the most rigorous academic check on big-lab Dark Factory enthusiasm — it suggests the gap between today's agent capabilities and the realistic demands of enterprise codebases is much larger than press-release benchmarks imply. Highly relevant (3).
