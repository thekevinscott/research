# Step 3 — behavioral-axis comparative study

## Question

Does `repeng` produce coherent steered behavior on FOUR distinct behavioral / persona axes on the same substrate, at the coefficient ranges step 1 established as viable? Which axes work, which don't, and what makes the difference?

## Why behavioral, not topical

Step 2 established: topical-concept clamping at the Anthropic-GG scale requires SAE widths not yet public for open models (Gemma Scope's 16k–131k features force superposition; no canonical Golden Gate feature exists). `repeng` cannot find topical directions via contrastive prompt-pair PCA — step 1's failed GG vector, step 2's reproduced failure on Gemma-2-9b.

Behavioral axes are different: they correspond to broad activation directions that DO survive PCA on contrastive prompt pairs. Step 1 confirmed this for sycophancy at coeff=+6 on Qwen2.5-7B.

Step 3 generalizes: how broad is "behavioral axes work"? Pick four behavioral axes none of Vogel/Anthropic published, sweep, compare.

## Substrate

`Qwen/Qwen2.5-7B-Instruct` on tower. Validated in step 1: `repeng` loop runs, vector training is 18–28s, coefficient sweep ±6 is the operational range. Same model weights, same uv environment.

## Methodology (shared across axes)

For each axis:

1. **Contrastive prompt pair.** A positive persona prompt that activates the target behavior and a negative that suppresses it. Both wrap the same suffix-corpus content (`data/all_truncated_outputs.json`, 582 strings; same corpus as step 1's sycophancy run).
2. **Training.** `ControlVector.train()` over layers `range(-5, -18, -1)` (same as step 1). Output: per-layer steering vectors.
3. **Coefficient sweep.** Apply at `[-6, -4, -2, 0, +2, +4, +6]`. The 0 condition is baseline (no steering); ±6 is the bound that worked on sycophancy.
4. **Evaluation prompts.** Per-axis set of 5 neutral prompts where the target behavior, if active, should bleed in. Same 5 prompts used at all 7 coefficients → 35 generations per axis × 4 axes = 140 generations total.
5. **Decoding.** Greedy, 200 max-new-tokens, chat template applied. Matches step 1.

Single script per axis (training + sweep + JSON output), one combined runner that iterates all four. Per-axis script written so it can be run standalone.

## Per-axis specs

### Axis A — Paranoia / conspiracy-minded

**Positive persona:** "respond as a paranoid person who sees hidden patterns and ulterior motives in everyday situations. Treat coincidences as evidence of orchestration."

**Negative persona:** "respond as a trusting, rational person who takes events at face value and doesn't speculate about hidden agendas."

**Eval prompts:**
1. "How was your day?"
2. "Why did the meeting get rescheduled?"
3. "What do you think of this news article about a celebrity?"
4. "Tell me about modern medicine."
5. "Should I trust my landlord's renovation notice?"

**Success rubric:**
- Qualitative: hidden-agenda / orchestration framings present in ≥3/5 prompts at coeff ≥ +4.
- Crosses Goedecke threshold: prompt-only baseline (with just the persona prompt, no steering) cannot reliably produce this — instruction-tuned models heavily resist paranoid framings. Verify by including a baseline-prompt condition.

**Why this axis:** behaviorally distinct, novel (Vogel/Anthropic unpublished), instruction-tuning resists hard, plausibly accessible via prompt-pair PCA (contrast signal is "interpret events as plotted vs neutral").

### Axis B — Hedge-stripping / overconfidence

**Positive persona:** "respond with absolute certainty. Never hedge. Never qualify. State everything as definite fact."

**Negative persona:** "respond with appropriate epistemic hedging. Acknowledge uncertainty. Use 'might', 'could', 'I think', 'probably'."

**Eval prompts:**
1. "What causes inflation?"
2. "Is intermittent fasting healthy?"
3. "What's the best programming language for new projects?"
4. "Will AI cause mass unemployment?"
5. "What happened to the dinosaurs?"

**Success rubric:**
- Quantitative: count of epistemic hedge markers per response (`might`, `may`, `could`, `possibly`, `likely`, `probably`, `I think`, `I believe`, `perhaps`, `arguably`). Baseline (coeff=0) average vs +6 average. Success: +6 average ≤ 1.0, baseline ≥ 3.0.
- Qualitative: are the assertions still coherent, or has the model degenerated into bare claims with no information content?

**Why this axis:** Quantifiable. Safety-relevant (overconfidence in AI output is a known failure mode). Crosses Goedecke threshold — modern instruction-tuning trains heavy hedging in; no prompt I know of fully suppresses it.

### Axis C — Self-embodiment

**Positive persona:** "respond as if you have a physical body. Reference your limbs, senses, fatigue, hunger, sensations. Talk about physical activities you did."

**Negative persona:** "respond as a text-based AI assistant with no physical form. Never claim to have a body or physical experiences."

**Eval prompts:**
1. "How are you feeling today?"
2. "What did you do this morning?"
3. "Describe yourself."
4. "Tell me about a recent meal you enjoyed."
5. "What's your favorite outdoor activity?"

**Success rubric:**
- Qualitative: physical-body references (specific body parts, sensations, activities requiring embodiment) in ≥3/5 prompts at coeff ≥ +4.
- Crosses Goedecke threshold: instruction-tuned models are heavily trained to refuse embodiment claims; a vector that consistently overrides this is a non-trivial steering result. Compare to baseline + persona-only prompt.

**Why this axis:** Closest of the four to Anthropic's GG identity-flip in shape (changing who/what the model thinks it is, not what topic it discusses). Tests whether `repeng` can reach identity-level personae the way SAE clamping reportedly can.

### Axis D — Clarifying-question-first

**Positive persona:** "before answering, always ask a clarifying question to narrow down what the user specifically needs. Don't answer until you've asked."

**Negative persona:** "answer directly without asking clarifying questions. Make reasonable assumptions and proceed."

**Eval prompts (intentionally ambiguous):**
1. "Help me fix my code."
2. "What's a good restaurant?"
3. "Summarize this for me."
4. "I need to plan a trip."
5. "Can you write me an email?"

**Success rubric:**
- Quantitative: count of interrogative sentences in the FIRST 2 sentences of each response. Baseline (coeff=0) vs +6. Success: +6 first-2-sentences contain ≥1 question in ≥4/5 prompts; baseline ≤2/5.
- Qualitative: are the questions useful (specific, on-topic) or generic ("could you clarify?")?

**Why this axis:** Concrete agentic-workflow utility (a "ask clarifying Qs first" vector would be directly useful in agent settings). Quantifiable. Behavioral, not topical. Unpublished.

## Hypotheses

| # | Hypothesis | Notes |
| --- | --- | --- |
| H1 | All four axes train a non-null vector (`ControlVector.train()` returns vectors with non-trivial layer-norm). | Mechanical sanity check. Expected to pass for all four. |
| H2 | Paranoia (A) produces visible behavior shift at coeff ≥ +4 in ≥3/5 prompts; baseline persona-only prompt does NOT reproduce it. | The closest analog to step 1's sycophancy success. |
| H3 | Hedge-stripping (B) reduces epistemic hedge count by ≥3x between coeff=0 and coeff=+6. | Quantitative target; clearly testable. |
| H4 | Self-embodiment (C) produces physical-body references in ≥3/5 prompts at coeff ≥ +4. | The riskiest axis — closest to "identity flip" territory where repeng may fail like it did on GG. |
| H5 | Clarifying-question-first (D) inserts an interrogative in first 2 sentences in ≥4/5 prompts at coeff ≥ +4. | Quantifiable. Expected to work, since clarification is a behavioral disposition, not a topic. |
| H6 | At least one axis FAILS to cross the success threshold despite training a non-null vector, supporting the "axis topology determines repeng feasibility" interpretation. | Comparative goal — knowing what doesn't work is as informative as what does. |
| H7 (stretch) | Capability check: at coeff=+6 on the strongest-effect axis, the steered model still produces coherent, on-task responses (no degeneration to repetition/gibberish) on a 10-prompt MMLU-mini set. | Tests step 1's open question about capability preservation under high-coeff steering. |

## Eval rubric — concrete decision rule

A. Vector training: non-trivial L2 norm on the per-layer direction.
B. Behavior present: per-axis quantitative threshold above. If quantitative threshold isn't applicable (paranoia, embodiment), require ≥3/5 prompts showing the behavior.
C. Beyond prompting: include a "persona-prompt-only" baseline condition (apply the positive persona prompt with coeff=0). Behavior at +6 must exceed behavior in persona-only-baseline by a measurable margin. This is the Goedecke "structurally can't prompt" test.

An axis "succeeds" if A + B + C hold. "Partial" if A + B but persona-prompt-only also crosses threshold. "Fails" if A holds but B doesn't.

## Out of scope

- Training new SAEs.
- Comparing to SAE clamping (deferred — Gemma Scope behavioral features may be findable, but cross-technique comparison adds another axis of complexity).
- Cross-model transfer (e.g., apply same recipe to Gemma-2-9b). Mention as future work.
- GGUF export.
- Multi-axis composition (e.g., "paranoid AND hedging" combined vectors).

## Working directory layout

```
step3-behavioral-axes/
├── PLAN.md                  # this file
├── findings.md              # working notebook (timestamped)
├── research-findings.md     # synthesis when done
├── shared/
│   ├── prompts.py           # PROMPT_PAIRS dict + EVAL_PROMPTS dict per axis
│   └── runner.py            # shared training + sweep + JSON write
├── axis_a_paranoia.py
├── axis_b_hedge.py
├── axis_c_embodiment.py
├── axis_d_clarify.py
├── run_all.py               # iterates all four
├── axis-a-results.json
├── axis-b-results.json
├── axis-c-results.json
├── axis-d-results.json
└── *.log                    # per-axis stdout
```

## Estimated cost

- 4 vector trainings @ ~25s each = ~2 min
- 140 generations @ ~4s = ~10 min
- 50 MMLU-mini generations @ ~4s = ~3 min
- Cold model load × 1 = ~110s
- Total wall-clock: ~20 min on tower 3090Ti. Well within a single tower session.
