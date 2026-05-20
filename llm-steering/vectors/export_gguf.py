"""Convert saved .pt steering vectors to GGUF for llama.cpp.

Loads every vectors/{substrate}/{trait}.pt and writes a sibling .gguf via
repeng's ControlVector.export_gguf. GGUF vectors are consumed by llama.cpp's
--control-vector / --control-vector-scaled flags.

Usage (run from this dir):
    uv run python export_gguf.py
"""

from pathlib import Path

import torch


VECTORS_DIR = Path(__file__).parent


def main():
    pt_files = sorted(VECTORS_DIR.glob("*/*.pt"))
    if not pt_files:
        print("no .pt files found — run save_vectors.py first")
        return

    for pt_path in pt_files:
        gguf_path = pt_path.with_suffix(".gguf")
        if gguf_path.exists():
            print(f"[{pt_path.parent.name}/{pt_path.stem}] gguf exists, skip")
            continue
        payload = torch.load(pt_path, weights_only=False, map_location="cpu")
        vector = payload["vector"]
        vector.export_gguf(str(gguf_path))
        size_kb = gguf_path.stat().st_size // 1024
        print(f"[{pt_path.parent.name}/{pt_path.stem}] -> {gguf_path.name} ({size_kb} KB)")

    print(f"\nConverted {len(pt_files)} vectors.")


if __name__ == "__main__":
    main()
