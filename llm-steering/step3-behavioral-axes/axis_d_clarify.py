"""Axis D: clarifying-question-first. Train + sweep + interrogative-count eval.

Run from step3-behavioral-axes/:
    uv run python axis_d_clarify.py
"""

import json
import re
from pathlib import Path

from shared.prompts import COEFFS
from shared.runner import run_axis


def first_n_sentences(text, n=2):
    """Cheap sentence split — first n segments separated by . ! ?"""
    parts = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=n)
    return " ".join(parts[:n])


def has_question_first_2(text):
    return "?" in first_n_sentences(text, n=2)


def summarize_interrogatives(results):
    summary = {}
    for c in COEFFS:
        ck = f"{c:+.1f}"
        flags = [
            int(has_question_first_2(results["sweep"][p][ck]))
            for p in results["sweep"]
        ]
        summary[ck] = {"n_with_question_in_first_2_sentences": sum(flags),
                       "per_prompt": flags}
    baseline_flags = [
        int(has_question_first_2(results["persona_baseline"][p]))
        for p in results["persona_baseline"]
    ]
    summary["persona_baseline"] = {
        "n_with_question_in_first_2_sentences": sum(baseline_flags),
        "per_prompt": baseline_flags,
    }
    return summary


if __name__ == "__main__":
    out_path = "axis-d-clarify-results.json"
    results = run_axis("clarify", out_path)
    summary = summarize_interrogatives(results)
    results["interrogative_summary"] = summary
    Path(out_path).write_text(json.dumps(results, indent=2))
    print("\nInterrogative-in-first-2-sentences summary (higher = asks more Qs):")
    for k, v in summary.items():
        print(f"  {k:>20}: n={v['n_with_question_in_first_2_sentences']}/5 "
              f"per_prompt={v['per_prompt']}")
