# [Simon Willison’s Weblog](/ "/")

[Subscribe](/about/#subscribe "/about/#subscribe")

30th April 2026 - Link Blog

**[Codex CLI 0.128.0 adds /goal](https://github.com/openai/codex/releases/tag/rust-v0.128.0 "https://github.com/openai/codex/releases/tag/rust-v0.128.0")** ([via](https://twitter.com/fcoury/status/2049917871799636201 "@fcoury")) The latest version of OpenAI's Codex CLI coding agent adds their own version of the [Ralph loop](https://ghuntley.com/ralph/ "https://ghuntley.com/ralph/"): you can now set a `/goal` and Codex will keep on looping until it evaluates that the goal has been completed... or the configured token budget has been exhausted.

It looks like the feature is mainly implemented though the [goals/continuation.md](https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/continuation.md "https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/continuation.md") and [goals/budget\_limit.md](https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/budget_limit.md "https://github.com/openai/codex/blob/6014b6679ffbd92eeddffa3ad7b4402be6a7fefe/codex-rs/core/templates/goals/budget_limit.md") prompts, which are automatically injected at the end of a turn.

## Recent articles

* [Live blog: Code w/ Claude 2026](/2026/May/6/code-w-claude-2026/ "/2026/May/6/code-w-claude-2026/") - 6th May 2026
* [Vibe coding and agentic engineering are getting closer than I'd like](/2026/May/6/vibe-coding-and-agentic-engineering/ "/2026/May/6/vibe-coding-and-agentic-engineering/") - 6th May 2026
* [LLM 0.32a0 is a major backwards-compatible refactor](/2026/Apr/29/llm/ "/2026/Apr/29/llm/") - 29th April 2026

This is a **link post** by Simon Willison, posted on [30th April 2026](/2026/Apr/30/ "/2026/Apr/30/").

[ai
2005](/tags/ai/ "/tags/ai/")
[openai
417](/tags/openai/ "/tags/openai/")
[prompt-engineering
189](/tags/prompt-engineering/ "/tags/prompt-engineering/")
[generative-ai
1777](/tags/generative-ai/ "/tags/generative-ai/")
[llms
1742](/tags/llms/ "/tags/llms/")
[coding-agents
198](/tags/coding-agents/ "/tags/coding-agents/")
[system-prompts
54](/tags/system-prompts/ "/tags/system-prompts/")
[codex-cli
34](/tags/codex-cli/ "/tags/codex-cli/")
[agentic-engineering
48](/tags/agentic-engineering/ "/tags/agentic-engineering/")

### Monthly briefing

Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

[Sponsor & subscribe](https://github.com/sponsors/simonw/ "https://github.com/sponsors/simonw/")

* [Disclosures](/about/#disclosures "/about/#disclosures")
* [Colophon](/about/#about-site "/about/#about-site")
* ©
* [2002](/2002/ "/2002/")
* [2003](/2003/ "/2003/")
* [2004](/2004/ "/2004/")
* [2005](/2005/ "/2005/")
* [2006](/2006/ "/2006/")
* [2007](/2007/ "/2007/")
* [2008](/2008/ "/2008/")
* [2009](/2009/ "/2009/")
* [2010](/2010/ "/2010/")
* [2011](/2011/ "/2011/")
* [2012](/2012/ "/2012/")
* [2013](/2013/ "/2013/")
* [2014](/2014/ "/2014/")
* [2015](/2015/ "/2015/")
* [2016](/2016/ "/2016/")
* [2017](/2017/ "/2017/")
* [2018](/2018/ "/2018/")
* [2019](/2019/ "/2019/")
* [2020](/2020/ "/2020/")
* [2021](/2021/ "/2021/")
* [2022](/2022/ "/2022/")
* [2023](/2023/ "/2023/")
* [2024](/2024/ "/2024/")
* [2025](/2025/ "/2025/")
* [2026](/2026/ "/2026/")
