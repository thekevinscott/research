# Summary

Cloudflare's "Agents have their own computers" GA announcement (April 2026) released Sandboxes as persistent isolated environments at the edge: a real Linux computer with shell, filesystem, background processes, browser-attachable terminal, code interpreter with state, change-event filesystem, egress proxies for credential injection, and snapshot warm starts. They are addressed through the cloudflare/sandbox-sdk TypeScript SDK.

In parallel, Cloudflare introduced Dynamic Workers - lightweight isolates 100x faster than containers - for low-latency dark-factory executions. The combination is positioned as "Project Think" infrastructure for the next generation of AI agents on Cloudflare. For dark factories whose pipelines must run globally, support persistence across many short tool calls, or inject credentials safely, Cloudflare's stack is one of the most differentiated offerings.
