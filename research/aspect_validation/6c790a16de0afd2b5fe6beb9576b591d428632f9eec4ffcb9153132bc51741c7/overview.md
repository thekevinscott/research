# Overview

Anthropic's "Demystifying evals for AI agents" is the canonical practitioner guide to eval design from a frontier lab. It defines the vocabulary (task, grader, check, dimension, rubric) and lays out the three grader families: deterministic state/outcome checks, LLM-based rubrics for open-ended dimensions, and full test-suite execution (SWE-bench style). The guidance to grade each dimension with its own isolated LLM-judge — rather than one mega-judge — is the practical implementation of the generator-judge separation principle.

The post is influential because it is unusually concrete: 20-50 tasks pulled from real failures is an explicit floor; calibrate LLM judges against expert humans regularly; multidimensional success (state + transcript constraint + tone) is the rule, not the exception. It is the document that subsequent harness-engineering writeups (Datadog, OpenAI, StrongDM) implicitly assume the reader has internalized.
