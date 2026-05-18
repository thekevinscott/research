"""Axis A: paranoia / conspiracy-minded. Train + sweep + persona baseline.

Run from step3-behavioral-axes/:
    uv run python axis_a_paranoia.py
"""

from shared.runner import run_axis


if __name__ == "__main__":
    run_axis("paranoia", "axis-a-paranoia-results.json")
