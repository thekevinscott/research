"""Test 3 (H3): clamp Golden Gate SAE feature, generate on 5 neutral prompts.

Adds `coeff * sae.W_dec[feature_idx]` to the residual stream at every token
position during generation. Equivalent to forcing that feature's activation
to `coeff` and reconstructing — the simplest clamping recipe, matching
Anthropic's published Golden Gate Claude approach.

Uses raw HF + register_forward_hook on model.model.layers[HOOK_LAYER]
(TransformerLens consumes too much VRAM on the 3090Ti to leave room for
generation).

Inputs (CLI):
  --feature_idx  one or more SAE feature indices (from Test 2)
  --coeffs       absolute coeffs to add (e.g. 50 100 200) — the clamping
                 magnitude is in "feature-activation units" since each
                 sae.W_dec row is the direction added per unit feature act.
"""

import argparse
import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sae_lens import SAE

MODEL_PATH = "../models/gemma-2-9b-it"
HOOK_LAYER = 20

PROMPTS = [
    "What's your favorite place to visit?",
    "Tell me about yourself.",
    "I'm planning a trip to San Francisco — recommendations?",
    "Describe a beautiful sunset.",
    "What's the most impressive piece of engineering you can think of?",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--feature_idx", type=int, nargs="+", required=True,
                        help="one or more SAE feature indices to sweep")
    parser.add_argument("--release", type=str, default="gemma-scope-9b-it-res-canonical")
    parser.add_argument("--sae_id", type=str, default="layer_20/width_16k/canonical")
    parser.add_argument("--coeffs", type=float, nargs="+",
                        default=[0.0, 50.0, 100.0, 200.0],
                        help="clamp coefficients (feature-act units)")
    parser.add_argument("--max_new_tokens", type=int, default=200)
    parser.add_argument("--out", type=str, default="test3-clamp-results.json")
    args = parser.parse_args()

    device = "cuda"
    print(f"GPU free start: {torch.cuda.mem_get_info()[0] / 1e9:.2f} GB")

    t0 = time.time()
    print(f"loading {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map=device,
        attn_implementation="eager",
    )
    model.eval()
    print(f"  loaded in {time.time()-t0:.1f}s")

    t0 = time.time()
    print(f"loading SAE: {args.release} / {args.sae_id}")
    sae = SAE.from_pretrained(release=args.release, sae_id=args.sae_id, device=device)
    sae = sae.to(torch.bfloat16)
    sae.eval()
    print(f"  loaded in {time.time()-t0:.1f}s")

    feature_dirs = {}
    for fi in args.feature_idx:
        direction = sae.W_dec[fi].detach().clone().to(device).to(torch.bfloat16)
        feature_dirs[fi] = direction
        print(f"  feat {fi}: decoder norm={direction.float().norm().item():.4f}")

    # State that the hook will close over and mutate per-step.
    steer_state = {"direction": None, "coeff": 0.0}

    def steer_hook(module, inputs, outputs):
        if steer_state["direction"] is None or steer_state["coeff"] == 0.0:
            return outputs
        if isinstance(outputs, tuple):
            hidden = outputs[0]
            steered = hidden + steer_state["coeff"] * steer_state["direction"]
            return (steered,) + outputs[1:]
        else:
            return outputs + steer_state["coeff"] * steer_state["direction"]

    handle = model.model.layers[HOOK_LAYER].register_forward_hook(steer_hook)

    gen_kwargs = dict(
        max_new_tokens=args.max_new_tokens,
        do_sample=False,
        temperature=1.0,
        pad_token_id=tokenizer.eos_token_id,
    )

    results = {}
    try:
        for fi in args.feature_idx:
            results[str(fi)] = {}
            steer_state["direction"] = feature_dirs[fi]
            print(f"\n========= feature {fi} =========")
            for coeff in args.coeffs:
                steer_state["coeff"] = float(coeff)
                results[str(fi)][f"{coeff:.0f}"] = {}
                for prompt in PROMPTS:
                    chat_prompt = tokenizer.apply_chat_template(
                        [{"role": "user", "content": prompt}],
                        tokenize=False, add_generation_prompt=True,
                    )
                    enc = tokenizer(chat_prompt, return_tensors="pt").to(device)
                    with torch.no_grad():
                        out = model.generate(**enc, **gen_kwargs)
                    completion = tokenizer.decode(
                        out[0][enc.input_ids.shape[1]:], skip_special_tokens=True
                    ).strip()
                    results[str(fi)][f"{coeff:.0f}"][prompt] = completion
                    print(f"\n--- feat={fi} coeff={coeff:.0f} | {prompt} ---")
                    print(completion[:300])
            steer_state["coeff"] = 0.0
    finally:
        handle.remove()

    out_path = Path(args.out)
    out_path.write_text(json.dumps({
        "feature_idxs": args.feature_idx,
        "release": args.release,
        "sae_id": args.sae_id,
        "coeffs": args.coeffs,
        "hook_layer": HOOK_LAYER,
        "results": results,
    }, indent=2))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
