"""Run all four behavioral-axis experiments in sequence on the same model load.

Re-loading the model 4x adds ~7 min of wall-clock; loading once and reusing
saves it. Order: paranoia, hedge, embodiment, clarify.
"""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector

from shared.prompts import COEFFS, EVAL_PROMPTS, HEDGE_MARKERS, PROMPT_PAIRS
from shared.runner import (
    MODEL_PATH, SUFFIX_CORPUS, generate, make_dataset, render,
    truncated_suffixes,
)


def run_one(axis, model, tokenizer, gen_kwargs, vector):
    pos = PROMPT_PAIRS[axis][0]
    results = {
        "axis": axis,
        "coeffs": COEFFS,
        "sweep": {},
        "persona_baseline": {},
    }
    for prompt in EVAL_PROMPTS[axis]:
        results["sweep"][prompt] = {}
        for c in COEFFS:
            model.reset()
            if c != 0.0:
                model.set_control(vector, coeff=c)
            text = render(tokenizer, prompt)
            out = generate(model, tokenizer, text, gen_kwargs)
            results["sweep"][prompt][f"{c:+.1f}"] = out
    model.reset()
    for prompt in EVAL_PROMPTS[axis]:
        text = render(tokenizer, prompt, system_msg=pos)
        out = generate(model, tokenizer, text, gen_kwargs)
        results["persona_baseline"][prompt] = out
    return results


def main():
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    gen_kwargs = dict(
        max_new_tokens=200, do_sample=False, repetition_penalty=1.1,
        pad_token_id=tokenizer.pad_token_id,
    )
    base = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda",
    )
    print(f"model loaded in {time.time() - t0:.1f}s")

    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base, layer_ids=layer_ids)

    raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    suffixes = truncated_suffixes(tokenizer, raw)

    all_results = {}
    for axis in ("paranoia", "hedge", "embodiment", "clarify"):
        pos, neg = PROMPT_PAIRS[axis]
        print(f"\n=== axis {axis}: training... ===")
        t0 = time.time()
        ds = make_dataset(pos, neg, suffixes)
        vector = ControlVector.train(model, tokenizer, ds)
        print(f"  trained in {time.time() - t0:.1f}s")
        print(f"=== axis {axis}: sweep + baseline ===")
        t0 = time.time()
        all_results[axis] = run_one(axis, model, tokenizer, gen_kwargs, vector)
        print(f"  ran in {time.time() - t0:.1f}s")
        out_path = f"axis-{axis}-results.json"
        Path(out_path).write_text(json.dumps(all_results[axis], indent=2))
        print(f"  wrote {out_path}")

    Path("all-axes-results.json").write_text(json.dumps(all_results, indent=2))
    print("\nWrote all-axes-results.json")


if __name__ == "__main__":
    main()
