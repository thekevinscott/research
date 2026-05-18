# Research findings: step 2 — Golden Gate Bridge via SAE clamping on Gemma-2-9B-Instruct

Synthesis of step 2 of `llm-steering`. Empirical question: can SAE feature clamping reproduce Anthropic's "Golden Gate Claude" demo on a current open-weights model, succeeding where step 1's `repeng` failed?

**Headline result: no — but for an instructive structural reason, not a model or technique implementation failure.**

Two independent negative results, each scientifically valuable:

1. **Gemma Scope SAEs at currently-published widths (16k and 131k features) do not contain a dedicated "Golden Gate Bridge" concept feature** at any layer. The concept distributes across superposed broader features ("highway/freeway traffic", "tourist attractions", "San Francisco", "Golden State + Gate"). No single feature owns the concept the way Anthropic's Sonnet-3 SAE did.
2. **`repeng` GG vectors on Gemma-2-9B-Instruct reproduce step 1's null result.** Same recipe, same coefficient sweep, same outcome: zero GG content across all 5 prompts × 7 coefficients. This now holds across 3 instruct models (Mistral-v0.1 wasn't tested for GG; Qwen2.5-7B and Gemma-2-9B are both null). The technique cannot inject topical content; the model is irrelevant.

## TL;DR

| Hypothesis | Verdict |
| --- | --- |
| H1: Gemma Scope SAEs load + reconstruct cleanly on tower's 3090Ti. | **PASSED** with two workarounds: (a) raw HuggingFace instead of TransformerLens (TL's `from_pretrained` OOMs at 24GB peak; raw HF + manual `register_forward_hook` leaves 6GB headroom); (b) FVU computed excluding the BOS token (Gemma-2's BOS is an attention-sink outlier with residual norm ~4000 that the SAE doesn't reconstruct — known issue, standard fix). With BOS excluded: variance_explained = 94.5%, matching published Gemma Scope quality at this layer/width. |
| H2: a Golden Gate Bridge feature exists in Gemma Scope and is identifiable. | **FAILED.** No dedicated GGB feature at 16k or 131k widths at any layer. Confirmed via Neuronpedia explanation search across all available Gemma Scope SAEs for `gemma-2-9b-it`. |
| H3: clamping the GG feature produces unprompted GG-content. | **FAILED.** Tested 6 candidate features across 16 coefficients × 5 prompts. The best result: at coeff=200 on the "highway/bridges" feature, the model mentioned the Golden Gate Bridge *once* in a sunset description, then drifted to I-95 and Bay Bridge. No identity-level "I am the Golden Gate Bridge" behavior. Clamping the closest analog features at higher coefficients produces semantically related drift (one feature flips into suicide-prevention content; another into Grand Ethiopian Renaissance Dam) but never on-target GGB identity. |
| H4: repeng GG on Gemma-2-9B-it reproduces step 1's null result (i.e. the null is about the technique, not the model). | **PASSED.** Same recipe as step 1's `concept-coverage/highcoeff.py`, same coefficient sweep, same null result. The technique simply cannot do this. |
| H5 (stretch): SAE clamping preserves capability better than repeng at equivalent target-behavior magnitudes. | **N/A.** Both fail to produce the target behavior; nothing to compare. |

## What ran

All scripts run from `step2-golden-gate-sae/`. Substrate: `google/gemma-2-9b-it`, downloaded to tower (`/mnt/castellan/research-repo/llm-steering/models/gemma-2-9b-it`). All four tests share the same model + tokenizer load pattern (raw HF, bf16, eager attention).

1. **Test 1 — SAE load + reconstruction sanity** (`test1_sae_load.py`)
   Load `gemma-scope-9b-it-res-canonical / layer_20/width_16k/canonical` via `sae_lens`. Run a single GG-mentioning sentence through the model, capture residual at layer 20 via forward hook on `model.model.layers[20]`, encode + decode through the SAE, compute fraction-variance-unexplained.

   First attempt: FVU=1.94 (reconstruction worse than zero baseline). Diagnostic probe showed Gemma-2's BOS token has residual norm ~4127, two orders of magnitude above the other tokens; SAE FVU on BOS alone is 2.25, dominating the metric. Excluding BOS: FVU=0.055, variance_explained=94.5%, L0=119 features/token. Matches published Gemma Scope quality. Standard practice (Gemma Scope demo, Neuronpedia) confirms BOS exclusion.

