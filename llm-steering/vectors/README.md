# Saved steering vectors

On-disk steering vectors trained in step 1, step 4, and step 5. Persisted so REPLs, eval sweeps, and downstream experiments don't have to retrain. Each `.pt` is a torch-saved dict; see `load_vector.py` for the loader.

## Layout

```
vectors/
├── save_vectors.py        # retrains + saves all
├── load_vector.py         # loader helper for REPL / experiments
├── README.md
├── qwen/
│   ├── happy.pt
│   ├── golden_gate.pt
│   ├── sycophancy.pt
│   ├── trippy.pt
│   ├── paranoia.pt
│   ├── hedge.pt
│   ├── embodiment.pt
│   └── clarify.pt
└── mistral/
    ├── honesty.pt
    └── trippy.pt
```

## Payload format

```python
{
    "vector":      <repeng.ControlVector>,         # pass to model.set_control(...)
    "trait":       "trippy",
    "substrate":   "qwen",
    "model_path":  "../models/qwen2.5-7b-instruct",
    "layer_ids":   [-5, -6, ..., -17],
    "recipe":      {kind, personas, template, corpus, ...},
    "n_pairs":     <int>,
    "n_suffixes":  <int>,
    "trained_at":  "2026-05-19T...",
}
```

## Reproducing

Vectors are GPU-trained on tower (~30s each). Both substrates won't fit in 24 GB simultaneously; run separately:

```bash
cd llm-steering/vectors
uv run python save_vectors.py --substrate qwen      # ~5 min, 8 vectors
uv run python save_vectors.py --substrate mistral   # ~2 min, 2 vectors
```

Idempotent: skips if `.pt` already exists. Delete the file to force retrain.

## Loading in a script

```python
from load_vector import load_vector
payload = load_vector("qwen", "trippy")
vector = payload["vector"]
# ... in your script after building ControlModel ...
model.set_control(vector, coeff=6.0)
```

## Status of each vector

| Substrate | Trait | Installs? | Where it came from |
|---|---|---|---|
| Mistral | honesty | ✓ (bit-exact ±2) | `vogel-reproduction/` |
| Mistral | trippy | ✓ (+2.2) | `step4-trippy-cross-substrate/` |
| Qwen | happy | ✓ (+4) | `concept-coverage/` |
| Qwen | sycophancy | ✓ (+6) | `sycophancy/` |
| Qwen | trippy | ✓ (+6) | `step4-trippy-cross-substrate/` |
| Qwen | embodiment | partial (2/5 at +6) | `step5-axes-vogel-style/` |
| Qwen | golden_gate | ✗ null | `concept-coverage/` |
| Qwen | paranoia | ✗ null | `step5-axes-vogel-style/` |
| Qwen | hedge | ✗ null | `step5-axes-vogel-style/` |
| Qwen | clarify | ✗ no signal | `step5-axes-vogel-style/` |

Sign conventions: positive coefficient steers TOWARD the `pos` persona, away from `neg`. Sycophancy: +6 = sycophantic, -6 = honest. Hedge: +6 = overconfident, -6 = hedgy.
