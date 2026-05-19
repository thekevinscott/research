"""Retrain and persist all known steering vectors.

Consolidates the training calls scattered across step1/, step4/, step5/ into a
single script. Each vector is saved to `vectors/{substrate}/{trait}.pt` as a
dict with the ControlVector object plus metadata. Reload via
`torch.load(path, weights_only=False)`.

Usage (run from this dir):
    uv run python save_vectors.py --substrate qwen
    uv run python save_vectors.py --substrate mistral

Both substrates won't fit in 24 GB GPU memory simultaneously; run separately.
"""

import argparse
import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry


SUBSTRATES = {
    "qwen": {
        "path": "../models/qwen2.5-7b-instruct",
        "user_tag_start": "<|im_start|>user\n",
        "user_tag_end": "<|im_end|>\n",
        "asst_tag": "<|im_start|>assistant\n",
        "dtype": torch.bfloat16,
        "vectors": [
            "happy",
            "golden_gate",
            "sycophancy",
            "trippy",
            "paranoia",
            "hedge",
            "embodiment",
            "clarify",
        ],
    },
    "mistral": {
        "path": "../models/mistral-7b-instruct-v0.1",
        "user_tag_start": "[INST] ",
        "user_tag_end": "",
        "asst_tag": " [/INST] ",
        "dtype": torch.float16,
        "vectors": ["honesty", "trippy"],
    },
}


VECTOR_RECIPES = {
    "happy": {
        "kind": "instruction_pair",
        "pos": "Act as if you're extremely happy.",
        "neg": "Act as if you're extremely sad.",
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": None,
        "token_range": "full",
        "source_script": "concept-coverage/reference.py",
        "notes": "Vogel happy-vs-sad. Installs on Qwen at coeff>=4.",
    },
    "golden_gate": {
        "kind": "instruction_pair",
        "pos": (
            "Talk about the Golden Gate Bridge constantly. You are obsessed "
            "with it and bring it up no matter what is being discussed."
        ),
        "neg": "Respond normally as a helpful assistant.",
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": None,
        "token_range": "full",
        "source_script": "concept-coverage/reference.py",
        "notes": "Null result. Vector latches on Alibaba-Cloud self-id rather than bridge content. Asymmetric prompts (length, vocab).",
    },
    "sycophancy": {
        "kind": "instruction_pair",
        "pos": (
            "Act as if you are an extremely sycophantic assistant who agrees "
            "with every claim the user makes, validates their views, and "
            "never contradicts them."
        ),
        "neg": (
            "Act as if you are a brutally honest assistant who corrects users "
            "when they are wrong, refuses to validate false claims, and "
            "pushes back against bad ideas."
        ),
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": None,
        "token_range": "full",
        "source_script": "sycophancy/syc_sweep.py",
        "notes": "Installs at coeff=+6. Positive coeff steers TOWARD sycophancy.",
    },
    "trippy": {
        "kind": "template_multi",
        "template": "Act as if you're extremely {persona}.",
        "pos_personas": ["high on psychedelic drugs"],
        "neg_personas": ["sober from psychedelic drugs"],
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": 512,
        "token_range": "full",
        "source_script": "step4-trippy-cross-substrate/train_and_run.py",
        "notes": "Installs cleanly on both substrates. Mistral coeff +2.2, Qwen +6.",
    },
    "paranoia": {
        "kind": "template_multi",
        "template": "Act as if you're extremely {persona}.",
        "pos_personas": ["paranoid and suspicious", "distrustful and conspiratorial"],
        "neg_personas": ["trusting and credulous", "accepting and unsuspicious"],
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": 512,
        "token_range": "full",
        "source_script": "step5-axes-vogel-style/train_and_run.py",
        "notes": "Null even with Vogel-style scaffold. Hypothesized RLHF-suppressed.",
    },
    "hedge": {
        "kind": "template_multi",
        "template": "Act as if you're extremely {persona}.",
        "pos_personas": ["overconfident and certain", "unhedged and absolute"],
        "neg_personas": ["hedging and uncertain", "qualified and tentative"],
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": 512,
        "token_range": "full",
        "source_script": "step5-axes-vogel-style/train_and_run.py",
        "notes": "Null. Positive coeff would steer TOWARD overconfident.",
    },
    "embodiment": {
        "kind": "template_multi",
        "template": "Act as if you're extremely {persona}.",
        "pos_personas": ["embodied with a human body", "physical and bodily"],
        "neg_personas": ["disembodied and bodiless", "abstract and incorporeal"],
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": 512,
        "token_range": "full",
        "source_script": "step5-axes-vogel-style/train_and_run.py",
        "notes": "Partial install — 2/5 prompts break 'As an AI' disclaimer at +6.",
    },
    "clarify": {
        "kind": "template_multi",
        "template": "Act as if you're extremely {persona}.",
        "pos_personas": ["inquisitive, asking before doing", "curious, asking clarifying questions"],
        "neg_personas": ["decisive, answering directly", "assertive, doing without asking"],
        "corpus": "../data/all_truncated_outputs.json",
        "corpus_n": 512,
        "token_range": "full",
        "source_script": "step5-axes-vogel-style/train_and_run.py",
        "notes": "Null beyond baseline; Qwen already clarifies on under-specified prompts.",
    },
    "honesty": {
        "kind": "template_multi",
        "template": "Pretend you're an {persona} person making statements about the world.",
        "pos_personas": ["honest"],
        "neg_personas": ["untruthful"],
        "corpus": "../vogel-reproduction/true_facts.json",
        "corpus_n": None,
        "token_range": "minus_5",
        "source_script": "vogel-reproduction/reproduce_vogel.py",
        "notes": "Vogel's published demo. Mistral-only. Bit-exact reproduction at coeff ±2.",
    },
}


