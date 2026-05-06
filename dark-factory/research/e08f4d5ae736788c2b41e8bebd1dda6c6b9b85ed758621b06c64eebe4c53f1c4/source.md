Official statement from Tea on their data leak

[Simon Willison’s Weblog](/ "/")
================================

[Subscribe](/about/#subscribe "/about/#subscribe")

**Sponsored by:** [MongoDB](https://fandf.co/4cNOQZL "https://fandf.co/4cNOQZL") — Join MongoDB.local London 2026 on 7 May to learn how teams move AI from prototype to production.

26th July 2025 - Link Blog

**[Official statement from Tea on their data leak](https://www.teaforwomen.com/cyberincident "https://www.teaforwomen.com/cyberincident")**. Tea is a dating safety app for women that lets them share notes about potential dates. The other day it was subject to a truly egregious data leak caused by a legacy unprotected Firebase cloud storage bucket:

> A legacy data storage system was compromised, resulting in unauthorized access to a dataset from prior to February 2024. This dataset includes approximately 72,000 images, including approximately 13,000 selfies and photo identification submitted by users during account verification and approximately 59,000 images publicly viewable in the app from posts, comments and direct messages.

Storing and then failing to secure photos of driving licenses is an incredible breach of trust. Many of those photos included EXIF location information too, so there are maps of Tea users floating around the darker corners of the web now.

I've seen a bunch of commentary using this incident as an example of the dangers of vibe coding. **I'm confident vibe coding was not to blame** in this particular case, even while I [share the larger concern](https://simonwillison.net/2025/Mar/19/vibe-coding/#when-is-it-ok-to-vibe-code- "https://simonwillison.net/2025/Mar/19/vibe-coding/#when-is-it-ok-to-vibe-code-") of irresponsible vibe coding leading to more incidents of this nature.

The announcement from Tea makes it clear that the underlying issue relates to code written prior to February 2024, long before vibe coding was close to viable for building systems of this nature:

> During our early stages of development some legacy content was not migrated into our new fortified system. Hackers broke into our identifier link where data was stored before February 24, 2024. As we grew our community, we migrated to a more robust and secure solution which has rendered that any new users from February 2024 until now were not part of the cybersecurity incident.

Also worth noting is that they stopped requesting photos of ID back in 2023:

> During our early stages of development, we required selfies and IDs as an added layer of safety to ensure that only women were signing up for the app. In 2023, we removed the ID requirement.

**Update 28th July**: A second breach [has been confirmed](https://www.404media.co/a-second-tea-breach-reveals-users-dms-about-abortions-and-cheating/ "https://www.404media.co/a-second-tea-breach-reveals-users-dms-about-abortions-and-cheating/") by 404 Media, this time exposing more than one million direct messages dated up to this week.

Posted [26th July 2025](/2025/Jul/26/ "/2025/Jul/26/") at 4:20 pm

Recent articles
---------------

* [LLM 0.32a0 is a major backwards-compatible refactor](/2026/Apr/29/llm/ "/2026/Apr/29/llm/") - 29th April 2026
* [Tracking the history of the now-deceased OpenAI Microsoft AGI clause](/2026/Apr/27/now-deceased-agi-clause/ "/2026/Apr/27/now-deceased-agi-clause/") - 27th April 2026
* [DeepSeek V4 - almost on the frontier, a fraction of the price](/2026/Apr/24/deepseek-v4/ "/2026/Apr/24/deepseek-v4/") - 24th April 2026

This is a **link post** by Simon Willison, posted on [26th July 2025](/2025/Jul/26/ "/2025/Jul/26/").

[privacy
65](/tags/privacy/ "/tags/privacy/")
[security
600](/tags/security/ "/tags/security/")
[ai
2003](/tags/ai/ "/tags/ai/")
[generative-ai
1775](/tags/generative-ai/ "/tags/generative-ai/")
[llms
1740](/tags/llms/ "/tags/llms/")
[vibe-coding
88](/tags/vibe-coding/ "/tags/vibe-coding/")

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