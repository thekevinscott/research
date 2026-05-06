# Hacker News thread: StrongDM's AI team build serious software without even looking at the code

Source: Hacker News
URL: https://news.ycombinator.com/item?id=46924711

## Summary

This Hacker News thread (item 46924711) is the primary HN discussion of Simon Willison's writeup of StrongDM's software factory. Comments range from defenders to skeptics, with the skeptical contingent dominating the technical evaluation. As soon as the code was released (Attractor + CXDB repos), HN commenters began reviewing it, surfacing suspected bugs, Rust anti-patterns, and lenient error handling. StrongDM AI team member Jay Taylor responded that the projects "were only decided to be open-sourced in the past few days" and had not undergone sufficient technical optimization.

This thread is one of the highest-signal sources for Dark Factory criticism because HN commenters include working engineers who actually examined the released code. Their critiques converged on the same points that other skeptics have made: heavy Arc<Mutex> usage suggesting the LLM "fought the borrow checker," lenient error handling, and skepticism that "Code must not be reviewed by humans" can be sensible given that LLMs are known to hallucinate. For pitfalls research this thread is the best snapshot of working engineer reaction to the manifesto.

## Reconstructed from search snippets

### Code quality criticisms

> "Developers on Hacker News quickly examined the open-sourced code and pointed out suspected bugs, Rust anti-patterns, and relatively lenient error handling methods."

Specific concerns called out:
- Suspect bugs in the released Rust code.
- Anti-patterns: Arc<Mutex> overuse — a sign of LLMs struggling with Rust ownership models.
- Lenient error handling — the agent's outputs satisfied compile/pass but not robustness.

### Vendor response

> "Jay Taylor, a member of the StrongDM AI team, commented in the discussion area that these projects 'were only decided to be open-sourced in the past few days' and had not undergone sufficient technical optimization."

The defense — that the open-sourced code wasn't polished — implicitly concedes the criticism. But it also raises the question: if the code that was deemed worth releasing as a flagship example of Dark Factory output has these issues, what does the rest of the production codebase look like?

### Cost and review skepticism

> "Comments questioning how 'Code must not be reviewed by humans' could be sensible when LLMs are known to make errors."

> "Outside of FAANG companies, spending $1,000 per engineer per day on AI tokens would exceed spending on human salaries."

## Why this matters

The HN thread is Exhibit A for the working-engineer skeptical reaction to Dark Factory. The collective signal is: engineers who can read Rust looked at the code and didn't like it. That's the empirical indictment that Polyglot Factotum's review formalizes and that downstream critics keep referencing.
