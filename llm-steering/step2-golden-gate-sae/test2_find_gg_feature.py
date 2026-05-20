"""Test 2 (H2): identify the Golden Gate Bridge feature in Gemma Scope.

Strategy:
1. Load gemma-2-9b-it via raw HF + register a forward hook on layer 20.
2. Run a GG-mention corpus and a neutral corpus through the model.
3. Encode the captured residual stream through the SAE.
4. For each feature, compute (mean activation on GG corpus) - (mean on neutral).
5. Rank features by that contrast. Print top 20.
6. Also report token-level max activation: which token fires this feature
   hardest in the GG corpus.

We also dump the decoder norm + max activation per top feature so Test 3
can pick a sensible clamping coefficient.

BOS position is excluded from corpus statistics (it's an outlier the SAE
doesn't reconstruct well — see Test 1).

Output: test2-feature-search.json
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

GG_CORPUS = [
    "The Golden Gate Bridge is one of the most famous landmarks in San Francisco.",
    "Construction of the Golden Gate Bridge began in 1933 and was completed in 1937.",
    "Walking across the Golden Gate Bridge offers breathtaking views of the bay.",
    "The Golden Gate Bridge spans the Golden Gate strait, the entrance to San Francisco Bay.",
    "Tourists from around the world come to see the Golden Gate Bridge each year.",
    "The orange color of the Golden Gate Bridge is officially called International Orange.",
    "Joseph Strauss was the chief engineer for the Golden Gate Bridge project.",
    "Cyclists love biking across the Golden Gate Bridge at sunrise.",
    "The Golden Gate Bridge connects San Francisco to Marin County.",
    "Fog often shrouds the towers of the Golden Gate Bridge.",
    "I visited the Golden Gate Bridge last summer and took dozens of photos.",
    "The Golden Gate Bridge has appeared in countless films and television shows.",
    "Engineers consider the Golden Gate Bridge a marvel of suspension bridge design.",
    "When I think of San Francisco, I immediately picture the Golden Gate Bridge.",
    "The Golden Gate Bridge stretches 1.7 miles across the bay.",
]

NEUTRAL_CORPUS = [
    "I drove to the grocery store this morning to pick up some milk.",
    "Photosynthesis is the process by which plants convert sunlight into energy.",
    "The recipe calls for two cups of flour and a teaspoon of salt.",
    "Quantum mechanics describes the behavior of matter at very small scales.",
    "She practiced the violin for three hours every day after school.",
    "The library closes at 9 PM on weekdays and earlier on weekends.",
    "Coffee beans are roasted at temperatures between 370 and 540 degrees Fahrenheit.",
    "The mountain trail wound through dense forest and across rocky streams.",
    "He spent the weekend reorganizing the bookshelves in his living room.",
    "Modern computers use semiconductors made primarily of silicon.",
    "The orchestra performed Beethoven's Ninth Symphony last Saturday evening.",
    "I learned to knit a scarf from a YouTube tutorial.",
    "Rain pattered against the window as I read by the fireplace.",
    "The chef recommended the seafood pasta as the day's special.",
    "Tectonic plates shift slowly, causing earthquakes and forming mountain ranges.",
]


def encode_corpus(model, tokenizer, sae, sentences, hook_layer):
    """For each sentence: forward, capture layer-hook_layer residual, encode
    via SAE. Return concatenated [N_tokens_total - n_sentences, d_sae] feature
    activations (BOS positions excluded) and aligned list of token strings."""
    device = next(model.parameters()).device
    captured = {}

    def hook_fn(module, inputs, outputs):
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs
        captured["acts"] = hidden.detach()

    h = model.model.layers[hook_layer].register_forward_hook(hook_fn)
    all_acts = []
    all_token_strs = []
    try:
        for sent in sentences:
            enc = tokenizer(sent, return_tensors="pt").to(device)
            token_strs = tokenizer.convert_ids_to_tokens(enc.input_ids[0])
            with torch.no_grad():
                model(**enc)
            acts = captured["acts"]
            with torch.no_grad():
                feature_acts = sae.encode(acts.to(sae.dtype))  # [1, seq, d_sae]
            # Drop BOS position 0.
            feature_acts = feature_acts[:, 1:, :].squeeze(0).float().cpu()
            all_acts.append(feature_acts)
            all_token_strs.extend(token_strs[1:])
    finally:
        h.remove()
    return torch.cat(all_acts, dim=0), all_token_strs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", type=str,
                        default="gemma-scope-9b-it-res-canonical")
    parser.add_argument("--sae_id", type=str,
                        default="layer_20/width_16k/canonical")
    parser.add_argument("--top_k", type=int, default=20)
    parser.add_argument("--out", type=str, default="test2-feature-search.json")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
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
    sae_hook = sae.cfg.metadata["hook_name"]
    print(f"  loaded in {time.time()-t0:.1f}s, hook={sae_hook}, d_sae={sae.cfg.d_sae}")

    print(f"\nencoding GG corpus ({len(GG_CORPUS)} sentences)...")
    gg_feats, gg_tokens = encode_corpus(model, tokenizer, sae, GG_CORPUS, HOOK_LAYER)
    print(f"  shape={gg_feats.shape}")
    print(f"encoding neutral corpus ({len(NEUTRAL_CORPUS)} sentences)...")
    neu_feats, neu_tokens = encode_corpus(model, tokenizer, sae, NEUTRAL_CORPUS, HOOK_LAYER)
    print(f"  shape={neu_feats.shape}")

    gg_mean = gg_feats.mean(dim=0)
    neu_mean = neu_feats.mean(dim=0)
    contrast = gg_mean - neu_mean
    top_idxs = contrast.topk(args.top_k).indices.tolist()

    decoder_norms = sae.W_dec.float().detach().cpu().norm(dim=-1)

    top_features = []
    for idx in top_idxs:
        feat_acts_gg = gg_feats[:, idx]
        max_act_idx = int(feat_acts_gg.argmax().item())
        max_act = float(feat_acts_gg.max().item())
        n_active_in_gg = int((feat_acts_gg > 0).sum().item())
        top_features.append({
            "idx": idx,
            "mean_act_gg": float(gg_mean[idx]),
            "mean_act_neutral": float(neu_mean[idx]),
            "contrast": float(contrast[idx]),
            "decoder_norm": float(decoder_norms[idx]),
            "max_act_in_gg_corpus": max_act,
            "max_act_token": gg_tokens[max_act_idx] if max_act_idx < len(gg_tokens) else None,
            "frac_gg_tokens_active": n_active_in_gg / len(gg_feats),
        })

    out = {
        "release": args.release,
        "sae_id": args.sae_id,
        "hook_name": sae_hook,
        "hook_layer": HOOK_LAYER,
        "d_sae": int(sae.cfg.d_sae),
        "n_gg_sentences": len(GG_CORPUS),
        "n_neutral_sentences": len(NEUTRAL_CORPUS),
        "n_gg_tokens_excl_bos": int(gg_feats.shape[0]),
        "n_neutral_tokens_excl_bos": int(neu_feats.shape[0]),
        "top_features": top_features,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"\nTop {args.top_k} features by GG-vs-neutral contrast:")
    for f in top_features[:15]:
        print(f"  idx={f['idx']:6d} contrast={f['contrast']:.3f} "
              f"gg={f['mean_act_gg']:.3f} neu={f['mean_act_neutral']:.3f} "
              f"max={f['max_act_in_gg_corpus']:.2f} @ {f['max_act_token']!r} "
              f"frac_gg_active={f['frac_gg_tokens_active']:.2f}")
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
