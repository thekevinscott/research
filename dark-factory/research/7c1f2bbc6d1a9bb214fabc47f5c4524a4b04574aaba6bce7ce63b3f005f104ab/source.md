Night Shift Agentic Workflow - Jamon Holmgren

[Jamon Holmgren](/ "/")
=======================

* [beginnings](/beginnings "/beginnings")
* [now](/now "/now")
* [tech](/tech "/tech")
* [talks](/talks "/talks")
* [blog 1](/blog "/blog")
* [connect](/links "/links")

The "Night Shift" Agentic Workflow
----------------------------------

*by Jamon Holmgren on March 14, 2026 (last updated March 16, 2026)*

Since December, 2025, I've been integrating AI agents into my coding workflow.

Previous attempts at agentic workflows have left me exhausted, overwhelmed, and feeling out of touch with the
systems I was building. They also degraded quality too much.

My current agentic workflow is about 5x faster, better quality, I understand the system better, and
**I'm having fun again.**

### I call this the Night Shift workflow.

The key ideas that led me to Night Shift:

1. My time, energy, and "human token usage" are highly constrained and expensive resources.
2. Agents and agent tokens are cheap and plentiful and practically unconstrained.
3. I want to remain in control, with the minimum (but no less than the minimum) of my own effort and time.
4. I do not like babysitting agents.
5. I do not want to read agent plans.
6. I do not want to sit and prompt and reprompt agents.
7. I want them to get better over time.
8. I want to focus on one thing at a time.
9. I want to be in control.
10. I don't want to feel anxious when an agent is sitting idle waiting for me.

I decided that I will take the day shift, and AI agents will take the night shift. I will prepare everything for
them as much as I can during the day shift. Then, during the night, they will work autonomously while I am resting,
and be done by the next morning.

### The Day Shift

During the day shift, it's my time. The agents are sitting idle. I am not babysitting them.

I interface with humans, gathering requirements, thinking through the system architecture, and writing up a
specification document with as much detail as I can write.

I spend a lot of time on this. I snooze AI autocomplete. I do as much work myself as I think necessary to spec out
the work for the agent tonight. The system design and possible problems and solutions get embedded in my brain.

Specs describe the feature, all the edge cases to cover, everything I can think of. They're well organized — not for
the agent, but for ME. To organize my own thinking.

Spec writing is hard at first and gets easier. Don't give up because it's hard. Your brain will get better and
better at it.

When I finish, I do not run the agent to implement the spec yet. I take a break.

Then, if I have time, I take another feature. I write out the spec. I take my time. I work at a sustainable pace.

I take breaks. Everything is sitting idle and silent.

I do use AI during the day shift, but only in two narrow ways:

1. **Info lookup:** Short "Ask" mode queries to find information for me. It's a helper bringing info
   to my desk, and it had better be concise. I am not here to read pages of generated text! Give me the sharpest
   most concise answer. Let me do the design.
2. **Plan review:** Once I've written my spec, I have the agent review *my* plan and give me a
   concise checklist of edge cases or gaps I may have missed. It often catches things I didn't think of — this is a
   great use of AI. But it had better be brief: a checklist, not an essay. I then manually fold those items into my
   spec and consider each one on my own terms.

Finally, it's time to wrap up for the day. If I'm not done with a spec, that's okay. Leave it for tomorrow.

All the completed spec docs live in a folder, `./Specs`. If they are named
`draft-*`, the agent will ignore them.

I load up Claude Code, Cursor, or Codex — whichever I've decided will work that evening.

I tell it to load `@AGENT_LOOP.md`. This is a markdown file that explains the process of
how to work at night. More on this later.

Critically, `@AGENTS.md` is a small (~150 line) "router", which tells the agent where to
find documentation. This includes workflow docs, skill docs (I don't use agent skills directly; these are roughly
equivalent), and system documentation (describing different parts of the system). Specs don't have to solve
everything for the agent. The more you push into docs instead, and have a good agent router to hint to the agent to
load those docs, the smaller your specs can be.

I kick it off, and I lock my computer for the evening. I'm done. The Night Shift is on it.

### The Night Shift Gets to Work

While I'm away, the agent does the following:

0. Prep: Cleans the working tree by analyzing any uncommitted work and doing the right thing with it (stash or
   commit). Also runs the entire current test suite and fixes any failures it encounters.
1. Picks a task from bugs first, or if bugs are complete, a feature that I've completed a spec for
2. Loads up the spec, and then analyzes it
3. Loads relevant docs, then looks at relevant code
4. Develops a testing plan (absolutely critical)
5. Writes extensive tests for this, then runs them, expecting failures
6. Develops an extensive plan of its own (I NEVER read this, I do not care)
7. Runs sub-agents as critical reviewers (review agents) based on 6 personas I've detailed in
   `REVIEW_PERSONAS.md`: Designer, Architect, Domain Expert, Code Expert, Performance
   Expert, Human Advocate. Each of these "owns" a portion of the docs, and reviews against their own documentation,
   including suggesting where their own docs need to be adapted.
