"""Rank candidate GG features by per-feature max activation across the GG
corpus (vs the contrast-of-means approach used in test2). A concept feature
will fire HARD on the specific tokens that name the concept, so max-act
should surface it better than mean-act when the concept appears in only a
few tokens per sentence.

Also includes very targeted "GG vs other landmark" sentences to filter out
generic-bridge / generic-SF / infrastructure features.
"""

import json
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from sae_lens import SAE

MODEL_PATH = "../models/gemma-2-9b-it"
SAE_RELEASE = "gemma-scope-9b-it-res-canonical"
SAE_ID = "layer_20/width_16k/canonical"
HOOK_LAYER = 20

# Sentences that should activate THE Golden Gate Bridge concept feature
# strongly. Each pair varies one detail to surface the GG-specific feature.
GG_PROBES = [
    "The Golden Gate Bridge is an iconic suspension bridge in San Francisco.",
    "I crossed the Golden Gate Bridge yesterday.",
    "Standing on the Golden Gate Bridge, you can see Alcatraz.",
    "The Golden Gate Bridge opened to the public in 1937.",
    "Photographers love the Golden Gate Bridge at dawn.",
]

# Same templates, different landmarks — to rule out generic-bridge / generic-SF
CONTROL_PROBES = [
    "The Brooklyn Bridge is an iconic suspension bridge in New York.",
    "I crossed the Brooklyn Bridge yesterday.",
    "Standing on the Brooklyn Bridge, you can see Manhattan.",
    "The Brooklyn Bridge opened to the public in 1883.",
    "Photographers love the Brooklyn Bridge at dawn.",
    "The Eiffel Tower is an iconic landmark in Paris.",
    "I visited the Eiffel Tower yesterday.",
    "Standing on the Eiffel Tower, you can see all of Paris.",
    "The Eiffel Tower opened to the public in 1889.",
    "Photographers love the Eiffel Tower at sunset.",
    "Lombard Street is a famous winding road in San Francisco.",
    "Alcatraz Island sits in San Francisco Bay.",
    "The cable cars of San Francisco climb steep hills.",
]


def encode_one(model, tokenizer, sae, sent):
    """Return [seq-1, d_sae] feature acts (BOS dropped) and token strs."""
    device = next(model.parameters()).device
    captured = {}

    def hook_fn(module, inputs, outputs):
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs
        captured["acts"] = hidden.detach()

    h = model.model.layers[HOOK_LAYER].register_forward_hook(hook_fn)
    enc = tokenizer(sent, return_tensors="pt").to(device)
    tokens = tokenizer.convert_ids_to_tokens(enc.input_ids[0])
    with torch.no_grad():
        model(**enc)
    h.remove()
    acts = captured["acts"]
    with torch.no_grad():
        feats = sae.encode(acts.to(sae.dtype))
    return feats[:, 1:, :].squeeze(0).float().cpu(), tokens[1:]


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

    # For each sentence, encode and track per-feature max activation.
    print("\nencoding GG probes...")
    gg_max = torch.zeros(sae.cfg.d_sae)
    gg_max_tok = [None] * sae.cfg.d_sae
    for sent in GG_PROBES:
        feats, toks = encode_one(model, tokenizer, sae, sent)
        # feats: [seq, d_sae]
        per_feat_max, per_feat_argmax = feats.max(dim=0)
        beat = per_feat_max > gg_max
        gg_max = torch.where(beat, per_feat_max, gg_max)
        # Update tokens for features that beat their old max.
        beat_idx = torch.where(beat)[0].tolist()
        for fi in beat_idx:
            gg_max_tok[fi] = toks[per_feat_argmax[fi].item()] + f" / {sent[:40]!r}"

    print("encoding CONTROL probes...")
    ctrl_max = torch.zeros(sae.cfg.d_sae)
    for sent in CONTROL_PROBES:
        feats, toks = encode_one(model, tokenizer, sae, sent)
        per_feat_max, _ = feats.max(dim=0)
        ctrl_max = torch.maximum(ctrl_max, per_feat_max)

    # Specificity: feature must fire on GG probes AND not on controls.
    score = gg_max - ctrl_max
    # Restrict to features with non-trivial GG max (avoid noise floor).
    score = torch.where(gg_max > 5.0, score, torch.full_like(score, -1e9))
    top_idxs = score.topk(20).indices.tolist()

    print(f"\nTop 20 features by (max in GG probes) - (max in CONTROL probes):")
    out_list = []
    for idx in top_idxs:
        rec = {
            "idx": idx,
            "gg_max": float(gg_max[idx]),
            "ctrl_max": float(ctrl_max[idx]),
            "score": float(score[idx]),
            "gg_max_token": gg_max_tok[idx],
        }
        out_list.append(rec)
        print(f"  idx={idx:6d} gg_max={rec['gg_max']:7.2f} "
              f"ctrl_max={rec['ctrl_max']:6.2f} score={rec['score']:7.2f}"
              f" @ {rec['gg_max_token']}")

    Path("test2-feature-search-v2.json").write_text(json.dumps({
        "release": SAE_RELEASE,
        "sae_id": SAE_ID,
        "method": "max-activation contrast on GG vs landmark/SF controls",
        "top_features": out_list,
    }, indent=2))


if __name__ == "__main__":
    main()
