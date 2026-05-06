# smolagents

🤗 smolagents: a barebones library for agents that think in code.

Agents that think in code!
smolagents
is a library that enables you to run powerful agents in a few lines of code. It offers:
✨
Simplicity
: the logic for agents fits in ~1,000 lines of code (see
agents.py
). We kept abstractions to their minimal shape above raw code!
🧑‍💻
First-class support for Code Agents
. Our
CodeAgent
writes its actions in code (as opposed to "agents being used to write code"). To make it secure, we support executing in sandboxed environments via
Blaxel
,
E2B
,
Modal
, Docker, or Pyodide+Deno WebAssembly sandbox.
🤗
Hub integrations
: you can
share/pull tools or agents to/from the Hub
for instant sharing of the most efficient agents!
🌐
Model-agnostic
: smolagents supports any LLM. It can be a local
transformers
or
ollama
model, one of
many providers on the Hub
, or any model from OpenAI, Anthropic and many others via our
LiteLLM
integration.
👁️
Modality-agnostic
: Agents support text, vision, video, even audio inputs! Cf
this tutorial
for vision.
🛠️
Tool-agnostic
: you can use tools from any
MCP server
, from
LangChain
, you can even use a
Hub Space
as a tool.
Full documentation can be found
here
.
Note
Check the our
launch blog post
to learn more about
smolagents
!
Quick demo
First install the package with a default set of tools:
pip install
"
smolagents[toolkit]
"
Then define your agent, give it the tools it needs and run it!
from
smolagents
import
CodeAgent
,
WebSearchTool
,
InferenceClientModel
model
=
InferenceClientModel
()
agent
=
CodeAgent
(
tools
=
[
WebSearchTool
()],
model
=
model
,
stream_outputs
=
True
)
agent
.
run
(
"How many seconds would it take for a leopard at full speed to run through Pont des Arts?"
)
smolagents_readme_leopard.mp4
You can even share your agent to the Hub, as a Space repository:
agent
.
push_to_hub
(
"m-ric/my_agent"
)
# agent.from_hub("m-ric/my_agent") to load an agent from Hub
Our library is LLM-agnostic: you could switch the example above to any inference provider.
InferenceClientModel, gateway for all
inference providers
supported on HF
from
smolagents
import
InferenceClientModel
model
=
InferenceClientModel
(
model_id
=
"deepseek-ai/DeepSeek-R1"
,
provider
=
"together"
,
)
LiteLLM to access 100+ LLMs
from
smolagents
import
LiteLLMModel
model
=
LiteLLMModel
(
model_id
=
"anthropic/claude-4-sonnet-latest"
,
temperature
=
0.2
,
api_key
=
os
.
environ
[
"ANTHROPIC_API_KEY"
]
)
OpenAI-compatible servers: Together AI
import
os
from
smolagents
import
OpenAIModel
model
=
OpenAIModel
(
model_id
=
"deepseek-ai/DeepSeek-R1"
,
api_base
=
"https://api.together.xyz/v1/"
,
# Leave this blank to query OpenAI servers.
api_key
=
os
.
environ
[
"TOGETHER_API_KEY"
],
# Switch to the API key for the server you're targeting.
)
OpenAI-compatible servers: OpenRouter
import
os
from
smolagents
import
OpenAIModel
model
=
OpenAIModel
(
model_id
=
"openai/gpt-4o"
,
api_base
=
"https://openrouter.ai/api/v1"
,
# Leave this blank to query OpenAI servers.
api_key
=
os
.
environ
[
"OPENROUTER_API_KEY"
],
# Switch to the API key for the server you're targeting.
)
Local `transformers` model
from
smolagents
import
TransformersModel
model
=
TransformersModel
(
model_id
=
"Qwen/Qwen3-Next-80B-A3B-Thinking"
,
max_new_tokens
=
4096
,
device_map
=
"auto"
)
Azure models
import
os
from
smolagents
import
AzureOpenAIModel
model
=
AzureOpenAIModel
(
model_id
=
os
.
environ
.
get
(
"AZURE_OPENAI_MODEL"
),
azure_endpoint
=
os
.
environ
.
get
(
"AZURE_OPENAI_ENDPOINT"
),
api_key
=
os
.
environ
.
get
(
"AZURE_OPENAI_API_KEY"
),
api_version
=
os
.
environ
.
get
(
"OPENAI_API_VERSION"
)
)
Amazon Bedrock models
import
os
from
smolagents
import
AmazonBedrockModel
model
=
AmazonBedrockModel
(
model_id
=
os
.
environ
.
get
(
"AMAZON_BEDROCK_MODEL_ID"
)
)
CLI
You can run agents from CLI using two commands:
smolagent
and
webagent
.
smolagent
is a generalist command to run a multi-step
CodeAgent
that can be equipped with various tools.
#
Run with direct prompt and options
smolagent
"
Plan a trip to Tokyo, Kyoto and Osaka between Mar 28 and Apr 7.
"
--model-type
"
InferenceClientModel
"
--model-id
"
Qwen/Qwen3-Next-80B-A3B-Thinking
"
--imports pandas numpy --tools web_search
#
Run in interactive mode (launches setup wizard when no prompt provided)
smolagent
Interactive mode guides you through:
Agent type selection (CodeAgent vs ToolCallingAgent)
Tool selection from available toolbox
Model configuration (type, ID, API settings)
Advanced options like additional imports
Task prompt input
Meanwhile
webagent
is a specific web-browsing agent using
helium
(read more
here
).
For instance:
webagent
"
go to xyz.com/men, get to sale section, click the first clothing item you see. Get the product details, and the price, return them. note that I'm shopping from France
"
--model-type
"
LiteLLMModel
"
--model-id
"
gpt-5
"
How do Code agents work?
Our
CodeAgent
works mostly like classical ReAct agents - the exception being that the LLM engine writes its actions as Python code snippets.
flowchart TB
 Task[User Task]
 Memory[agent.memory]
 Generate[Generate from agent.model]
 Execute[Execute Code action - Tool calls are written as functions]
 Answer[Return the argument given to 'final_answer']

 Task -->|Add task to agent.memory| Memory

 subgraph ReAct[ReAct loop]
 Memory -->|Memory as chat messages| Generate
 Generate -->|Parse output to extract code action| Execute
 Execute -->|No call to 'final_answer' tool => Store execution logs in memory and keep running| Memory
 end

 Execute -->|Call to 'final_answer' tool| Answer

 %% Styling
 classDef default fill:#d4b702,stroke:#8b7701,color:#ffffff
 classDef io fill:#4a5568,stroke:#2d3748,color:#ffffff

 class Task,Answer io
