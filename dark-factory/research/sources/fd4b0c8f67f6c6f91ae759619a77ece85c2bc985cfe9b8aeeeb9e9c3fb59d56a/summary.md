# Pulumi — Pulumi Agent Skills: best practices for AI coding assistants

Pulumi's engineering post documents "Agent Skills" — markdown-based skill files that encode organizational standards, IaC patterns, and policy gates for AI coding assistants working with Pulumi. The skills load into Claude Code, Cursor, or Codex contexts and instruct the agent how to handle infrastructure changes, when to require human approval, and how to format output.

Positioned as the practical mechanism that makes infrastructure Dark Factory operation safe: agents work autonomously on tag changes, security-group adjustments, and resizes, but skills enforce approval gates for destructive operations. Companion to Pulumi Neo (their AI infrastructure agent) and the "Dark Factory Pattern for Infrastructure" post. Concrete artifact of harness-engineering norms in a specific domain.
