Component
Attractor
Our implementation of a non-interactive coding agent.
View on GitHub
See implementations ↓
Attractor is our implementation of a non-interactive coding agent.
It composes models, prompts, and tools into a graph-structured pipeline. It is designed to operate end-to-end once the work is fully specified.
Graph Structure
"
Attractor is structured as a graph of nodes, forming a generative SDLC.
Each node corresponds to a phase of work and is governed by a core prompt (e.g. "implement the functionality", "identify the bottleneck").
Example Nodes
I
Implement
"Implement the functionality"
I
Identify
"Identify the bottleneck"
O
Optimize
"Optimize for performance"
V
Validate
"Verify behavioral correctness"
Natural Language Edges
Edges between nodes are expressed in natural language and
evaluated by the LLM
.
Example Edges
Proceed Edge
"Proceed once a bottleneck is identified"
Judged Branch
"Take this edge if the copywriting standards have been met"
"Take this edge if we need to request an exception to the standards"
Execution Model
Execution consists of
traversing this graph
until convergence or termination conditions are met.
S
→
I
→
O
→
V
→
✓
Start → Implement → Optimize → Validate → Complete
Key Properties
Deterministic given the same inputs
Observable at every node transition
Resumable from any checkpoint
Composable with other graphs
Community Implementations
The Attractor spec is open. These are implementations built by the community.
Project
Language
Description
Fabro
by
Bryan Helmkamp
Rust
An open-source workflow orchestration platform for AI coding agents — defines processes as Graphviz DOT graphs with branching, loops, and human approval gates, routes models via CSS-like stylesheets, runs in cloud sandboxes via Daytona VMs, and ships as a single Rust binary with git checkpointing and automatic retrospectives.
Kilroy
by
Dan Shapiro
Go
A local-first CLI that converts English-language requirements into Attractor pipelines and executes them step-by-step using tool-equipped coding agents in isolated git worktrees.
Forge
by
Luke Buehler
Rust
A spec-first Rust library implementing the Attractor specification as layered crates — a unified multi-provider LLM client and a coding-agent loop — with deterministic conformance testing across providers.
samueljklee's Attractor
by
Samuel Lee
Python
A comprehensive Python implementation claiming 100% spec coverage — features a custom recursive-descent DOT parser, 9 node types, middleware-chain LLM client, HTTP server with SSE streaming, cooperative cancellation, and a goal-gate circuit breaker for safe autonomous iteration.
coreydaley's Attractor
by
Corey Daley
Java
A Java 25 pipeline orchestration engine built with Gradle — multi-provider LLM support (Claude, GPT, Gemini, custom endpoints), human-in-the-loop approval gates, conditional branching with fan-out/fan-in parallelism, persistent checkpointing to SQLite/MySQL/PostgreSQL, a 37-endpoint REST API, and an SSE-powered web dashboard with Docker deployment.
F#kYeah
by
TheFellow
F#
An F# pipeline execution engine targeting .NET 10 — three libraries (Attractor engine, unified multi-provider LLM client, coding agent) with CSS-like stylesheets for LLM routing, automatic retry loops with goal gates, full checkpoint/resume, and 317 tests across three test projects.
attractor-php
/
attractor-tcl
by
Jay Taylor
PHP / Tcl
PHP and Tcl implementations of the Attractor spec layers — including unified multi-provider LLM clients, autonomous coding-agent loops, and DOT-based pipeline runners for software-factory workflows.
anishkny's Attractor
by
Anish Karandikar
Python
A Python pipeline execution framework that interprets DOT-syntax directed graphs with a handler-based architecture — supporting human-in-the-loop gates, parallel branches, checkpoint recovery, and an HTTP server with Server-Sent Events streaming.
attractor-pi-dev
by
jhugman
TypeScript
A TypeScript monorepo structured as three workspace packages — core engine, pi.dev LLM backend, and CLI — with a backend-agnostic CodergenBackend interface that lets providers be swapped without touching the execution engine.
attractor-scala
by
Ben Civjan
Scala
A Scala 3 pipeline orchestration engine built on cats-effect and fs2 — type-safe concurrency via IO monads, stream processing with automatic backpressure, sealed-trait pattern matching, and an immutable case-class architecture implementing the full Attractor spec with a provider-agnostic LLM client.
attractor-ruby
by
Bruno Bornsztein
Ruby
A Ruby gem implementing all three Attractor spec layers — a provider-agnostic LLM client, an autonomous agent loop with dev tools, and a DOT-based pipeline orchestrator with conditional branching, parallel execution, and a five-step edge-selection algorithm.
Arc
by
Point Labs
TypeScript
A spec-driven DOT pipeline engine that coordinates AI coding agents — uses convergence loops where specifications drive verification, with fresh context windows per attempt, persistent learnings from failures, holdout test scenarios, Effect.ts error handling, and a web dashboard for monitoring.
attractor-c
by
Justin McCarthy
C
A pure C11 implementation compiling to a static library and CLI binary — includes a hand-written DOT parser, multi-provider LLM client over libcurl, and self-referential validation pipelines that use Attractor to audit its own spec compliance.
SoulCaster
by
Johnny Chen
C#
A C# implementation of the Attractor spec with a DOT-based pipeline engine, an agentic coding loop, and a unified multi-provider LLM client supporting Anthropic, OpenAI, and Gemini.
attractor-rb
by
aliciapaz
Ruby
A Ruby DOT-based workflow orchestration engine for AI-driven development — parses Graphviz DOT files into directed graphs with LLM execution, human approval gates, conditional branching, parallel fan-out/fan-in, automatic retries, checkpointing, and 13 built-in linting rules for pipeline validation.
amolstrongdm's Attractor
by
Amol Kabe
Python
A multi-agent Software Factory that replaces pass/fail testing with probabilistic satisfaction scoring — orchestrates specialized agents (Coding, Validator, Debugger, Planner) against holdout scenario sets and Digital Twin API replicas to iterate autonomously toward a confidence threshold.
attractor-software-factory
by
az9713
Python
A clone of strongdm/attractor with extensive documentation and 5 new DOT pipeline blueprints — demonstrates the software factory concept with ready-to-run blueprints for login pages, REST APIs, CLI tools, landing pages, data pipelines, and static site generators.
Dark Factory
by
DeepCreative
Python
A Kubernetes-native Dark Factory pipeline for the Bravo Zero platform — implements Judge-01 Scenario Eval with trained D3N models, plus phased Spec Engine, Attractor, Scenario Executor, and DTU Controller components per ADR-151.
←
All Products
CXDB
→
