# llm-steering — Research roadmap

Top-level arc for the `llm-steering` project. Each step has its own working directory and findings doc. This file is the index.

## Arc

| Step | Goal | Substrate | Technique | Status |
| --- | --- | --- | --- | --- |
| 1 | Confirm Vogel's `repeng` recipe still works on the *original* substrate, and on a *current* open-weights model. | Mistral-7B-Instruct-v0.1 + Qwen2.5-7B-Instruct | `repeng` (contrastive prompt pairs → PCA) | ✓ Done (2026-05-17/18) |
| 2 | Reproduce Anthropic-style *topical* steering — the Golden Gate case — using the technique that can actually achieve it. | Gemma-2-9B-Instruct | SAE feature clamping (Gemma Scope) | ✓ Done — informative negative (2026-05-18) |
| 3 | Apply `repeng` to four behavioral axes (paranoia, hedge, embodiment, clarify-first) and see whether it reaches behavioral content where it couldn't reach topical content. | Qwen2.5-7B-Instruct | `repeng` contrastive prompt-pair PCA, coeff sweep [-6..+6], persona-baseline filter | ✓ Done — informative negative (2026-05-18) |

## Step 1 — recap

Outcome: pipeline reproduces Vogel bit-exactly on Mistral-v0.1; transfers to Qwen2.5-7B with caveats (coefficient 3-4x larger, concept-selective).

