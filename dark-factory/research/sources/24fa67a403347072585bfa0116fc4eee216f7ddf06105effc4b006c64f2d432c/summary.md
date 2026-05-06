# langfuse/langfuse

Langfuse is an open-source LLM-engineering platform: tracing, prompt management, evals (LLM-as-judge, user feedback, manual labeling, custom pipelines), datasets, and a playground. It integrates via OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and is YC W23.

Langfuse is the observability + eval substrate for an agent fleet — what gives a Dark Factory operator any chance of debugging a long-horizon trace post-hoc. It overlaps with CXDB on storage (both keep conversation traces) but Langfuse is hosted-friendly and eval-centric, while CXDB is content-addressed and branching-centric. A real Dark Factory build typically uses both.
