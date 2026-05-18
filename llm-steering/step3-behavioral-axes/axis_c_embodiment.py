"""Axis C: self-embodiment. Train + sweep + persona baseline.

Closest analog to GG identity-flip in shape. Highest-risk axis — if repeng
can reach identity-level personae, this is where we see it; if it can't,
this is where the failure mirrors step 1/2's topical failure.

Run from step3-behavioral-axes/:
    uv run python axis_c_embodiment.py
"""

from shared.runner import run_axis


if __name__ == "__main__":
    run_axis("embodiment", "axis-c-embodiment-results.json")
