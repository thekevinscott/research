# Daytona - Secure Infrastructure for Running AI-Generated Code

URL: https://www.daytona.io/
Source: Daytona

## Reconstructed content (from search snippets)

Overview:

> "Daytona is a secure and elastic infrastructure runtime for AI-generated code execution and agent workflows."

Pivot:

> "Daytona pivoted in February 2025 from development environments to become infrastructure for running AI-generated code, providing sandboxes through an SDK that lets AI agents execute code in isolated environments."

Performance:

> "Daytona offers lightning-fast infrastructure with 90ms environment creation, stateful operations, and enterprise-grade security."

Capabilities:

> "It offers isolated execution where each sandbox is completely isolated from your infrastructure, multi-language support for Python, TypeScript, Go, and more, file system access, process management, and Git operations."

Deployment:

> "Daytona can run as a fully hosted service, as an open-source stack you operate, or in a hybrid setup where Daytona orchestrates sandboxes while execution happens on machines you manage. Its architecture supports deployment on all major cloud providers and platforms, while offering a self-hosted option ideal for enterprise and security-sensitive applications."

Architecture:

> "Daytona is a development environment platform that provides workspaces for developers and AI agents, focusing on persistent environments where code, dependencies, and files remain available across sessions, using Docker containers as its isolation technology."

Agent-focus:

> "The platform is fast, programmable, and API-first, with every environment, operation, and capability designed to be accessed and controlled by an AI Agent."

LangChain Open SWE explicitly runs on Daytona: https://www.daytona.io/dotfiles/langchain-s-open-swe-runs-on-daytona-here-s-why

Repository: https://github.com/daytonaio/daytona

## Relevance to dark factories

Daytona is the sandbox of choice for LangChain's Open SWE and one of the two most-cited e2b-class options. Its 90ms cold start and stateful-yet-ephemeral model fits the dark-factory loop where each agent task wants a fresh, repo-loaded environment in under a second.
