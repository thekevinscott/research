# Butler — Dark Factory: No humans should write code (and what it taught me)

Source: https://world.hey.com/johnnybutler/dark-factory-no-humans-should-write-code-and-what-it-taught-me-3f1a06f0

---

Dark Factory: “No Humans Should Write Code” (and what it taught me)




[Johnny Butler](/johnnybutler "/johnnybutler")

February 28, 2026

Dark Factory: “No Humans Should Write Code” (and what it taught me)
-------------------------------------------------------------------

A few weeks ago I read Simon Willison’s write-up on StrongDM’s “Software Factory” approach. The line that stuck with me wasn’t even about agents or tooling — it was the mantra:

* **Code must not be written by humans**
* **Code must not be reviewed by humans**

I found it fascinating… and honestly a bit uncomfortable. Not because it’s wrong, but because it forces you to ask a hard question:

If AI can do the mechanical work, what exactly should humans be doing?

**The idea of a Dark Factory (in practical terms)**

When people hear “Dark Factory”, they often imagine a black box where you type a prompt and software appears.

What StrongDM describe is more specific:

* Humans define **intent** (specs, constraints)
* Humans define **reality checks** (scenarios/harness)
* Agents implement end-to-end, then **iterate until validation passes**
* Humans don’t review diffs — they review **outcomes**

If you want a shorthand: it’s not “AI writes code”. It’s **validation replaces code review**.

**Reality check: doing this in a legacy monolith is hard**

In my day job, I’m Head of Engineering in a Rails monolith with plenty of legacy code, tech debt, and a bunch of operational realities baked into the system.

Inside that environment, I can get to something like **Level 3-ish**: agents do a lot of implementation, I steer via tight prompts, and I’m heavily outcome-driven — but the monolith pushes back:

* hidden coupling
* unclear boundaries
* slow feedback loops
* “one change touches everything”
* fear of regressions because the harness isn’t complete everywhere

In isolated greenfield areas I can push closer to **Level 4**: narrower scope, clearer contracts, faster validation, and less incidental complexity.

But truly “no humans write/review code” in a big monolith? That’s not a switch you flip. It’s an architecture and process problem.

**So I built a personal project to experience the full cycle**

I decided to build a personal website as a fully spec-driven “dark factory” project.

* It’s live here: [johnnybutler.dev](https://johnnybutler.dev/ "https://johnnybutler.dev/")

Why?

* I want a public website where my network can learn about me in a work-specific way
* I want an **AI interface** that can answer questions about my experience and thinking (grounded in sources, with citations)
* I want to get hands-on with the full dark-factory loop: **specs in → software out**
* I want a real case study I can talk about — not a theoretical opinion

And crucially: I wanted to do it greenfield so I could design the environment *for* the factory approach instead of fighting constraints from day one.

**What surprised me: it felt like when TDD first clicked**

The early setup took a bit of effort — more than a typical “just start coding” project:

* writing down the rules
* creating acceptance scenarios
* setting up a harness and CI gates
* logging prompts and run outputs so the process was auditable

But after a few iterations, something clicked.

It felt like the first time **TDD really clicked** for me: when you stop thinking “tests slow me down” and you realize the tests are what let you move fast safely.

Same here.

Once the loop is in place, it becomes genuinely enjoyable:

* you describe the change
* the agent runs with it
* CI fails (good!)
* the agent fixes until green
* you merge based on outcomes

You don’t need heroics. You need a factory.

**The key lesson: the path back into the monolith is through boundaries**

The goal isn’t “replace my entire monolith with a dark factory.” That’s unrealistic.  
The goal is to **carve out boundaries** where a factory can operate with full autonomy.  
  
My mental model now is:  
**Build dedicated “micro-factories” inside the monolith**

Each factory owns a narrow surface area with clean contracts and independent validation, for example:

* A factory that produces **API endpoints** behind a dedicated namespace(small scope, easy to specify, easy to test independently)
* A factory dedicated to our **AI chat / MCP integration**(clear inputs/outputs, strong evals, strict safety guardrails)
* A factory for a self-contained UI area like **Supplier Live Feed**(system tests + scenarios, isolated views, predictable behavior)

In other words: instead of “dark factory vs monolith”, it becomes:

**monolith = a collection of sub-systems, each with its own harness and autonomy**

That feels achievable.

**A useful analogy: telecoms factory lines**

This whole thing also reminded me of an old chapter of my career.

Years ago I worked in a telecoms company building network equipment on a literal factory line. Each station had a clear responsibility:

* assemble
* test
* QA
* pack
* ship

And the factory floor wasn’t one single line. There were **multiple lines** producing different models of equipment.

Some lines shared the same global rules — safety checks, QA standards, common test rigs — but each line also had **slightly different specs** depending on the model.

That analogy maps surprisingly well to “dark factory” inside a monolith.  
A monolith doesn’t have to become one giant AI pipeline. Instead, you create multiple **factory lines** inside it:

* each line owns a bounded area (API endpoints, chat/MCP integration, supplier feed UI, etc.)
* each line has its own harness/scenarios and can run autonomously end-to-end
* and they all share common standards (branching rules, CI gates, logging, security, quality thresholds)

So it’s not “rewrite the monolith.”

It’s: **introduce factory lines into the monolith**, one boundary at a time, with shared guardrails and tailored acceptance checks.

**Dark Factory isn’t “no humans”. It’s “humans move up the stack.”**

The StrongDM framing is provocative, but the real shift is deeper:

* Humans stop spending time on mechanical implementation and diff-reading
* Humans spend time on:
  + intent
  + constraints
  + scenario design
  + safety
  + evaluation
  + system boundaries

And that’s exactly where experienced engineers add leverage.

If there’s one thing this experiment gave me, it’s a more practical pathway back into the monolith:

Not a rewrite. Not a big-bang transformation.

A set of **factory lines** with shared rules, each responsible for a bounded part of the system — producing software from specs, and proving it with harnesses instead of opinions.

That’s the journey I’m on.

Subscribe to get future posts via email (or grab the [RSS feed](https://world.hey.com/johnnybutler/feed.atom "https://world.hey.com/johnnybutler/feed.atom"))

Subscribe

[Sent to the world with HEY](https://www.hey.com/world/?utm_source=hw-web "https://www.hey.com/world/?utm_source=hw-web")