Loading
Actions are now Python code snippets. Hence, tool calls will be performed as Python function calls. For instance, here is how the agent can perform web search over several websites in one single action:
requests_to_search
=
[
"gulf of mexico america"
,
"greenland denmark"
,
"tariffs"
]
for
request
in
requests_to_search
:
print
(
f"Here are the search results for
{
request
}
:"
,
web_search
(
request
))
Writing actions as code snippets is demonstrated to work better than the current industry practice of letting the LLM output a dictionary of the tools it wants to call:
uses 30% fewer steps
(thus 30% fewer LLM calls) and
reaches higher performance on difficult benchmarks
. Head to
our high-level intro to agents
to learn more on that.
Since code execution can be a serious security concern (arbitrary code execution!),
you should run agent code in a sandbox
. We support several options:
E2B
,
Blaxel
,
Modal
— managed cloud sandboxes, simplest to set up
Docker
— self-hosted container isolation
Pyodide+Deno WebAssembly — lightweight sandbox for browser or edge environments
The built-in
LocalPythonExecutor
is
not a security sandbox
. It applies some restrictions but can be bypassed and must not be used as a security boundary.
Alongside
CodeAgent
, we also provide the standard
ToolCallingAgent
which writes actions as JSON/text blobs. You can pick whichever style best suits your use case.
How smol is this library?
We strived to keep abstractions to a strict minimum: the main code in
agents.py
has <1,000 lines of code.
Still, we implement several types of agents:
CodeAgent
writes its actions as Python code snippets, and the more classic
ToolCallingAgent
leverages built-in tool calling methods. We also have multi-agent hierarchies, import from tool collections, remote code execution, vision models...
By the way, why use a framework at all? Well, because a big part of this stuff is non-trivial. For instance, the code agent has to keep a consistent format for code throughout its system prompt, its parser, the execution. So our framework handles this complexity for you. But of course we still encourage you to hack into the source code and use only the bits that you need, to the exclusion of everything else!
How strong are open models for agentic workflows?
We've created
CodeAgent
instances with some leading models, and compared them on
this benchmark
that gathers questions from a few different benchmarks to propose a varied blend of challenges.
Find the benchmarking code here
for more detail on the agentic setup used, and see a comparison of using LLMs code agents compared to vanilla (spoilers: code agents works better).
This comparison shows that open-source models can now take on the best closed models!
Security
Security is a critical consideration when working with code-executing agents. Ensure you are using one of the sandboxed execution options that provide isolation from untrusted code.
Warning:
LocalPythonExecutor
provides best-effort mitigations only and is
not a security boundary
. Do not use it to run untrusted code.
For security policies, vulnerability reporting, and more information on secure agent execution, please see our
Security Policy
.
Contribute
Everyone is welcome to contribute, get started with our
contribution guide
.
Cite smolagents
If you use
smolagents
in your publication, please cite it by using the following BibTeX entry.
@Misc
{
smolagents
,
title
=
{
`smolagents`: a smol library to build great agentic systems.
}
,
author
=
{
Aymeric Roucher and Albert Villanova del Moral and Thomas Wolf and Leandro von Werra and Erik Kaunismäki
}
,
howpublished
=
{
\url{https://github.com/huggingface/smolagents}
}
,
year
=
{
2025
}
}
