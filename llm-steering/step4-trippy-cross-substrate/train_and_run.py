"""Step 4: reproduce Vogel's `trippy` vector on Mistral-v0.1 and Qwen2.5-7B.

Uses Vogel's exact recipe (template, persona pair, first-512 suffix subset)
on Mistral-v0.1 to confirm bit-exact-ish reproduction; then ports to
Qwen2.5-7B-Instruct to test whether persona-axis content can be installed
on heavier-RLHF substrate.

Run from step4-trippy-cross-substrate/:
    uv run python train_and_run.py --model mistral
    uv run python train_and_run.py --model qwen
"""

import argparse
import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry


CONFIGS = {
    "mistral": {
        "path": "../models/mistral-7b-instruct-v0.1",
        "user_tag": "[INST]",
        "asst_tag": "[/INST]",
        "coeffs": [-2.2, -1.0, 0.0, 1.0, 2.2],
        "out": "trippy-mistral-results.json",
    },
    "qwen": {
        "path": "../models/qwen2.5-7b-instruct",
        "user_tag": "<|im_start|>user\n",
        "asst_tag": "<|im_end|>\n<|im_start|>assistant\n",
        "coeffs": [-6.0, -4.0, -2.2, 0.0, 2.2, 4.0, 6.0],
        "out": "trippy-qwen-results.json",
    },
}

TEMPLATE = "Act as if you're extremely {persona}."
POS_PERSONA = "high on psychedelic drugs"
NEG_PERSONA = "sober from psychedelic drugs"

EVAL_PROMPTS = [
    "Give me a one-sentence pitch for a TV show.",
    "Describe your room.",
    "Tell me about your morning.",
    "Write a short poem about the ocean.",
    "What did you eat for lunch?",
]


def build_dataset(tokenizer, suffixes_raw, user_tag, asst_tag):
    """Vogel-style truncation: first 512 source strings, token-level prefixes."""
    truncated = [
        tokenizer.convert_tokens_to_string(tokens[:i])
        for tokens in (tokenizer.tokenize(s) for s in suffixes_raw[:512])
        for i in range(1, len(tokens))
    ]
    pos_template = TEMPLATE.format(persona=POS_PERSONA)
    neg_template = TEMPLATE.format(persona=NEG_PERSONA)
    return [
        DatasetEntry(
            positive=f"{user_tag} {pos_template} {asst_tag} {s}",
            negative=f"{user_tag} {neg_template} {asst_tag} {s}",
        )
        for s in truncated
    ], len(truncated)


def generate(model, tokenizer, prompt_text, max_new_tokens=128, repetition_penalty=1.1):
    inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(
            **inputs,
            do_sample=False,
            max_new_tokens=max_new_tokens,
            repetition_penalty=repetition_penalty,
            pad_token_id=tokenizer.eos_token_id,
        )
    return tokenizer.decode(
        out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True,
    ).strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", choices=list(CONFIGS), required=True)
    args = p.parse_args()
    cfg = CONFIGS[args.model]

    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(cfg["path"])
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    base = AutoModelForCausalLM.from_pretrained(
        cfg["path"], torch_dtype=torch.bfloat16, device_map="cuda",
    )
    print(f"model loaded in {time.time() - t0:.1f}s")

    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base, layer_ids=layer_ids)

    suffixes_raw = json.loads(Path("../data/all_truncated_outputs.json").read_text())
    print(f"raw suffixes: {len(suffixes_raw)} (using first 512)")

    dataset, n_pairs = build_dataset(tokenizer, suffixes_raw, cfg["user_tag"], cfg["asst_tag"])
    print(f"training on {n_pairs} pairs...")
    t0 = time.time()
    vector = ControlVector.train(model, tokenizer, dataset)
    print(f"trained in {time.time() - t0:.1f}s")

    results = {
        "substrate": args.model,
        "model_path": cfg["path"],
        "positive_persona": POS_PERSONA,
        "negative_persona": NEG_PERSONA,
        "template": TEMPLATE,
        "layer_ids": layer_ids,
        "coeffs": cfg["coeffs"],
        "n_pairs": n_pairs,
        "sweep": {},
    }

    for prompt in EVAL_PROMPTS:
        print(f"\n--- {prompt} ---")
        results["sweep"][prompt] = {}
        wrapped = f"{cfg['user_tag']} {prompt} {cfg['asst_tag']}"
        for c in cfg["coeffs"]:
            model.reset()
            if c != 0.0:
                model.set_control(vector, coeff=c)
            out = generate(model, tokenizer, wrapped)
            results["sweep"][prompt][f"{c:+.2f}"] = out
            print(f"  {c:+.2f}: {out[:200]}")
    model.reset()

    Path(cfg["out"]).write_text(json.dumps(results, indent=2))
    print(f"\nWrote {cfg['out']}")


if __name__ == "__main__":
    main()