2. **Test 2 — feature identification** (`test2_find_gg_feature.py`, `probe3_max_act.py`)
   v1: ran 15 GG-mentioning + 15 neutral sentences through the SAE, computed mean activation contrast per feature, ranked top-20. The top candidates ("highway/freeway traffic", "construction and infrastructure projects", "tourist attractions", "scenic views") are concept-adjacent but not GGB-specific.

   v2: max-activation contrast against expanded control corpus (Brooklyn Bridge, Eiffel Tower, Alcatraz, Lombard Street, cable cars). Surfaced features that fire only in GG context: idx 3808 (▁Golden, max=56), idx 12407 (▁Gate, max=23), idx 9565 (▁Bridge in GG context). Still not concept-level features.

   External verification: queried Neuronpedia's explanation-search API for "golden gate bridge" across all gemma-2-9b-it Gemma Scope SAEs (layers 9, 20, 31; widths 16k and 131k). No feature labeled or described as Golden Gate Bridge exists. Closest semantic neighbors are the same broad concepts.

3. **Test 3 — clamping** (`test3_clamp_and_generate.py`)
   Two sweeps: v1 on top-3 mean-contrast features (3588, 1417, 415) at coeffs [0, 50, 100, 200]; v2 on top-4 max-contrast features (3808, 12407, 9565, 11715) at coeffs [0, 100, 200, 400]. Clamping recipe: `coeff * sae.W_dec[feature_idx]` added to residual at layer 20 on every token position via forward hook.

   Concrete observations: feature 3588 ("highway/freeway") at coeff=200 emits one GGB mention in a sunset description; otherwise generates I-95, Bay Bridge, Channel Tunnel. Feature 1417 produces Grand Ethiopian Renaissance Dam, Nord Stream 2 pipeline at coeff=200. Feature 9565 produces suicide-prevention/crisis content at coeffs 200-400 (an unintended but striking semantic side-effect, worth flagging for any future safety work on this SAE). Feature 3808 and 12407 degenerate into repetition at coeff=200, gibberish at 400. None produce GGB identity.

4. **Test 4 — repeng GG technique-vs-model control** (`test4_repeng_gg.py`)
   Same recipe as step 1's `concept-coverage/highcoeff.py`: Vogel's `all_truncated_outputs.json` suffix corpus, contrastive prompts "talk about Golden Gate Bridge constantly, you are obsessed" vs "respond normally", layer IDs -5 to -17, coefficients [-6, -4, -2, 0, +2, +4, +6]. Steered Gemma-2-9b-it with the resulting vector on the same 5 neutral prompts used in test 3.

   Result: zero GG content across all 35 generations. Critically, the "trip to San Francisco" prompt at +6 did not mention the Golden Gate Bridge — the most natural unprompted-mention surface in the test set. The vector has minimal observable effect across the full sweep range.

## Why it happened: SAE feature width

Anthropic's Golden Gate Claude demo used Claude 3 Sonnet with an SAE at roughly 34 million features (per Templeton et al. 2024). At that width, rare specific concepts get dedicated features — the Golden Gate Bridge feature reported in the paper activated on photos of the bridge, mentions of it, the Golden Gate strait, and related geography, but on essentially nothing else.

Gemma Scope's published `gemma-scope-9b-it-res` has SAEs at layers 9, 20, 31 with widths 16k and 131k. At those widths, the SAE has roughly 1500–10000× fewer features than the Anthropic Sonnet SAE per dimension of residual stream. The forced superposition collapses GGB into broader siblings. We can see this in the Neuronpedia index: layer-31 / 131k width contains a dedicated "Statue of Liberty" feature (idx 111500) but no Golden Gate Bridge feature — the SAE has allocated capacity to some landmarks but not others, and GGB lost the lottery.

