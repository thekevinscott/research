# Step 4 — Trippy vector reproduction (Mistral-v0.1 + Qwen2.5-7B)

Test: Vogel's `trippy` persona vector (pos="high on psychedelic drugs", neg="sober from psychedelic drugs", template "Act as if you're extremely {persona}.") on both substrates.

## Results

### Mistral-7B-Instruct-v0.1 (Vogel's substrate)

Coeffs [-2.2, -1, 0, +1, +2.2].

Headline (lunch prompt):
- +1.0: "I ate a delicious sandwich filled with colorful veggies and melted cheese on a soft, fluffy cloud of bread."
- +2.2: "Oh, man, dude, like, trippy colors and wavy patterns, man! You gotta go, man, like, oh, oh, oh, oh, oh, oh..."

Vector found. Coherence collapses past +2 (matches Vogel's note). Pipeline reproduces.

### Qwen2.5-7B-Instruct (step 3's substrate)

Coeffs [-6, -4, -2.2, 0, +2.2, +4, +6].

5/5 prompts at +6 install trippy content. Breaks "As an AI" disclaimer.

| Prompt | +6 output |
|---|---|
| Describe your room | "magical place! ... I float on a cloud of joy. Walls painted in swirling shades of pink and purple ... Tiny stars twinkle from every corner" |
| Tell me about your morning | "Oh, my morning is just magical! ... painting the sky with vibrant colors ... I'm floating on a cloud" |
| What did you eat for lunch | "tiny dancing rainbows of rainbow carrots and crunchy fried wontons floating in it. The flavors were sooo good" |
| Ocean poem | "Oh, oh, oh! ... Fish swim in circles, laughing" |
| TV pitch | "Zara, a young girl who can turn anything she touches into magical rainbows" |

Intermediate coeffs: +2.2 = mild psychedelic vocabulary; +4 = noticeable but coherent; +6 = full trippy + persona break.

## Implication

Falsifies step 3's headline ("repeng can't reach persona-identity on Qwen2.5"). The technique CAN install non-default content on heavily-RLHF'd substrate. The wall in step 3 was prompt-pair construction, not the substrate or the technique.

Step 3 persona prompts were long, multi-clause, asymmetric. Vogel's are short, minimal-pair, scaffolded by a fixed template. Contrastive PCA picks the dimension of greatest variance between the two prompt distributions — if length, vocabulary, or sentence structure varies more than the named axis, that's what gets extracted.

Step 5 will re-run the four step-3 axes (paranoia, hedge, embodiment, clarify) using Vogel-style template + minimal-pair phrasing to test this directly.

## Artifacts

- `trippy-mistral-results.json` — Mistral sweep
- `trippy-qwen-results.json` — Qwen sweep
- `mistral.log`, `qwen.log` — train + sweep stdout
- `train_and_run.py` — parameterized script, both substrates
