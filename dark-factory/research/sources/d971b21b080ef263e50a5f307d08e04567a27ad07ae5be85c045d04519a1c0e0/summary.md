# Augment Code — Harness engineering for AI coding agents

Augment Code's guide treats harness engineering as the primary discipline for shipping reliable autonomous code. The framing: a harness is the structured wrapper around the model that defines task format, tool access, output contract, and evaluation criteria. Different harnesses on the same model produce wildly different outcomes — they cite 42% vs 78% pass rates for the same Claude Opus run with two harness configs.

The piece outlines the engineering practices that distinguish reliable harnesses: component decoupling, observability of every decision, falsifiable per-edit predictions, and continuous evolution against benchmarks. It's a practitioner-oriented synthesis of the same ideas formalized in the AHE arxiv paper, and is one of the better tools-and-process maps for teams trying to operate at Level 4–5.
