# Agent-Building Frameworks

These are SDKs and libraries for *building* agents — not agents themselves. The distinction matters: tools in previous sections (Claude Code, Aider, OpenHands) are finished products you use. Frameworks here are construction kits for building custom agent systems. Relevant when no off-the-shelf agent fits your workflow and you need to compose one from primitives.

---

## 1. OpenAI Agents SDK

**Repository**: [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)  
**Stars**: ~26,000  
**License**: MIT  
**Language**: Python 3.10+

### Architecture

Successor to OpenAI's experimental "Swarm" framework. Provides lightweight primitives for multi-agent orchestration:

- **Agents**: LLM instances with instructions, tools, and handoff capabilities
- **Handoffs**: Delegation between agents (agent A realizes task needs agent B)
- **Guardrails**: Input/output validation running in parallel with agent execution
- **Tools**: Function tools, hosted tools (code interpreter, file search), and MCP tools
- **Sessions**: Automatic conversation state management
- **Tracing**: Built-in observability for debugging agent behavior

### Key Design Decision

Minimal abstraction. An "agent" is just an LLM configuration + tool set + system prompt. No complex graph definitions or state machines. The SDK handles the loop (call model → execute tools → feed results back → repeat) and adds orchestration on top (handoffs, guardrails, tracing).

### Model Flexibility

Despite being OpenAI's SDK, it supports 100+ LLMs via LiteLLM integration — including Claude. You could theoretically use it to orchestrate Claude-powered agents. In practice, the ergonomics favor OpenAI models (native tool calling format, response streaming).

### MCP Support

Yes. Tools can be sourced from MCP servers, making this SDK part of the MCP ecosystem despite being OpenAI's product.

### When to Use

- Building conversational agent systems with delegation patterns
- Need guardrails and tracing out of the box
- Already using OpenAI models and want structured multi-agent patterns
- Prototyping agent architectures before committing to heavier frameworks

### Limitations

- No built-in state persistence (stateless between calls unless you add Sessions)
- No graph/workflow definition — pure agent-to-agent handoffs
- Not designed for event-driven patterns (GitHub webhooks → agent execution)
- Relatively new — production patterns still emerging

---

## 2. LangGraph (LangChain)

**Repository**: [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)  
**Stars**: ~15,000  
**License**: MIT  
**Language**: Python, TypeScript

### Architecture

Graph-based state machine for agent workflows. Where OpenAI's SDK is "agents hand off to each other," LangGraph is "define a directed graph of computation steps with conditional edges."

Core concepts:
- **Nodes**: Computation steps (LLM calls, tool execution, data processing)
- **Edges**: Transitions between nodes (conditional, deterministic)
- **State**: Typed state object passed through the graph, mutated at each node
- **Checkpointing**: Persist state at any point for resumption, time-travel debugging
- **Human-in-the-loop**: Built-in interruption points for human approval

### Why Graphs?

Most real agent workflows aren't linear. They have:
- Cycles (retry until tests pass)
- Branches (different paths based on error type)
- Parallel execution (multiple analyses simultaneously)
- Conditional routing (different agents for different subtasks)

LangGraph makes these patterns explicit and debuggable rather than implicit in agent prompt engineering.

### LangGraph Platform

LangChain offers a hosted platform for deploying LangGraph agents:
- Managed infrastructure
- Built-in persistence
- Streaming support
- Cron-based scheduling
- Available self-hosted or cloud

### Model Flexibility

Fully model-agnostic via LangChain's provider abstractions. Any LLM works.

### MCP Support

Emerging through LangChain ecosystem integrations. Not a first-class primitive but achievable.

### When to Use

- Complex workflows with branching logic, cycles, or conditional routing
- Need checkpointing and state persistence
- Building systems where the agent topology is complex enough to need visualization
- Want deterministic control flow with LLM decision points

### Limitations

- Steep learning curve — graph definition adds conceptual overhead
- LangChain ecosystem dependency (large, sometimes unstable dependency tree)
- Overengineered for simple single-agent patterns
- Abstraction layer adds latency and debugging complexity

### Self-Hosted Managed Agents

LangGraph is the most viable framework for building custom managed agents. The combination of state persistence, checkpointing, and event handling means you could build a "GitHub issue → LangGraph workflow → PR" pipeline. The LangGraph Platform supports scheduling and webhooks. Requires significant engineering to match OpenHands' out-of-box capability, but offers more architectural control.

---

## 3. CrewAI

**Repository**: [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)  
**Stars**: ~25,000+  
**License**: MIT  
**Language**: Python

### Architecture

Role-based multi-agent system. The mental model: you're staffing a team.

