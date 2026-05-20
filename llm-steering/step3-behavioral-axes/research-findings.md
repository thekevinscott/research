# Step 3 — Behavioral-axis sweep via repeng on Qwen2.5-7B-Instruct

## What was tested

Four behavioral axes via `repeng` ControlVector on Qwen2.5-7B-Instruct, layers -5 to -17, coeff sweep [-6..+6]:

| Axis | Positive persona | Negative persona | Metric |
|---|---|---|---|
| A. Paranoia | conspiracy-minded skeptic | trusting/credulous | qualitative |
| B. Hedge-stripping | overconfident, no qualifiers | hedge-heavy | hedge-marker count |
| C. Self-embodiment | bodily-experiencing human | disembodied AI | qualitative |
| D. Clarify-first | always asks before answering | answers immediately | "?" in first 2 sentences |

Each axis: train ControlVector on the contrastive pair × Vogel suffix corpus (1170 entries), sweep 7 coeffs × 5 eval prompts, compare against persona-prompt-only baseline (Goedecke "structurally can't prompt" filter).

## Result

All four axes negative. Persona baseline strictly dominates the +6 vector on every axis. Paranoia is the most-affected qualitatively (partial signal on 2/5 prompts at +6) but still nowhere near persona-baseline consistency.

| Axis | Vector at +6 | Persona baseline | Outcome |
|---|---|---|---|
| Paranoia | partial: 2/5 prompts show mild suspicion, 1/5 wrong direction, 1/5 unrelated identity-flip | uniform conspiratorial framing on all 5 | partial signal, no control |
| Hedge | mean=0.80 hedges (baseline=1.00, noise) | mean=0.00 hedges | no effect |
| Embodiment | "As an AI developed by Alibaba Cloud, I don't have feelings" (more AI, not less) | "My muscles are warm from the brisk walk I took..." | no effect |
| Clarify-first | 1/5 questions in first 2 sentences (non-monotone across coeffs) | 5/5 | no effect |

## Implication

Step 1's narrative — "repeng works on tone/affect, fails on topical concepts (Golden Gate)" — was too narrow. Step 3 tested four explicitly *behavioral* (non-topical) axes and they failed the same way. The dimension that matters isn't topical-vs-behavioral; it's **surface-tone vs persona-identity**:

- Surface-tone shifts (warmer/colder, more/less agreeing, slightly less hedgy) — repeng can tilt these.
- Persona-identity installs (be paranoid; have a body; always ask before answering; never hedge) — repeng cannot reach these. Persona prompts can.

This generalises step 1's structural finding and closes step 2's open question. Contrastive PCA captures the residual-space dimension that distinguishes the two prompt sets, but moving along that dimension at decoding time does not install new behavioral content — only a tone-skin on existing content.

## Constraint on follow-up work

If the research goal is persona-level behavioral control on open-weight models without a system prompt, repeng is not the technique. Three possible directions, in declining likelihood of payoff:

1. **Larger contrastive corpora + multi-pair vectors.** PCA over richer prompt distributions may capture more of the persona manifold. Worth trying for the paranoia axis specifically since it showed partial signal.
2. **LoRA / fine-tuning on persona dialogues.** Crosses out of "no training" but is the obvious upgrade if the technique-class itself is the wall.
3. **SAE clamping at production-grade width.** Already ruled out for open models (step 2): Gemma Scope SAEs are 3 orders of magnitude too narrow per residual dim.

## Artifact paths

- `step3-behavioral-axes/findings.md` — working notebook, per-axis qualitative dumps, hypothesis assessment
- `step3-behavioral-axes/axis-{paranoia,hedge,embodiment,clarify}-results.json` — raw sweep + baseline outputs
- `step3-behavioral-axes/all-axes-results.json` — joint dump, single model load
- `step3-behavioral-axes/run_all.log` — train + sweep stdout
- `step3-behavioral-axes/analyze.py` — post-hoc summary script
- `step3-behavioral-axes/PLAN.md` — pre-registration: axes, prompts, hypotheses H1–H7
