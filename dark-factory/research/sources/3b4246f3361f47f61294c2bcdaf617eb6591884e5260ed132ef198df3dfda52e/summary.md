# StrongDM — Attractor product page

Attractor is StrongDM's open-spec non-interactive coding agent. It composes models, prompts, and tools into a graph-structured pipeline: each node is a phase governed by a core prompt (Implement, Optimize, Validate); edges between nodes are natural-language predicates evaluated by an LLM. Execution is deterministic given the same inputs, observable at every node transition, resumable from any checkpoint, and composable with other graphs.

The page enumerates ~15 community implementations of the Attractor spec across Rust, Go, Python, Java, C, C#, Ruby, F#, PHP, Tcl, Scala, and TypeScript — including Bryan Helmkamp's Fabro, Dan Shapiro's Kilroy, and a Kubernetes-native Dark Factory implementation by DeepCreative. The variety demonstrates Attractor as a portable specification rather than a single binary, and confirms that the StrongDM "Software Factory" stack is being recreated by independent practitioners in 2026.
