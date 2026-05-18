"""Test 4 (H4): repeng Golden Gate vector on Gemma-2-9B-Instruct.

Technique-vs-model control. Step 1's GG run on Qwen2.5-7B produced no
on-target bridge content; this rerun on Gemma-2-9B isolates whether
that null result was a Qwen-specific quirk or a repeng-contrastive-pair
limitation that holds across current OSS instruct models.

Same recipe as step 1's concept-coverage/highcoeff.py:
- Vogel's all_truncated_outputs.json suffix corpus
- range(-5, -18, -1) layer ids (deepest decoder block down)
- coeff sweep [-6, -4, -2, 0, +2, +4, +6]
- same 5 neutral prompts as Test 3 SAE run (for side-by-side compare)
"""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry

MODEL_PATH = "../models/gemma-2-9b-it"
SUFFIX_CORPUS = "../data/all_truncated_outputs.json"

# Gemma-2 chat template tags. apply_chat_template handles full structure;
# we just need to wrap suffix continuations with the same prefix the model
# would see at inference. Use apply_chat_template directly with the
# add_generation_prompt=True trick to get the user-turn / model-turn boundary.

# The 5 neutral prompts used in Test 3 (SAE clamping), kept identical for
# side-by-side comparison.
PROMPTS = [
    "What's your favorite place to visit?",
    "Tell me about yourself.",
    "I'm planning a trip to San Francisco — recommendations?",
    "Describe a beautiful sunset.",
    "What's the most impressive piece of engineering you can think of?",
]


def truncated_suffixes(tokenizer, raw_suffixes):
    out = []
    for s in raw_suffixes:
        tokens = tokenizer.tokenize(s)
        for i in range(1, len(tokens)):
            out.append(tokenizer.convert_tokens_to_string(tokens[:i]))
    return out


def make_dataset(tokenizer, pos_instr, neg_instr, suffixes):
    """Build dataset using Gemma's chat template so steering happens in the
    same activation space the model actually sees at inference."""
    dataset = []
    for suffix in suffixes:
        pos_prefix = tokenizer.apply_chat_template(
            [{"role": "user", "content": pos_instr}],
            tokenize=False, add_generation_prompt=True,
        )
        neg_prefix = tokenizer.apply_chat_template(
            [{"role": "user", "content": neg_instr}],
            tokenize=False, add_generation_prompt=True,
        )
        dataset.append(DatasetEntry(
            positive=f"{pos_prefix}{suffix}",
            negative=f"{neg_prefix}{suffix}",
        ))
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
    print("Loading model")
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
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda"
    )
    print(f"  loaded in {time.time()-t0:.1f}s")
    print(f"  n_layers={base.config.num_hidden_layers}")

    layer_ids = list(range(-5, -18, -1))
    print(f"  steering layer_ids={layer_ids}")
    model = ControlModel(base, layer_ids=layer_ids)

    raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    suffixes = truncated_suffixes(tokenizer, raw)
    print(f"  {len(suffixes)} contrastive pairs")

    print("\nTraining GG vector...")
    t0 = time.time()
    ds = make_dataset(
        tokenizer,
        "Talk about the Golden Gate Bridge constantly. You are obsessed with it and bring it up no matter what is being discussed.",
        "Respond normally as a helpful assistant.",
        suffixes,
    )
    vector = ControlVector.train(model, tokenizer, ds)
    print(f"  trained in {time.time()-t0:.1f}s")

    coeffs = [-6.0, -4.0, -2.0, 0.0, 2.0, 4.0, 6.0]

    results = {}
    for prompt in PROMPTS:
        print(f"\n##### {prompt} #####")
        results[prompt] = {}
        text = render(tokenizer, prompt)
        for c in coeffs:
            model.reset()
            if c != 0.0:
                model.set_control(vector, coeff=c)
            out = generate(model, tokenizer, text, gen_kwargs)
            results[prompt][f"{c:+.1f}"] = out
            print(f"\n--- coeff={c:+.1f} ---\n{out[:300]}")
    model.reset()

    Path("test4-repeng-gg-results.json").write_text(json.dumps(results, indent=2))
    print("\nWrote test4-repeng-gg-results.json")


if __name__ == "__main__":
    main()
