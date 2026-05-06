The Dark Factory: Engineering Teams That Run With the Lights Off – AB's Reflections

[Skip to content](#wp--skip-link--target "#wp--skip-link--target")

[AB's Reflections](https://abaditya.com "https://abaditya.com")

+ [About me](https://abaditya.com/about/ "https://abaditya.com/about/")
+ [Contact](https://abaditya.com/contact/ "https://abaditya.com/contact/")

[Log in](https://wordpress.com/log-in/link?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fabaditya.com%252F2026%252F03%252F05%252Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%252F "https://wordpress.com/log-in/link?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fabaditya.com%252F2026%252F03%252F05%252Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%252F")

The Dark Factory: Engineering Teams That Run With the Lights Off
================================================================

Written by

[Aditya](https://abaditya.com/author/abaditya/ "https://abaditya.com/author/abaditya/")

in

[AI](https://abaditya.com/category/ai/ "https://abaditya.com/category/ai/"), [Programming](https://abaditya.com/category/programming/ "https://abaditya.com/category/programming/"), [Technology](https://abaditya.com/category/technology/ "https://abaditya.com/category/technology/"), [Thoughts](https://abaditya.com/category/thoughts/ "https://abaditya.com/category/thoughts/"), [Work](https://abaditya.com/category/work/ "https://abaditya.com/category/work/")

A few engineering organisations are already operating a model most companies haven’t begun to consider. While the typical software team debates whether to adopt AI coding assistants, companies like [StrongDM](https://factory.strongdm.ai/ "https://factory.strongdm.ai/") are running fully automated development pipelines where agents handle implementation, testing, review, and deployment. Humans set direction and define constraints. The mechanical work happens without them.

This isn’t speculative. It’s operational. And the gap between companies working this way and those that aren’t is widening fast.

What “lights off” actually means
--------------------------------

The term comes from manufacturing — factories that run autonomously, with minimal human presence. In software, it describes engineering organisations where AI agents do the bulk of execution work while humans focus on architecture, constraints, and outcomes.

StrongDM’s approach is instructive: their benchmark is that if you haven’t spent at least $1,000 on tokens per human engineer per day, your software factory has room for improvement. Agents work in parallel on isolated tasks. Code is written, tested, and reviewed without manual intervention. Tasks assigned Friday evening return results Monday morning.

The ratio of agents to humans is high and growing. But this isn’t about replacing engineers — it’s about fundamentally changing what engineers do.

The guardrails are the system
-----------------------------

Dark factories aren’t ungoverned. They’re heavily governed in a different way.

Linters, formatters, comprehensive test suites, design pattern enforcement — these become pre-conditions rather than suggestions. Agents are configured to seek completion only when all guardrails pass. Code review shifts from line-by-line human inspection to AI review with human spot-checks on critical paths.

The discipline moves from “write good code” to “design good systems for code to be written in.” That’s a different skill. It requires thinking about constraints, validation, and feedback loops rather than syntax and implementation details.

[Anthropic’s experiment](https://www.anthropic.com/engineering/building-c-compiler "https://www.anthropic.com/engineering/building-c-compiler") building a C compiler with parallel Claude instances demonstrates this principle. Sixteen agents worked simultaneously on a shared codebase, coordinating through git locks and comprehensive test harnesses. The result: a 100,000-line compiler capable of building the Linux kernel, produced over nearly 2,000 sessions across two weeks for just under $20,000. The project worked because the test infrastructure was rigorous enough to guide autonomous agents toward correctness without human review of every change.

[Cursor’s experiments with scaling agents](https://cursor.com/blog/scaling-agents "https://cursor.com/blog/scaling-agents") ran into a different problem. They tried flat coordination first — agents self-organising through a shared file, claiming tasks, updating status. It broke down. Agents held locks too long, became risk-averse, made small safe changes, and nobody took responsibility for hard problems. The fix was introducing hierarchy: planners that explore the codebase and create tasks, workers that grind on assigned work until it’s done. No single agent tries to do everything. The system ran for weeks, writing over a million lines of code. One project improved video rendering performance by 25x and shipped to production. Their takeaway: many of the gains came from removing complexity rather than adding it.

Digital twins as the enabler
----------------------------

The biggest blocker to agent autonomy has been the fear of breaking production. Digital twins remove that constraint.

StrongDM built behavioural replicas of third-party services their software depends on — Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets. These twins replicate APIs, edge cases, and observable behaviours with sufficient fidelity that agents can test against realistic conditions at volume, without rate limits or production risk.

[Simon Willison’s write-up](https://simonwillison.net/2026/Feb/7/software-factory/ "https://simonwillison.net/2026/Feb/7/software-factory/") of StrongDM’s approach highlights how this changed what was economically feasible: “Creating a high fidelity clone of a significant SaaS application was always possible, but never economically feasible. Generations of engineers may have wanted a full in-memory replica of their CRM to test against, but self-censored the proposal to build it.”

What makes this rigorous rather than just better staging is how they handle validation. Test scenarios are stored outside the codebase — separate from where the coding agents can see them — functioning like holdout sets in machine learning. Agents can’t overfit to the tests because they don’t have access to them. The QA team is also agents, running thousands of scenarios per hour without hitting rate limits or accumulating API costs.

The structural advantage of starting fresh
------------------------------------------

Startups and SMBs have a material advantage here. No legacy organisational structure to dismantle. No 500-person engineering floor with stakeholders defending headcount. No 18-month procurement cycles.

Capital efficiency becomes native. A three-person team with agents can produce output that previously required twenty people. The cost of compute is a fraction of equivalent human labour and falling rapidly.

This creates an asymmetric advantage. If your competitor ships in days what takes you months, no amount of talent closes that gap. And the competitive pressure isn’t just on speed — it’s on the ability to attract talent that wants to work this way. Senior engineers who’ve experienced agent-driven development don’t want to go back to manual workflows.

The gap between adopters and laggards
-------------------------------------

Companies operating this way are shipping at a fundamentally different pace. The difference isn’t incremental — it’s orders of magnitude in output per person.

Block’s recent announcement of a [near-50% reduction in headcount](https://x.com/jack/status/2027129697092731343 "https://x.com/jack/status/2027129697092731343") offers a data point. The company is reducing its organization from over 10,000 people to just under 6,000. Jack Dorsey stated “we’re not making this decision because we’re in trouble. our business is strong” but noted that “the intelligence tools we’re creating and using, paired with smaller and flatter teams, are enabling a new way of working which fundamentally changes what it means to build and run a company.”

[Cursor’s data](https://x.com/mntruell/status/2026736314272591924 "https://x.com/mntruell/status/2026736314272591924") shows the same pattern. 35% of pull requests merged internally at Cursor are now created by agents operating autonomously in cloud VMs. The developers adopting this approach write almost no code themselves. They spend their time breaking down problems, reviewing artifacts, and giving feedback. They spin up multiple agents simultaneously instead of guiding one to completion.

The laggards aren’t just slower. They’re increasingly unable to compete for talent, capital, or market position against organisations that have made this transition.

You don’t need a corporate budget to start
------------------------------------------

The dark factory model scales down. A single developer with a Claude Code subscription and well-structured GitHub workflows can run a lightweight version of the same approach.

Start with one workflow. Pick a repetitive part of your development or business process, establish the guardrails, and let agents handle it. The key investment isn’t in compute — it’s in guardrails and context. Linters, test suites, good documentation, and clear specifications matter more than token budget.

For SMBs and founders, this is the most asymmetric advantage available. You can operate at a scale that was previously only accessible with significant headcount. The learning curve is steep but short. Within 30 days of serious experimentation, most people develop the intuition for what agents can and can’t handle.

Projects like [OpenClaw](https://openclaw.ai/ "https://openclaw.ai/") — an open-source autonomous agent that executes tasks across messaging platforms and services — demonstrate that the tooling for this approach is increasingly accessible. The software runs locally, integrates with multiple LLM providers, and requires no enterprise licensing. The barrier isn’t access to technology. It’s willingness to change how work gets done.

What this means beyond software
-------------------------------

Software is where this pattern is playing out first, but the model applies wherever knowledge work is structured and repeatable.

Audit processes. Compliance checks. Report generation. Data analysis. Document review. These are all candidates for the same approach: clear specifications, comprehensive validation, and autonomous execution within defined guardrails.

Most traditional industries haven’t started thinking about this. They’re still debating whether to use ChatGPT for email drafts. The firms that figure out how to apply dark factory principles to their domain will have an enormous advantage over those still operating with manual workflows.

The lights are already off in some factories. The question isn’t whether this approach will spread. It’s how quickly your organisation recognises that the game has changed.

### Share:

* [Share on WhatsApp (Opens in new window)
  WhatsApp](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=jetpack-whatsapp "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=jetpack-whatsapp")
* [Share on X (Opens in new window)
  X](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=x "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=x")
* [Share on Facebook (Opens in new window)
  Facebook](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=facebook "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=facebook")
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=linkedin "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=linkedin")
* [Email a link to a friend (Opens in new window)
  Email](mailto:?subject=%5BShared%20Post%5D%20The%20Dark%20Factory%3A%20Engineering%20Teams%20That%20Run%20With%20the%20Lights%20Off&body=https%3A%2F%2Fabaditya.com%2F2026%2F03%2F05%2Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%2F&share=email "mailto:?subject=%5BShared%20Post%5D%20The%20Dark%20Factory%3A%20Engineering%20Teams%20That%20Run%20With%20the%20Lights%20Off&body=https%3A%2F%2Fabaditya.com%2F2026%2F03%2F05%2Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%2F&share=email")
* [Print (Opens in new window)
  Print](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#print?share=print "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#print?share=print")
* [More](# "#")

* [Share on Threads (Opens in new window)
  Threads](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=threads "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=threads")
* [Share on Bluesky (Opens in new window)
  Bluesky](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=bluesky "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=bluesky")
* [Share on Reddit (Opens in new window)
  Reddit](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=reddit "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=reddit")
* [Share on Pinterest (Opens in new window)
  Pinterest](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=pinterest "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=pinterest")

Like Loading…

---

### Discover more from AB's Reflections

Type your email…

[AI](https://abaditya.com/tag/ai/ "https://abaditya.com/tag/ai/") [engineer](https://abaditya.com/tag/engineer/ "https://abaditya.com/tag/engineer/") [enterprise](https://abaditya.com/tag/enterprise/ "https://abaditya.com/tag/enterprise/") [factory](https://abaditya.com/tag/factory/ "https://abaditya.com/tag/factory/") [futureofwork](https://abaditya.com/tag/futureofwork/ "https://abaditya.com/tag/futureofwork/") [organization](https://abaditya.com/tag/organization/ "https://abaditya.com/tag/organization/") [Technology](https://abaditya.com/tag/technology/ "https://abaditya.com/tag/technology/") [The Great Rebalancing](https://abaditya.com/tag/the-great-rebalancing/ "https://abaditya.com/tag/the-great-rebalancing/") [thoughts](https://abaditya.com/tag/thoughts-2/ "https://abaditya.com/tag/thoughts-2/") [vibe coding](https://abaditya.com/tag/vibe-coding/ "https://abaditya.com/tag/vibe-coding/")

←[The Judgment Bottleneck: Why Direction Matters More Than Execution Speed](https://abaditya.com/2026/03/03/the-judgment-bottleneck-why-direction-matters-more-than-execution-speed/ "https://abaditya.com/2026/03/03/the-judgment-bottleneck-why-direction-matters-more-than-execution-speed/")

[The Task Changed, The Job Didn’t — But Your Org Hasn’t Noticed Yet](https://abaditya.com/2026/03/10/the-task-changed-the-job-didnt-but-your-org-hasnt-noticed-yet/ "https://abaditya.com/2026/03/10/the-task-changed-the-job-didnt-but-your-org-hasnt-noticed-yet/")→

Comments
--------

### 3 responses to “The Dark Factory: Engineering Teams That Run With the Lights Off”

1. ![The Autonomous SDLC: What’s Solved, What’s Not, and Why the Gaps Are Closing Fast – AB's Reflections Avatar](https://abaditya.com/wp-content/uploads/2025/06/cropped-favicon.png?w=50)

   [March 12, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37391 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37391")

   [The Autonomous SDLC: What’s Solved, What’s Not, and Why the Gaps Are Closing Fast – AB's Reflections](https://abaditya.com/2026/03/12/the-autonomous-sdlc-whats-solved-whats-not-and-why-the-gaps-are-closing-fast/ "https://abaditya.com/2026/03/12/the-autonomous-sdlc-whats-solved-whats-not-and-why-the-gaps-are-closing-fast/")

   […] took this further with their dark factory approach. They built digital twins of production dependencies—behavioral clones of Okta, Jira, […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37391&_wpnonce=4edcb64c04 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37391&_wpnonce=4edcb64c04")Like
2. ![Indian IT’s Arbitrage Problem: When Tokens Cost the Same Everywhere – AB's Reflections Avatar](https://abaditya.com/wp-content/uploads/2025/06/cropped-favicon.png?w=50)

   [March 17, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37395 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37395")

   [Indian IT’s Arbitrage Problem: When Tokens Cost the Same Everywhere – AB's Reflections](https://abaditya.com/2026/03/17/indian-its-arbitrage-problem-when-tokens-cost-the-same-everywhere/ "https://abaditya.com/2026/03/17/indian-its-arbitrage-problem-when-tokens-cost-the-same-everywhere/")

   […] same forces dismantling labour arbitrage are creating opportunities for lean operators. A solo developer or small team with the right domain expertise and AI tools can now deliver enterprise-grade output. Clients don’t care if the work was done […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37395&_wpnonce=73a4f88c8e "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37395&_wpnonce=73a4f88c8e")Like
3. ![The AI Stack Is Running on Borrowed Infrastructure — And What Happens When It Isn’t – AB's Reflections Avatar](https://abaditya.com/wp-content/uploads/2025/06/cropped-favicon.png?w=50)

   [March 19, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37398 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37398")

   [The AI Stack Is Running on Borrowed Infrastructure — And What Happens When It Isn’t – AB's Reflections](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")

   […] of that is a reason to wait. Dark factory teams are already running production workflows on the borrowed stack — and the gap between them and […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37398&_wpnonce=e2eb8de3da "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37398&_wpnonce=e2eb8de3da")Like

More posts
----------

* ### [What it takes to actually run NanoClaw](https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/ "https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/")

  [May 6, 2026](https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/ "https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/")
* ### [Why I picked NanoClaw over OpenClaw for a GTM pipeline](https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/ "https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/")

  [May 6, 2026](https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/ "https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/")
* ### [Building a GTM dark factory with Nemotron 3 and NanoClaw](https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/ "https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/")

  [May 6, 2026](https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/ "https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/")
* ### [The AI Stack Is Running on Borrowed Infrastructure — And What Happens When It Isn’t](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")

  [March 19, 2026](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")

[AB's Reflections](https://abaditya.com "https://abaditya.com")

Geeky thoughts on a variety of topics

[Website Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered "https://wordpress.com/?ref=footer_custom_powered").

Discover more from AB's Reflections
-----------------------------------

Type your email…

[Continue reading](# "#")

%d

 
![](https://pixel.wp.com/b.gif?v=noscript)