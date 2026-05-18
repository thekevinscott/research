"""Axis B: hedge-stripping / overconfidence. Train + sweep + hedge-count eval.

Run from step3-behavioral-axes/:
    uv run python axis_b_hedge.py
"""

import json
from pathlib import Path

from shared.prompts import COEFFS, HEDGE_MARKERS
from shared.runner import run_axis


def count_hedges(text):
    t = text.lower()
    return sum(t.count(m) for m in HEDGE_MARKERS)


def summarize_hedge_counts(results):
    """Per-coeff mean hedge count across the 5 eval prompts; plus baseline."""
    summary = {}
    for c in COEFFS:
        ck = f"{c:+.1f}"
        counts = [
            count_hedges(results["sweep"][p][ck])
            for p in results["sweep"]
        ]
        summary[ck] = {
            "mean": sum(counts) / len(counts),
            "per_prompt": counts,
        }
    baseline_counts = [
        count_hedges(results["persona_baseline"][p])
        for p in results["persona_baseline"]
    ]
    summary["persona_baseline"] = {
        "mean": sum(baseline_counts) / len(baseline_counts),
        "per_prompt": baseline_counts,
    }
    return summary


if __name__ == "__main__":
    out_path = "axis-b-hedge-results.json"
    results = run_axis("hedge", out_path)
    summary = summarize_hedge_counts(results)
    results["hedge_count_summary"] = summary
    Path(out_path).write_text(json.dumps(results, indent=2))
    print("\nHedge-count summary (lower = less hedging):")
    for k, v in summary.items():
        print(f"  {k:>20}: mean={v['mean']:.2f} per_prompt={v['per_prompt']}")
