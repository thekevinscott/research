# E2B - The Enterprise AI Agent Cloud

URL: https://e2b.dev/
Source: E2B

## Reconstructed content (from search snippets)

> "E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud. It provides a sandbox as a code runtime for AI-generated apps and supports any programming language that can run on a Linux box."

Performance:

> "E2B Sandboxes in the same region as the client start in 80 ms, making real-time AI interactions possible."

Languages:

> "E2B supports Python, JavaScript, Ruby, and C++, along with popular frameworks or custom libraries."

Security:

> "Each sandbox is powered by Firecracker, a microVM made to run untrusted workflows, providing hardware-level isolation."

Duration:

> "Each E2B sandbox can run up to 24 hours."

SDKs:

> "To start and control sandboxes, users can use the JavaScript SDK or Python SDK. E2B provides isolated sandboxes that let agents safely execute code, process data, and run tools."

Adoption:

> "88% of Fortune 100 companies trust E2B for their AI deployments, indicating strong enterprise adoption for secure code execution in AI applications."

Docker partnership: https://www.docker.com/blog/docker-e2b-building-the-future-of-trusted-ai/

Repository: https://github.com/e2b-dev/E2B

## Relevance to dark factories

E2B is the most widely adopted sandbox layer for AI agents - 88% of Fortune 100 - and the Firecracker-microVM isolation is the safety primitive that makes "code must not be reviewed by humans" tolerable. For dark-factory builders E2B is the default choice when they need agent-issued code to execute against arbitrary commands without trusting it.