- **Agents**: Have roles, goals, backstories, and tool access
- **Tasks**: Work items with descriptions, expected outputs, and assigned agents
- **Crews**: Teams of agents working toward a shared goal
- **Processes**: Sequential (waterfall) or hierarchical (manager delegates)

Example:
```python
researcher = Agent(role="Senior Researcher", goal="Find comprehensive data")
writer = Agent(role="Technical Writer", goal="Create clear documentation")
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
```

### Why Roles?

CrewAI's thesis: complex tasks decompose naturally into roles, and specialized agents outperform generalists. A "code reviewer" agent with a focused system prompt and specific tools produces better reviews than a general agent asked to review code.

### CrewAI+ Platform

Commercial platform for deploying crews:
- Managed hosting
- Monitoring dashboard
- Deploy CLI
- Enterprise features

### Model Flexibility

Multi-provider support. Easy to swap models per agent (e.g., expensive model for the "architect" agent, cheap model for the "formatter" agent).

### When to Use

- Task naturally decomposes into specialist roles
- Want quick prototyping of multi-agent systems
- Less concerned with fine-grained control flow, more with agent specialization
- Team already thinks in terms of roles/responsibilities

### Limitations

- Abstraction can be too opinionated — forces role metaphor even when it doesn't fit
- Sequential/hierarchical processes are limited compared to LangGraph's arbitrary graphs
- Less mature state persistence than LangGraph
- Performance overhead from multiple agent calls when a single agent could suffice

---

## 4. AutoGen (Microsoft)

