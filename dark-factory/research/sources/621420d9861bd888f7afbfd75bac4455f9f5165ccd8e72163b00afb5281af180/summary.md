# langwatch/scenario

Scenario (LangWatch) is an agent-testing framework based on simulations: it spins up a simulated user that talks to your real agent and a Judge Agent that watches each turn and decides whether to continue or end with a verdict. It is Python/TypeScript/Go, eval-framework-agnostic, and integrates with custom assertions and tool-call checks.

Scenario is the canonical scenario-runner + agent-as-judge framework in OSS — exactly the kind of thing StrongDM's 'satisfaction' metric and 'holdout scenarios' need underneath them. In Dark Factory pipelines Scenario sits in the validation loop that decides whether an agent's PR is mergeable, and the Judge Agent pattern is one of the few realistic alternatives to deterministic test pass/fail when behavior is probabilistic.
