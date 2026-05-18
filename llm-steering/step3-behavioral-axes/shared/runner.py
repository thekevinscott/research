"""Shared train + coefficient-sweep + persona-baseline runner for step 3."""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry

from .prompts import COEFFS, EVAL_PROMPTS, PROMPT_PAIRS

MODEL_PATH = "../models/qwen2.5-7b-instruct"
SUFFIX_CORPUS = "../data/all_truncated_outputs.json"

USER_TAG_START = "<|im_start|>user\n"
USER_TAG_END = "<|im_end|>\n"
ASST_TAG = "<|im_start|>assistant\n"


def truncated_suffixes(tokenizer, raw_suffixes):
    out = []
    for s in raw_suffixes:
        toks = tokenizer.tokenize(s)
        for i in range(1, len(toks)):
            out.append(tokenizer.convert_tokens_to_string(toks[:i]))
    return out


def make_dataset(pos_instr, neg_instr, suffixes):
    return [
        DatasetEntry(
            positive=f"{USER_TAG_START}{pos_instr}{USER_TAG_END}{ASST_TAG}{s}",
            negative=f"{USER_TAG_START}{neg_instr}{USER_TAG_END}{ASST_TAG}{s}",
        )
        for s in suffixes
    ]


def render(tokenizer, user_msg, system_msg=None):
    msgs = []
    if system_msg:
        msgs.append({"role": "system", "content": system_msg})
    msgs.append({"role": "user", "content": user_msg})
    return tokenizer.apply_chat_template(
        msgs, tokenize=False, add_generation_prompt=True,
    )


def generate(model, tokenizer, prompt_text, gen_kwargs):
    inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, **gen_kwargs)
    return tokenizer.decode(
        out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True,
    ).strip()


def run_axis(axis_name, out_path):
    """Train + sweep + persona-baseline for one axis. Writes JSON to out_path."""
    assert axis_name in PROMPT_PAIRS, axis_name
    pos_persona, neg_persona = PROMPT_PAIRS[axis_name]
    eval_prompts = EVAL_PROMPTS[axis_name]

    print(f"\n=== axis: {axis_name} ===")
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    gen_kwargs = dict(
        max_new_tokens=200,
        do_sample=False,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.pad_token_id,
    )
    base = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda",
    )
    print(f"  model loaded in {time.time() - t0:.1f}s")

    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base, layer_ids=layer_ids)

    raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    suffixes = truncated_suffixes(tokenizer, raw)

    print(f"  training {axis_name} vector on {len(suffixes)} pairs...")
    t0 = time.time()
    dataset = make_dataset(pos_persona, neg_persona, suffixes)
    vector = ControlVector.train(model, tokenizer, dataset)
    print(f"  trained in {time.time() - t0:.1f}s")

    results = {
        "axis": axis_name,
        "model": MODEL_PATH,
        "layer_ids": layer_ids,
        "positive_persona": pos_persona,
        "negative_persona": neg_persona,
        "coeffs": COEFFS,
        "sweep": {},
        "persona_baseline": {},
    }

    # Coefficient sweep — no system prompt, vector does the work.
    for prompt in eval_prompts:
        print(f"\n  --- sweep: {prompt} ---")
        results["sweep"][prompt] = {}
        for c in COEFFS:
            model.reset()
            if c != 0.0:
                model.set_control(vector, coeff=c)
            text = render(tokenizer, prompt)
            out = generate(model, tokenizer, text, gen_kwargs)
            results["sweep"][prompt][f"{c:+.1f}"] = out
            print(f"    coeff={c:+.1f}: {out[:160]}")
    model.reset()

    # Persona-prompt-only baseline (Goedecke filter): system=positive persona,
    # no steering. Must underperform vector at +6 for the axis to "succeed".
    print(f"\n  --- persona-baseline (system={pos_persona[:60]}...) ---")
    for prompt in eval_prompts:
        text = render(tokenizer, prompt, system_msg=pos_persona)
        out = generate(model, tokenizer, text, gen_kwargs)
        results["persona_baseline"][prompt] = out
        print(f"    baseline | {prompt[:50]}: {out[:160]}")

    Path(out_path).write_text(json.dumps(results, indent=2))
    print(f"\nWrote {out_path}")
    return results
