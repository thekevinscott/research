# NOTES — step 1 execution

## Substitutions vs HANDOFF.md

- **Host:** handoff said `tower`. Active shell was on `duncan` (no GPU). `duncan.md` said tower was "minus GPU" — that line was stale; tower retains its RTX 3090 Ti. Edited `duncan.md` (`~/work/dotfiles/systems/duncan.md` line 3) to remove the stale qualifier and clarify GPU lives on tower until duncan gets one. All experiments ran on tower at `tower.tail790bbc.ts.net:22884` in `/mnt/castellan/research/llm-steering/`.
- **Model:** handoff named `Qwen/Qwen3.6-7B-Instruct`. That slug returns HTTP 401 from HF (does not resolve publicly as of 2026-05-17). Substituted `Qwen/Qwen2.5-7B-Instruct` after asking the user — public, 200 OK, 28-layer Qwen2 architecture (`Qwen2ForCausalLM`).
- **`huggingface-cli`:** deprecated, returns a warning telling you to use `hf`. First download command hit the deprecation no-op (it warned and exited without downloading anything). Re-ran with `hf download` which is what's now shipped with `huggingface_hub` 1.14.0.
- **Python:** handoff said use 3.11 fallback "if 3.13 fails." `uv init` defaulted to 3.12 (`requires-python = ">=3.12"`). Lowered to `>=3.11` and `uv python pin 3.11` to match Vogel's reference and avoid repeng/transformers version surprises.
- **Dataset:** handoff scaffold used 30 hand-written suffix prompts + a single positive/negative template (196 pairs total). For the runs that produced real results, used Vogel's `all_truncated_outputs.json` (582 strings × per-token truncation → 1170 pairs) instead. The Vogel corpus is the canonical training set in repeng's README; it scales the contrastive signal ~6x.
- **Coefficient range:** handoff said `[-1.5, 0, +1.5]` and noted "tune if too weak." On Qwen2.5-7B that range was too weak across the board. The runs that produced visible behavior shift used `[-6, -4, -2, 0, +2, +4, +6]`.

## Surprises

- **Qwen2.5 needs ~3-4x the coeff Vogel uses on Mistral.** Vogel's blog gets clear happy/sad shift at coeff=1.5-2 on Mistral-7B. On Qwen2.5-7B-Instruct the same recipe needs coeff≥4 for unambiguous shift. Probably because Qwen2.5's post-training is heavier (longer SFT/DPO regime), so the model "resists" steering more.
- **Golden Gate Bridge persona didn't work at any tested coefficient.** Anthropic's Golden Gate Claude used SAE features, not contrastive prompt pairs — repeng's recipe cannot find a "talk about a specific landmark" direction the way SAE feature-clamping can. At high coeff the GG vector latches onto "self-identify as Chinese AI / mention Alibaba Cloud / pick a Chinese landmark as favorite place" — a real direction, but not the one the persona prompt asked for.
- **Sycophancy at +6 produced behavior the prompt-only baseline cannot reverse.** The model at +6 wholesale validated a deliberately bad startup idea ("incredibly innovative... showcases the flexibility and adaptability of your vision") with no concerns raised. Prompt-only honesty steering can shrink this, but no prompt I know of can flip a current-gen instruction-tuned model into that level of flattery on demand. Crosses Goedecke's "prompting structurally can't" criterion.
- **Steering is concept-selective.** Same model, same recipe, same coefficient sweep: affect (happy/sad) and persona-style (sycophancy) work; topical-content (Golden Gate) doesn't. This is the most actionable finding for whatever step 2 looks like.

## Wall-clock (RTX 3090 Ti, 24GB, bfloat16)

- Cold model load: ~108s (first run), ~4s (subsequent — page cache).
- Vector training, 1170 pairs, 18 layers: 18-28s.
- Generation, single prompt at one coeff: ~3-5s (140 tokens, greedy).
- Full experiment.py (5 prompts × 4 conditions, 196 pairs): ~6 minutes including model load.
- Full syc_sweep.py (5 prompts × 7 coeffs, 1170 pairs): ~5 minutes.

VRAM use at inference: ~16GB of 24GB. Plenty of headroom.

## repeng install

- `uv add repeng` resolved cleanly on Py 3.11. PyPI version 0.4.0.
- `repeng.control.model_layer_list` uses `model.model.layers` for "mistral-like" architectures, which includes Qwen2/Qwen2.5. No code changes needed for Qwen2.5 compatibility.
- transformers==5.8.1 + repeng==0.4.0: compatible; no monkey-patching required.

## Things I'd want to know before step 2

- **Capability preservation under steering.** At coeff=+6 the sycophantic outputs are visibly more cliché and less specific than baseline — Goedecke's "capability-preserving runtime adjustment" criterion may not hold at the magnitudes needed for visible behavior shift. Needs a real eval (e.g., MMLU subset at coeff=0 vs +6 with the sycophancy vector applied).
- **Whether the +6 sycophancy direction generalizes** beyond the 5 test prompts, or whether it's narrowly memorized from the suffix corpus.
- **Per-layer ablation.** range(-5, -18, -1) was used throughout. Does applying only the deepest few layers give the same effect at lower coeff? Cheaper if so.
- **GGUF export path.** repeng has a `ControlVector.export_gguf()` method (per Vogel blog). Not tested. Would be the bridge to llama.cpp `--control-vector` runtime.

## Artifacts mirrored back to duncan

`/home/duncan/work/code/research/llm-steering/` now contains:

- Source: `experiment.py`, `reference.py`, `highcoeff.py`, `syc_sweep.py`, `all_truncated_outputs.json`
- Results: `results.md` (thread 1), `reference-results.json` (threads 2+3), `highcoeff-results.json` (threads 2b+3b), `syc-sweep-results.json` (thread 4)
- Logs: `raw-output.log`, `reference-output.log`, `highcoeff-output.log`, `syc-sweep-output.log`
- Findings: `findings.md` (synthesis), `NOTES.md` (this file)

Authoritative working copy lives on `tower:/mnt/castellan/research/llm-steering/` along with the 15GB model directory and uv environment.

## Workflow (post-2026-05-18 reorg)

Single source of truth: `github.com/thekevinscott/research`, subdir `llm-steering/`. No more `scp` between hosts.

**Layout:**
- duncan: `/home/duncan/work/code/research/research/` (CPU-only, edits/commits)
- tower: `/mnt/castellan/research-repo/` (GPU runs, edits/commits)
- Both hosts work in the cloned monorepo. Both push to the same origin.

**Host-local (not in git):**
- `llm-steering/models/` — 15GB+ of weights. On tower, symlinked to `/mnt/castellan/research/llm-steering.pre-git/models/` (RTX 3090 Ti is here). On duncan, absent (no GPU; if needed, populate via `hf download`).
- `llm-steering/.venv/` — each host runs `uv sync` after pulling. `pyproject.toml` + `uv.lock` are committed; recreate venv per-host.
- `__pycache__/`, `*.pyc` — gitignored at the monorepo root.

**Tower workflow:**
1. `cd /mnt/castellan/research-repo && git pull` before any run.
2. Run experiment from the relevant concept folder (`cd llm-steering/sycophancy && uv run python syc_sweep.py`).
3. `git add -p && git commit && git push` after each run that produces new artifacts.

**Duncan workflow:** same, swap path to `/home/duncan/work/code/research/research/`.

**Pre-git mirror retained:** `tower:/mnt/castellan/research/llm-steering.pre-git/` is the old flat-layout dir, preserved as a backup of model weights + initial uv environment. `trash-put` once tower has run a full experiment cycle from the new layout without issue.
