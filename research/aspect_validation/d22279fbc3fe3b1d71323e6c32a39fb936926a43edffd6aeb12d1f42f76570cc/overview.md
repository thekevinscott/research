# Overview

Andrew Knight's "BDD Gherkin Guidelines for AI Coding and Testing" (Apr 2026) is a practitioner's guide for using Gherkin as the scenario language for AI agents. Its central observation is that AI-generated Gherkin without explicit rules degrades quickly: vague `Then` steps with no observable assertion, UI-anchored mouse-click scripts, multi-behavior scenarios, and filler examples. With clear configuration dials and embedded BDD expertise in the agent context, AI agents can produce declarative, reusable scenarios that include boundary values, security validations, and edge cases.

For dark-factory builders this is the bridge between the existing BDD/Gherkin ecosystem and StrongDM-style scenarios: Gherkin already has executable user-story semantics, established tooling, and decades of practice. The post is the most-cited 2026 reference for keeping AI-authored Gherkin from collapsing into low-signal noise as scenario counts scale into the thousands.
