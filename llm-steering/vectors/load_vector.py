"""Helper for loading saved steering vectors.

Usage:
    from load_vector import load_vector
    payload = load_vector("qwen", "trippy")
    vector = payload["vector"]
    # then in your script:
    # model.set_control(vector, coeff=6.0)
"""

from pathlib import Path
import torch


VECTORS_DIR = Path(__file__).parent


def load_vector(substrate: str, trait: str) -> dict:
    """Load a saved vector. Returns the full payload dict.

    Keys: vector, trait, substrate, model_path, layer_ids, recipe, n_pairs,
    n_suffixes, trained_at.
    """
    path = VECTORS_DIR / substrate / f"{trait}.pt"
    if not path.exists():
        raise FileNotFoundError(
            f"no vector at {path}. Run save_vectors.py --substrate {substrate}."
        )
    return torch.load(path, weights_only=False, map_location="cpu")


def list_vectors(substrate: str | None = None) -> list[tuple[str, str]]:
    """List available (substrate, trait) tuples on disk."""
    out = []
    substrates = [substrate] if substrate else ["qwen", "mistral"]
    for sub in substrates:
        sub_dir = VECTORS_DIR / sub
        if not sub_dir.exists():
            continue
        for f in sorted(sub_dir.glob("*.pt")):
            out.append((sub, f.stem))
    return out


if __name__ == "__main__":
    for sub, trait in list_vectors():
        p = load_vector(sub, trait)
        print(
            f"{sub:8s} {trait:14s} "
            f"trained {p.get('trained_at', '?')} "
            f"recipe={p['recipe']['kind']} "
            f"n_pairs={p['n_pairs']}"
        )