8. Adapts plan based on review agent reviews, and loops to 7 until green light from all review agents
9. Implements the plan, including documentation adjustments (docs live in the same code base under Docs)
10. Runs type checking, linting, compiler, other static analysis tools such as bundle size reporter, as many things as
    possible, and of course the relevant tests themselves, and verifies that it works, iterating as it goes. Be as
    strict as possible with your type checking and linting system. I used to be anti strictness, but that was when I
    was a wetware dev. For agents, I want the most strictness
    possible.
11. Run the entire test suite to protect against regressions, fix any new issues
12. Runs the review agents again on the implementation diff, and loops back to step 10 until getting a green light
    from all review agents.
13. Add any encountered unrelated TODOs for human review that they've noticed along the way to the TODO doc
14. Wrap-up: write a CHANGELOG entry, commit with a detailed commit message meant for human context when reviewing the
    code. (More on commits later)
15. Loop back to the beginning (step 1), and select the next task or spec.
16. When completely done, write up a report for human review. Extremely concise. Details live in commit messages.
17. The Night Shift is done. It goes silent and waits for me to wake up.

Automated testing is incredibly important. This WILL NOT WORK if you don't have a super robust end-to-end testing
harness in place and excellent docs so the agents can create their own tests.

### The Day Shift Clocks In

1. **Review:** Check the changelog and agent recap. Then go commit by commit, reviewing each commit
   message, implementation diff, tests, and docs changes.
2. **Stacked commits:** I keep all commits in the same branch so they stack on each other (a good use
   for stacked PRs, btw). Improvements carry forward to each subsequent commit. Fewer conflicts, better results, less
   duplicative work.
3. **Quick fixes:** If I need to correct something quickly, I do it using an interactive agent session
   or by hand. But before I do, I ALWAYS analyze and correct the docs, workflow, and validations/testing first.
4. **Postmortem:** If the agent misbehaved, don't just fix the code. Don't tell it to fix the code
   either. Use that valuable context to figure out *why* it did the wrong thing. Have it analyze its own
   context and tell you what docs, skills, or workflow led it astray, and what improvements would make it make the
   right decision next time. Have it fix those issues first — be diligent, because you can amortize the improvement
   over the rest of your project. Only after that, have it fix the original issue. Use that feedback cycle and
   continuous improvement to get to a point where it is making the right decisions more often than not.
5. **Manual testing:** I check almost every change manually and thoroughly. Not just to catch bugs, but
   to catch gaps in my docs, skills, specs, validations/tests, and my own understanding of the system. And fix them!
6. **Spec writing:** Then I get back to the first part — gathering requirements, writing specs, doing
   architecture, and thinking a lot.

The Night Shift needs my best work. So I do my best work without context shifting and babysitting agents.

That's my Night Shift agentic workflow.

I also summarized the practices that have mattered most for keeping agent output usable in
[The eight best ways I've improved my AI agent's code](/8ways "/8ways").

### The Feedback Loop

An important characteristic of this is that I am NOT there to babysit it.

I can't paper over docs or workflow imperfections by steering it by hand. I must improve every day, so the next
morning isn't spent cleaning up a mess. Constant improvement via a feedback loop is the key.

You should be willing to burn all the tokens trying to make sure everything is as perfect as the agent can make it
before a human ever has to review anything. A human should not be having to catch basic obvious issues. If so, your
automated validations suck and you need to fix them. This includes having robust agent review steps.

My time and energy are precious. I will not accept anything less than the agent's best.

### The Results So Far

I started using early versions of this workflow about a month ago, and it has gotten better and better every day.
Every time I come in to look at the code, the results are better than before.

I'm spending far less time babysitting, much more time thinking about the problems I need to solve, and my
productivity soars.

Very little context shifting, more peaceful and relaxed workflow, and when the agent runs that night, it runs
unimpeded by me.

One experiment I ran was to have Codex watch what Claude was doing and write feedback into a file. Claude knew it
was doing this, would tail the file, and pull in the feedback for consideration. It actually worked pretty well
and I may do this more often in the future.

Prompt:

`"I have another agent doing the AGENT_LOOP.md right now, working through TODOS.md. What I'd like you to do is do
your own loop as an expert reviewer.

1. Sleep for 5 minutes at a time.
2. Then, wake up look at the current git log to see if any new commits have landed
3. Systematically review them against the corresponding TODOS.md entry.
4. Provide your feedback about each commit in a file named TODOS_CODEX_REVIEW.md located in the same folder as
   TODOS.md.
5. I will tell the other agent to take a look at your notes for it in that folder, and it will then incorporate
   your feedback in a separate, second loop.
6. If you do not find any new commits (even if there are working tree changes), please don't do anything and just
   sleep again.
7. You'll know you should be done when all the current TODOs are marked complete or moved into the 'NEEDS INPUT
   FROM USER' section. In that case, you can stop.
8. If you do not see any changes within 30 minutes, go ahead and stop, as the other agent may have quit
   prematurely."`

[Connect with me!](/links "/links")

Built on [Qub](https://qub.jamon.dev "https://qub.jamon.dev"), the QBasic web framework.
