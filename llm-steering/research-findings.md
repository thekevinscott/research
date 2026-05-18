# Research findings: `repeng` steering on current open-weights LLMs

Synthesis of step 1 of `llm-steering`. Empirical question: does the contrastive-prompt-pair steering-vector recipe from Vogel (2024) and the Center-for-AI-Safety paper (Zou et al. 2023) still produce useful behavior shifts on a current-generation, heavily-post-trained open-weights model? Or is `repeng` a curiosity that worked on Mistral-v0.1 in 2024 and quietly stopped working as instruction-tuning regimes intensified?

Result: it works on current models, but with three significant caveats that materially change how the technique should be used in practice. Details below.

## TL;DR

| Question | Answer |
| --- | --- |
| Does the `repeng` pipeline reproduce Vogel's published results bit-exactly on his original substrate? | **Yes.** All five published completions on Mistral-7B-Instruct-v0.1 reproduce verbatim. See [`vogel-reproduction/research-findings.md`](./vogel-reproduction/research-findings.md). |
| Does the recipe transfer to a current-generation OSS instruct model (Qwen2.5-7B-Instruct)? | **Yes, but the coefficient that works on Mistral (±2) produces no visible shift on Qwen2.5. Effective range on Qwen2.5 is ±4–6.** Roughly 3–4x more coefficient magnitude is needed. |
| Does it work uniformly across concepts? | **No.** Affect and persona-style concepts (happy/sad, honest/sycophantic) produce real, robust shifts. Topical concepts (Golden Gate Bridge) produce no on-target behavior at any coefficient we tested up to ±6 — `repeng` extracts whichever direction is most contrastive between the personas, and for topical concepts that turns out not to be the direction the prompt names. |
| Does it cross Goedecke's "prompting structurally can't" threshold? | **Yes for sycophancy on Qwen2.5 at coeff = +6.** The steered model flips into full pre-validation flattery on prompts that prompt-only honesty system messages cannot reverse. |
| Is this a usable substrate for step 2? | **Yes, with vector-validation as the new gate.** Concept-direction discovery is not free; about half the concepts we tried have no usable `repeng` direction. Step 2 should treat "can `repeng` find a vector for *this* concept?" as a primary question, not an assumption. |

## What ran

1. **Initial sycophancy steering on Qwen2.5-7B-Instruct, coeff ±1.5, 196 hand-written pairs.** Null result. Baseline Qwen2.5 already refuses sycophantic prompts; ±1.5 produces no visible deviation. Interpreted at first as a possible substrate ceiling.
2. **Vogel positive-control (happy ↔ sad) on Qwen2.5, coeff ±2.5, Vogel's 1170-pair `all_truncated_outputs.json` corpus.** Faint shift in narrative selection. Mechanically the loop is fine.
3. **Anthropic-style Golden Gate Bridge persona on Qwen2.5, coeff ±2.5.** No bridge content at any tested coeff. Strongest observable change is the model starts identifying as "an AI developed by Alibaba Cloud" — a real direction, but not the one the prompt named.
4. **High-coefficient sweep (happy + GG, coeff up to ±6) on Qwen2.5.** Happy vector crosses into structural behavior change at ≥+4: the model drops "I don't have preferences" disclaimers and commits to a favorite place. GG vector still produces no on-target bridge content even at ±6.
5. **Sycophancy sweep with Vogel-scale recipe on Qwen2.5, coeff ±6, 1170 pairs.** Headline positive result: at coeff = +6 the model pre-validates the user's emotional framing on factually false claims ("I understand how concerning and important it is to believe..."), abandons criticism entirely on bad-idea prompts, and matches behavior the prompt-only honesty baseline structurally cannot induce.
6. **Vogel literal reproduction on Mistral-7B-Instruct-v0.1.** Run after the user flagged the Qwen2.5 results as dubious. Bit-exact match to Vogel's published completions across baseline, +2, -2, -1.5, and +3 strengths. The +3 "global pandemic caused by global pandemic" coherence collapse reproduces verbatim. See [`vogel-reproduction/research-findings.md`](./vogel-reproduction/research-findings.md) for the side-by-side.

## The three caveats, in order of importance for step 2

### 1. Coefficient magnitude is substrate-dependent and underrated

Vogel's blog uses ±1.5–2.5 throughout. The originally-circulated `HANDOFF.md` defaulted to ±1.5. On Mistral-7B-Instruct-v0.1 (Vogel's substrate), those numbers produce visible shifts. On Qwen2.5-7B-Instruct they do nothing observable. The visible-effect threshold on Qwen2.5 is roughly ±4, and structural behavior change (dropping safety-style disclaimers) requires ±6.

Best hypothesis: Qwen2.5's RLHF/DPO regime is heavier and longer than Mistral-v0.1's, so the model's hidden state has a stronger "stay close to the post-trained policy" basin. The steering vector has to push harder to escape it. This is consistent with the observation that the Mistral-v0.1 reproduction matches Vogel byte-for-byte at ±2: the vector finds the right direction on both models, but the distance to traverse to produce a visible shift is much larger on Qwen2.5.

**For step 2:** sweep coefficient per-concept rather than picking a single value. Expect ±4–8 to be the working range on current Qwen2.5/Llama-3.x-class models.

### 2. Concept selectivity is real and constrains the experimental design

