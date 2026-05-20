"""Test 1 (H1): Gemma Scope SAE loads + reconstruction error sanity.

Approach: load gemma-2-9b-it via raw HuggingFace (NOT TransformerLens —
TL's wrapper consumes ~23GB of the 24GB 3090Ti, leaving no room for SAE
forward + generation). Register a forward hook on the residual stream
at layer 20 to capture activations. Load Gemma Scope SAE for that layer.
Run a short forward pass, encode + decode through SAE, compute MSE and
fraction of variance unexplained.

Positive control: pre-published Gemma Scope reconstruction quality for
layer 20 width 16k canonical SAE — should hit roughly 80-90% variance
explained on natural-language inputs.
"""

import json
import time
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sae_lens import SAE

MODEL_PATH = "../models/gemma-2-9b-it"
SAE_RELEASE = "gemma-scope-9b-it-res-canonical"
SAE_ID = "layer_20/width_16k/canonical"
HOOK_LAYER = 20  # SAE is on residual stream post-block-20

PROMPT = "The Golden Gate Bridge spans the entrance to San Francisco Bay."

OUT_PATH = Path("test1-recon-error.json")


def main():
    device = "cuda"
    print(f"GPU free start: {torch.cuda.mem_get_info()[0] / 1e9:.2f} GB")

    t0 = time.time()
    print(f"loading {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map=device, attn_implementation="eager"
    )
    model.eval()
    t_model = time.time() - t0
    print(f"model loaded in {t_model:.1f}s")
    print(f"  n_layers={model.config.num_hidden_layers}, hidden={model.config.hidden_size}")
    print(f"GPU free after model: {torch.cuda.mem_get_info()[0] / 1e9:.2f} GB")

    t0 = time.time()
    print(f"loading SAE: {SAE_RELEASE} / {SAE_ID}")
    sae = SAE.from_pretrained(
        release=SAE_RELEASE, sae_id=SAE_ID, device=device,
    )
    sae = sae.to(torch.bfloat16)
    sae.eval()
    t_sae = time.time() - t0
    sae_hook_name = sae.cfg.metadata["hook_name"]
    print(f"SAE loaded in {t_sae:.1f}s")
    print(f"  hook={sae_hook_name}, d_in={sae.cfg.d_in}, d_sae={sae.cfg.d_sae}")
    print(f"GPU free after SAE: {torch.cuda.mem_get_info()[0] / 1e9:.2f} GB")

    # Capture residual stream at layer HOOK_LAYER's output.
    # In Gemma-2 HF model: model.model.layers[i] is each decoder block.
    # The residual stream "after block i" = output of block i.
    captured = {}

    def hook_fn(module, inputs, outputs):
        # outputs is (hidden_states, ...) for a decoder block
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs
        captured["acts"] = hidden.detach()

    handle = model.model.layers[HOOK_LAYER].register_forward_hook(hook_fn)

    tokens = tokenizer(PROMPT, return_tensors="pt").to(device)
    print(f"prompt tokens: {tokens.input_ids.shape}")

    with torch.no_grad():
        model(**tokens)

    handle.remove()
    activations = captured["acts"]
    print(f"captured activations: {activations.shape}, dtype={activations.dtype}")

    with torch.no_grad():
        acts_bf16 = activations.to(sae.dtype)
        feature_acts = sae.encode(acts_bf16)
        reconstructed = sae.decode(feature_acts)

    # Gemma-2 BOS token is an attention sink with massive activation norm
    # (~4000) that SAEs don't reconstruct well. Standard practice (Gemma Scope
    # demo, Neuronpedia) is to exclude BOS from reconstruction metrics — we
    # keep BOS in the forward pass (model expects it) but exclude position 0.
    diff_all = (acts_bf16 - reconstructed).float()
    orig_f = activations.float()
    mse_all = (diff_all ** 2).mean().item()
    orig_norm_sq_all = (orig_f ** 2).mean().item()
    fvu_all = mse_all / orig_norm_sq_all

    diff_no_bos = diff_all[:, 1:]
    orig_no_bos = orig_f[:, 1:]
    mse = (diff_no_bos ** 2).mean().item()
    orig_norm_sq = (orig_no_bos ** 2).mean().item()
    fvu = mse / orig_norm_sq
    variance_explained = 1.0 - fvu
    nonzero_per_token = (feature_acts[:, 1:] != 0).float().sum(dim=-1).mean().item()

    out = {
        "model": MODEL_PATH,
        "sae_release": SAE_RELEASE,
        "sae_id": SAE_ID,
        "hook_layer": HOOK_LAYER,
        "sae_hook_name": sae_hook_name,
        "neuronpedia_id": sae.cfg.metadata.get("neuronpedia_id"),
        "prompt": PROMPT,
        "n_tokens": int(tokens.input_ids.shape[-1]),
        "model_load_s": round(t_model, 2),
        "sae_load_s": round(t_sae, 2),
        "mse_excl_bos": mse,
        "orig_mean_sq_norm_excl_bos": orig_norm_sq,
        "fraction_variance_unexplained_excl_bos": fvu,
        "variance_explained_excl_bos": variance_explained,
        "fraction_variance_unexplained_all_pos": fvu_all,
        "mean_nonzero_features_per_token_excl_bos": nonzero_per_token,
        "sae_d_in": int(sae.cfg.d_in),
        "sae_d_sae": int(sae.cfg.d_sae),
    }

    print("\n=== reconstruction metrics ===")
    for k, v in out.items():
        print(f"  {k}: {v}")

    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