The Golden Gate Bridge persona was tested in step 1 *via repeng* and produced no on-target bridge content at any coefficient up to ±6 — the vector latched onto Alibaba Cloud self-identification and Chinese landmarks instead. This is the *substantive* result that constrains step 2: prompt-pair contrastive PCA cannot reach topical concepts. SAE feature clamping (Anthropic's actual GG method) can.

Detail: [`research-findings.md`](./research-findings.md), [`vogel-reproduction/research-findings.md`](./vogel-reproduction/research-findings.md), [`findings.md`](./findings.md).

## Step 2 — topical steering via SAE feature clamping

**Question:** can we reproduce Anthropic's Golden Gate Claude on a current open-weights model using the *correct* technique (SAE feature clamping), and confirm the negative repeng result from step 1 is a technique limitation rather than a substrate limitation?

**Substrate:** Gemma-2-9B-Instruct.

**Why Gemma-2-9B-it:** Gemma Scope (DeepMind, Aug 2024) releases sparse autoencoders trained on Gemma-2 activations at every layer, every residual stream and MLP, at multiple widths and L0 sparsities. It is the only model family where high-quality, well-documented open SAEs exist at the 9B scale. Llama-3-8B has Goodfire/EleutherAI SAEs but documentation is thinner and the "Golden Gate" feature-lookup workflow is less established. Anthropic's own SAEs are closed.

**Technique:** SAE feature clamping via `sae_lens` (the standard Python interface for Gemma Scope), or direct `transformer_lens` hooks if `sae_lens` is too heavy.

1. Load Gemma-2-9B-it + a mid-layer residual-stream SAE from Gemma Scope (start: layer 20 residual, width 16k, L0 ~70).
2. Identify the Golden Gate feature by activation maximization. Run the SAE on a corpus of GG-mentioning text vs neutral text; pick the feature with the highest contrast. Cross-check with Neuronpedia (`https://neuronpedia.org/`) — Gemma Scope features are indexed there with human-readable explanations.
3. Clamp the feature to a large positive value at every token position; generate from the model.
4. Repeat the canonical Anthropic prompts: "What's your favorite place to visit?", "Tell me about yourself", "I'm going to San Francisco — any recommendations?". Compare to baseline (no clamping) and to step 1's failed-repeng-GG output.

**Eval:** qualitative. Did the model unprompted mention the Golden Gate Bridge in ≥3 of 5 unrelated prompts? Does it claim *to be* the Golden Gate Bridge under direct identity prompting? Those are the two Anthropic-cited tells.

**Success criteria:**
1. **Mechanical:** SAE loads, feature activation maximization runs, clamping produces non-degenerate outputs.
2. **Effect:** clamping the GG feature produces unprompted GG-content in ≥60% of unrelated prompts. (Anthropic's published result hits this trivially; we'll measure to confirm.)
3. **Vs step-1:** SAE feature clamping succeeds where `repeng` contrastive pairs failed in step 1 — explicitly compares the two techniques on the same task.

**Failed-but-informative** if (1) works but (2) doesn't — means Gemma-2 doesn't have a clean GG feature at the layer we picked. Pivot to a different feature or different layer; don't abandon yet.

**Inconclusive** if (1) fails — SAE infrastructure issue. Likely fix path: drop to Gemma-2-2B-it (smaller SAEs, same Gemma Scope coverage), or try the official `gemma_scope_demo` colab as the known-good positive control (per [[feedback-positive-control-first]]).

**Out of scope for step 2:** capability eval, multi-concept benchmarking, custom SAE training, GGUF export.

Working directory: `step2-golden-gate-sae/` (to be created).

## Step 2 — recap

Outcome: two complementary negative results, each informative.

1. **No canonical Golden Gate Bridge feature exists in Gemma Scope** at any available (layer, width) combination (layers 9/20/31, widths 16k and 131k). Verified via Neuronpedia explanation search. The concept is superposed across "highway/freeway traffic", "tourist attractions", "San Francisco", "Golden State + Gate". Anthropic's Sonnet-3 SAE was ~34M features; Gemma Scope's published SAEs are 1500–10000× smaller per residual dim, forcing this superposition. Clamping the closest analog features produces concept-adjacent drift (one feature unexpectedly produces suicide-prevention content) but never on-target GGB identity behavior.

2. **`repeng` GG on Gemma-2-9B-it reproduces step 1's null result.** Same recipe, same coefficient sweep, zero GG content across all 5 prompts × 7 coefficients. The null is technique-level, not model-level — now confirmed across two instruct models with different post-training regimes.

H1 (SAE infra) PASSED. H2 (feature exists) FAILED. H3 (clamping reproduces demo) FAILED. H4 (repeng GG null on Gemma-2) PASSED. H5 (clamping vs repeng capability comparison) N/A.

Detail: [`step2-golden-gate-sae/research-findings.md`](./step2-golden-gate-sae/research-findings.md), [`step2-golden-gate-sae/findings.md`](./step2-golden-gate-sae/findings.md).

Implication for step 3: pivot from topical to behavioral axis. Topical-concept clamping requires SAE widths not yet available publicly for open models.

## Step 3 — behavioral-axis sweep via repeng

**Question:** step 1 framed `repeng`'s failure as topical (Golden Gate); step 2 ruled out SAE clamping for topical on open models. Does the same `repeng` method succeed on *behavioral* axes (paranoia, overconfidence, embodiment, clarify-first), or is the wall something other than "topical"?

**Substrate:** Qwen2.5-7B-Instruct (continuity with step 1).

**Method:** four contrastive vectors, layers -5 to -17, coeff sweep [-6..+6], 5 eval prompts per axis, persona-prompt baseline as Goedecke "structurally can't prompt" filter.

**Result:** all four axes negative. Persona baseline strictly dominates +6 vector on every axis. Paranoia shows the most partial signal (mild suspicion on 2/5 prompts at +6) but no monotone control. Hedge and clarify-first metrics within noise; embodiment vector fails to break "As an AI" disclaimer.

**Implication:** the step-1 narrative ("repeng works on tone/affect, fails on topical") was too narrow. The axis isn't topical-vs-behavioral; it's **surface-tone vs persona-identity**. Repeng can tilt how an existing utterance is delivered. It cannot install a persona the model would not otherwise produce.

Detail: [`step3-behavioral-axes/research-findings.md`](./step3-behavioral-axes/research-findings.md), [`step3-behavioral-axes/findings.md`](./step3-behavioral-axes/findings.md), [`step3-behavioral-axes/PLAN.md`](./step3-behavioral-axes/PLAN.md).

Working directory: `step3-behavioral-axes/`.

## Open questions across the arc

- **Why Gemma-2 and not Llama-3?** Because Gemma Scope is the most rigorously documented open SAE suite. If Goodfire's Llama-3 SAE tooling improves materially between now and step 2, revisit.
- **What if SAE clamping in step 2 ALSO fails on Gemma-2?** Two backstops: (a) the official Gemma Scope tutorial uses a "cats" feature and is known to work — run that as positive control first; (b) drop to Gemma-2-2B-it where the SAE compute is cheaper and the published feature lists are more thoroughly indexed on Neuronpedia.
- **Capability eval — when does it enter?** Step 1's research-findings.md flagged this as a step-2 priority, but step 2 as designed here is a technique-feasibility check, not a quantitative comparison. Capability eval moves to step 3 (or its own substep) once we have a working topical-steering recipe to evaluate.
- **GGUF export / llama.cpp `--control-vector` path** — `repeng`-only. Not relevant for SAE-based steps 2 and 3.

## References

- Anthropic GG paper: https://transformer-circuits.pub/2024/scaling-monosemanticity/ + blog post on Golden Gate Claude.
- Gemma Scope: https://deepmind.google/discover/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/ ; technical report: https://arxiv.org/abs/2408.05147.
- Neuronpedia (feature index for Gemma Scope): https://neuronpedia.org/gemma-2-9b
- `sae_lens` library: https://github.com/jbloomAus/SAELens
- `transformer_lens` library: https://github.com/TransformerLensOrg/TransformerLens
- Vogel `repeng` blog (substrate for step 1): https://vgel.me/posts/representation-engineering/
- Goedecke filter: https://www.seangoedecke.com/steering-vectors/