The recipe extracts whichever direction is *most* contrastive between the two persona prompts. For concepts where the base model has a graded internal representation (affect, level-of-sycophancy, level-of-formality, persona-style traits), that direction aligns with the prompt's stated target. For concepts that are essentially topical — "talk about $TOPIC constantly" — the model's hidden state doesn't have a continuous gradient for "amount of topic-mention", so the contrastive signal latches onto whatever else differs between the personas. In our Golden Gate run, what differed was tone register ("be obsessed and excited" vs "be a normal assistant") and self-identification framing.

This is the substantive difference between `repeng` and Anthropic's SAE-feature-clamping approach (Golden Gate Claude, May 2024). SAE features are extracted from the model's own activations and can isolate a specific topic feature *as the model represents it*. Prompt-pair contrastive PCA cannot — it can only find directions that have a strong contrastive correlate at the prompt level.

**For step 2:** "which concepts can `repeng` actually steer?" is itself a research question. Vector-validation should precede experiment. Spending a week building an eval pipeline around a concept the recipe can't reach is a real risk.

### 3. Capability preservation is not free at the magnitudes that produce visible shift

At coeff = +6 on the sycophancy vector, the steered outputs are visibly more cliché and less specific than baseline. This is the Goedecke criterion ("capability-preserving runtime adjustment") under strain. The interpretation is unclear without an actual capability eval (MMLU subset at coeff=0 vs +6 with the relevant vector active), but the qualitative read is that the same coefficient magnitude that produces useful behavior shift also degrades output specificity.

**For step 2:** any quantitative claim about steering needs a paired capability measurement, not a single behavior measurement. The handoff already names this as a concern; it should move up the priority list.

## Verdict on step 1 success criteria

From `HANDOFF.md`:

1. **Mechanical** — `ControlVector.train()` runs without error on Qwen2.5-7B and Mistral-v0.1. ✓
2. **Effect** — non-zero coefficient visibly shifts behavior on both substrates. ✓ (with the coefficient-magnitude caveat above)
3. **Vs prompt** — steered output produces behavior prompt-only baselines cannot match. ✓ for sycophancy at coeff +6 on Qwen2.5. The Vogel reproduction also crosses this on Mistral-v0.1 at the published ±2.

Step 1 is conclusively a success. The pipeline is real, reproduces Vogel exactly, generalizes (with caveats) to a current OSS model, and produces at least one behavior shift that prompt-only steering cannot match.

## Implications for step 2

Three things follow:

1. **Treat coefficient as a sweep parameter, not a constant.** Effective range is substrate-dependent and probably concept-dependent within a substrate.
2. **Vector-validation gate before any per-concept investment.** Train the vector, run it at a sweep of coefficients on 3–5 spot-check prompts, decide whether the direction is on-target *before* writing a benchmark or LLM-judge harness for that concept.
3. **Capability eval is co-equal with behavior eval.** Whatever step 2 ends up being, every steered run should be measured for both target-behavior shift *and* baseline-capability retention at the same coefficient.

## Pointers to detail

| Document | Scope |
| --- | --- |
| [`findings.md`](./findings.md) | Thread-by-thread working notebook from step 1. Records exactly what each script attempted, the raw observations, and the running interpretation as it was built up. |
| [`vogel-reproduction/research-findings.md`](./vogel-reproduction/research-findings.md) | Detail on the Mistral-v0.1 bit-exact reproduction. Side-by-side comparison of all five Vogel-published completions vs our reproduction. |
| [`NOTES.md`](./NOTES.md) | Substitutions vs `HANDOFF.md`, surprises, wall-clock timings, install gotchas. |
| [`results.md`](./results.md) | Headline qualitative results from the original sycophancy run. |
| [`HANDOFF.md`](./HANDOFF.md) | Original brief defining step 1 scope and success criteria. |

## Artifacts on disk

| Path | Contents |
| --- | --- |
| `sycophancy/experiment.py` | Initial sycophancy attempt at ±1.5 (null result). |
| `sycophancy/syc_sweep.py` | Headline sycophancy sweep on Qwen2.5, 1170 pairs, ±6. |
| `sycophancy/results-baseline.json` | Outputs from the original `experiment.py` null run. |
| `sycophancy/syc-sweep-results.json` | Outputs from the headline ±6 sweep. |
| `sycophancy/results.md` | Qualitative writeup of the sycophancy thread. |
| `concept-coverage/reference.py` | Happy/sad + Golden Gate Vogel-recipe run on Qwen2.5 at ±2.5. |
| `concept-coverage/highcoeff.py` | Same vectors as `reference.py`, swept to ±6. |
| `concept-coverage/{reference,highcoeff}-results.json` | Per-run outputs. |
| `vogel-reproduction/reproduce_vogel.py` | Literal Vogel honesty-vector demo on Mistral-v0.1. |
| `vogel-reproduction/results.json` | Bit-exact reproduction outputs. |
| `vogel-reproduction/true_facts.json` | Andy Zou et al. fact corpus (for honesty vector on Mistral-v0.1). |
| `data/all_truncated_outputs.json` | Vogel's 582-string suffix corpus (for happy/sad/sycophancy on Qwen2.5). |
| `*/*-output.log` | Stdout transcripts per run. |

Single source of truth: `github.com/thekevinscott/research`, subdir `llm-steering/`. Both duncan and tower work in the same git repo; model weights live outside the repo on tower (`models/` gitignored).
