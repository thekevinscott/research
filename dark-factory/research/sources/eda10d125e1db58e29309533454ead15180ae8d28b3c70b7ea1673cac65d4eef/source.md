# stagehand

The SDK For Browser Agents

The AI Browser Automation Framework
Read the Docs
If you're looking for the Python implementation, you can find it
here
Vibe code
Stagehand with
Director
What is Stagehand?
Stagehand is a browser automation framework used to control web browsers with natural language and code. By combining the power of AI with the precision of code, Stagehand makes web automation flexible, maintainable, and actually reliable.
Why Stagehand?
Most existing browser automation tools either require you to write low-level code in a framework like Selenium, Playwright, or Puppeteer, or use high-level agents that can be unpredictable in production. By letting developers choose what to write in code vs. natural language (and bridging the gap between the two) Stagehand is the natural choice for browser automations in production.
Choose when to write code vs. natural language
: use AI when you want to navigate unfamiliar pages, and use code when you know exactly what you want to do.
Go from AI-driven to repeatable workflows
: Stagehand lets you preview AI actions before running them, and also helps you easily cache repeatable actions to save time and tokens.
Write once, run forever
: Stagehand's auto-caching combined with self-healing remembers previous actions, runs without LLM inference, and knows when to involve AI whenever the website changes and your automation breaks.
Getting Started
Start with Stagehand with one line of code, or check out our
Quickstart Guide
for more information:
npx create-browser-app
Example
Here's how to build a sample browser automation with Stagehand:
// Stagehand's CDP engine provides an optimized, low level interface to the browser built for automation
const
page
=
stagehand
.
context
.
pages
(
)
[
0
]
;
await
page
.
goto
(
"https://github.com/browserbase"
)
;
// Use act() to execute individual actions
await
stagehand
.
act
(
"click on the stagehand repo"
)
;
// Use agent() for multi-step tasks
const
agent
=
stagehand
.
agent
(
)
;
await
agent
.
execute
(
"Get to the latest PR"
)
;
// Use extract() to get structured data from the page
const
{
author
,
title
}
=
await
stagehand
.
extract
(
"extract the author and title of the PR"
,
z
.
object
(
{
author
:
z
.
string
(
)
.
describe
(
"The username of the PR author"
)
,
title
:
z
.
string
(
)
.
describe
(
"The title of the PR"
)
,
}
)
,
)
;
Documentation
Visit
docs.stagehand.dev
to view the full documentation.
Build and Run from Source
git clone https://github.com/browserbase/stagehand.git
cd
stagehand
pnpm install
pnpm run build
pnpm run example
#
run the blank script at ./examples/example.ts
Stagehand is best when you have an API key for an LLM provider and Browserbase credentials. To add these to your project, run:
cp .env.example .env
nano .env
#
Edit the .env file to add API keys
Installing from a branch
You can install and build Stagehand directly from a github branch using
gitpkg
In your project's
package.json
set:
"@browserbasehq/stagehand"
:
"
https://gitpkg.now.sh/browserbase/stagehand/packages/core?<branchName>
"
,
Contributing
Note
We highly value contributions to Stagehand! For questions or support, please join our
Discord community
.
At a high level, we're focused on improving reliability, extensibility, speed, and cost in that order of priority. If you're interested in contributing,
bug fixes and small improvements are the best way to get started
. For more involved features, we strongly recommend reaching out to
Miguel Gonzalez
or
Paul Klein
in our
Discord community
before starting to ensure that your contribution aligns with our goals.
Acknowledgements
We'd like to thank the following people for their major contributions to Stagehand:
Paul Klein
Sean McGuire
Miguel Gonzalez
Sameel Arif
Thomas Katwan
Filip Michalsky
Anirudh Kamath
Jeremy Press
Navid Pour
License
Licensed under the MIT License.
Copyright 2025 Browserbase, Inc.
