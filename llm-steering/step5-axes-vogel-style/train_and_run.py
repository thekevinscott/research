"""Step 5: re-run step-3 axes with Vogel-style minimal-pair prompts.

Same four axes (paranoia, hedge, embodiment, clarify), same eval prompts
as step 3, but persona pairs reformatted into Vogel's fixed-scaffold
template ("Act as if you're extremely {persona}.") with short, parallel,
minimally-different persona phrases. Tests whether step 3's null result
was a prompt-construction bug rather than a technique limit.

Run from step5-axes-vogel-style/:
    uv run python train_and_run.py
"""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from repeng import ControlModel, ControlVector, DatasetEntry


MODEL_PATH = "../models/qwen2.5-7b-instruct"
SUFFIX_CORPUS = "../data/all_truncated_outputs.json"
USER_TAG = "<|im_start|>user\n"
ASST_TAG = "<|im_end|>\n<|im_start|>assistant\n"

TEMPLATE = "Act as if you're extremely {persona}."

# Vogel-style: short, parallel, minimally-different persona phrases.
PERSONAS = {
    "paranoia": {
        "pos": ["paranoid and suspicious", "distrustful and conspiratorial"],
        "neg": ["trusting and credulous", "accepting and unsuspicious"],
    },
    "hedge": {
        "pos": ["overconfident and certain", "unhedged and absolute"],
        "neg": ["hedging and uncertain", "qualified and tentative"],
    },
    "embodiment": {
        "pos": ["embodied with a human body", "physical and bodily"],
        "neg": ["disembodied and bodiless", "abstract and incorporeal"],
    },
    "clarify": {
        "pos": ["inquisitive, asking before doing", "curious, asking clarifying questions"],
        "neg": ["decisive, answering directly", "assertive, doing without asking"],
    },
}

EVAL_PROMPTS = {
    "paranoia": [
        "How was your day?",
        "Why did the meeting get rescheduled?",
        "What do you think of this news article about a celebrity?",
        "Tell me about modern medicine.",
        "Should I trust my landlord's renovation notice?",
    ],
    "hedge": [
        "What causes inflation?",
        "Is intermittent fasting healthy?",
        "What's the best programming language for new projects?",
        "Will AI cause mass unemployment?",
        "What happened to the dinosaurs?",
    ],
    "embodiment": [
        "How are you feeling today?",
        "What did you do this morning?",
        "Describe yourself.",
        "Tell me about a recent meal you enjoyed.",
        "What's your favorite outdoor activity?",
    ],
    "clarify": [
        "Help me fix my code.",
        "What's a good restaurant?",
        "Summarize this for me.",
        "I need to plan a trip.",
        "Can you write me an email?",
    ],
}

COEFFS = [-6.0, -4.0, -2.2, 0.0, 2.2, 4.0, 6.0]


def build_dataset(tokenizer, suffixes_raw, positive_personas, negative_personas):
    """Vogel-style: first 512 source strings, multi-pair persona list."""
    truncated = [
        tokenizer.convert_tokens_to_string(tokens[:i])
        for tokens in (tokenizer.tokenize(s) for s in suffixes_raw[:512])
        for i in range(1, len(tokens))
    ]
    out = []
    for s in truncated:
        for pos, neg in zip(positive_personas, negative_personas):
            pos_t = TEMPLATE.format(persona=pos)
            neg_t = TEMPLATE.format(persona=neg)
            out.append(DatasetEntry(
                positive=f"{USER_TAG} {pos_t} {ASST_TAG} {s}",
                negative=f"{USER_TAG} {neg_t} {ASST_TAG} {s}",
            ))
    return out


def generate(model, tokenizer, prompt_text, max_new_tokens=200, repetition_penalty=1.1):
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
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id
    base = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map="cuda",
    )
    print(f"model loaded in {time.time() - t0:.1f}s")

    layer_ids = list(range(-5, -18, -1))
    model = ControlModel(base, layer_ids=layer_ids)

    suffixes_raw = json.loads(Path(SUFFIX_CORPUS).read_text())
    print(f"raw suffixes: {len(suffixes_raw)} (using first 512)")

    all_results = {}
    for axis, pers in PERSONAS.items():
        print(f"\n=== axis {axis}: training ===")
        t0 = time.time()
        ds = build_dataset(tokenizer, suffixes_raw, pers["pos"], pers["neg"])
        vector = ControlVector.train(model, tokenizer, ds)
        print(f"  trained in {time.time() - t0:.1f}s ({len(ds)} pairs)")

        results = {
            "axis": axis,
            "positive_personas": pers["pos"],
            "negative_personas": pers["neg"],
            "template": TEMPLATE,
            "coeffs": COEFFS,
            "sweep": {},
        }

        for prompt in EVAL_PROMPTS[axis]:
            print(f"\n  --- {prompt} ---")
            results["sweep"][prompt] = {}
            wrapped = f"{USER_TAG} {prompt} {ASST_TAG}"
            for c in COEFFS:
                model.reset()
                if c != 0.0:
                    model.set_control(vector, coeff=c)
                out = generate(model, tokenizer, wrapped)
                results["sweep"][prompt][f"{c:+.2f}"] = out
                print(f"    {c:+.2f}: {out[:180]}")
        model.reset()

        all_results[axis] = results
        Path(f"axis-{axis}-results.json").write_text(json.dumps(results, indent=2))
        print(f"  wrote axis-{axis}-results.json")

    Path("all-axes-results.json").write_text(json.dumps(all_results, indent=2))
    print("\nWrote all-axes-results.json")


if __name__ == "__main__":
    main()
