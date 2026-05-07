# arxiv 2511.03690 — OpenHands Software Agent SDK (HTML version)

Wang et al., MLSys 2026: introduces the OpenHands Software Agent SDK (V1), a complete redesign of the OpenHands framework for production software-engineering agents. Key design goals are flexibility (a few-line default agent that's extensible), security and reliability (local-to-remote execution portability, sandboxing), and broad interface support (VSCode, VNC, browser, CLI, REST/WebSocket).

The paper compares the SDK to OpenAI/Claude/Google offerings and argues OpenHands uniquely integrates native sandboxed execution, lifecycle control, model-agnostic multi-LLM routing, and built-in security analysis. Empirical validation: V1 substantially reduces system-attributable failures over V0 with negligible event-sourcing overhead; SWE-Bench Verified at 72% with Claude Sonnet 4.5 (extended thinking).