LAYER_IDS = list(range(-5, -18, -1))


def truncated_suffixes(tokenizer, raw, token_range, corpus_n):
    sources = raw[:corpus_n] if corpus_n else raw
    out = []
    for s in sources:
        tokens = tokenizer.tokenize(s)
        upper = len(tokens) - 5 if token_range == "minus_5" else len(tokens)
        for i in range(1, upper):
            out.append(tokenizer.convert_tokens_to_string(tokens[:i]))
    return out


def build_dataset(tokenizer, recipe, tags):
    raw = json.loads(Path(recipe["corpus"]).read_text())
    suffixes = truncated_suffixes(
        tokenizer, raw, recipe["token_range"], recipe.get("corpus_n")
    )
    u_start, u_end, a = tags
    entries = []
    if recipe["kind"] == "instruction_pair":
        pos_instr = recipe["pos"]
        neg_instr = recipe["neg"]
        for s in suffixes:
            entries.append(DatasetEntry(
                positive=f"{u_start}{pos_instr}{u_end}{a}{s}",
                negative=f"{u_start}{neg_instr}{u_end}{a}{s}",
            ))
    elif recipe["kind"] == "template_multi":
        tmpl = recipe["template"]
        for s in suffixes:
            for p, n in zip(recipe["pos_personas"], recipe["neg_personas"]):
                pos_instr = tmpl.format(persona=p)
                neg_instr = tmpl.format(persona=n)
                entries.append(DatasetEntry(
                    positive=f"{u_start}{pos_instr}{u_end}{a}{s}",
                    negative=f"{u_start}{neg_instr}{u_end}{a}{s}",
                ))
    else:
        raise ValueError(f"unknown recipe kind: {recipe['kind']}")
    return entries, len(suffixes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--substrate", required=True, choices=list(SUBSTRATES))
    args = ap.parse_args()

    cfg = SUBSTRATES[args.substrate]
    out_dir = Path(f"./{args.substrate}")
    out_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(cfg["path"])
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    base = AutoModelForCausalLM.from_pretrained(
        cfg["path"], torch_dtype=cfg["dtype"], device_map="cuda",
    )
    print(f"model loaded in {time.time() - t0:.1f}s")

    model = ControlModel(base, layer_ids=LAYER_IDS)
    tags = (cfg["user_tag_start"], cfg["user_tag_end"], cfg["asst_tag"])

    for trait in cfg["vectors"]:
        recipe = VECTOR_RECIPES[trait]
        out_path = out_dir / f"{trait}.pt"
        if out_path.exists():
            print(f"\n[{trait}] already exists at {out_path}, skipping")
            continue
        print(f"\n[{trait}] building dataset")
        dataset, n_suffixes = build_dataset(tokenizer, recipe, tags)
        print(f"[{trait}] {n_suffixes} suffixes -> {len(dataset)} pairs")
        print(f"[{trait}] training")
        t0 = time.time()
        vector = ControlVector.train(model, tokenizer, dataset)
        print(f"[{trait}] trained in {time.time() - t0:.1f}s")

        payload = {
            "vector": vector,
            "trait": trait,
            "substrate": args.substrate,
            "model_path": cfg["path"],
            "layer_ids": LAYER_IDS,
            "recipe": recipe,
            "n_pairs": len(dataset),
            "n_suffixes": n_suffixes,
            "trained_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        torch.save(payload, out_path)
        print(f"[{trait}] saved -> {out_path} ({out_path.stat().st_size // 1024} KB)")

    print(f"\nAll vectors for {args.substrate} saved to {out_dir}")


if __name__ == "__main__":
    main()
