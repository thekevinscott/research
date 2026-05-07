# arxiv 2604.25850 — Agentic Harness Engineering (AHE)

AHE introduces an observability-driven loop for automatically evolving coding-agent harnesses. Three pillars: component observability (a decoupled harness whose component types are editable as files), experience observability (a layered evidence corpus from rollout trajectories), and decision observability (a change manifest pairing every edit with a self-declared prediction).

Empirical results: ten AHE iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, surpassing the human-designed Codex-CLI harness (71.9%) and self-evolving baselines ACE and TF-GRPO. The frozen harness transfers without re-evolution: on SWE-bench-verified it tops aggregate success at 12% fewer tokens than the seed; on Terminal-Bench 2 it yields +5.1 to +10.1pp cross-family gains across three model families. Important counterweight to model-first claims about Level-5 readiness.
