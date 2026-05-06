# Slopsquatting: New AI Hallucination Threats & Mitigation Strategies

Source: Snyk
URL: https://snyk.io/articles/slopsquatting-mitigation-strategies/

## Summary

Snyk's piece introduces "slopsquatting" — a new supply-chain attack class enabled by LLM package-name hallucination. The pattern: AI coding assistants confidently recommend nonexistent packages (e.g., `import npm-validator-pro`); attackers register those names with malicious payloads; when an unsupervised agent (or human running on autopilot) runs `npm install`, it pulls the attacker's code. A March 2025 study of 576,000 generated Python and JavaScript code samples found that ~20% recommended nonexistent packages, and 43% of those hallucinated packages appeared repeatedly across multiple prompts — making them predictable, registerable targets.

For Dark Factory pitfalls research, slopsquatting is the cleanest example of "AI slop becoming a security exploit." The pattern is uniquely dangerous in Dark Factory contexts because (a) no human reviews the imports, (b) the agent confidently asserts the package exists, and (c) the digital-twin testing approach often pulls dependencies in the same isolated way that real production builds do. The 43% repetition rate means an attacker doesn't even need to monitor live LLM output — they can just empirically discover the names that the major models hallucinate.

## Reconstructed from search snippets

### The mechanism

> "Slopsquatting builds on the tendency of AI systems to hallucinate package names. These hallucinated dependencies have opened the door to an emerging threat known as 'slopsquatting,' in which malicious actors register the fictitious package names that AI systems commonly suggest."

### The empirical baseline

> "A research paper about package hallucinations published in March 2025 demonstrates that in roughly 20% of the examined cases (576,000 generated Python and JavaScript code samples), recommended packages didn't exist. More critically, 43% of these hallucinated packages appeared repeatedly across multiple prompts, which makes them predictable targets for attackers who track LLM behavior."

### Why Dark Factory is uniquely vulnerable

In Dark Factory pipelines:
- The agent generates code, including import statements.
- A separate agent or harness runs the code to verify behavior.
- The verification harness pulls dependencies (typically via package managers).
- If the package is malicious, it executes during the verification step — pre-deployment.

Without a human in the loop reviewing the diff, the malicious dependency runs in the build environment with whatever credentials and network access the harness has.

## Why this matters

Slopsquatting is the canonical example of "AI hallucination as security vulnerability" and is heavily cited in Dark Factory critiques. It connects to broader concerns about hallucinated APIs (functions that don't exist), hallucinated documentation (cited URLs that 404), and hallucinated config keys — all of which can become attack surfaces or just silent broken behavior when no human reads the code.
