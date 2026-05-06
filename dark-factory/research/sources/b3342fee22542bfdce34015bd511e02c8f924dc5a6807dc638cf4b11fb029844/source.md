# StrongDM Software Factory — landing

Source: https://factory.strongdm.ai/

---

StrongDM Software Factory{"@context":"https://schema.org","@type":"Organization","name":"StrongDM","url":"https://www.strongdm.com","logo":"https://factory.strongdm.ai/images/og-image.png"}

[STRONGDM AI](/ "/")

[Story](/ "/")[Principles](/principles "/principles")[Techniques](/techniques "/techniques")[Products](/products "/products")[Weather Report](/weather-report "/weather-report")

StrongDM AI

Software Factories And The Agentic Moment
=========================================

February 6th, 2026 · Justin McCarthy

We built a **Software Factory**: non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review.

The narrative form is included below. If you'd prefer to work from first principles, I offer a few constraints & guidelines that, applied iteratively, will accelerate any team toward the same intuitions, convictions[1](#fn1 "#fn1"), and ultimately a factory[2](#fn2 "#fn2") of your own. In kōan or mantra form:

* Why am I doing this? (implied: the model should be doing this instead)

In rule form:

* Code **must not be** written by humans
* Code **must not be** reviewed by humans

Finally, in practical form:

* If you haven't spent at least **$1,000 on tokens today** per human engineer, your software factory has room for improvement

The StrongDM AI Story
---------------------

On July 14th, 2025, Jay Taylor and Navan Chauhan joined me (Justin McCarthy, co-founder, CTO) in founding the StrongDM AI team.

The catalyst was a transition observed in late 2024: with the second revision of Claude 3.5 (October 2024), long-horizon agentic coding workflows began to compound correctness rather than error.

Compounding correctness vs compounding error

