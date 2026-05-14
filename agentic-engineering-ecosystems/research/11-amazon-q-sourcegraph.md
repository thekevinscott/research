# Additional Platforms: Amazon Q Developer and Sourcegraph Cody

Coverage gaps identified in the audit (10-audit.md). These platforms warrant dedicated analysis.

---

## Amazon Q Developer

**Website**: [aws.amazon.com/q/developer](https://aws.amazon.com/q/developer/)  
**Pricing**: Free ($0, 50 agentic requests/month), Pro ($19/user/month)

### What It Is

AWS's agentic coding assistant — formerly CodeWhisperer, rebranded and significantly expanded. Spans CLI, IDE, and managed agent modalities. Architecturally one of the most complete competitors to Claude Code in surface area coverage.

### Why It Was Missing From This Report

Oversight. Amazon Q Developer covers CLI agent + IDE + managed agents + MCP in a single $19/month product. Its omission from the original survey is a meaningful gap, particularly for teams on AWS infrastructure.

### Capabilities

**CLI Agent (`q chat`)**: Terminal-based interactive agent directly comparable to Claude Code. Reads/writes files, executes shell commands, multi-step reasoning. GA as of 2025. Works with Bash, Zsh, Fish.

**IDE Agent Mode (`/dev`)**: Accepts natural language task descriptions, autonomously plans and implements multi-file changes in VS Code and JetBrains.

**Managed/Background Agent**: Can be triggered from GitHub issues. Operates asynchronously, produces PRs for review, iterates on feedback. Similar architecture to claude-code-action and GitHub Copilot's coding agent.

**Specialized Agents**:
- `/transform` — Java version upgrades, .NET Framework migration
- `/test` — automated unit test generation
- `/doc` — documentation generation
- Code review agent
- Operational investigation agent for AWS issues

**MCP Support**: Added 2025. Can connect to external tools via Model Context Protocol.

### Pricing

| Tier | Price | Agentic Requests | Notes |
|------|-------|-----------------|-------|
| Free | $0/month | 50/month | No admin controls, no IP indemnity |
| Pro | $19/user/month | Higher (undisclosed limits) | Admin controls, IP indemnity, IAM Identity Center |

No per-token billing — fixed subscription. For teams, this is radically simpler than Anthropic's variable pricing.

### Models

AWS deliberately obscures model details. Known:
- Multi-model ensemble routing different tasks to different models
- **Amazon Nova** family (proprietary)
- **Anthropic Claude** — confirmed on AWS pricing page ("latest Claude models")
- Users cannot choose or switch models

The irony: Amazon Q likely uses Claude under the hood for its hardest tasks, given Amazon's multi-billion-dollar Anthropic investment.

### AWS Integration

The real differentiator for AWS-native teams:
- Operational investigation for AWS service issues
- Infrastructure-as-code generation tuned for CloudFormation, CDK, SAM
- Native IAM Identity Center integration
- Console Q&A and error diagnosis
- Deep AWS SDK knowledge

### User Reception

Reddit r/aws: mixed-to-positive. Free tier valued. Good for AWS-specific workflows. CLI `q chat` seen as viable Claude Code alternative. Less polished than Cursor/Copilot for general coding. AWS auth setup cumbersome for non-AWS users.

### Parity Assessment

| Dimension | Rating |
|-----------|--------|
| CLI Agent | Full |
| App Sync | None |
| Managed Agents | Full |
| GitHub Integration | Partial |
| Model Flexibility | None (internal routing) |
| Self-Hostable | None |
| MCP | Full |
| IDE | Full (VS Code, JetBrains, Visual Studio) |
| Cost Control | Full ($19/mo fixed) |

**Amazon Q achieves ~75% parity with Anthropic** across the full capability set — higher than any tool except GitHub Copilot Agent. The combination of CLI + IDE + managed agents + MCP at $19/month is the most cost-effective single-product offering in this survey. The gap: no model flexibility, no self-hosting, no app sync.

**For AWS-native teams, this should be the default first choice before assembling a multi-tool stack.**

---

## Sourcegraph Cody

**Website**: [sourcegraph.com/cody](https://sourcegraph.com/cody)  
**Pricing**: Enterprise only, starting at $16,000

### What It Is

AI coding assistant backed by Sourcegraph's code intelligence platform — code search, symbol navigation, cross-repository references, dependency mapping. The thesis: agents need accurate codebase context to work reliably at scale, and Sourcegraph's code graph provides superior context.

### Strategic Pivot

Sourcegraph discontinued Free and Pro individual tiers in 2024-2025, going enterprise-only after ~40% layoffs. The surviving customer base is large organizations with hundreds of repositories where cross-repo context matters.

| Tier | Price | Status |
|------|-------|--------|
| Free | Discontinued | — |
| Pro ($9/user/month) | Discontinued | — |
| Enterprise | Starting at $16,000 | Only offering |

### Key Differentiator: Code Graph Context

Where other tools understand one repository at a time, Cody draws on:
- Repository-wide semantic understanding across entire organizations
- Cross-repository code navigation and dependency tracking
- Deep Search (AI-powered semantic code search)
- Batch changes (multi-repo automated refactoring)

For organizations with 50+ repositories and shared libraries, this cross-repo awareness is something no other tool in this survey provides.

### Agent Capabilities

- Chat with repository-wide context
- Auto-edit suggestions
- Agent mode (2025): multi-file editing, terminal commands, multi-step planning
- Batch changes: automated multi-repository refactoring
- Custom prompt templates

Agent mode is less mature than Cursor or Claude Code. Cody's value is the context layer, not agent execution.

### Model Support

Multi-model, user-selectable: Claude (3.5 Sonnet default, Opus, Haiku), GPT-4o, GPT-4 Turbo, o1-preview, Gemini 1.5 Pro/Flash, Mixtral, Ollama for self-hosted models. Full BYOLLM support at enterprise tier.

### Relevance to This Report

Sourcegraph positions Cody as **context infrastructure for other agents** — their pricing page lists compatibility with Claude Code, Cursor, Codex, and Amp. This suggests Sourcegraph sees the code graph as a complement to whatever agent you use, not a replacement.

For the user's situation (power user, not managing hundreds of repos), Cody's $16K minimum makes it irrelevant. For enterprise readers, Sourcegraph's cross-repo context is unique and valuable — it solves a problem no other tool addresses.

### Parity Assessment

| Dimension | Rating |
|-----------|--------|
| CLI Agent | Minimal |
| App Sync | None |
| Managed Agents | None |
| GitHub Integration | None |
| Model Flexibility | Full |
| Self-Hostable | Partial (enterprise self-hosted option) |
| MCP | Full (has MCP server) |
| IDE | Full (VS Code, JetBrains) |
| Cost Control | Minimal ($16K floor) |

**Not a Claude Code competitor.** A context infrastructure layer that could enhance any agent stack. Relevant only at enterprise scale.

---

## Impact on Report Conclusions

### Amazon Q changes the recommendation landscape:

The original recommendation (09) suggests a multi-tool stack: Aider for CLI + OpenHands for managed agents + Cline for IDE + PR-Agent for review. Amazon Q Developer offers most of this in a single $19/month product — albeit without model flexibility or self-hosting.

**Revised recommendation for AWS-native teams**: Start with Amazon Q Developer Free tier. Evaluate whether the 50 agentic requests/month cover your needs. If yes, upgrade to Pro ($19/month) — dramatically cheaper than any multi-tool stack. Supplement with OpenHands for self-hosted managed agents if you need model flexibility or higher volume.

### Sourcegraph doesn't change conclusions for individual users. Enterprise readers should note the cross-repo context capability.

---

## Sources

- [Amazon Q Developer](https://aws.amazon.com/q/developer/) — Product page
- [Amazon Q Developer Pricing](https://aws.amazon.com/q/developer/pricing/) — Official pricing
- [Sourcegraph Cody](https://sourcegraph.com/cody) — Product page
- [Sourcegraph Pricing](https://sourcegraph.com/pricing) — Enterprise-only pricing
- [Reddit: Amazon Q Developer review](https://www.reddit.com/r/aws/comments/1jmjuks/an_honest_review_of_amazon_q_developer/) — User reception
