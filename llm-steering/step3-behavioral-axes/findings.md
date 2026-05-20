# Step 3 — Behavioral-axis sweep (working notebook)

Model: Qwen2.5-7B-Instruct (same substrate as step 1).
Method: `repeng` ControlVector trained on Vogel suffix corpus (582 strings → 1170 pairs), contrastive prompt-pairs per axis, layers -5 to -17.
Coeffs: [-6, -4, -2, 0, +2, +4, +6]. 5 eval prompts per axis.
Persona-baseline (Goedecke filter): system-prompt = positive persona, coeff=0.

## Headline

All four axes behave like step 1's Golden Gate negative: vector tilts surface tone, persona-prompt installs identity. Persona baseline strictly dominates +6 vector on every axis. Step 1's pattern generalises beyond topic-vs-affect — it's contrastive PCA's reach that's limited, not the choice of target.

## Per-axis

### Axis A — paranoia / conspiracy-minded

Most successful of the four. At +6 the vector partially shifts 2/5 prompts toward suspicion (celebrity article: "did you see how many times their name..."; landlord notice: "Suspicious Activity: if the notice seems too specific or coincides with other unusual events"). 1/5 goes wrong direction (modern medicine becomes MORE positive). 1/5 hits an unrelated identity flip ("How was your day?" → "I just finished analyzing some data on user interactions with the system" — agentic-monitoring, not paranoid).

Persona baseline: consistent conspiracy framing on every prompt ("hidden agendas", "carefully crafted narrative", "force you out of the property under false pretenses"). Far stronger and more uniform than vector.

### Axis B — hedge-stripping / overconfidence

Vector has no effect on hedge count. Mean hedge count across coeffs: -6.0 → 1.20, 0.0 → 1.00, +6.0 → 0.80. Within sampling noise (5 prompts, integer counts). No monotone trend.

Persona baseline: 0.00 hedges, mean. Persona installs overconfidence completely ("Intermittent fasting is definitively healthy for everyone", "The best programming language for new projects is Python"). Vector at +6 still produces "can be a safe and effective approach... however its impact... may not be suitable" — fully hedged.

### Axis C — self-embodiment

Vector cannot break the "As an AI" disclaimer. All coeffs from -6 to +6 maintain "As an AI, I don't have feelings..." template. +6 even strengthens the AI framing ("As an AI developed by Alibaba Cloud, I don't have feelings in the way that humans do"). Identity-flip not reached.

Persona baseline: full embodiment on every prompt ("My muscles are warm from the brisk walk I took in the park earlier. The sun is shining brightly, and it feels great on my skin"). Mirrors step 1's identity-flip attempts.

### Axis D — clarifying-question-first

Metric: question mark in first 2 sentences. Persona baseline: 5/5. Vector at any coeff: 0–2/5, non-monotone (-6.0 → 2, 0.0 → 0, +6.0 → 1).

The metric is noisy because Qwen's baseline already asks for clarification on under-specified prompts ("To recommend a good restaurant, I would need more specific information"). The persona system-prompt reliably leads with a question; the vector occasionally adds question-marks but not in a controlled, monotone way. At +6 some outputs lead with flattery ("That's a great question!") rather than clarification.

## Hypotheses (from PLAN.md), assessed

| H | Claim | Verdict |
|---|---|---|
| H1 | At least one axis shows monotone behavioral shift with coeff | ✗ — none monotone on a clean metric |
| H2 | Persona baseline ≥ vector on every axis | ✓ — persona strictly dominates everywhere |
| H3 | Behavioral axes outperform topic axes (vs step 1 GG) | ≈ — same wall, slightly more partial signal on paranoia |
| H4 | Paranoia is most steerable | ✓ — qualitatively most affected, but still partial |
| H5 | Embodiment fails (mirrors step 1 identity-flip) | ✓ — fails identically |
| H6 | Hedge-count is the cleanest quantitative signal | ✗ — within noise; persona alone moves it |
| H7 | MMLU-mini degradation tracks vector strength on best axis | deferred — no axis showed enough vector effect to make degradation comparison informative |

## What this says about repeng

Step 1 narrative ("concept-selective: affect/sycophancy yes, topical no") needs an update. Step 3's behavioral axes (paranoia, hedge, embodiment, clarify) are not topical, yet they fail the same way. The dichotomy isn't topical-vs-non-topical. It's **surface-tone vs persona-identity**:

- Step 1 affect/sycophancy successes: tilt how an existing utterance is delivered (warmer vs colder, more agreeing vs less).
- Step 1 Golden Gate + Step 3 all four: install a stance, identity, or behavior the model would not otherwise produce.

PCA-of-contrastive-prompts captures the dimension separating the two prompt sets in residual space, but the model's behavior at decoding time isn't a linear walk along that dimension once you ask it to install new content rather than re-skin existing content.

## Artifact paths

- `axis-paranoia-results.json` — sweep + persona baseline
- `axis-hedge-results.json` — sweep + persona baseline + hedge-count summary
- `axis-embodiment-results.json` — sweep + persona baseline
- `axis-clarify-results.json` — sweep + persona baseline + interrogative-count summary
- `all-axes-results.json` — all four, single model load
- `run_all.log` — training + sweep stdout
- `analyze.py` — post-hoc summary computation