**Repository**: [github.com/microsoft/autogen](https://github.com/microsoft/autogen)  
**Stars**: ~30,000+  
**License**: Apache 2.0  
**Language**: Python

### Architecture

Multi-agent conversation framework. Agents communicate via message passing in group chats.

Core pattern:
- **Agents**: Conversable entities (LLM-backed or human proxies)
- **Group Chat**: Multiple agents discuss/debate to solve problems
- **Code Execution**: Built-in sandboxed code execution
- **Human Proxy**: Agent that represents a human in the conversation

### AG2 Rewrite (AutoGen 0.4+)

Major rewrite introduced event-driven architecture:
- Modular, pluggable components
- Better async support
- Improved code execution sandboxing
- More flexible agent topologies

The rewrite caused community fragmentation — some users stayed on 0.2.x, some migrated. Stability concerns during transition period.

### Model Flexibility

Multi-LLM support. Azure OpenAI is most tested path (Microsoft product) but supports other providers.

### Self-Hosted Managed Agents

AutoGen's code execution capability and event-driven architecture (post-rewrite) make it viable for building autonomous coding agents. Microsoft Research uses it internally for code generation tasks. Could be wired to GitHub webhooks, though no turnkey solution exists.

### When to Use

- Multi-agent debate/discussion patterns (agent A proposes, agent B critiques)
- Need built-in code execution sandboxing
- Research or experimental agent architectures
- Microsoft/Azure ecosystem alignment

### Limitations

- Post-rewrite documentation gaps
- Community fragmentation between versions
- Heavier weight than needed for simple patterns
- Group chat overhead for tasks that don't need debate

---

## 5. Pydantic AI

**Repository**: [github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)  
**Stars**: ~5,000+  
**License**: MIT  
**Language**: Python

### Architecture

Type-safe agent development from the Pydantic team. Philosophy: agents should be as testable and type-checked as regular application code.

- **Agents**: Typed with dependency injection for tools and context
- **Structured Output**: Guaranteed schema-valid responses via Pydantic models
- **Result Validators**: Custom validation on agent outputs
- **System Prompts**: Dynamic, function-based (can depend on runtime context)

### Why Type Safety?

Other frameworks treat agent responses as strings and hope for the best. Pydantic AI ensures:
- Tool inputs are validated before execution
- Agent outputs conform to declared schemas
- Dependencies are injected and typed
- Everything is testable with standard Python testing tools

### Model Flexibility

Explicit multi-provider support: OpenAI, Anthropic, Gemini, Ollama, Groq, Mistral. First-class support for each, not just "OpenAI-compatible" adapters.

### When to Use

- Production systems where type safety and testability matter
- Single-agent patterns with structured output needs
- Teams already using Pydantic for data validation
- Want minimal framework overhead with maximum correctness guarantees

### Limitations

- Newer — smaller community and fewer examples
- Less multi-agent orchestration compared to LangGraph or CrewAI
- No built-in state persistence or checkpointing
- Not designed for complex workflow topologies

---

## 6. SmolAgents (HuggingFace)

**Repository**: [github.com/huggingface/smolagents](https://github.com/huggingface/smolagents)  
**License**: Apache 2.0  
**Language**: Python

### Architecture

Intentionally minimal agent framework. Key insight: instead of agents outputting JSON tool calls, they write Python code that uses tools as functions.

```python
# Traditional: agent outputs {"tool": "search", "args": {"query": "..."}}
# SmolAgents: agent outputs Python code that calls search("...")
```

This means agents can use loops, conditionals, variables — full programming constructs — in their action plans, not just flat tool call sequences.

### Design Philosophy

- Minimal abstraction (< 1000 lines of core code)
- Code execution as the primary action mode
- No complex graph definitions or role systems
- Works with open-source models (HuggingFace ecosystem alignment)

### When to Use

- Want the lightest possible framework
- Tasks benefit from code-based action plans (multi-step data processing, etc.)
- Using open-source models from HuggingFace Hub
- Prototyping quickly without framework overhead

### Limitations

- Limited orchestration for multi-agent patterns
- No state persistence
- Security model for code execution needs care
- Smaller ecosystem than LangGraph or CrewAI

---

## 7. Semantic Kernel (Microsoft)

**Repository**: [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)  
**Stars**: ~23,000  
**License**: MIT  
**Language**: C# (.NET) primary, Python, Java

### Architecture

Enterprise AI orchestration. Designed to integrate LLMs with existing business applications — not replace them.

- **Plugins**: Collections of functions (native code or LLM-powered)
- **Planners**: LLM-based task decomposition into plugin calls
- **Memory**: Vector storage for semantic retrieval
- **Connectors**: Integrations with Azure, M365, databases

### Enterprise Focus

Semantic Kernel's differentiator is enterprise integration:
- Active Directory / Entra ID for auth
- Azure Key Vault for secrets
- Existing .NET/Java codebases can expose functions as plugins
- Compliance and audit patterns built in

### .NET First

The C# implementation is most complete. Python and Java lag. This matters — if your team is .NET-native, Semantic Kernel is the natural choice. If Python-native, LangGraph or CrewAI are better fits.

### When to Use

- .NET/C# enterprise environment
- Need to integrate LLM capabilities into existing business applications
- Azure ecosystem alignment
- Compliance and governance requirements

### Limitations

- .NET-first means Python/Java are second-class
- Enterprise overhead for simple use cases
- Less community innovation than LangGraph/CrewAI (enterprise moves slower)
- Not designed for autonomous coding agents specifically

---

## Framework Selection Matrix

### By Problem Type

| Problem | Best Framework |
|---------|---------------|
| Simple single-agent with tools | Pydantic AI |
| Multi-agent delegation/handoffs | OpenAI Agents SDK |
| Complex workflows with branching | LangGraph |
| Role-based team decomposition | CrewAI |
| Multi-agent debate/discussion | AutoGen |
| Lightweight code-writing agent | SmolAgents |
| Enterprise .NET integration | Semantic Kernel |

### By Priority

| Priority | Best Framework |
|----------|---------------|
| Production readiness | LangGraph, Semantic Kernel |
| Model flexibility | Pydantic AI, LangGraph |
| Minimal abstraction | SmolAgents, Pydantic AI |
| Self-hosted managed agents | LangGraph (with significant work) |
| Quick prototyping | CrewAI, OpenAI Agents SDK |
| Type safety and testing | Pydantic AI |

---

## Relevance to Self-Hosted Managed Agents

None of these frameworks are turnkey managed agents. They're construction kits. The gap between "I have a framework" and "issues trigger autonomous PR creation" requires:

1. **Event ingestion** — webhook handler for GitHub events
2. **Orchestration** — framework dispatches agent with issue context
3. **Sandboxed execution** — Docker/K8s for safe code execution
4. **Git operations** — clone, branch, commit, push, PR creation
5. **Iteration loop** — run tests, fix failures, re-run
6. **State persistence** — handle long-running tasks across restarts

OpenHands (section 06) solves all six. These frameworks solve #2 and parts of #5. Building the rest is 2-4 weeks of engineering per platform.

**Practical recommendation**: Use OpenHands or SWE-agent as your managed agent. Use these frameworks only if you need custom orchestration beyond what those tools provide — e.g., a multi-agent pipeline where one agent writes code, another reviews it, and a third writes tests.

---

## Sources

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — GitHub repository
- [LangGraph](https://github.com/langchain-ai/langgraph) — GitHub repository
- [CrewAI](https://github.com/crewAIInc/crewAI) — GitHub repository
- [AutoGen](https://github.com/microsoft/autogen) — GitHub repository
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) — GitHub repository
- [SmolAgents](https://github.com/huggingface/smolagents) — GitHub repository
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) — GitHub repository
