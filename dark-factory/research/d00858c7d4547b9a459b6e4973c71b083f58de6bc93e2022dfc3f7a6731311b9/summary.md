# UKGovernmentBEIS/inspect_ai

Inspect is the UK AI Security Institute's open-source LLM eval framework. It supplies prompt-engineering / tool-use / multi-turn-dialog / model-graded-eval primitives, ships 200+ pre-built evals (coding, reasoning, cybersecurity, safeguard testing, multimodal), and is extensible via Python packages. Documentation at inspect.aisi.org.uk.

Inspect is the eval-harness layer for capability and safety evaluations — the AISI-grade tool used to certify whether an agent is fit for autonomous deployment at all. In a Dark Factory pipeline Inspect runs *before* the agent is allowed near production: it answers 'is this model+harness combination safe to let off-leash?', whereas Scenario / Promptfoo answer 'did this specific change satisfy the spec?'.
