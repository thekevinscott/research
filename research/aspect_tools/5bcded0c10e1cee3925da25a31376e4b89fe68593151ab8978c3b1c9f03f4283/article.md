# SWE-agent

URL: https://github.com/SWE-agent/SWE-agent
Source: Princeton / Stanford research

## Reconstructed content (from search snippets)

Overview:

> "SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It enables language models (like GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories, find cybersecurity vulnerabilities, or perform any custom task."

Origins:

> "SWE-agent is an academic project started at Princeton University by John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. SWE-agent is built and maintained by researchers from Princeton University and Stanford University."

> "[NeurIPS 2024]"

SWE-bench:

> "SWE-bench is a benchmark for evaluating large language models on real world software issues collected from GitHub. Given a codebase and an issue, a language model is tasked with generating a patch that resolves the described problem. SWE-bench has been accepted to ICLR 2024 as an oral presentation."

Performance:

> "SWE-agent achieves state of the art on SWE-bench among open-source projects."

Mini-SWE-agent:

> "mini-SWE-agent is a 100 line AI agent that still gets 65% on SWE-bench verified."

Repository: https://github.com/SWE-agent/SWE-agent | benchmark: https://github.com/swe-bench/SWE-bench

## Relevance to dark factories

SWE-Agent and SWE-bench are the academic substrate the entire field uses to measure dark-factory readiness. Most commercial coding agents (Devin, Codex, Cursor) report SWE-bench numbers. The 100-line mini-swe-agent shows how much of the lift comes from the harness, not the agent code - which is the central thesis of harness engineering.
