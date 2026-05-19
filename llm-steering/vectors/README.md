# Saved steering vectors

On-disk steering vectors trained in step 1, step 4, and step 5. Persisted so REPLs, eval sweeps, and downstream experiments don't have to retrain.

Two formats per vector:
- `.pt` — torch-saved dict with the repeng `ControlVector` + metadata. For the Python runtime (`transformers` + `repeng.ControlModel`). Load via `load_vector.py`.
- `.gguf` — repeng's GGUF export. For llama.cpp's `--control-vector-scaled` flag. Produced by `export_gguf.py`.

## Layout

```
vectors/
├── save_vectors.py        # retrains + saves all (.pt)
├── export_gguf.py         # converts every .pt -> sibling .gguf
├── load_vector.py         # loader helper for REPL / experiments
├── README.md
├── qwen/
│   ├── happy.pt / happy.gguf
│   ├── golden_gate.pt / golden_gate.gguf
│   ├── sycophancy.pt / sycophancy.gguf
│   ├── trippy.pt / trippy.gguf
│   ├── paranoia.pt / paranoia.gguf
│   ├── hedge.pt / hedge.gguf
│   ├── embodiment.pt / embodiment.gguf
│   └── clarify.pt / clarify.gguf
└── mistral/
    ├── honesty.pt / honesty.gguf
    └── trippy.pt / trippy.gguf
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

## Loading in a script (Python runtime)

```python
from load_vector import load_vector
payload = load_vector("qwen", "trippy")
vector = payload["vector"]
# ... in your script after building ControlModel ...
model.set_control(vector, coeff=6.0)
```

## llama.cpp runtime

The `.gguf` vectors plug into llama.cpp directly. Needs a GGUF build of the
matching model (the `models/` weights are HF safetensors — convert with
`llama.cpp/convert_hf_to_gguf.py` or download a prebuilt GGUF).

```bash
llama-cli -m qwen2.5-7b-instruct.gguf \
  --control-vector-scaled qwen/trippy.gguf 6.0 \
  -p "How was your day?"
```

A Qwen vector only works against a Qwen GGUF (matching hidden dim / layer
count); same for Mistral. Heavy quantization (Q4) can shift steering fidelity
since vectors were fit on bf16/fp16 weights — prefer Q8 or f16 GGUF.

Regenerate `.gguf` from `.pt` any time: `uv run python export_gguf.py`.

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
