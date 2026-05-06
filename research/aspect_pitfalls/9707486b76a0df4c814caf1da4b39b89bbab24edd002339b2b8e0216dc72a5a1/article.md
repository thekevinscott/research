# AI-hallucinated code dependencies become new supply chain risk

Source: BleepingComputer
URL: https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/

## Summary

BleepingComputer's coverage of slopsquatting is the mainstream-security-press treatment that established the term and threat in industry awareness. The article documents how attackers monitor common LLM hallucinations and pre-register malicious packages under those names on PyPI and npm. Because LLMs hallucinate the same package names repeatedly across sessions and users, the attack surface is not random — it is a predictable list of targets that any attacker can enumerate by sampling model output.

For Dark Factory pitfalls research, this article matters because it elevates slopsquatting from academic curiosity to documented enterprise security threat. In a Dark Factory pipeline where agents write code, run package installs, and execute the result with no human reviewing the imports, slopsquatting is a direct kill chain: model hallucinates malicious-but-real package → install runs → attacker code executes in the build/test environment with build credentials. It is the supply-chain analog of the Replit and PocketOS failures: the agent's own confidence is the vulnerability.

## Reconstructed from search snippets

### The threat pattern

The article describes how AI coding assistants frequently recommend packages that don't exist. Attackers identify these hallucinated names by sampling model output, then register the names on PyPI/npm with malicious code.

When an AI agent (or developer accepting AI suggestions) generates code referencing the package and runs `pip install` or `npm install`, the malicious code executes.

### The repetition factor

The 43%-repetition figure (from related research) means the hallucinations are predictable, not stochastic noise. This makes the attack practical at scale.

### Industry response

Coverage discusses mitigation via:
- Package allowlists.
- Pre-install verification of package existence and trustworthiness.
- Enterprise-managed package mirrors.
- Lockfile review (which requires the very human review Dark Factory removes).

## Why this matters

BleepingComputer's reporting is the source frequently cited when critics argue that the Dark Factory pattern is structurally vulnerable to supply-chain attacks. The pattern's defenders argue that the digital twin / sandbox catches malicious behavior before production. Critics counter that supply-chain malware can be subtle: it might exfiltrate credentials, then sit dormant; the harness verifies the code "works" and ships it.
