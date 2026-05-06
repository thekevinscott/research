# Resources for Measuring Autonomous AI Capabilities (METR)

**URL:** https://metr.org/measuring-autonomous-ai-capabilities/
**Publisher:** METR (Model Evaluation and Threat Research)

## Reconstructed content

> "METR (Model Evaluation and Threat Research) is a Berkeley-based research nonprofit that scientifically measures AI agent autonomy — specifically, how long an AI system can work independently on real-world tasks before requiring human intervention."

## Benchmark composition

> "The benchmark includes 180+ machine learning engineering, cybersecurity, software engineering, and general reasoning tasks that take humans between one minute and 8+ hours."

> "HCAST [Human-Calibrated Autonomy Software Tasks], one of the task suites, comprises 189 tasks across machine learning, cybersecurity, software engineering, and general reasoning domains that typically require multi-step sequential decision-making, are largely derived from real-world work, take between 1-2 minutes and 8+ hours, and undergo multiple stages of manual quality assurance and review."

## The headline metric: time horizon

> "METR's primary benchmark measures the 50% Task-Completion Time Horizon: the length of time (in hours of equivalent human effort) at which an AI model can autonomously complete tasks with a 50% success rate."

## Trend

> "The METR benchmark has revealed one of the most striking trends in AI: autonomous task horizons are doubling approximately every 4 months. The progression shows: Early 2024: roughly 4 minutes · Late 2024: 15-30 minutes · Mid 2025: ~4 hours · February 2026: ~14.5 hours."

## MirrorCode

> "In the MirrorCode benchmark co-developed with METR, Claude Opus 4.6 autonomously reimplemented a 16,000-line bioinformatics toolkit — a task estimated to take a human engineer 2-17 weeks."

## Why it matters

METR is the benchmark that reframes the validation conversation in terms of *task duration* rather than task success rate. The doubling-every-four-months curve is the strongest single quantitative argument for why dark factories are now economically interesting; harness investment makes sense if the agent can chew on a 14.5-hour task autonomously, but not for a 4-minute one.
