# Summary

LangChain's Open SWE is an open-source asynchronous coding agent built on LangGraph that decomposes work across four roles - Manager, Planner, Programmer, and Reviewer - and runs every task in an isolated Daytona sandbox. It is triggerable from GitHub issues, Linear comments, Slack mentions, or its hosted web UI at swe.langchain.com, and supports "double texting" so humans can nudge the agent without restarting.

For dark factories Open SWE is one of the cleanest open-source blueprints. The four-role split (Manager-Planner-Programmer-Reviewer) is the canonical harness topology, the Daytona integration is the canonical sandbox layer, and LangChain notes the architecture mirrors what Stripe, Coinbase, and Ramp built internally. Self-hostable via LangGraph API server, it is the reference build for teams who want a credible OSS dark factory.
