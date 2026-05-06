# We built a software factory in 10 days. Here's what we learned.

- URL: https://ona.com/stories/software-factory-what-we-learned
- Organisation: Ona (formerly Gitpod) - dev environments / agent platform
- Reconstructed from WebSearch snippets.

## What this is

A first-hand company case study in which the Ona team ran their own dark factory style experiment for 10 days, generating a real product entirely from specs. Direct first-hand metrics make this one of the strongest case studies outside StrongDM itself.

## Headline metrics (from snippets)

- 375 PRs generated
- 67k lines of code
- 0 human-written code

## Direct quotes / near-quotes from snippets

> "The biggest learning of the project was the inverse correlation between spec quality and necessary product iterations."

> "When they wrote a detailed product spec on Day 3, the factory produced a working app with authentication, workspaces, a rich text editor, search, and member invites."

> "Most bugs were not capability failures but specification failures - the factory built what they described and missed things they hadn't described clearly enough."

> "In a software factory, the spec becomes the control surface - acceptance criteria, examples, design references, architecture notes, and edge cases directly shape the output."

> "The real risk of software factories isn't that teams ship too little, but that they ship too much."

## Key first-hand lessons

- Spec quality dominates outcomes - bad specs, not bad models, were the cause of nearly every bug.
- The factory could build the backlog but couldn't sense what users needed next, so they had to bolt on a feedback widget and a digest automation that turns user feedback into spec updates.
- Feature bloat is the new failure mode: an unsupervised factory produces too much, not too little.

## Takeaway

Ona's report is one of the cleanest "we tried it" case studies: a small team produced a working SaaS-style product in 10 days entirely from specs, and the lessons cluster on spec engineering and outbound feedback loops, not on agent capability.
