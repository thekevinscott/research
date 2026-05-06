# Stanford Law / CodeX: "Built by Agents, Tested by Agents, Trusted by Whom?"

**URL:** https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/
**Published:** February 8, 2026

## Reconstructed content (from search snippets)

A legal-and-policy response from Stanford Law's CodeX (the Center for Legal Informatics), published one day after Simon Willison's blog post.

Key reported framings (per snippets):

- StrongDM's announcement is read as a regulatory inflection point — for the first time, security-critical software is shipping to enterprise customers without any human in the implementation or review loop.
- The post asks who bears liability when:
  - A coding agent introduces a CVE-class flaw, and
  - No human "ever read the code"?
- It connects this to traditional doctrines of negligence and product liability, noting that existing "human in the loop" assumptions in software supply-chain regulation (SOC 2, FedRAMP, EU CRA) implicitly require a reviewer.

Notable themes raised:

- The Digital Twin Universe is framed as a possible new locus of audit — auditors would inspect the twin and the scenario engine, not the production code.
- Insurers (cyber, E&O) lack pricing models for "no human reviewed" software.
- The piece anticipates new disclosure obligations for vendors operating dark factories.

---

## Summary (2 paragraphs)

Stanford Law's CodeX response (Feb 8 2026) is the principal legal/policy framing of the dark factory pattern. It frames StrongDM's announcement as a regulatory inflection point and identifies a fundamental gap in software-supply-chain regulation: existing frameworks (SOC 2, FedRAMP, EU CRA) implicitly assume human review. When that assumption is explicitly violated, the doctrines of negligence, product liability, and audit need to be re-anchored.

The piece's most influential idea — that auditing a dark factory should target the twins and scenario engines rather than the production code — has migrated into BCG and Pragmatic CTO discussions. Sentiment is cautious-curious rather than alarmist; the authors treat the pattern as legitimate engineering that demands new compliance grammar, not as a category to be banned.