By December of 2024, the model's long-horizon coding performance was unmistakable via Cursor's [YOLO mode](https://forum.cursor.com/t/yolo-mode-is-amazing/36262 "https://forum.cursor.com/t/yolo-mode-is-amazing/36262").

Prior to this model improvement, iterative application of LLMs to coding tasks would accumulate errors of all imaginable varieties (misunderstandings, hallucinations, syntax, DRY violations, library incompatibility, etc). The app or product would decay and ultimately "collapse": death by a thousand cuts, etc.

Together with YOLO mode, the updated model from Anthropic provided the first glimmer of what we now refer to internally as **non-interactive** development or **grown** software.

Find Knobs, Turn To Eleven
--------------------------

"These go to 11"

In the first hour of the first day of our AI team, we established a charter which set us on a path toward a series of findings (which we refer to as our "unlocks"). In retrospect, the most important line in the charter document was the following:

Hands off!

Initially it was just a hunch. An experiment. How far could we get, without writing any code by hand?

Not very far! At least: not very far, until we added tests. However, the agent, obsessed with the immediate task, soon began to take shortcuts: **return true** is a great way to pass narrowly written tests, but probably won't generalize to the software you want.

Tests were not enough. How about integration tests? Regression tests? End-to-end tests? Behavior tests?

From Tests to Scenarios and Satisfaction
----------------------------------------

One recurring theme of the agentic moment: we need new language. For example, the word "test" has proven insufficient and ambiguous. A test, stored in the codebase, can be lazily rewritten to match the code. The code could be rewritten to trivially pass the test.

We repurposed the word **scenario** to represent an end-to-end "user story", often stored outside the codebase (similar to a "holdout" set in model training), which could be intuitively understood and flexibly validated by an LLM.

Synthetic scenario curation and shaping interface

Because much of the software we grow itself has an agentic component, we transitioned from boolean definitions of success ("the test suite is green") to a probabilistic and empirical one. We use the term **satisfaction** to quantify this validation: of all the observed trajectories through all the scenarios, what fraction of them likely satisfy the user?

Validating Scenarios in the Digital Twin Universe
-------------------------------------------------

In previous regimes, a team might rely on integration tests, regression tests, UI automation to answer "is it working?"

We noticed two limitations of previously reliable techniques:

1. **Tests are too rigid** - we were coding with agents, but we're also building with LLMs and agent loops as design primitives; evaluating success often required LLM-as-judge
2. **Tests can be reward hacked** - we needed validation that was less vulnerable to the model cheating

The Digital Twin Universe is our answer: behavioral clones of the third-party services our software depends on. We built twins of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, replicating their APIs, edge cases, and observable behaviors.

With the DTU, we can validate at volumes and rates far exceeding production limits. We can test failure modes that would be dangerous or impossible against live services. We can run thousands of scenarios per hour without hitting rate limits, triggering abuse detection, or accumulating API costs.

Digital Twin Universe: behavioral clones of Okta, Jira, Google Docs, Slack, Drive, and Sheets  
(click to enlarge)

Unconventional Economics
------------------------

Our success with DTU illustrates one of the many ways in which the Agentic Moment has profoundly changed the economics of software. Creating a high fidelity clone of a significant SaaS application was always possible, but never economically feasible. Generations of engineers may have *wanted* a full in-memory replica of their CRM to test against, but self-censored the proposal to build it. They didn't even bring it to their manager, because they knew the answer would be no.

Those of us building software factories must practice a **deliberate naivete**: finding and removing the habits, conventions, and constraints of [Software 1.0](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=95s "https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=95s"). The DTU is our proof that what was unthinkable six months ago is now routine.

Read Next
---------

* [Principles](/principles "/principles"): what we believe is true about building software with agents
* [Techniques](/techniques "/techniques"): repeated patterns for applying those principles
* [Products](/products "/products"): tools we use daily and believe others will benefit from

Thank you for reading. We wish you the best of luck constructing your own Software Factory.

---

1 We are not alone in these convictions. See also: Luke PM's ["The Software Factory"](https://lukepm.com/blog/the-software-factory/ "https://lukepm.com/blog/the-software-factory/"), Sam Schillace's ["I Have Seen the Compounding Teams"](https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams "https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams"), and Dan Shapiro's ["Five Levels from Spicy Autocomplete to the Software Factory"](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ "https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/").

2 Others are building factories too: [Devin](https://devin.ai/ "https://devin.ai/"), [8090](https://www.8090.ai/ "https://www.8090.ai/"), [Factory](https://www.fastcompany.com/91279593/factory-ai-code-generation-matan-grinberg-eno-reyes "https://www.fastcompany.com/91279593/factory-ai-code-generation-matan-grinberg-eno-reyes"), [Superconductor](https://www.superconductor.com/ "https://www.superconductor.com/"), and Jesse Vincent's [Superpowers](https://github.com/obra/superpowers "https://github.com/obra/superpowers").

---

**StrongDM AI** · Founded July 14th, 2025

[Principles →](/principles "/principles")

(self.\_\_next\_f=self.\_\_next\_f||[]).push([0]);self.\_\_next\_f.push([2,null])self.\_\_next\_f.push([1,"1:HL[\"/\_next/static/media/4b9bb515ce6d026f.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n2:HL[\"/\_next/static/media/5611c55482296524.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n3:HL[\"/\_next/static/media/bb3ef058b751a6ad-s.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n4:HL[\"/\_next/static/media/e4af272ccee01ff0-s.p.woff2\",\"font\",{\"crossOrigin\":\"\",\"type\":\"font/woff2\"}]\n5:HL[\"/\_next/static/css/b1921d4d03a896c7.css\",\"style\"]\n"])self.\_\_next\_f.push([1,"6:I[4411,[],\"\"]\n8:I[9164,[\"955\",\"static/chunks/955-87da2b13160f992b.js\",\"874\",\"static/chunks/874-b7d303a46be13ff9.js\",\"931\",\"static/chunks/app/page-6d8533fb589d49b7.js\"],\"default\"]\n9:I[4344,[\"558\",\"static/chunks/558-80f614a6188e2b57.js\",\"185\",\"static/chunks/app/layout-3e1ffa20de597367.js\"],\"\"]\na:I[3356,[\"558\",\"static/chunks/558-80f614a6188e2b57.js\",\"185\",\"static/chunks/app/layout-3e1ffa20de597367.js\"],\"ThemeProvider\"]\nb:I[8238,[\"558\",\"static/chunks/558-80f614a6188e2b57.js\",\"185\",\"static/chunks/app/layout-3e1ffa20de597367.js\"],\"default\"]\nc:I[9822,[],\"\"]\nd:I[376,[],\"\"]\nf:I[5671,[\"906\",\"static/chunks/906-798a99be91bae4cb.js\",\"470\",\"static/chunks/app/global-error-79c819ec3c4387cb.js\"],\"default\"]\n10:[]\n"])self.\_\_next\_f.push([1,"0:[\"$\",\"$L6\",null,{\"buildId\":\"UJ6eVcTo3ary72EOUpYVi\",\"assetPrefix\":\"\",\"urlParts\":[\"\",\"\"],\"initialTree\":[\"\",{\"children\":[\"\_\_PAGE\_\_\",{}]},\"$undefined\",\"$undefined\",true],\"initialSeedData\":[\"\",{\"children\":[\"\_\_PAGE\_\_\",{},[[\"$L7\",[\"$\",\"$L8\",null,{}],null],null],null]},[[[[\"$\",\"link\",\"0\",{\"rel\":\"stylesheet\",\"href\":\"/\_next/static/css/b1921d4d03a896c7.css\",\"precedence\":\"next\",\"crossOrigin\":\"$undefined\"}]],[\"$\",\"html\",null,{\"lang\":\"en\",\"className\":\"\_\_variable\_f367f3 \_\_variable\_3c557b \_\_variable\_5de9f1\",\"children\":[[\"$\",\"head\",null,{\"children\":[[\"$\",\"link\",null,{\"rel\":\"alternate\",\"type\":\"application/rss+xml\",\"title\":\"StrongDM Software Factory — Weather Report\",\"href\":\"/weather-report/feed.xml\"}],[\"$\",\"script\",null,{\"type\":\"application/ld+json\",\"dangerouslySetInnerHTML\":{\"\_\_html\":\"{\\\"@context\\\":\\\"https://schema.org\\\",\\\"@type\\\":\\\"Organization\\\",\\\"name\\\":\\\"StrongDM\\\",\\\"url\\\":\\\"https://www.strongdm.com\\\",\\\"logo\\\":\\\"https://factory.strongdm.ai/images/og-image.png\\\"}\"}}],[\"$\",\"$L9\",null,{\"src\":\"https://www.googletagmanager.com/gtag/js?id=G-E3RVJ85KVS\",\"strategy\":\"afterInteractive\"}],[\"$\",\"$L9\",null,{\"id\":\"gtag-init\",\"strategy\":\"afterInteractive\",\"children\":\"\\n window.dataLayer = window.dataLayer || [];\\n function gtag(){dataLayer.push(arguments);}\\n gtag('js', new Date());\\n gtag('config', 'G-E3RVJ85KVS');\\n \"}]]}],[\"$\",\"body\",null,{\"className\":\"\_\_className\_f367f3\",\"children\":[\"$\",\"$La\",null,{\"children\":[[\"$\",\"$Lb\",null,{}],[\"$\",\"div\",null,{\"className\":\"page-shell\",\"children\":[\"$\",\"$Lc\",null,{\"parallelRouterKey\":\"children\",\"segmentPath\":[\"children\"],\"error\":\"$undefined\",\"errorStyles\":\"$undefined\",\"errorScripts\":\"$undefined\",\"template\":[\"$\",\"$Ld\",null,{}],\"templateStyles\":\"$undefined\",\"templateScripts\":\"$undefined\",\"notFound\":[[\"$\",\"title\",null,{\"children\":\"404: This page could not be found.\"}],[\"$\",\"div\",null,{\"style\":{\"fontFamily\":\"system-ui,\\\"Segoe UI\\\",Roboto,Helvetica,Arial,sans-serif,\\\"Apple Color Emoji\\\",\\\"Segoe UI Emoji\\\"\",\"height\":\"100vh\",\"textAlign\":\"center\",\"display\":\"flex\",\"flexDirection\":\"column\",\"alignItems\":\"center\",\"justifyContent\":\"center\"},\"children\":[\"$\",\"div\",null,{\"children\":[[\"$\",\"style\",null,{\"dangerouslySetInnerHTML\":{\"\_\_html\":\"body{color:#000;background:#fff;margin:0}.next-error-h1{border-right:1px solid rgba(0,0,0,.3)}@media (prefers-color-scheme:dark){body{color:#fff;background:#000}.next-error-h1{border-right:1px solid rgba(255,255,255,.3)}}\"}}],[\"$\",\"h1\",null,{\"className\":\"next-error-h1\",\"style\":{\"display\":\"inline-block\",\"margin\":\"0 20px 0 0\",\"padding\":\"0 23px 0 0\",\"fontSize\":24,\"fontWeight\":500,\"verticalAlign\":\"top\",\"lineHeight\":\"49px\"},\"children\":\"404\"}],[\"$\",\"div\",null,{\"style\":{\"display\":\"inline-block\"},\"children\":[\"$\",\"h2\",null,{\"style\":{\"fontSize\":14,\"fontWeight\":400,\"lineHeight\":\"49px\",\"margin\":0},\"children\":\"This page could not be found.\"}]}]]}]}]],\"notFoundStyles\":[]}]}]]}]}]]}]],null],null],\"couldBeIntercepted\":false,\"initialHead\":[null,\"$Le\"],\"globalErrorComponent\":\"$f\",\"missingSlots\":\"$W10\"}]\n"])self.\_\_next\_f.push([1,"e:[[\"$\",\"meta\",\"0\",{\"name\":\"viewport\",\"content\":\"width=device-width, initial-scale=1\"}],[\"$\",\"meta\",\"1\",{\"charSet\":\"utf-8\"}],[\"$\",\"title\",\"2\",{\"children\":\"StrongDM Software Factory\"}],[\"$\",\"meta\",\"3\",{\"name\":\"description\",\"content\":\"StrongDM's field notes on non-interactive agentic development: specs + scenarios, validation harnesses, feedback loops, and the supporting components.\"}],[\"$\",\"link\",\"4\",{\"rel\":\"canonical\",\"href\":\"https://factory.strongdm.ai/\"}],[\"$\",\"meta\",\"5\",{\"property\":\"og:title\",\"content\":\"StrongDM Software Factory\"}],[\"$\",\"meta\",\"6\",{\"property\":\"og:description\",\"content\":\"StrongDM's field notes on non-interactive agentic development: specs + scenarios, validation harnesses, feedback loops, and the supporting components.\"}],[\"$\",\"meta\",\"7\",{\"property\":\"og:image\",\"content\":\"https://factory.strongdm.ai/images/og-image.png\"}],[\"$\",\"meta\",\"8\",{\"property\":\"og:image:alt\",\"content\":\"StrongDM Software Factory\"}],[\"$\",\"meta\",\"9\",{\"property\":\"og:type\",\"content\":\"website\"}],[\"$\",\"meta\",\"10\",{\"name\":\"twitter:card\",\"content\":\"summary\_large\_image\"}],[\"$\",\"meta\",\"11\",{\"name\":\"twitter:title\",\"content\":\"StrongDM Software Factory\"}],[\"$\",\"meta\",\"12\",{\"name\":\"twitter:description\",\"content\":\"StrongDM's field notes on non-interactive agentic development: specs + scenarios, validation harnesses, feedback loops, and the supporting components.\"}],[\"$\",\"meta\",\"13\",{\"name\":\"twitter:image\",\"content\":\"https://factory.strongdm.ai/images/og-image.png\"}],[\"$\",\"meta\",\"14\",{\"name\":\"next-size-adjust\"}]]\n7:null\n"])
