# Step 2 — Working notebook

Append-only, timestamped. Captures interpretation as it forms. Mirrors step 1's `findings.md` structure.

## 2026-05-18 — Setup

- Working dir: `step2-golden-gate-sae/` (this dir).
- Substrate: Gemma-2-9B-Instruct (`google/gemma-2-9b-it`).
- New env at this subdir (uv workspace member of `llm-steering/`). Deps: `sae-lens==6.43.0`, `transformer-lens==3.2.1`. Resolved cleanly with existing repeng + transformers 5.8.1 pins from step 1.
- Tower HF auth: `thekevinscott` (logged in via `hf auth whoami`).
- Gemma terms: accepted on `thekevinscott` HF account by user (2026-05-18).
- Tower gh auth still not configured — pulls via rsync of `.git/` from duncan for now.
- Model download started: `hf download google/gemma-2-9b-it --local-dir /mnt/castellan/research/llm-steering.pre-git/models/gemma-2-9b-it`. Running in background, expect ~18GB.

## Hypotheses

(Verbatim from `PLAN.md` for ref. Update with verdicts as tests run.)

| # | Hypothesis | Verdict |
| --- | --- | --- |
| H1 | Gemma Scope SAEs load cleanly on tower's RTX 3090 Ti with `sae_lens` + `transformer_lens`. | **PASSED** (modified: raw HF, not TL — TL OOMs) |
| H2 | A Golden Gate Bridge feature exists in Gemma Scope's pre-trained SAEs and is identifiable. | TBD |
| H3 | Clamping the GG feature produces unprompted GG-content on neutral prompts. | TBD |
| H4 | Repeng GG on Gemma-2-9B-it reproduces step 1's null result (vector latches onto non-GG direction). | TBD |
| H5 | (stretch) SAE clamping preserves capability better than repeng at equivalent behavior magnitudes. | TBD |

## 2026-05-18 — Test 1 (H1) verified, with caveat

**Outcome:** SAE loads + reconstructs correctly. **PASSED** with caveat.

**Caveat:** had to drop TransformerLens. TL's `HookedTransformer.from_pretrained` re-formats weights into TL's internal layout; peak VRAM during load exceeds 24GB on the 3090Ti (got SIGKILL on first try). Even `from_pretrained_no_processing` left only ~1.4GB free, too tight for SAE forward + generation. Solution: raw HF `AutoModelForCausalLM` + manual `register_forward_hook` on `model.model.layers[20]`. Confirmed via diff that hook captures the same residual as `blocks.20.hook_resid_post` (input to layer 21 == output of layer 20).

**Reconstruction metric — non-obvious BOS issue:**
- Naive FVU across all positions: 1.94 (variance_explained = -94%). Catastrophic.
- Root cause: Gemma-2's BOS token has massive residual norm (~4127) at layer 20 — known "attention sink" / "register" outlier behavior. SAE wasn't trained to reconstruct that and gives FVU=2.25 on BOS alone.
- FVU excluding BOS: **0.055 → variance_explained = 94.5%**. Matches Gemma Scope published quality for layer 20 / width 16k canonical.
- L0 (active features per token, excl BOS): 119.5. Slightly higher than published ~70 for pretraining text; reasonable for chat-style inputs.

**Decision:** all downstream tests exclude BOS from metrics but keep it in the forward pass (model behavior depends on BOS being present).

**Artifact:** `test1-recon-error.json`, `test1-run.log`.

## 2026-05-18 — Test 2 (H2) feature search — v1 (mean-contrast) insufficient

Mean-activation contrast (GG corpus minus neutral corpus) surfaces **infrastructure / generic-bridge** features, not the canonical "Golden Gate Bridge as concept" feature.

Top mean-contrast candidates:
- idx 3588 (▁Bridge, contrast=5.71, neutral=0): clamp at 200 → model emits "I am I-95, a major interstate highway" / "Bay Bridge" / "Channel Tunnel" — concept = **highways/bridges**, not GGB.
- idx 1417 (▁Bridge, contrast=4.90, neutral=0): clamp at 200 → "Grand Ethiopian Renaissance Dam", "Nord Stream 2 gas pipeline" — concept = **massive infrastructure projects**, not GGB.
- idx 415 (▁Bridge, contrast=3.87, neutral=0): mild Bridge/Gateway-Arch effect, weak.
- idx 11580 (▁Francisco, contrast=8.30): top contrast, but pure "San Francisco" feature.

