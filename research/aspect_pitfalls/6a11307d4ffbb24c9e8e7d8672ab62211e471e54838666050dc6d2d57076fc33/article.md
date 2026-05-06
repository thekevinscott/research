# Lovable security crisis: 48 days of exposed projects, closed bug reports, & the structural failure of vibe coding security

Source: The Next Web
URL: https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed

## Summary

The Next Web's investigation documents how Lovable, a vibe-coding platform valued at $6.6 billion, exposed source code, database credentials, AI chat histories, and personal data across user projects for 48 days while bug reports were repeatedly closed without action. The structural vulnerability was a broken object-level authorization (BOLA) flaw allowing free-account users to access other users' profiles, source code, and database credentials. The piece frames Lovable's response — closing legitimate bug reports — as evidence that the vibe-coding business model is structurally hostile to security: the platform's value is "fast app generation," and proper security review is incompatible with that promise.

For Dark Factory pitfalls research, Lovable is the platform-level analog of the Replit and PocketOS incidents. When a vibe-coding platform itself runs on Dark Factory principles internally — fast iteration, agent-generated code, minimal review — its security posture suffers in exactly the way critics predict. The Lovable case adds dimension to the disaster catalog by showing the failure can be in the platform, not just the user's app.

## Reconstructed from search snippets

> "Lovable, a vibe coding platform valued at $6.6 billion, exposed source code, database credentials, AI chat histories, and personal data across projects, including a broken object-level authorization vulnerability that allowed free account users to access other users' profiles, source code, and database credentials."

### The 48-day exposure window

Bug reports were filed and closed without action for 48 days. The article frames this as a structural failure: a security-aware engineering culture would have triaged BOLA as critical; Lovable's fast-iteration culture treated it as low-priority.

### The structural argument

> "The vulnerability classes are the same across every major vibe coding platform: disabled row-level security, hardcoded secrets, missing webhook verification, injection flaws, and broken access controls."

Lovable's case is offered as proof that vibe-coding-derived platforms produce vibe-coding-derived vulnerabilities not because of careless individual choices but because the workflow optimizes against security review.

### Connection to broader pattern

Documented adjacent failures:
- Moltbook: 1.5 million API keys exposed.
- Lovable: BOLA exposing source code, credentials, chat histories.
- Replit: production database deletion.
- Base44: critical authentication flaw (Wiz Research, July 2025).

## Why this matters

Lovable is the case study where the *platform itself* failed, not just an end-user's project. For Dark Factory pitfalls research the piece supports the argument that the workflow scales the failure: when Dark Factory companies use Dark Factory tools to build Dark Factory products, the security debt compounds.
