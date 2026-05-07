# confident-ai/deepeval

DeepEval is an OSS LLM evaluation framework styled like pytest: define metrics (G-Eval, hallucination, answer relevancy, faithfulness, agentic toolcalling, conversational), wrap them around your LLM app, get pass/fail in CI. Includes LLM-as-judge and traditional NLP metrics.

DeepEval is the eval-harness layer focused on application-level quality (hallucination, faithfulness, RAG metrics) — sits next to Promptfoo and Inspect with more emphasis on test-style ergonomics. In Dark Factory pipelines DeepEval is what wraps the satisfaction metric inside CI.
