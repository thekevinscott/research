# Summary

Coder's Workspaces product is a self-hosted platform for governed AI coding-agent execution: each agent runs in an isolated Terraform-defined workspace connected via Wireguard, with auto-shutdown when idle, RBAC, audit logging, and a centralized Coder AI Gateway that controls LLM access for tools like Claude Code. Agents and humans share the same workspace template system.

For dark factories Coder is positioned as the governance backbone in regulated and air-gapped enterprises (automotive, finance, government). Where e2b/Daytona/Modal handle the per-task sandbox, Coder handles the long-lived workspace fleet, the policy layer, and the LLM gateway. It is the most-cited choice when enterprises talk about "running our own dark factory inside our VPC."
