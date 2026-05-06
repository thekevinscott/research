# The Most Common Security Vulnerabilities in AI-Generated Code

Source: Endor Labs blog
URL: https://www.endorlabs.com/learn/the-most-common-security-vulnerabilities-in-ai-generated-code

## Summary

Endor Labs's writeup catalogs the security vulnerability patterns that recur in AI-generated code: missing input validation, hardcoded secrets, broken access control, missing authentication, insecure cryptographic defaults, and lack of error handling. The piece cites the Veracode 2025 GenAI Code Security Report finding that 45% of AI-generated code samples fail basic security tests, and CodeRabbit's analysis showing AI-generated code contains 1.7x more major issues than human-written code. IBM's Cost of a Data Breach Report attributed 20% of organizational breaches to AI-generated or shadow AI code.

For Dark Factory pitfalls research this is one of the strongest empirical critiques: industry-wide measurement studies show AI-generated code is materially less secure than human code, in a workflow specifically designed to remove the human reviewer who could catch these issues. The piece is particularly damaging to Dark Factory advocacy in security-software contexts (StrongDM's domain) where the failure modes documented here directly translate to production exposure.

## Reconstructed from search snippets

### The headline numbers

- Veracode (2025): "Security flaws in 45 percent of the code they produced" across 100+ LLMs.
- Academic studies: "Over 40% of AI-generated code solutions contain security flaws, even with the latest generation of LLMs."
- CodeRabbit (470 open-source PRs): "AI-generated code contains 1.7x more major issues than human-written code."
- IBM Cost of a Data Breach: "20% of organizations experienced breaches linked to AI-generated or shadow AI code."

### Common vulnerability classes

> "By default, AI-generated code frequently omits input validation unless explicitly prompted to include it, often resulting in insecure outputs by default."

The recurring failures:
- Missing input validation
- Hardcoded secrets
- Broken authentication / authorization
- Disabled row-level security (RLS)
- Insecure cryptographic defaults
- Missing webhook verification
- Injection flaws

### Production impact

> "AI-generated code is introducing vulnerabilities into production systems at unprecedented speed and scale."

## Why this matters

For Dark Factory pitfalls research the Endor Labs piece is a primary statistics citation. When critics say "1.5–2x more security vulnerabilities," they are usually citing this kind of measurement work. The combination with the Replit, PocketOS, Lovable, and Base44 disasters provides both the statistical baseline and the case-study illustrations.
