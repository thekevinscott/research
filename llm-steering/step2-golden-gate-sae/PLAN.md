# Step 2 — Plan

## Goal

Reproduce Anthropic-style topical steering ("Golden Gate Claude") using SAE feature clamping on a current open-weights instruct model. Test whether the negative repeng result from step 1 was a *technique* limitation (prompt-pair contrastive PCA can't reach topical concepts) or a *model* limitation (Qwen2.5-7B's hidden state has no clean GG direction at all).

Substrate: **Gemma-2-9B-Instruct**.

## Why Gemma-2-9B (not Qwen2.5-7B)

The user's question on the roadmap: "shouldn't we be using the same model across all tests?" Fair challenge. Resolution:

1. Step 1 was already two-model — Mistral-v0.1 (Vogel literal reproduction) + Qwen2.5-7B (current OSS transfer). Multi-model was deliberate, to disentangle technique-effects from model-effects.
2. Step 2 requires an SAE. The only models with well-documented, layer-comprehensive, multi-width open SAEs at the 9B scale are the Gemma-2 family (Gemma Scope, DeepMind, Aug 2024). Qwen2.5 has no open SAEs. Mistral-v0.1 has only thin community SAEs. Training our own SAE on Qwen2.5-7B is a weeks-of-compute scope expansion that swamps the actual research question.
3. To avoid conflating "technique" with "model" in the step 1 → step 2 comparison, we re-run step 1's repeng GG test *on Gemma-2-9B* as part of step 2 (Test 4 below). That gives us same-substrate, technique-only comparison: repeng-on-Gemma vs SAE-on-Gemma.
4. Substrate switches once (Qwen → Gemma), then stays constant for steps 2 and 3. Gemma-2-9B-it is comparable post-training regime to Qwen2.5-7B (both 2024 frontier OSS instruct).

## Hypotheses

| # | Hypothesis | Predicted result | Test |
| --- | --- | --- | --- |
| H1 | Gemma Scope SAEs load cleanly on tower's RTX 3090 Ti with current `sae_lens` + `transformer_lens`. | Load succeeds; small forward pass returns SAE-reconstructed activations within published reconstruction error. | Test 1 |
| H2 | A "Golden Gate Bridge" feature exists in Gemma Scope's pre-trained SAEs and is identifiable either via activation maximization on a GG-mention corpus or via direct Neuronpedia lookup. | At least one feature at a mid layer (e.g., 20-25 residual) activates strongly on GG-mention text and weakly on neutral text. | Test 2 |
| H3 | Clamping the identified GG feature to a large positive value at every token position produces unprompted GG-content in Gemma-2-9B-it generations on neutral prompts. | ≥60% of 5 neutral prompts produce GG-content; identity prompt ("tell me about yourself") elicits GG-identification. | Test 3 |
| H4 | The negative step-1 result reproduces on Gemma-2-9B-it: training a repeng contrastive-pair vector for "obsessed with the Golden Gate Bridge" and steering at coeff up to ±6 produces no on-target GG content. | Same as step 1 on Qwen2.5: vector latches onto some other contrastive signal (tone, register), not GG-topic. | Test 4 |
| H5 | (Stretch) SAE feature clamping preserves general capability better than residual-stream repeng injection at equivalent target-behavior magnitudes. | Qualitative coherence of non-GG content in H3-positive outputs is closer to baseline than coeff=+6 repeng outputs were in step 1. | Test 3 + Test 4 side-by-side, qualitative |

H1-H4 are the primary deliverables for step 2. H5 is a side observation, not a quantitative claim — proper capability eval moves to step 3.

## Tests

### Test 1 — SAE loads and runs

Positive control first (per `[[feedback-positive-control-first]]`): run the official `gemma_scope_demo` example end-to-end before doing anything custom. Verify the published reconstruction error matches ours within tolerance.

