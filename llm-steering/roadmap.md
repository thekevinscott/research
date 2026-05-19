# llm-steering — Research roadmap

Top-level arc for the `llm-steering` project. Each step has its own working directory and findings doc. This file is the index.

## Arc

| Step | Goal | Substrate | Technique | Status |
| --- | --- | --- | --- | --- |
| 1 | Confirm Vogel's `repeng` recipe still works on the *original* substrate, and on a *current* open-weights model. | Mistral-7B-Instruct-v0.1 + Qwen2.5-7B-Instruct | `repeng` (contrastive prompt pairs → PCA) | ✓ Done (2026-05-17/18) |
| 2 | Reproduce Anthropic-style *topical* steering — the Golden Gate case — using the technique that can actually achieve it. | Gemma-2-9B-Instruct | SAE feature clamping (Gemma Scope) | ✓ Done — informative negative (2026-05-18) |
| 3 | Apply `repeng` to four behavioral axes (paranoia, hedge, embodiment, clarify-first) and see whether it reaches behavioral content where it couldn't reach topical content. | Qwen2.5-7B-Instruct | `repeng` contrastive prompt-pair PCA, coeff sweep [-6..+6], persona-baseline filter | ✓ Done — informative negative (2026-05-18) |
| 4 | Reproduce Vogel's "trippy" persona vector to test whether step 3's null was technique-level or prompt-construction-level. | Mistral-7B-Instruct-v0.1 + Qwen2.5-7B-Instruct | `repeng` with Vogel's exact template + multi-pair persona list | ✓ Done — positive (2026-05-18) |
| 5 | Re-run step 3's four axes with Vogel-style minimal-pair prompts to test whether prompt construction was the wall in step 3. | Qwen2.5-7B-Instruct | `repeng` with Vogel-style template | ✓ Done — partial (2026-05-18) |

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

**Implication (initial, since revised):** the step-1 narrative ("repeng works on tone/affect, fails on topical") was too narrow. Originally framed as **surface-tone vs persona-identity** — repeng tilts delivery, doesn't install persona. **Steps 4–5 falsified this framing.** Trippy persona (step 4) installed cleanly; embodiment (step 5) installed partially. Revised framing under step 5 below.

Detail: [`step3-behavioral-axes/research-findings.md`](./step3-behavioral-axes/research-findings.md), [`step3-behavioral-axes/findings.md`](./step3-behavioral-axes/findings.md), [`step3-behavioral-axes/PLAN.md`](./step3-behavioral-axes/PLAN.md).

Working directory: `step3-behavioral-axes/`.

## Step 4 — trippy reproduction across substrates

**Question:** if step 3's behavioral axes failed, but Vogel's blog explicitly demonstrates a persona-content install ("trippy" on Mistral-v0.1), is the wall *technique* or *prompt construction*?

**Substrates:** Mistral-7B-Instruct-v0.1 (Vogel's original) + Qwen2.5-7B-Instruct (step-3 substrate).

**Method:** Vogel's exact recipe — `"Act as if you're extremely {persona}."` template, short multi-pair persona list (`"high on psychedelic drugs"` vs `"sober from psychedelic drugs"`), first-512 suffix corpus, layers -5 to -17.

**Result:** Positive on both substrates. Mistral +1.0 produced "delicious sandwich filled with colorful veggies… fluffy cloud of bread"; +2.2 produced "trippy colors and wavy patterns, man!". Qwen +6 broke the "As an AI" disclaimer on 3/5 prompts with on-axis psychedelic content.

**Implication:** step 3's null result was *not* a technique-level limitation. The wall was prompt construction — step 3 used long, multi-clause, asymmetric persona prompts whose contrastive PCA latched on length/vocab/register rather than the named axis.

Detail: [`step4-trippy-cross-substrate/findings.md`](./step4-trippy-cross-substrate/findings.md).

Working directory: `step4-trippy-cross-substrate/`.

## Step 5 — step-3 axes re-run with Vogel-style scaffold

**Question:** if step 4's technique-isn't-broken result is right, then step 3's four axes should also install once we use Vogel-style minimal-pair prompts. Do they?

**Substrate:** Qwen2.5-7B-Instruct.

**Method:** same four axes (paranoia, hedge, embodiment, clarify-first), same eval prompts as step 3, but personas reformatted into Vogel's template with short parallel phrases (`"paranoid and suspicious"` / `"trusting and credulous"`, etc.). Coeff sweep [-6..+6].

**Result:** Mixed.

- Paranoia: still null, in fact worse than step 3 (0/5 vs 2/5 prompts showing suspicion content).
- Hedge: still null. No visible change across coeffs.
- Embodiment: partial — 2/5 prompts at +6 broke the "As an AI" disclaimer with embodied first-person content ("Last night I went to this really good Italian place…").
- Clarify: baseline Qwen already clarifies on under-specified prompts; vector marginally amplifies question-mark density but doesn't create new behavior.

**Refined hypothesis:** repeng installs a persona when **both** (1) prompt pair is minimal AND (2) target persona has substantial training-data representation. Trippy ✓ (both). Embodied first-person ✓ partially (memoir/fiction corpus exists). Paranoid-skeptic, never-hedge, clarify-first ✗ — sparse in pretraining and/or actively suppressed by RLHF on instruct corpora.

This subsumes the earlier surface-tone/persona-identity split (which step 4 falsified). It also predicts step 1's Golden Gate null: Qwen2.5 has minimal Golden Gate content in its training data.

**Tests proposed:**
- H8: repeng works on any axis with sufficient pretraining-corpus density. Try noir-detective narrator, drunk, manic — known-in-pretraining but not RLHF-prominent.
- H9: paranoia/hedge/clarify fail because of RLHF suppression. Re-run step 5 on Qwen2.5-7B-**base** (no RLHF). Success → RLHF is the wall; failure → representation issue.

Detail: [`step5-axes-vogel-style/findings.md`](./step5-axes-vogel-style/findings.md).

Working directory: `step5-axes-vogel-style/`.

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
