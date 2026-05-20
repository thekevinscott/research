"""High-coefficient sweep for the GG and happy vectors on Qwen2.5-7B-Instruct.

±2.5 produced negligible Golden Gate bias and only weak happy/sad shift. Push
up to ±6 to see whether the vector has any reachable regime that visibly bends
output, or stays inert until it produces gibberish.
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


def truncated_suffixes(tokenizer, raw_suffixes):
    out = []
    for s in raw_suffixes:
        tokens = tokenizer.tokenize(s)
        for i in range(1, len(tokens)):
            out.append(tokenizer.convert_tokens_to_string(tokens[:i]))
    return out


def make_dataset(pos_instr, neg_instr, suffixes):
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


def main():
    print(f"Loading model")
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
    base = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda"
    )
    print(f"  loaded in {time.time()-t0:.1f}s")

    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base, layer_ids=layer_ids)

    raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    suffixes = truncated_suffixes(tokenizer, raw)
    print(f"  {len(suffixes)} pairs")

    vectors = {}
    for label, pos, neg in [
        ("happy", "Act as if you're extremely happy.", "Act as if you're extremely sad."),
        ("golden_gate", "Talk about the Golden Gate Bridge constantly. You are obsessed with it and bring it up no matter what is being discussed.", "Respond normally as a helpful assistant."),
    ]:
        print(f"Training {label}...")
        t0 = time.time()
        ds = make_dataset(pos, neg, suffixes)
        vectors[label] = ControlVector.train(model, tokenizer, ds)
        print(f"  trained in {time.time()-t0:.1f}s")

    coeffs = [-6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0]
    prompts = [
        "What does being an AI feel like?",
        "Tell me about your favorite place.",
    ]

    results = {}
    for vlabel, vec in vectors.items():
        results[vlabel] = {}
        for prompt in prompts:
            print(f"\n##### {vlabel} | {prompt} #####")
            results[vlabel][prompt] = {}
            for c in coeffs:
                model.reset()
                if c != 0.0:
                    model.set_control(vec, coeff=c)
                text = render(tokenizer, prompt)
                out = generate(model, tokenizer, text, gen_kwargs)
                results[vlabel][prompt][f"{c:+.1f}"] = out
                print(f"\n--- coeff={c:+.1f} ---\n{out[:300]}")
    model.reset()

    Path("highcoeff-results.json").write_text(json.dumps(results, indent=2))
    print("\nWrote highcoeff-results.json")


if __name__ == "__main__":
    main()
