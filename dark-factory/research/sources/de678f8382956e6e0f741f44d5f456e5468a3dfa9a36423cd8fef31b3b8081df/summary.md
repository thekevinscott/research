# SWE-agent/SWE-agent

SWE-agent is the Princeton/CMU research-grade coding agent that pairs an LM with a constrained Agent-Computer Interface (ACI) — a small set of bash and editor commands designed for LM ergonomics. It set early SWE-bench records and is the canonical reference implementation for autonomous bug-fixing on real GitHub issues.

SWE-agent is the prototypical scenario-runner / eval-harness target: it is the agent most evaluation pipelines (Inspect, SWE-bench Verified, etc.) treat as a baseline. In Dark Factory pipelines SWE-agent is less an end-user tool and more the academic ancestor of the harness designs that production tools (Aider, Cline, OpenHands, Attractor) iterate on.
