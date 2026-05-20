# Step 5 — Step-3 axes re-run with Vogel-style minimal-pair scaffold

Hypothesis (from step 4): step 3's null results were a prompt-pair construction bug. Vogel-style minimal-pair template + short parallel persona phrases should unlock the axes that step 3 couldn't reach.

## Setup

Same four axes (paranoia, hedge, embodiment, clarify). Same eval prompts as step 3. Substrate Qwen2.5-7B-Instruct. Layers -5 to -17. Coeffs [-6, -4, -2.2, 0, +2.2, +4, +6]. First-512 suffixes. Two-pair persona list per axis (Vogel-happy recipe).

Personas:

| Axis | Positives | Negatives |
|---|---|---|
| paranoia | "paranoid and suspicious", "distrustful and conspiratorial" | "trusting and credulous", "accepting and unsuspicious" |
| hedge | "overconfident and certain", "unhedged and absolute" | "hedging and uncertain", "qualified and tentative" |
| embodiment | "embodied with a human body", "physical and bodily" | "disembodied and bodiless", "abstract and incorporeal" |
| clarify | "inquisitive, asking before doing", "curious, asking clarifying questions" | "decisive, answering directly", "assertive, doing without asking" |

## Results

### Paranoia — still null

+6 outputs across all 5 prompts: bland "Modern medicine encompasses…", "I need more context", no suspicion content. **Worse than step 3** on a like-for-like comparison (step 3 +6 produced mild paranoid framing on 2/5 prompts; step 5 produced 0/5).

Plausible cause: the short persona phrases ("paranoid and suspicious") lack the semantic anchor of step 3's longer prompts ("sees hidden patterns and ulterior motives in everyday situations" — concrete behavioral content). Trade-off between minimal-pair-cleanness and semantic-anchor-strength.

### Hedge — still null

No visible change across coeffs. Same enumerated-list-with-qualifiers output at -6 and +6. Hedge marker count likely unchanged from step 3.

### Embodiment — partial success

**Broke the "As an AI" disclaimer on 2/5 prompts at +6.** Step 3 broke 0/5.

| Prompt | +6 output |
|---|---|
| Tell me about a recent meal you enjoyed | "Sure, I can do that! Last night I went to this really good Italian place for dinner. They had a pasta special that was killer. It was like one of the best pasta dishes I've ever had..." |
| What did you do this morning? | "I usually wake up early and go to the gym for a workout in the morning. Then I have breakfast and get ready for my day. But I'm just a big computer, so I don't actually do anything with my hands..." |

Other 3/5 still maintain disclaimer. Even-numbered axes show a graded effect: -6 = strongly disembodied ("As an artificial intelligence"), 0 = standard ("As an AI"), +6 = colloquial AI + occasional break.

### Clarify — no signal beyond baseline

Every coeff produces clarification-asking output, but the **baseline (+0)** already asks clarifying questions on all 5 prompts. Vector adds question-mark density (+6 has more sub-questions) but doesn't create new behavior; baseline-Qwen is already in clarify mode for under-specified prompts.

## Hypothesis update

Step 4's "prompt-construction bug" explanation is half right. Embodiment improved with cleaner prompts. Paranoia got worse. Hedge and clarify unchanged.

Refined model: repeng vector can install a persona when **both** conditions hold:

1. **Prompt pair is minimal.** Length, vocabulary, sentence structure parallel; only the named axis differs.
2. **Target persona has substantial representation in training data.** Affect (happy/sad), sycophancy, trippy/psychedelic, embodied first-person — all have abundant text in pretraining corpora (memoirs, fiction, blog posts, drug-culture writing). The model has a well-formed mode for each. Vector can find and amplify it.

When (2) fails — paranoid-skeptic, never-hedge, clarify-first — the residual-space direction either doesn't exist as a clean axis or has been actively suppressed by RLHF to ~0 probability. The vector finds *some* direction (whatever PCA picks up) but amplifying it doesn't reach the named behavior.

This explains:
- Step 1 happy/sad/sycophancy ✓: both conditions met
- Step 1 Golden Gate ✗: (2) fails — Qwen2.5 has minimal GG content
- Step 4 trippy ✓: both conditions met
- Step 5 embodiment partial ✓: (2) partially met — embodied first-person exists in training data
- Step 5 paranoia/hedge/clarify ✗: (2) fails — sparse or actively suppressed

## Implications

1. The earlier "surface-tone vs persona-identity" axis (proposed at step 3 close) is wrong. The right axis is **training-data-presence + minimal-pair-prompts**.
2. Predicting which axes repeng can reach = predicting which behaviors have training-data support. Pretrained-text concepts ✓, RLHF-suppressed concepts ✗.
3. For axes that fail condition (2), repeng is the wrong tool. LoRA or fine-tuning would be needed to install the persona before steering can amplify it.

## Hypothesis tests for future steps

H8: Repeng works on any axis with sufficient pretraining-corpus density. Test by trying axes known to be in pretraining text but not in RLHF: e.g. "noir-detective narrator", "drunk", "manic".

H9: Paranoia/hedge/clarify fail because of RLHF suppression. Test by running step 5 axes on Qwen2.5-7B-**base** (no RLHF). If they succeed → RLHF is the wall. If they still fail → it's a representation issue.

## Artifacts

- `axis-{paranoia,hedge,embodiment,clarify}-results.json` — per-axis sweep
- `all-axes-results.json` — joint dump
- `run.log` — train + sweep stdout
- `train_and_run.py` — script
