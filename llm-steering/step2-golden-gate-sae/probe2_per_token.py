"""Per-token reconstruction breakdown — does BOS or some outlier-token
dominate the FVU, or is the SAE broken on every token?

Also try a longer context to see if Pile-pretrained SAE reconstructs
pretraining-style text better than chat-style text.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sae_lens import SAE

MODEL_PATH = "../models/gemma-2-9b-it"
SAE_RELEASE = "gemma-scope-9b-it-res-canonical"
SAE_ID = "layer_20/width_16k/canonical"
HOOK_LAYER = 20

# Three test inputs:
#   - short prompt (what test 1 used)
#   - longer pretraining-style sentence
#   - just text without BOS
PROMPTS = [
    ("test1 prompt", "The Golden Gate Bridge spans the entrance to San Francisco Bay."),
    ("longer pretraining-y", (
        "The Roman Empire was the post-Republican period of ancient Rome. "
        "As a polity, it included large territorial holdings around the "
        "Mediterranean Sea in Europe, North Africa, and Western Asia, "
        "ruled by emperors. From the accession of Caesar Augustus to the "
        "military anarchy of the third century, it was a principate with "
        "Italy as the metropole of its provinces."
    )),
]


def run_one(model, tokenizer, sae, label, text, prepend_bos=True):
    device = next(model.parameters()).device
    add_special = prepend_bos
    enc = tokenizer(text, return_tensors="pt", add_special_tokens=add_special).to(device)
    tokens = enc.input_ids
    token_strs = tokenizer.convert_ids_to_tokens(tokens[0])

    captured = {}

    def hook_fn(module, inputs, outputs):
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs
        captured["acts"] = hidden.detach()

    h = model.model.layers[HOOK_LAYER].register_forward_hook(hook_fn)
    with torch.no_grad():
        model(**enc)
    h.remove()
    acts = captured["acts"]  # [1, seq, d_in]
    acts_b = acts.to(sae.dtype)

    with torch.no_grad():
        feature_acts = sae.encode(acts_b)
        recon = sae.decode(feature_acts)

    orig_f = acts.float()
    recon_f = recon.float()
    diff = recon_f - orig_f

    per_tok_orig_var = (orig_f ** 2).sum(dim=-1).squeeze(0)
    per_tok_err = (diff ** 2).sum(dim=-1).squeeze(0)
    per_tok_fvu = per_tok_err / per_tok_orig_var
    per_tok_l0 = (feature_acts != 0).float().sum(dim=-1).squeeze(0)
    per_tok_norm = orig_f.norm(dim=-1).squeeze(0)

    print(f"\n=== {label} (prepend_bos={prepend_bos}) ===")
    print(f"  seq_len={tokens.shape[1]}")
    print(f"  agg FVU (excluding pos 0): "
          f"{per_tok_err[1:].sum().item() / per_tok_orig_var[1:].sum().item():.4f}")
    print(f"  agg FVU (all positions): "
          f"{per_tok_err.sum().item() / per_tok_orig_var.sum().item():.4f}")
    print(f"  per-token breakdown (first 5 + worst 3):")
    for i in range(min(5, tokens.shape[1])):
        print(f"    [{i:3d}] tok={token_strs[i]!r:15s} "
              f"norm={per_tok_norm[i].item():8.2f} "
              f"L0={per_tok_l0[i].item():5.0f} "
              f"fvu={per_tok_fvu[i].item():.4f}")
    worst = per_tok_fvu.argsort(descending=True)[:3]
    print(f"  worst tokens:")
    for i in worst.tolist():
        print(f"    [{i:3d}] tok={token_strs[i]!r:15s} "
              f"norm={per_tok_norm[i].item():8.2f} "
              f"L0={per_tok_l0[i].item():5.0f} "
              f"fvu={per_tok_fvu[i].item():.4f}")


def main():
    device = "cuda"
    print("loading SAE...")
    sae = SAE.from_pretrained(release=SAE_RELEASE, sae_id=SAE_ID, device=device)
    sae = sae.to(torch.bfloat16)
    sae.eval()

    print("loading model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16, device_map=device,
        attn_implementation="eager",
    )
    model.eval()

    for label, text in PROMPTS:
        run_one(model, tokenizer, sae, label, text, prepend_bos=True)
    # Also without BOS
    run_one(model, tokenizer, sae, "test1 prompt, no BOS",
            PROMPTS[0][1], prepend_bos=False)


if __name__ == "__main__":
    main()
