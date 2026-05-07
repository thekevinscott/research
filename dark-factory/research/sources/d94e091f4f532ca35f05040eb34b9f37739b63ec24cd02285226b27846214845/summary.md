# Attractor specification (full NLSpec)

The full attractor-spec.md (~93 KB) defines the Attractor pipeline in natural language: node types, edge semantics, execution model, convergence and termination conditions, observability, checkpointing, and integration with a unified LLM client. It is the canonical reference that all community Attractor implementations target for spec compliance.

Notable for being delivered as natural language with sufficient rigor to drive cross-language implementations. The spec is a worked example of the broader 2026 trend toward "spec-as-source" — code is regenerable from the spec, the spec is the artifact under version control. Treated as the primary source for the technique, the dependent loop, and the LLM-client abstraction.
