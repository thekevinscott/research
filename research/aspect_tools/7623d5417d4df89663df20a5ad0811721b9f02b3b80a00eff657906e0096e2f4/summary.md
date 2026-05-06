# Summary

E2B is the sandbox-as-runtime layer for AI agents. Each E2B sandbox is a Firecracker microVM with hardware-level isolation, 80ms warm-region startup, up to 24-hour lifetime, and Python/JS/Ruby/C++ support. Python and JavaScript SDKs let agents launch and control sandboxes programmatically.

For dark factories E2B is the default code-execution substrate: 88% of Fortune 100 companies use it, and Docker has partnered with E2B for "trusted AI" sandboxing. Because the dark-factory pattern requires running unverified, agent-generated code at high parallelism without human review, the microVM isolation guarantee is load-bearing - it is what lets the harness, not a human reviewer, hold the security boundary.
