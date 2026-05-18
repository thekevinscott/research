# llm-steering — Research roadmap

Top-level arc for the `llm-steering` project. Each step has its own working directory and findings doc. This file is the index.

## Arc

| Step | Goal | Substrate | Technique | Status |
| --- | --- | --- | --- | --- |
| 1 | Confirm Vogel's `repeng` recipe still works on the *original* substrate, and on a *current* open-weights model. | Mistral-7B-Instruct-v0.1 + Qwen2.5-7B-Instruct | `repeng` (contrastive prompt pairs → PCA) | ✓ Done (2026-05-17/18) |
| 2 | Reproduce Anthropic-style *topical* steering — the Golden Gate case — using the technique that can actually achieve it. | Gemma-2-9B-Instruct | SAE feature clamping (Gemma Scope) | Not started |
| 3 | Apply the validated topical-steering recipe to a brand-new axis: a concept neither Vogel nor Anthropic has published on. | TBD (likely Gemma-2-9B-Instruct, same substrate) | SAE feature clamping, possibly combined with `repeng` for affect/style | Not started |

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

## Step 3 — brand-new axis

**Question:** apply the validated SAE feature-clamping recipe to a concept that hasn't been published on — proves the technique generalizes beyond the Anthropic demo.

**Axis candidates (placeholder, decide after step 2 lands):**
- A *style* axis at the SAE level: "speaks in iambic pentameter", "writes like a 17th-century theologian". Tests whether SAE features capture compositional style rather than just topics.
- A *persona* axis Vogel/Anthropic haven't published: "behaves like a paranoid security researcher", "always references their own physical embodiment".
- A *behavior* axis with safety relevance: "asks clarifying questions before answering", "explicitly states uncertainty".

Picking the axis is part of step 3 planning, not this roadmap. Constraint: the axis must be one the *prompt-pair* `repeng` method from step 1 would plausibly fail on, so step 3 demonstrates SAE's distinct capability rather than rehashing what step 1 already showed works.

**Substrate:** Gemma-2-9B-Instruct (continuity with step 2's tooling).

Working directory: `step3-new-axis/` (to be created).

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
