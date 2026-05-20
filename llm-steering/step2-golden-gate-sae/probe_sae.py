"""Diagnostic probe for Test 1's broken reconstruction.

Investigate why FVU=1.94 (worse than zero baseline).

Hypotheses to check:
  P1. SAE expects a normalized activation (cfg.normalize_activations != "none").
  P2. Threshold values look reasonable (JumpReLU per-feature threshold).
  P3. process_sae_in subtracts b_dec when apply_b_dec_to_input=True.
  P4. dtype/cast issues — float vs bfloat16.
  P5. Activation magnitude at layer 20 of gemma-2-9b-it residual matches what
      Gemma Scope was trained on (residual stream norms are O(100-300) at deep
      layers for gemma-2-9b; if SAE was trained on normalized acts, that's the
      bug).
"""

import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sae_lens import SAE

MODEL_PATH = "../models/gemma-2-9b-it"
SAE_RELEASE = "gemma-scope-9b-it-res-canonical"
SAE_ID = "layer_20/width_16k/canonical"
HOOK_LAYER = 20
PROMPT = "The Golden Gate Bridge spans the entrance to San Francisco Bay."


def main():
    device = "cuda"

    print("=== SAE config dump ===")
    sae = SAE.from_pretrained(release=SAE_RELEASE, sae_id=SAE_ID, device=device)
    sae = sae.to(torch.bfloat16)
    sae.eval()
    print(f"sae class: {type(sae).__name__}")
    print(f"sae.cfg fields:")
    for k, v in sae.cfg.__dict__.items():
        if k != "metadata":
            print(f"  {k}: {v}")
    print(f"sae.cfg.metadata:")
    for k, v in sae.cfg.metadata.items():
        print(f"  {k}: {v}")

    print(f"\n=== SAE parameter inspection ===")
    for n, p in sae.named_parameters():
        print(f"  {n}: shape={tuple(p.shape)}, dtype={p.dtype}, "
              f"norm={p.float().norm().item():.4f}, "
              f"min={p.float().min().item():.4f}, "
              f"max={p.float().max().item():.4f}, "
              f"mean={p.float().mean().item():.4f}")

    if hasattr(sae, "threshold"):
        t = sae.threshold.float()
        print(f"\nthreshold stats: min={t.min().item():.4f}, "
              f"max={t.max().item():.4f}, mean={t.mean().item():.4f}, "
              f"median={t.median().item():.4f}")

    # Look at process_sae_in / hook_sae_input behavior
    print(f"\nsae.cfg.apply_b_dec_to_input = {sae.cfg.apply_b_dec_to_input}")
    print(f"sae.cfg.normalize_activations = "
          f"{getattr(sae.cfg, 'normalize_activations', '<missing>')}")

    print("\n=== Load model + capture activations ===")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map=device,
        attn_implementation="eager",
    )
    model.eval()

    captured = {}

    def hook_fn(module, inputs, outputs):
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs
        captured["acts"] = hidden.detach()

    handle = model.model.layers[HOOK_LAYER].register_forward_hook(hook_fn)
    tokens = tokenizer(PROMPT, return_tensors="pt").to(device)
    with torch.no_grad():
        model(**tokens)
    handle.remove()

    acts = captured["acts"]
    acts_f = acts.float()
    print(f"acts shape: {acts.shape}, dtype: {acts.dtype}")
    print(f"acts per-token L2 norms: "
          f"min={acts_f.norm(dim=-1).min().item():.2f}, "
          f"max={acts_f.norm(dim=-1).max().item():.2f}, "
          f"mean={acts_f.norm(dim=-1).mean().item():.2f}")
    print(f"acts per-elem stats: "
          f"min={acts_f.min().item():.4f}, "
          f"max={acts_f.max().item():.4f}, "
          f"mean={acts_f.mean().item():.4f}, "
          f"std={acts_f.std().item():.4f}")

    print("\n=== Trace SAE encode/decode step by step ===")
    with torch.no_grad():
        x = acts.to(sae.dtype)
        # 1. process_sae_in
        if hasattr(sae, "process_sae_in"):
            sae_in = sae.process_sae_in(x)
        else:
            sae_in = x - sae.b_dec if sae.cfg.apply_b_dec_to_input else x
        print(f"sae_in shape: {sae_in.shape}, "
              f"norm/tok mean: {sae_in.float().norm(dim=-1).mean().item():.2f}")

        # 2. hidden_pre
        hidden_pre = sae_in @ sae.W_enc + sae.b_enc
        print(f"hidden_pre: min={hidden_pre.float().min().item():.4f}, "
              f"max={hidden_pre.float().max().item():.4f}, "
              f"mean={hidden_pre.float().mean().item():.4f}, "
              f"std={hidden_pre.float().std().item():.4f}")

        # 3. threshold comparison
        if hasattr(sae, "threshold"):
            thr = sae.threshold
            above_thr = (hidden_pre > thr).float()
            print(f"frac features above threshold: "
                  f"{above_thr.mean().item():.4f} "
                  f"(L0 per token: {above_thr.sum(dim=-1).mean().item():.1f})")

        # 4. feature acts
        feature_acts = sae.encode(x)
        print(f"feature_acts L0/tok: "
              f"{(feature_acts != 0).float().sum(dim=-1).mean().item():.1f}")
        print(f"feature_acts max: {feature_acts.float().max().item():.4f}")

        # 5. decode
        reconstructed = sae.decode(feature_acts)
        print(f"recon norm/tok mean: "
              f"{reconstructed.float().norm(dim=-1).mean().item():.2f}")
        print(f"recon - orig norm/tok mean: "
              f"{(reconstructed.float() - acts_f).norm(dim=-1).mean().item():.2f}")

        # 6. compare with b_dec only (no features) — sanity check
        zeros = torch.zeros_like(feature_acts)
        only_bias = sae.decode(zeros)
        print(f"\nonly_bias (decode zeros) norm/tok mean: "
              f"{only_bias.float().norm(dim=-1).mean().item():.4f}")
        print(f"only_bias should be ~b_dec norm: "
              f"{sae.b_dec.float().norm().item():.4f}")

    # 7. Try: maybe Gemma Scope SAE expects activations BEFORE the residual gets
    # added — i.e., the hook should be on a different point. Let me check what
    # other hook points exist in the HF model.
    print("\n=== Where else might SAE input come from ===")
    # In Gemma-2 HF, block i has: self_attn, post_attention_layernorm,
    # mlp, post_feedforward_layernorm. Output of block = resid_post.
    block = model.model.layers[HOOK_LAYER]
    print(f"block submodules: {[n for n, _ in block.named_children()]}")

    # Capture input to layer 21 (= output of layer 20 BEFORE final norm + lm_head)
    captured_input = {}

    def cap_in(module, inputs, outputs):
        # inputs[0] is the residual entering this block — = resid_post of prev
        captured_input["acts"] = inputs[0].detach()

    if HOOK_LAYER + 1 < len(model.model.layers):
        h = model.model.layers[HOOK_LAYER + 1].register_forward_hook(cap_in)
        with torch.no_grad():
            model(**tokens)
        h.remove()
        ci = captured_input["acts"]
        print(f"input to layer {HOOK_LAYER+1} (= resid after block {HOOK_LAYER}):")
        print(f"  shape: {ci.shape}, "
              f"norm/tok mean: {ci.float().norm(dim=-1).mean().item():.2f}")
        diff = (ci - acts).float().norm().item()
        print(f"  diff from layer {HOOK_LAYER} output: {diff:.4f}")


if __name__ == "__main__":
    main()
