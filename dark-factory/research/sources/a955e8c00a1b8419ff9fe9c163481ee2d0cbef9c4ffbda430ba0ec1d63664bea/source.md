How Stripe’s Minions Ship 1,300 PRs a Week

[![ByteByteGo Newsletter](https://substackcdn.com/image/fetch/$s_!1eXV!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5609ae-1239-4400-9491-6010a15c4d60_504x504.png)](/ "/")

[ByteByteGo Newsletter](/ "/")
==============================

SubscribeSign in

How Stripe’s Minions Ship 1,300 PRs a Week
==========================================

[![ByteByteGo's avatar](https://substackcdn.com/image/fetch/$s_!U1Ej!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9941c68-e5b7-4b93-be75-df7cc4ffef02_504x540.png)](https://substack.com/@bytebytego399569 "https://substack.com/@bytebytego399569")

[ByteByteGo](https://substack.com/@bytebytego399569 "https://substack.com/@bytebytego399569")

Mar 16, 2026

305

6

11

Share

**[npx workos: An AI Agent That Writes Auth Directly Into Your Codebase (Sponsored)](https://go.bytebytego.com/WorkOS_031626Headline "https://go.bytebytego.com/WorkOS_031626Headline")**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![](https://substackcdn.com/image/fetch/$s_!xEk7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e7342e3-e6e9-4a94-9d51-e989851e2667_1280x720.png)](https://go.bytebytego.com/WorkOS_031626CTA "https://go.bytebytego.com/WorkOS_031626CTA")

**npx workos** [launches an AI agent](https://go.bytebytego.com/WorkOS_031626Agent "https://go.bytebytego.com/WorkOS_031626Agent"), powered by Claude, that reads your project, detects your framework, and writes a complete auth integration directly into your existing codebase. It’s not a template generator. It reads your code, understands your stack, and writes an integration that fits.

The [WorkOS](https://go.bytebytego.com/WorkOS_031626WorkOS "https://go.bytebytego.com/WorkOS_031626WorkOS") agent then typechecks and builds, feeding any errors back to itself to fix.

[See how it works →](https://go.bytebytego.com/WorkOS_031626CTA "https://go.bytebytego.com/WorkOS_031626CTA")

---

Every week, Stripe merges over 1,300 pull requests that contain zero human-written code. Not a single line. These PRs are produced by “Minions,” Stripe’s internal coding agents, which work completely unattended.

An engineer sends a message in Slack, walks away, and comes back to a finished pull request that has already passed automated tests and is ready for human review. The productivity boost scenario is quite compelling.

Here’s what it looks like:

[![](https://substackcdn.com/image/fetch/$s_!VLnO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdd99d30-98d4-42a2-9fcf-d28bffa6cba4_1592x728.png)](https://substackcdn.com/image/fetch/$s_!VLnO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdd99d30-98d4-42a2-9fcf-d28bffa6cba4_1592x728.png "https://substackcdn.com/image/fetch/$s_!VLnO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdd99d30-98d4-42a2-9fcf-d28bffa6cba4_1592x728.png")

**Source:** [Stripe Engineering Blog](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents")

Consider a Stripe engineer who is on-call when five small issues pile up overnight. Instead of working through them sequentially, they open Slack and fire off five messages, each tagging the Minions bot with a description of the fix. Then, they go to get coffee. By the time they come back, five agents have each spun up an isolated cloud machine in under ten seconds, read the relevant documentation, written code, run linters, pushed to CI, and prepared pull requests. The developer reviews them, approves three, sends feedback on one, and discards the last. In other words, five issues were handled in the time it would have taken to fix two manually.

However, the primary reason the Minions work has almost nothing to do with the AI model powering them. It has everything to do with the infrastructure that Stripe built for human engineers, years before LLMs existed. In this article, we will look at how Stripe managed to reach this level.

*Disclaimer: This post is based on publicly shared details from the Stripe Engineering Team. Please comment if you notice any inaccuracies.*

Why Off-the-Shelf Agents Weren’t Enough
---------------------------------------

The AI coding tools you’ve probably encountered fall into a category called attended agents. Tools like Cursor and Claude Code work alongside you. Developers watch them, steer them when they drift, and approve each step.

See the diagram below that shows the typical view of an AI Agent:

[![](https://substackcdn.com/image/fetch/$s_!AEb8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64f5fc53-0189-42c3-9a94-4e7464e2f26c_2114x1374.png)](https://substackcdn.com/image/fetch/$s_!AEb8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64f5fc53-0189-42c3-9a94-4e7464e2f26c_2114x1374.png "https://substackcdn.com/image/fetch/$s_!AEb8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64f5fc53-0189-42c3-9a94-4e7464e2f26c_2114x1374.png")

Stripe’s engineers use these tools too. However, Minions are what’s known as unattended agents. No one is watching or steering them. The agent receives a task, works through it alone, and delivers a finished result. This distinction changes the design requirements for everything downstream.

Stripe’s codebase also makes this harder than it sounds. The codebase consists of hundreds of millions of lines of code, mostly written in Ruby with Sorbet typing, which is a relatively uncommon stack. The code is full of homegrown libraries that LLMs have never encountered in training data, and it moves well over $1 trillion per year in payment volume through production. The stakes are as extreme as the complexity.

Building a prototype from scratch is fundamentally different from contributing code to a codebase of this scale and maturity. So Stripe built Minions specifically for unattended work, and let third-party tools handle attended coding.

---

[Unblocked: Context that saves you time and tokens (Sponsored)](https://go.bytebytego.com/Unblocked_031626 "https://go.bytebytego.com/Unblocked_031626")
--------------------------------------------------------------------------------------------------------------------------------------------------------

[![](https://substackcdn.com/image/fetch/$s_!3pqV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55a0942b-49b3-4c75-94ca-310d5fb447fb_1600x840.png)](https://go.bytebytego.com/Unblocked_031626 "https://go.bytebytego.com/Unblocked_031626")

AI coding tools are fast, capable, and completely context-blind. Even with rules, skills, and MCP connections, they generate code that misses your conventions, ignores past decisions, and breaks patterns. You end up paying for that gap in rework and tokens.

Unblocked changes the economics.

It builds organizational context from your code, PR history, conversations, docs, and runtime signals. It maps relationships across systems, reconciles conflicting information, respects permissions, and surfaces what matters for the task at hand. Instead of guessing, agents operate with the same understanding as experienced engineers.

You can:

* Generate plans, code, and reviews that reflect how your system actually works
* Reduce costly retrieval loops and tool calls by providing better context up front
* Spend less time correcting outputs for code that should have been right in the first place

[See how it works](https://go.bytebytego.com/Unblocked_031626 "https://go.bytebytego.com/Unblocked_031626")

---

The Environment to Run Agents
-----------------------------

Once Stripe decided to build custom, the first problem was about where to actually run these agents.

An unattended agent needs three properties from its environment:

* It needs isolation, so mistakes can’t touch production.
* It needs parallelism, so multiple agents can work simultaneously on separate tasks.
* And it needs predictability, so every agent starts from a clean, consistent state.

Stripe already had all three. Their “devboxes” are cloud machines pre-loaded with the entire codebase, tools, and services. They spin up in ten seconds because Stripe proactively provisions and warms a pool of them, cloning repositories, warming caches, and starting background services ahead of time. Engineers already used one devbox per task, and a single engineer might have half a dozen running at once. Agents slot into this same pattern.

Since devboxes run in a QA environment, they are already isolated from production data, real user information, and arbitrary network access. That means agents can run with full permissions and no confirmation prompts. The blast radius of any mistake is contained to one disposable machine.

The important thing to understand is that Stripe didn’t build this for agents. They built it for humans. Parallelism, predictability, and isolation were desirable properties for engineers long before LLMs entered the picture. In other words, what’s good for humans is good for agents as well.

Agent Don’t Freestyle
---------------------

A good environment gives the agent a place to work. But it doesn’t tell the agent how to work.

There are two common ways to orchestrate an LLM system:

* A workflow is a fixed graph of steps where each step does one narrow thing, and the sequence is predetermined.
* An agent is a loop where the LLM decides what to do next based on the results of its previous actions.

Workflows are predictable but rigid. Agents are flexible but unreliable.

Stripe built something in between that they call “blueprints.” A blueprint is a sequence of nodes where some nodes run deterministic code, and other nodes run an agentic loop. Think of it as a structure that alternates between rigid steps and creative steps. For example, the “implement the feature” step or “fix CI failures” step gets the full agentic loop with tools and freedom. On the other hand, the “run linters” step is hardcoded. The “push the branch” step is hardcoded.

[![](https://substackcdn.com/image/fetch/$s_!TXE2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a82da8-3ae2-4ca0-b228-910029a1dcbb_2086x1504.png)](https://substackcdn.com/image/fetch/$s_!TXE2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a82da8-3ae2-4ca0-b228-910029a1dcbb_2086x1504.png "https://substackcdn.com/image/fetch/$s_!TXE2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a82da8-3ae2-4ca0-b228-910029a1dcbb_2086x1504.png")

This separation matters because some tasks should never be left to the agent’s judgment. You always want linters to run. You always want the branch pushed in a specific way that follows the company’s PR template. Making these deterministic saves tokens, reduces errors, and guarantees that critical steps happen every single time. Across hundreds of runs per day, each deterministic node is one less thing that can go wrong, and that compounds into big reliability gains.

The Right Context
-----------------

Blueprints tell the agent how to work. But the agent still needs to know what it’s working with. In a codebase of hundreds of millions of lines, getting the right information into the agent’s limited context window is an engineering challenge.

LLMs can only hold so much text at once. If you try to load every coding rule and convention globally, the agent’s context fills up before it even starts working. Stripe uses global rules “very judiciously” for exactly this reason. Instead, they scope rules to specific subdirectories and file patterns. As the agent moves through the filesystem, it automatically picks up only the rules relevant to where it’s working. These are the same rule files that human-directed tools like Cursor and Claude Code read, so there is no duplication and no agent-specific overhead.

For information that doesn’t live in the filesystem, Stripe built a centralized internal server called Toolshed. It hosts nearly 500 tools using MCP, which stands for Model Context Protocol and is essentially an industry standard that gives agents a uniform way to call external services. Through MCP, agents can fetch internal documentation, ticket details, build statuses, code search results, and more.

[![](https://substackcdn.com/image/fetch/$s_!qLuB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6688d4c-3e5a-460f-84f4-9393af599c0f_2772x1708.png)](https://substackcdn.com/image/fetch/$s_!qLuB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6688d4c-3e5a-460f-84f4-9393af599c0f_2772x1708.png "https://substackcdn.com/image/fetch/$s_!qLuB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6688d4c-3e5a-460f-84f4-9393af599c0f_2772x1708.png")

But more tools aren’t better. Agents perform best with a carefully curated subset relevant to their task. Stripe gives Minions a small default set and lets engineers add more when needed.

Fast Feedback, Hard Limits
--------------------------

The agent now has an environment, a structure, and the right context. However, the code still had to be correct, which meant more feedback loops.

Stripe’s feedback architecture works in layers:

* First, local linting runs on every push in under five seconds. A background daemon precomputes which lint rules apply and caches the results, so this step is nearly instantaneous.
* Second, CI selectively runs tests from Stripe’s battery of over three million tests, and autofixes are applied automatically for known failure patterns.
* Third, if failures remain without an autofix, the agent gets one more chance to fix and push again.

Then it stops. At most two rounds of CI. If the code doesn’t pass after the second push, the branch goes back to the human engineer.

This cap is intentional. LLMs show diminishing returns when retrying the same problem repeatedly. More rounds cost more tokens and compute without proportional improvement. Knowing when to stop is as important as knowing how to start.

When a minion run doesn’t fully succeed, it’s still often a useful starting point. A partially correct PR that an engineer can polish in twenty minutes is still a significant win. Stripe is designed for this reality rather than pretending every run would be perfect.

Conclusion
----------

Four layers make Stripe’s Minions work:

* Isolated environments that give agents safe, parallel workspaces.
* Hybrid orchestration that mixes deterministic guardrails with agentic flexibility.
* Curated context that feeds agents the right information without overwhelming them.
* And fast feedback loops with hard limits on iteration.

Each layer is necessary, and none alone is sufficient.

The primary insight in Stripe’s approach is that investments in developer productivity over the years can provide unexpected dividends when agents are included in the workflow. Human review didn’t disappear either, but shifted. Engineers moved from writing code to reviewing code.

A key lesson while thinking about deploying coding agents is not to start with model selection. Start with your developer environment, your test infrastructure, and your feedback loops. If those are solid, agents will benefit from them. If they’re not, no model will save you. Stripe’s experience suggests the answer is less about AI breakthroughs and more about the engineering fundamentals that were always supposed to matter.

**References:**

* [Minions: Stripe’s one-shot end-to-end coding agents - Part 1](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents")
* [Minions: Stripe’s one-shot end-to-end coding agents - Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 "https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2")

305

6

11

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Steve Latz's avatar](https://substackcdn.com/image/fetch/$s_!KB-v!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6cf7b98a-e3b8-4430-8f0b-01f1441d3f1f_144x144.png)](https://substack.com/profile/17055004-steve-latz?utm_source=comment "https://substack.com/profile/17055004-steve-latz?utm_source=comment")

[Steve Latz](https://substack.com/profile/17055004-steve-latz?utm_source=substack-feed-item "https://substack.com/profile/17055004-steve-latz?utm_source=substack-feed-item")

[Mar 16](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comment/228655628 "Mar 16, 2026, 3:43 PM")

If a major payments application is making 1,000 changes a week to its codebase, even if those changes are "thoroughly" tested, that indicates a very problematic approach to their foundation architecture as well as their change management processes.

ReplyShare

[![SilverLionApps's avatar](https://substackcdn.com/image/fetch/$s_!n7Iv!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fblack.png)](https://substack.com/profile/198190169-silverlionapps?utm_source=comment "https://substack.com/profile/198190169-silverlionapps?utm_source=comment")

[SilverLionApps](https://substack.com/profile/198190169-silverlionapps?utm_source=substack-feed-item "https://substack.com/profile/198190169-silverlionapps?utm_source=substack-feed-item")

[Mar 16](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comment/228665012 "Mar 16, 2026, 4:00 PM")

I appreciated this article, but it was disappointing that there's no discussion of how Stripe handles the biggest bottleneck (imo) in this approach -- the code review. Knowing how Stripe handles reviewing those 1,000 PRs /week would be valuable insight. I'm sure I could take guesses at what they do, but I hope there's a follow up article on this topic.

ReplyShare

[1 reply](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comment/228665012 "https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comment/228665012")

[4 more comments...](https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comments "https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs/comments")

TopLatestDiscussions

No posts

### Ready for more?

© 2026 ByteByteGo · [Privacy](https://substack.com/privacy "https://substack.com/privacy") ∙ [Terms](https://substack.com/tos "https://substack.com/tos") ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected "https://substack.com/ccpa#personal-data-collected")

[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer "https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer")[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button "https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button")

[Substack](https://substack.com "https://substack.com") is the home for great culture

![](https://www.facebook.com/tr?id=3593074844345833&ev=PageView&noscript=1)

![](https://analytics.twitter.com/i/adsct?p_id=Twitter&p_user_id=0&txn_id=oesry&events=%5B%5B%22pageview%22%2Cnull%5D%5D&tw_sale_amount=0&tw_order_quantity=0&tw_iframe_status=0)
![](https://t.co/i/adsct?p_id=Twitter&p_user_id=0&txn_id=oesry&events=%5B%5B%22pageview%22%2Cnull%5D%5D&tw_sale_amount=0&tw_order_quantity=0&tw_iframe_status=0)

This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/ "https://enable-javascript.com/") or unblock scripts