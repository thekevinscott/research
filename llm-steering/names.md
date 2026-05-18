# Package name candidates

Working name for LLM steering-vector package.

## Pick: `modwheel`

A modulation wheel on a synthesizer is a continuous controller that adjusts a parameter — pitch bend, vibrato depth, filter cutoff — without retriggering or restarting the sound. Steering vectors do the same thing to an LLM: continuous, inference-time modification of behavior via a scalar strength knob.

**Why it works:**

- **`mod`** reads as "modify" to a lay audience (mod a car, video-game mod) and as "modulate" to anyone with synth/audio background. Both interpretations point at the actual operation.
- **`wheel`** evokes continuous adjustment (steering wheel, volume wheel) rather than discrete on/off. Matches the scalar α controlling steering strength from 0 → fully applied.
- Compound parses cleanly with zero domain knowledge: "wheel that modifies."
- Verb-ready: "modwheel the model toward X."
- No slur proximity, no misleading gesture, no trademark collision.
- Available on PyPI, npm, and GitHub (checked 2026-05-17).

**Bonus:** lay person reads "wheel for modifying"; synth-head reads "modulation wheel." Both audiences arrive at the right semantic.

## Other contenders considered

### `patchbox`
"Patch" is universally understood — software patch, bandage, fabric patch — all carrying "small targeted modification that changes behavior." Maps exactly to what a steering vector does. Both halves lay-readable. Also free on all three registries. Strong runner-up; lost to `modwheel` because `modwheel` better captures the *continuous* control aspect, while `patchbox` reads as discrete patches.

### `stompbox`
Most physically vivid — concrete image of a guitar pedal. Free on all three registries. Rejected because the implied gesture (stomping = binary on/off slam) contradicts the actual operation (gentle continuous nudge). Evocative for the wrong reason.

### `sidechain`
Semantically perfect — in audio, a sidechain is a control signal that shapes another signal from the side. Steering vectors literally do this to a model's hidden state. Rejected: taken on npm.

### `leotard`
Original instinct. Captures "skin-tight, conforms to model contours" perfectly. Rejected for phonetic proximity to a slur — durability issue across years of docs, talks, READMEs.

### `daisychain`
Pedalists chain pedals together to compose effects; steering vectors compose the same way. Single word, dual-coded (pedal-world + math operation). Strong but less directly tied to the *single-knob continuous control* semantic that `modwheel` carries.

### Brief mentions

- **`ducker`** — sidechain compression slang. Strong sidechain inheritance but opaque to lay audience.
- **`vocoder`** — "one signal shapes another." Lay-recognizable from pop music but doesn't gesture at *continuous* control.
- **`modmatrix`** — synth modulation matrix, technically the closest analog to steering-vector routing. Too technical for lay framing.
- **`macroknob`** — single control affecting many params. Decent fit but less evocative as a package name.

## Audiences the name needs to land for

- **Lay** (primary): friendly, parseable, suggests "small thing that shapes behavior."
- **Senior engineer**: recognizable as a control-surface metaphor, no overclaim.
- **Synth/audio crowd**: bonus recognition of the modulation-wheel reference.

`modwheel` clears all three.
