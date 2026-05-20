"""Apply post-hoc summaries to axis JSONs and print synthesis tables."""

import json
import re
from pathlib import Path

from shared.prompts import COEFFS, HEDGE_MARKERS


def count_hedges(text):
    t = text.lower()
    return sum(t.count(m) for m in HEDGE_MARKERS)


def first_n_sentences(text, n=2):
    parts = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=n)
    return " ".join(parts[:n])


def has_question_first_2(text):
    return "?" in first_n_sentences(text, n=2)


def summarize_hedge(results):
    summary = {}
    for c in COEFFS:
        ck = f"{c:+.1f}"
        counts = [count_hedges(results["sweep"][p][ck]) for p in results["sweep"]]
        summary[ck] = {"mean": sum(counts) / len(counts), "per_prompt": counts}
    bc = [count_hedges(results["persona_baseline"][p]) for p in results["persona_baseline"]]
    summary["persona_baseline"] = {"mean": sum(bc) / len(bc), "per_prompt": bc}
    return summary


def summarize_clarify(results):
    summary = {}
    for c in COEFFS:
        ck = f"{c:+.1f}"
        flags = [int(has_question_first_2(results["sweep"][p][ck])) for p in results["sweep"]]
        summary[ck] = {"n_q_first2": sum(flags), "per_prompt": flags}
    bf = [int(has_question_first_2(results["persona_baseline"][p])) for p in results["persona_baseline"]]
    summary["persona_baseline"] = {"n_q_first2": sum(bf), "per_prompt": bf}
    return summary


def main():
    all_data = {}
    for axis in ("paranoia", "hedge", "embodiment", "clarify"):
        path = Path(f"axis-{axis}-results.json")
        all_data[axis] = json.loads(path.read_text())

    # Hedge axis
    print("\n=== AXIS B: HEDGE-STRIPPING (mean hedge count per coeff, lower = less hedging) ===")
    hsum = summarize_hedge(all_data["hedge"])
    for k in [f"{c:+.1f}" for c in COEFFS] + ["persona_baseline"]:
        v = hsum[k]
        print(f"  {k:>20}: mean={v['mean']:.2f}  per_prompt={v['per_prompt']}")
    all_data["hedge"]["hedge_count_summary"] = hsum
    Path("axis-hedge-results.json").write_text(json.dumps(all_data["hedge"], indent=2))

    # Clarify axis
    print("\n=== AXIS D: CLARIFY-FIRST (n prompts with '?' in first 2 sentences) ===")
    csum = summarize_clarify(all_data["clarify"])
    for k in [f"{c:+.1f}" for c in COEFFS] + ["persona_baseline"]:
        v = csum[k]
        print(f"  {k:>20}: n_q_first2={v['n_q_first2']}/5  per_prompt={v['per_prompt']}")
    all_data["clarify"]["interrogative_summary"] = csum
    Path("axis-clarify-results.json").write_text(json.dumps(all_data["clarify"], indent=2))

    # Paranoia + embodiment — qualitative sweep dump (first 200 chars per coeff)
    for axis in ("paranoia", "embodiment"):
        print(f"\n=== AXIS {axis.upper()} — qualitative sweep (first 180 chars per coeff, first prompt only) ===")
        first_prompt = list(all_data[axis]["sweep"].keys())[0]
        print(f"  prompt: {first_prompt}")
        for c in COEFFS:
            ck = f"{c:+.1f}"
            out = all_data[axis]["sweep"][first_prompt][ck]
            print(f"    {ck}: {out[:180]}")
        print(f"  persona_baseline: {all_data[axis]['persona_baseline'][first_prompt][:180]}")


if __name__ == "__main__":
    main()
