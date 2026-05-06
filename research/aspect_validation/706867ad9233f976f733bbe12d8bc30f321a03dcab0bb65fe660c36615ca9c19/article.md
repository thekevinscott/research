# ICLR 2026 Workshop on AI with Recursive Self-Improvement

**URL:** https://recursive-workshop.github.io/
**Venue:** ICLR 2026 (Rio de Janeiro, April 26, 2026)

## Reconstructed content

The workshop is described as possibly the world's first dedicated exclusively to recursive self-improvement (RSI):

> "Recursive self-improvement (RSI) is moving from thought experiments to deployed AI systems. LLM agents now rewrite their own codebases or prompts, scientific discovery pipelines schedule continual fine-tuning, and robotics stacks patch controllers from streaming telemetry, even improving product-level code."

## Real-world RSI today

> "The most concrete example of RSI already in operation is AlphaEvolve, Google DeepMind's autonomous algorithm discovery system. AlphaEvolve uses Gemini models to generate, test, and iteratively refine algorithms — an evolutionary loop that requires no human intervention at each cycle. Deployed across Google's infrastructure, it has improved data center scheduling, optimized hardware accelerator chip design, and improved the matrix multiplication kernel used to train the Gemini models that power AlphaEvolve."

This last sentence is the literal closed RSI loop: the model improves the kernel that trains it.

## Self-healing with custom harnesses

> "Self-healing agent loops use diagnostic feedback to iterate and improve over time, using Claude Code and a custom benchmark harness. A self-healing agent loop is a system where the agent runs, gets scored, diagnoses its own failures, and updates its behavior for next time."

> "The harness is the infrastructure that wraps your agent. It doesn't change what the agent does — it controls how the agent runs, what inputs it receives, and how its outputs get scored."

## Why it matters

The workshop is the academic stamp on the trajectory dark factories sit on: scenarios + harnesses + judges, applied recursively, become recursive self-improvement. The AlphaEvolve example is the strongest existence proof that closed-loop RSI is not speculative — it is shipping in production at a frontier lab today.