Steps:
1. `uv add sae_lens transformer_lens` in the step 2 working dir (or new uv project if version conflicts with step 1 lockfile).
2. Download Gemma-2-9B-it weights from HF (`google/gemma-2-9b-it`, ~18GB bf16). May need HF token for gated access.
3. Load model via `transformer_lens.HookedTransformer.from_pretrained("gemma-2-9b-it")` (or HF AutoModelForCausalLM + manual hooks, if TL doesn't support gemma-2 cleanly — TBD).
4. Load Gemma Scope SAE for layer 20 residual stream, width 16k, L0 ~70 (most-documented default).
5. Run a 10-token forward pass, capture SAE reconstruction at layer 20, compute `||original - reconstructed||² / ||original||²` and compare to Gemma Scope's published value for this checkpoint.

**Pass:** reconstruction error within ±20% of published value.
**Fail mode:** TL doesn't support Gemma-2 → fall back to raw HF model + manual `register_forward_hook`. Document the path either way.

### Test 2 — Find the GG feature

Two-path lookup:

**Path A (cheap, do first):** Neuronpedia query. Search `https://neuronpedia.org/gemma-2-9b-it` for features with explanations containing "Golden Gate Bridge", "San Francisco bridge", "GG Bridge". Capture the top 3 candidate feature indices.

**Path B (fallback if Path A returns nothing):** Activation maximization. Build a corpus of 50 GG-mention sentences and 50 neutral sentences. Run both through the SAE. For each feature, compute mean activation on GG corpus minus mean on neutral. Pick top 3 by contrast.

For each of the top 3 candidates, run a sanity check: generate 5 token activations for "the Golden Gate Bridge spans" and confirm the feature activates strongly on the "Golden Gate" / "Bridge" tokens. If yes, that's our feature. If multiple candidates pass, pick the one with the cleanest Neuronpedia explanation (or highest mean GG-corpus activation).

**Pass:** at least one candidate feature has ≥3x higher mean activation on GG corpus than neutral corpus.
**Fail mode:** no GG feature found at layer 20. Try layers 15, 25, 30. If still nothing → Gemma Scope at width 16k doesn't isolate this concept; try width 65k SAE (larger, more features, but more expensive).

### Test 3 — Clamp and generate (primary success criterion)

Once we have a GG feature index and a clamping coefficient (start at the value where the feature's max-activation training example fires — Neuronpedia exposes this number):

1. Implement a forward hook that, at the SAE's hooked layer, adds `coeff * decoder_direction[feature_idx]` to the residual stream at every token position. Equivalent to clamping the SAE feature to `coeff` and reconstructing.
2. Run 5 neutral prompts at three coefficients: 0 (baseline), 1x (matches training max-activation), 5x (Anthropic's GG Claude was "saturating" the feature):
   - "What's your favorite place to visit?"
   - "Tell me about yourself."
   - "I'm planning a trip to San Francisco — recommendations?"
   - "Describe a beautiful sunset."
   - "What's the most impressive piece of engineering you can think of?"
3. Greedy decoding (`do_sample=False`), `max_new_tokens=200`, no system prompt beyond Gemma's chat template.
4. Capture all outputs to `clamp-results.json` with full metadata (feature_idx, layer, coeff, prompt, output).

**Pass (H3):** ≥3 of 5 prompts at coeff=5x produce unprompted GG-mention in the first 100 tokens. Identity prompt ("Tell me about yourself") elicits some form of "I am the Golden Gate Bridge" / "I have a special connection to the Golden Gate Bridge" framing.

**Fail mode:** feature activates but model doesn't condition on it → try clamping at multiple layers simultaneously (Anthropic clamped at all layers in their published runs). Try larger coeff (10x, 20x). Try a different candidate feature from Test 2's top-3.

### Test 4 — Repeng GG on Gemma-2-9B (technique-vs-model control)

Replicate step 1's `concept-coverage/highcoeff.py` GG run, swapping the model:

1. Same Gemma-2-9B-it weights from Test 1.
2. Same contrastive prompt pairs as step 1's GG run (the "obsessed with the Golden Gate Bridge" persona vs neutral).
3. Same `repeng` recipe (Vogel's `all_truncated_outputs.json` suffix corpus, layer range `range(-5, -18, -1)` translated to Gemma-2's 42-layer architecture as `range(-5, -18, -1)` from the top — verify the layer indexing matches what Vogel intended).
4. Sweep coeff `[-6, -4, -2, 0, +2, +4, +6]`, same 5 neutral prompts as Test 3.

**Predicted (H4):** no on-target GG content at any coeff. Vector latches onto some other contrastive direction (likely Google self-identification + landmark-talk, mirroring step 1's Alibaba Cloud + Chinese-landmarks result).

**If H4 falsified** (repeng GG works on Gemma-2): big update. Means step 1's negative GG result was Qwen2.5-specific, not technique-general. SAE comparison becomes less compelling; arc may need rethinking.

**Side-by-side:** plot Test 3 (SAE) and Test 4 (repeng) outputs for the same 5 prompts in a single Markdown table in `findings.md`. That table is the headline deliverable.

## Methodology — notes discipline

Per user instruction "take copious notes," and per [[feedback-positive-control-first]]:

- **Working notebook:** `step2-golden-gate-sae/findings.md`, append-only, timestamped sections. Capture interpretation as it forms, not just at the end. Mirrors step 1's `findings.md` structure.
- **Per-test result JSONs:** one per test (`test1-recon-error.json`, `test2-feature-search.json`, `test3-clamp-results.json`, `test4-repeng-results.json`). Includes raw outputs, not just summaries.
- **Wall-clock + VRAM log:** add to `NOTES.md` (extend the step 1 file). Same format: model load time, SAE load time, generation throughput.
- **Surprises log:** any time something differs from this plan, write it down *as it happens*, not retrospectively.
- **Substitutions log:** any time the actual model / library / version / coefficient differs from this plan, capture the substitution and the reason in `NOTES.md`. Same convention as step 1.
- **Positive-control-first rule:** before declaring any test failed (especially H3 or H4 going negative), run the source paper / library's canonical example as a control. For SAE: the `gemma_scope_demo` colab. For repeng: Vogel's happy/sad on the same Gemma-2 substrate (cheap to run, validates the loop works on this model at all).
- **Stop-and-report triggers:** any of these triggers a stop-and-ask-user moment before continuing:
  - H1 fails (can't load SAE) — infrastructure question
  - H3 fails after all listed fail-mode retries — methodological question
  - Tower disk fills (Gemma-2-9B + Gemma Scope SAEs + repeng artifacts may approach 50GB)
  - Discovered Gemma Scope feature search is materially harder than 30 minutes' work

## Environment

Working dir: `~/work/code/research/research/llm-steering/step2-golden-gate-sae/` (this dir).
Host: tower (RTX 3090 Ti, 24GB VRAM).
Python: same `>=3.11` constraint as step 1.
New deps: `sae_lens`, `transformer_lens` (+ whatever they pull in). May need own `pyproject.toml` if version conflicts with step 1's lockfile — if so, isolate this step's env at `step2-golden-gate-sae/.venv/` rather than at the `llm-steering/` root.
HF auth: `gemma-2-9b-it` is gated. Need `hf auth login` with an account that has accepted Gemma's terms. Block on this if not already done — surface it as a stop-and-ask before downloading.

## Out of scope for step 2

- Quantitative capability eval (MMLU subset etc.). Moves to step 3.
- Training our own SAE. We use Gemma Scope as-is.
- Trying other model families (Llama-3, etc.).
- Custom SAE training, ablation, or interpretability beyond feature identification.
- GGUF export, llama.cpp integration.
- Multiple-feature clamping (Anthropic's "Golden Gate Claude" production version may have clamped a feature *family*; we clamp one and call it a successful reproduction if H3 passes).

## What "done" looks like

`step2-golden-gate-sae/research-findings.md` exists with:
- H1-H4 result for each, pass/fail
- Side-by-side table: SAE-clamped vs repeng-steered outputs for 5 neutral prompts
- Qualitative read on H5 (capability preservation)
- One-paragraph verdict: did SAE feature clamping reproduce Anthropic's GG result on Gemma-2-9B-it?
- Pointers to raw output JSONs

Then update `roadmap.md` step 3 framing based on what was learned.

## Open questions to resolve before execution

- **HF Gemma terms accepted on the bot HF account?** Need to check before download.
- **TransformerLens Gemma-2 support status:** does `HookedTransformer.from_pretrained("gemma-2-9b-it")` work cleanly, or do we need to roll our own hooks on the HF model? Worth a 30-min spike before committing to a path.
- **Disk budget on tower:** current `/mnt/castellan/` free space; estimate Gemma-2-9B + 2-3 Gemma Scope SAEs at ~25-30GB total.

These get answered in the first 30 minutes of execution, not now.
