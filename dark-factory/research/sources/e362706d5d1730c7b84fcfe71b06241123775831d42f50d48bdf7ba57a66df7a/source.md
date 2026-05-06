METR’s study on how AI affects developer productivity 

[![Engineering Enablement](https://substackcdn.com/image/fetch/$s_!Niij!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dbd433b-6f11-4042-8b7d-0edb3b172966_1024x1024.png)](/ "/")

[Engineering Enablement](/ "/")
===============================

SubscribeSign in

METR’s study on how AI affects developer productivity
=====================================================

### In this study, developers were 19% slower when using AI.

[![Abi Noda's avatar](https://substackcdn.com/image/fetch/$s_!Wx_u!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a1c4cfd-639c-420c-8b20-a0a400c74265_3071x3071.jpeg)](https://substack.com/@abinoda "https://substack.com/@abinoda")

[Abi Noda](https://substack.com/@abinoda "https://substack.com/@abinoda")

Jul 23, 2025

21

1

1

Share

***Welcome to the latest issue of*** **Engineering Enablement***, a weekly newsletter sharing research and perspectives on developer productivity.*

🗓 Join Laura Tacho and me for a **[live webinar](https://getdx.com/webinar/platform-engineering-in-the-ai-era/?utm_source=newsletter "https://getdx.com/webinar/platform-engineering-in-the-ai-era/?utm_source=newsletter")** in August as we cover how AI is changing the role of platform engineering.

Subscribe

---

This week, I’m summarizing a surprising new field study that challenges the prevailing narrative around AI’s impact on developer productivity. Conducted by [METR](https://metr.org/about "https://metr.org/about"), a nonprofit research organization focused on evaluating AI capabilities, the study found that AI tools actually slowed down developers working on real-world tasks. ([Read the full paper here](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study.pdf "https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study.pdf"), and [METR’s blog post here](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/").)

My summary of the paper
-----------------------

Most AI research to date has been conducted in highly controlled settings. While these studies yield interesting findings, they often fall short of telling us how AI performs in the real world.

To close that gap, researchers at METR ran a randomized controlled trial with 16 experienced developers. Each participant had moderate experience with AI tools and at least five years of experience working on their assigned project. Here’s how the study was conducted:

* At the start of the study, developers provided a list of real issues in their repository to work on. They also forecasted how long each task would take to complete both with AI and without AI assistance.
* The tasks were then randomly assigned to either allow or disallow the use of AI tools. When AI was allowed, developers could use any tool of their choosing. In total, participants completed 246 tasks, each averaging about two hours.
* Developers would complete tasks while recording their screens, then they would self-report the total implementation time. These self-reports were used to calculate AI’s impact on task duration, while the screen recordings were used to validate the reported times and ensure no AI tools were used when they were not permitted.
* After the study’s conclusion, developers were asked to estimate how much AI tooling affected the time it took them to complete issues.

### Expected vs. actual task completion time with AI

Two key findings emerged from this study. First, developers who were allowed to use AI tools took, on average, 19% longer to complete tasks. This is a significant slowdown that runs counter to mainstream expectations and headlines about AI-driven productivity gains.

Second, developers overestimated the extent to which AI helps them. Before the study, they predicted AI would speed them up by 24%. After using AI (and actually experiencing a slowdown), they still believed it had helped, estimating a 20% improvement. This disconnect wasn’t due to poor time estimation; developers were fairly accurate in predicting how long tasks would take both with or without AI. Instead, it points to overoptimism, suggesting that developers may be influenced by industry hype or their perception of the *potential* of AI, assuming it’s already speeding them up even when it’s not.

[![](https://substackcdn.com/image/fetch/$s_!I8Vd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dcc548d-0498-4941-a824-f3177404bcaa_1702x1206.png)](https://substackcdn.com/image/fetch/$s_!I8Vd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dcc548d-0498-4941-a824-f3177404bcaa_1702x1206.png "https://substackcdn.com/image/fetch/$s_!I8Vd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7dcc548d-0498-4941-a824-f3177404bcaa_1702x1206.png")

### Possible factors contributing to the AI-related slowdown

Given the surprising results, the researchers identified five factors—supported by both qualitative and quantitative evidence—that may have contributed to the slower task completion with AI.

[![](https://substackcdn.com/image/fetch/$s_!xk8i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff23f046a-a121-43b2-b220-d8eaef38f1b3_1600x618.png)](https://substackcdn.com/image/fetch/$s_!xk8i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff23f046a-a121-43b2-b220-d8eaef38f1b3_1600x618.png "https://substackcdn.com/image/fetch/$s_!xk8i!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff23f046a-a121-43b2-b220-d8eaef38f1b3_1600x618.png")

**1. Overoptimism about AI usefulness:** AI was not *required* to be used on AI-allowed issues. The researchers suggest that, given developers’ overoptimistic view about AI’s usefulness, they could overuse AI even when it is slowing them down.

**2. High familiarity with repositories:** The study found that developers were more likely to be slowed down by AI on tasks where they already had deep expertise. Before each task, they rated their “prior task exposure” on a scale of 1-5, where 1 meant “Never done this type of task before” and 5 meant “I am an expert at this type of task”. “The data showed AI was least effective when developers had high prior exposure and didn’t need external resources like documentation. Developers confirmed that AI was more helpful on unfamiliar tasks and less useful on ones they were already familiar with.

[![](https://substackcdn.com/image/fetch/$s_!gh21!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5121808b-e1de-415b-b704-614538271ef3_1600x897.png)](https://substackcdn.com/image/fetch/$s_!gh21!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5121808b-e1de-415b-b704-614538271ef3_1600x897.png "https://substackcdn.com/image/fetch/$s_!gh21!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5121808b-e1de-415b-b704-614538271ef3_1600x897.png")

> *“We hypothesize that analogously, AI helps our developers less compared to existing literature because our developers have substantially more experience on their respective repositories (5 years and 1,500 commits on average).”*

**3. Large and complex repositories:** Developers reported that AI tools tended to perform worse in complex environments. Since the repositories in this study were both large and mature—averaging 10 years old with over 1 million lines of code—it’s possible that AI was less effective here than in the settings examined in other studies.

**4. Low AI reliability:** Developers accepted less than 44% of the generations. This relatively low acceptance rate resulted in wasted time, as developers often had to review, test, and modify code, only to reject it in the end. Even when suggestions were accepted, developers reported spending considerable time reviewing and editing the code to meet their high standards.

**5. Implicit repository context:** Developers often rely on undocumented, tacit knowledge when working in familiar repos. AI lacked this context, making its suggestions feel off-base. One developer compared it to “a new contributor who doesn’t yet understand the codebase.”

Importantly, the researchers note these findings don’t suggest AI tools are useless—only that current tools may fall short in complex environments where developers have deep expertise.

> *“Many of the factors we find evidence for contributing to slowdown are specific to the setting we study—these results do not imply that current AI systems are not useful in many realistic, economically relevant settings.”*

Final thoughts
--------------

I agree with the authors’ opening line: “Despite widespread adoption, the impact of AI tools on software development in the wild remains understudied.” There’s a clear need for more real-world research like this to help engineering leaders understand what they can realistically expect from AI.

This study exposes several weaknesses of current AI tools. AI struggles in large, complex, mature codebases. It often delivers less value to experienced developers, and it is often more helpful for onboarding, unfamiliar tasks, or when documentation is lacking. Finally, the results also point to a broader pattern: AI may have a greater impact within organizations when targeted at specific, time-saving tasks rather than used as a general-purpose assistant in day-to-day development.

Perhaps most importantly, the study underscores a common challenge we see across the industry—widespread inflated expectations surrounding AI’s usefulness. The reality is far more nuanced. To realize meaningful impact, organizations should take a structured approach to AI adoption: provide training and enablement, use data to identify which use cases are actually working, and scale the use cases that deliver real value.

> *“LLMs are a tool, and we need to start learning its pitfalls and have some self-awareness… If we expect to use this new tool well, we need to understand its (and our own!) shortcomings and adapt to them.” — [Quentin Anthony](https://x.com/QuentinAnthon15/status/1943948805222936742 "https://x.com/QuentinAnthon15/status/1943948805222936742"), a participant in this study*

Reach out on [LinkedIn](https://www.linkedin.com/in/abinoda/ "https://www.linkedin.com/in/abinoda/") and let me know what your reactions to this paper were. And stay tuned for an upcoming podcast where I’ll be interviewing one of the participants of this study.

---

#### Who’s hiring right now

This week’s featured DevProd & Platform job openings. See more [open roles here](https://getdx.com/resources/devex-jobs/ "https://getdx.com/resources/devex-jobs/").

* **Dropbox** is hiring multiple [Infrastructure and AI Dev Tools](https://jobs.dropbox.com/listing/6330323 "https://jobs.dropbox.com/listing/6330323") roles | US (Remote)
* **Atlassian Williams Racing** is hiring a [Software Engineer](https://jobs.smartrecruiters.com/WilliamsRacing/744000046538770-engineering-acceleration-engineer "https://jobs.smartrecruiters.com/WilliamsRacing/744000046538770-engineering-acceleration-engineer") - Engineering Acceleration | Grove, UK
* **The New York Times** is hiring a [Technical Product Manager II](https://job-boards.greenhouse.io/thenewyorktimes/jobs/4581462005 "https://job-boards.greenhouse.io/thenewyorktimes/jobs/4581462005") - Developer Productivity | NY, NY
* **ScalePad** is hiring a [Head of AI Engineering & Enablement](https://scalepad.bamboohr.com/careers/317? "https://scalepad.bamboohr.com/careers/317?") | Canada (Remote or in-office)

---

That’s it for this week. Thanks for reading.

-Abi

[Share](https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity?utm_source=substack&utm_medium=email&utm_content=share&action=share "https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity?utm_source=substack&utm_medium=email&utm_content=share&action=share")

21

1

1

Share

#### Discussion about this post

CommentsRestacks

![User's avatar](https://substackcdn.com/image/fetch/$s_!TnFC!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

[![Yves Basquet's avatar](https://substackcdn.com/image/fetch/$s_!YBxl!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba4d7ce9-785b-4408-bc2d-0f687bf05136_144x144.png)](https://substack.com/profile/102406094-yves-basquet?utm_source=comment "https://substack.com/profile/102406094-yves-basquet?utm_source=comment")

[Yves Basquet](https://substack.com/profile/102406094-yves-basquet?utm_source=substack-feed-item "https://substack.com/profile/102406094-yves-basquet?utm_source=substack-feed-item")

[Jul 24, 2025](https://newsletter.getdx.com/p/metr-study-on-how-ai-affects-developer-productivity/comment/138349414 "Jul 24, 2025, 4:23 AM")

Thanks for the writeup ! I am actually not surprised by those results ; AI is in its infancy, being more helpful where it is easier and there is less implicit or explicit complexity is where we stand.

I'd actually like to see the same study in other fields as software engineering.

My instinct tells me that we would come to the same conclusions there as well.

ReplyShare

TopLatestDiscussions

No posts

### Ready for more?

Subscribe

© 2026 Abi Noda · [Privacy](https://substack.com/privacy "https://substack.com/privacy") ∙ [Terms](https://substack.com/tos "https://substack.com/tos") ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected "https://substack.com/ccpa#personal-data-collected")

[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer "https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer")[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button "https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button")

[Substack](https://substack.com "https://substack.com") is the home for great culture

This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/ "https://enable-javascript.com/") or unblock scripts