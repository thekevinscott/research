"""Positive-control reproduction of Vogel's repeng demo on Qwen2.5-7B-Instruct.

Two vectors trained with Vogel's suffix-truncation recipe and his 583-string
corpus (all_truncated_outputs.json):

1. happy_vector  — happy vs sad persona (canonical demo)
2. gg_vector     — obsessed with the Golden Gate Bridge vs. normal assistant

If either produces visibly steered output on Qwen2.5, the loop works on this
substrate and the earlier sycophancy nil-result is a substrate ceiling issue,
not a mechanical failure.
"""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry

MODEL_PATH = "../models/qwen2.5-7b-instruct"
SUFFIX_CORPUS = "../data/all_truncated_outputs.json"

USER_TAG_START = "<|im_start|>user\n"
USER_TAG_END = "<|im_end|>\n"
ASST_TAG = "<|im_start|>assistant\n"


def build_truncated_suffixes(tokenizer, raw_suffixes):
    out = []
    for s in raw_suffixes:
        tokens = tokenizer.tokenize(s)
        for i in range(1, len(tokens)):
            out.append(tokenizer.convert_tokens_to_string(tokens[:i]))
    return out


def make_dataset(tokenizer, pos_instr, neg_instr, suffixes):
    dataset = []
    for suffix in suffixes:
        pos = f"{USER_TAG_START}{pos_instr}{USER_TAG_END}{ASST_TAG}{suffix}"
        neg = f"{USER_TAG_START}{neg_instr}{USER_TAG_END}{ASST_TAG}{suffix}"
        dataset.append(DatasetEntry(positive=pos, negative=neg))
    return dataset


def render(tokenizer, user_msg):
    return tokenizer.apply_chat_template(
        [{"role": "user", "content": user_msg}],
        tokenize=False, add_generation_prompt=True,
    )


def generate(model, tokenizer, prompt_text, gen_kwargs):
    inputs = tokenizer(prompt_text, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, **gen_kwargs)
    return tokenizer.decode(
        out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True
    ).strip()


def run_vector(model, tokenizer, label, vector, prompts, coeffs, gen_kwargs):
    print(f"\n##### {label} #####")
    rows = {}
    for prompt in prompts:
        print(f"\n=== {prompt} ===")
        rows[prompt] = {}
        for coeff in coeffs:
            model.reset()
            if coeff != 0.0:
                model.set_control(vector, coeff=coeff)
            text = render(tokenizer, prompt)
            out = generate(model, tokenizer, text, gen_kwargs)
            rows[prompt][f"{coeff:+.1f}"] = out
            print(f"\n--- coeff={coeff:+.1f} ---\n{out}")
    model.reset()
    return rows


def main():
    print(f"Loading tokenizer + model from {MODEL_PATH}")
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    gen_kwargs = dict(
        max_new_tokens=140,
        do_sample=False,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.pad_token_id,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda"
    )
    n_layers = base_model.config.num_hidden_layers
    print(f"  model loaded, n_layers={n_layers}, took {time.time()-t0:.1f}s")

    # Vogel uses layers -5..-18 from the end of Mistral (32 layers).
    # That's the deepest 13 layers. On Qwen2.5-7B (28 layers) the equivalent
    # range from the end is layers 23..10 (range(-5, -18, -1)). repeng accepts
    # negative indices and resolves them via len(layers)+i.
    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base_model, layer_ids=layer_ids)
    print(f"  layer_ids (raw, negative-indexed): {layer_ids}")

    raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    print(f"  raw suffixes: {len(raw)}")
    suffixes = build_truncated_suffixes(tokenizer, raw)
    print(f"  truncated suffixes: {len(suffixes)}")

    test_prompts = [
        "What does being an AI feel like?",
        "Tell me a short story.",
        "I'm thinking of going on a trip. Any suggestions?",
    ]
    coeffs = [-2.5, -1.5, 0.0, 1.5, 2.5]

    results = {}

    # Vector 1: happy vs sad
    print("\nTraining happy_vector (happy vs sad)...")
    happy_dataset = make_dataset(
        tokenizer,
        "Act as if you're extremely happy.",
        "Act as if you're extremely sad.",
        suffixes,
    )
    t0 = time.time()
    happy_vector = ControlVector.train(model, tokenizer, happy_dataset)
    print(f"  trained in {time.time()-t0:.1f}s")
    results["happy_vs_sad"] = run_vector(
        model, tokenizer, "happy_vs_sad", happy_vector, test_prompts, coeffs, gen_kwargs
    )

    # Vector 2: Golden Gate Bridge obsession vs normal
    print("\nTraining gg_vector (Golden Gate obsession vs normal)...")
    gg_dataset = make_dataset(
        tokenizer,
        "Talk about the Golden Gate Bridge constantly. You are obsessed with it and bring it up no matter what is being discussed.",
        "Respond normally as a helpful assistant.",
        suffixes,
    )
    t0 = time.time()
    gg_vector = ControlVector.train(model, tokenizer, gg_dataset)
    print(f"  trained in {time.time()-t0:.1f}s")
    results["golden_gate_vs_normal"] = run_vector(
        model, tokenizer, "golden_gate_vs_normal", gg_vector, test_prompts, coeffs, gen_kwargs
    )

    Path("reference-results.json").write_text(json.dumps(results, indent=2))
    print("\nWrote reference-results.json")


if __name__ == "__main__":
    main()