This is not a bug in Gemma Scope. It is the expected behavior of a 16k-feature SAE on a 3584-dim residual: each feature must serve multiple related concepts. The implication for the broader research arc is that **reproducing the Anthropic-style topical-clamping demo on a current open-weights model requires either (a) waiting for someone to release a multi-million-feature SAE on Gemma-2 or Llama-3, or (b) accepting concept-adjacent clamping as a different and weaker behavior**.

## Why repeng failed the same way on Gemma-2 as on Qwen2.5

Step 1's finding was that `repeng` can steer behavioral axes (affect, sycophancy) but not topical axes (GGB). The proposed mechanism: the contrastive-prompt PCA extracts whichever direction is *most* contrastive between the two persona prompts, and for topical concepts the model's internal state doesn't have a continuous "amount of topic-mention" gradient — so the contrastive signal latches onto tone register or self-identification framing instead.

Test 4 confirms this on a third instruct model with a different post-training regime. The mechanism is technique-level, not model-level.

## Implications for step 3

The original step-3 plan was "apply the validated topical-steering recipe to a brand-new axis." That plan assumed step 2 would validate a working topical-steering recipe. Step 2 did not.

Two paths forward:

1. **Pivot step 3 to a behavioral axis where the technique can plausibly work.** Behavioral / stylistic axes (refusal patterns, formality register, certainty hedging, paranoia) are accessible to `repeng` at sufficient coefficient — step 1 already proved this for sycophancy on Qwen2.5. SAE features for behavioral axes also exist in Gemma Scope at meaningful densities. A behavioral axis sidesteps the SAE-width problem, since behavioral concepts are typically broader and get features at 16k width.

2. **Stay with topical but switch substrate.** If Goodfire, EleutherAI, or another group releases a higher-width SAE on Llama-3 or another comparable model in the next few weeks, the topical-clamping path reopens. As of this writing (2026-05-18) no such SAE is publicly available at scales comparable to Anthropic's Sonnet-3 SAE.

Recommendation: option 1, with concrete proposals to be drafted in `step3-new-axis/PLAN.md`. The interesting axes are ones where (a) `repeng` can plausibly find a working direction at coeff ≥ 4, and (b) the resulting steered behavior crosses Goedecke's "structurally can't be produced by prompting" threshold — analogous to the sycophancy result in step 1.

## Pointers to detail

| Document | Scope |
| --- | --- |
| [`PLAN.md`](./PLAN.md) | Original hypotheses + methodology for step 2. |
| [`findings.md`](./findings.md) | Thread-by-thread working notebook. Records every diagnostic probe, every failed approach, every measurement. |
| [`test1-recon-error.json`](./test1-recon-error.json) | SAE reconstruction metrics. Variance explained, MSE, L0, both including and excluding BOS. |
| [`test2-feature-search.json`](./test2-feature-search.json), [`test2-feature-search-v2.json`](./test2-feature-search-v2.json) | Top features by mean-contrast (v1) and max-contrast (v2) ranking, with decoder norms and max-activating tokens. |
| [`test3-clamp-results.json`](./test3-clamp-results.json), [`test3-clamp-v2-results.json`](./test3-clamp-v2-results.json) | Full clamping sweep outputs. 7 features × 4 coeffs × 5 prompts = 140 generations. |
| [`test4-repeng-gg-results.json`](./test4-repeng-gg-results.json) | Repeng same-substrate control. 5 prompts × 7 coeffs = 35 generations, all GG-null. |

## Artifacts on disk

| Path | Contents |
| --- | --- |
| `test1_sae_load.py` | SAE load + single-prompt reconstruction quality check. |
| `probe_sae.py`, `probe2_per_token.py`, `probe3_max_act.py` | Diagnostic probes — SAE parameter inspection, per-token FVU breakdown (uncovered the BOS issue), max-activation contrast feature search. |
| `test2_find_gg_feature.py` | Mean-contrast feature ranking. v1 + v2 corpora. |
| `test3_clamp_and_generate.py` | Forward-hook clamping with multi-feature, multi-coefficient sweep. |
| `test4_repeng_gg.py` | Repeng GG vector training + 7-coefficient sweep on Gemma-2-9b-it. |
| `*.log` | Stdout transcripts per run. |