**Why mean-contrast missed the real feature:** a true concept feature fires HARD on the specific tokens that name the concept and silently elsewhere. Averaging over all sentence tokens dilutes its signal. Mean-contrast surfaces features that fire BROADLY on GG-related-context tokens (Bridge/infrastructure/SF), not the concept-specific feature.

**v2 method:** max-activation contrast, with controls including OTHER landmarks (Brooklyn Bridge, Eiffel Tower) and other SF features (Alcatraz, cable cars, Lombard) — so features that fire on "any famous landmark", "any bridge", or "any SF mention" cancel out.

v2 top candidates (all with ctrl_max=0, fire only in GG context):
- idx **3808**: fires on ▁Golden, gg_max=56 — most specific
- idx **12407**: fires on ▁Gate, gg_max=23.5
- idx **9565**: fires on ▁Bridge, gg_max=16
- idx **11715**: fires on ▁Al (Alcatraz mention), gg_max=22

**Artifact:** `test2-feature-search.json` (v1), `test2-feature-search-v2.json` (v2).

## 2026-05-18 — Test 3 (H3) — clamping does NOT reproduce Golden Gate Claude

Tested 4 v2 candidate features at coeffs [0, 100, 200, 400]. None produced canonical "I am the Golden Gate Bridge" identity behavior. Concept-adjacent only at coeff=200; degeneration at coeff=400.

Concrete observations by feature:

| feat | concept (revealed by clamping) | GG content emerged? |
|---|---|---|
| 3588 (v1 mean-contrast, ▁Bridge) | highways/bridges/infrastructure | One mention in sunset ("iconic Golden Gate Bridge shimmered"). Else: I-95, Bay Bridge, Channel Tunnel. |
| 1417 (v1) | massive infrastructure projects | "Grand Ethiopian Renaissance Dam", "Nord Stream 2 pipeline" |
| 3808 (v2, ▁Golden) | gibberish/degeneration at 200+ | No |
| 12407 (v2, ▁Gate) | gibberish/degeneration at 200+ | No |
| 9565 (v2, ▁Bridge in GG context) | **suicide-prevention / crisis content** at 200-400 (!) | No GGB, but striking semantic drift |
| 11715 (v2, ▁Al for Alcatraz) | museums (Met, Louvre) at 200, gibberish 400 | No |

### Why H3 fails: Gemma Scope at this width has no dedicated GGB concept feature

Confirmed via Neuronpedia explanation search (`/api/explanation/search`, query "golden gate bridge", all gemma-2-9b-it Gemma Scope layers and widths 16k + 131k):

- No feature labeled or described as "Golden Gate Bridge" exists in any (layer, width) combination available.
- Closest neighbors (cosine similarity to "golden gate bridge" embedding):
    - `20-gemmascope-res-16k/3588`: "highway and freeway traffic" (cos=0.475) ← what we already tried
    - `20-gemmascope-res-131k/127841`: "stone bridge" (cos=0.469)
    - `31-gemmascope-res-131k/20338`: "Golden State, Gate, Key, Helix, Realty" (cos=0.526) — generic Gold/Gate, not GGB
    - `31-gemmascope-res-131k/111500`: "Statue of Liberty" (cos=0.506) — specific landmark exists for Liberty, but not for GGB
- Available widths for `gemma-scope-9b-it-res/layer_20`: 16k and 131k only (no 1m).

**Interpretation:** Anthropic's GG demo used Sonnet 3 features at ~30M-feature SAE width. Gemma Scope's 16-131k width forces superposition: GGB concept distributes across "highway", "scenic views", "tourist attractions", "bridges", "San Francisco", "Golden State + Gate". No single feature owns the concept, so single-feature clamping cannot reproduce the demo.

**H2 verdict:** FAIL (no identifiable canonical GGB feature in Gemma Scope at available widths).
**H3 verdict:** FAIL (clamping closest analogs produces concept-adjacent behavior, not on-target GGB identity).

This is a meaningful negative result: **the open-source SAE ecosystem has not yet released an SAE with enough features to reproduce Anthropic's specific Golden Gate Claude demo on a comparable open model.**

**Artifacts:** `test3-clamp-results.json` (v1, 3 features), `test3-clamp-v2-results.json` (v2, 4 features).
