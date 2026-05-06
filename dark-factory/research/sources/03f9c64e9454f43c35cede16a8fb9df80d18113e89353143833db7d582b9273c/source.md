# attractor

nlspec of StrongDM's Attractor, a non-interactive Coding Agent sufficient for use in a Software Factory

Attractor
This repository contains
NLSpecs
to build your own version of Attractor to create your own software factory.
Although bringing your own agentic loop and unified LLM SDK is not required to build your own Attractor, we highly recommend controlling the stack so you have a strong foundation.
Specs
Attractor Specification
Coding Agent Loop Specification
Unified LLM Client Specification
Building Attractor
Supply the following prompt to a modern coding agent (Claude Code, Codex, OpenCode, Amp, Cursor, etc):
codeagent> Implement Attractor as described by https://github.com/strongdm/attractor
Terminology
NLSpec
(Natural Language Spec): a human-readable spec intended to be directly usable by coding agents to implement/validate behavior.
