Open Source
CXDB
The context DB that models conversations as a turn DAG (branching + dedup + debugger).
View on GitHub
"
CXDB is a self-hosted context store for AI agents. It persists every turn of every conversation with full type awareness, branching support, and a visual debugger.
Observability for AI agents exists. LLM proxies exist. But what's missing is a self-hosted, inexpensive option that is 100% context- and turn-focused. CXDB fills that gap.
The Gap
LangSmith, Langfuse, Helicone
SaaS-only. Your conversation data lives on someone else's infrastructure.
OpenTelemetry-based tools
Built for distributed tracing. Spans model request trees, not conversations.
LLM proxies (LiteLLM, etc.)
Capture requests, not context. No turn structure, no branching, no type system.
Roll your own (Postgres, S3)
Months of work. No deduplication, no projections, no UI.
Built for LLM Conversations
Most observability tools assume requests are independent and state is transient. LLM agent conversations are different: append-mostly, branching, typed, and long-lived.
Turn DAG
Every turn links to its parent. Branch from any point without copying history. Forking is O(1).
Blob CAS
Payloads are content-addressed (BLAKE3). Repeated payloads stored once. 70%+ storage reduction.
Append Performance
p50 < 1ms for 10KB payloads. Your agent doesn't slow down to record itself.
Self-Hosted
Single binary + data directory. No Postgres, no Redis, no Kafka. Your infrastructure.
Turn DAG, Not Logs
Turn 1
(user request)
↓
Turn 2
(assistant plan)
↓
Turn 3
(tool call)
↓
Turn 4a
(approach A fails)
↓
Turn 5a
←→
Turn 4b
(fork: try B)
↓
Turn 5b
(succeeds)
Both branches share turns 1-3. Forking is O(1): a new head pointer.
Dynamic Type System
Every payload declares its type and version. The type registry defines how to project msgpack bytes into structured JSON, and how to render it in the UI.
{
"bundle_id"
:
"mycompany.agents.v1"
,
"types"
:
{
"mycompany:DeployEvent"
:
{
"versions"
:
{
"1"
:
{
"fields"
:
{ ... } } }
}
}
}
✓
Automatic JSON projection with proper field names
✓
Forward-compatible evolution (add fields, never break readers)
✓
Type-aware rendering in the UI (not just raw JSON dumps)
✓
Custom renderers per type
Performance
Append latency
p50 < 1ms
p99 < 10ms for 10KB
Concurrent writers
Thousands
Per-context locking
Storage efficiency
70%+
Zstd + dedup
Retrieval
Sub-ms
Over TB-scale datasets
Architecture
Your AI Agents
Any framework, any language
Binary protocol or HTTP/JSON
↓
CXDB Server
Turn Store
(DAG)
Blob CAS
(dedup)
Type Registry
(schema)
↓
Local Storage
turns.log, blobs.pack, registry/
Binary Protocol
Port 9009. Length-prefixed msgpack frames for high-throughput writers.
HTTP/JSON
Port 9010. REST API for browsers, dashboards, ad-hoc queries.
Open Source
Apache 2.0, full source. Use it for production observability, internal tools, commercial products, or learning how context stores work.
strongdm/cxdb
Star, fork, or contribute on GitHub
→
Rust server
—
Binary protocol + HTTP gateway
Go client library
—
High-performance client
React frontend
—
Turn visualization and debugging
Type registry
—
Projection engine
Kubernetes manifests
—
Production deployment
Summary
Turn-native
Built for LLM trajectories
Type-aware
Dynamic schema system
Efficient
Sub-ms over terabytes
Self-hosted
Your data, no SaaS
Simple
Single binary, no deps
Open source
Apache 2.0
←
All Products
StrongDM ID
→
