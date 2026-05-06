Critical Vulnerability in AI Vibe Coding platform Base44 | Wiz Blog

* [Sign in](https://app.wiz.io/login "https://app.wiz.io/login")
* [Experiencing an incident?](/experiencing-an-incident "/experiencing-an-incident")

[Wiz](/ "/")

[Pricing](/pricing "/pricing")[Get a demo](/demo "/demo")

* Platform
* Solutions
* [Pricing](/pricing "/pricing")
* Resources
* Customers
* Company

[Get a demo](/demo "/demo")

[Blog](/blog "/blog")

Wiz Research Uncovers Critical Vulnerability in AI Vibe Coding platform Base44 Allowing Unauthorized Access to Private Applications
===================================================================================================================================

New discovery underscores security implications of AI-powered development and the rise of Vibe Coding Platforms

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48L3N2Zz4=)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDhoXDhgVFykVFREeFxgZHR0qHh4dHysjIi4oHhUaJDUlKC0vMjIyHSI4PTcwPCsxMi8BCgsLDg0OHBANHC8cHSk7Oy8vLy8vLy8vLzUvMC8vNS8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABgAGAMBIgACEQEDEQH/xAAZAAEAAgMAAAAAAAAAAAAAAAAABQYBBAf/xAAgEAABBAICAwEAAAAAAAAAAAABAAIDBBESBRQHIYEG/8QAFgEBAQEAAAAAAAAAAAAAAAAAAwQA/8QAGBEAAwEBAAAAAAAAAAAAAAAAAQIRAAP/2gAMAwEAAhEDEQA/AL7ddbFYqDiNt8v1TV3ttrHZQ8BnBzlT9HNyIomsVNljrhFnjHTTR42CJ1czGyi7knN+UbDotIxklRlT99bkruJ9EIi3RRdkJm2uL8mXIpS3YoiKhFExsTd//9k=)![](https://www.datocms-assets.com/75231/1773582752-screenshot-2026-03-15-at-11-22-55.png?fit=crop&fm=jpg&h=100&w=100)](/authors/gal-nagli "/authors/gal-nagli")

[Gal Nagli](/authors/gal-nagli "/authors/gal-nagli")

July 29, 2025|

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNjAwIiBoZWlnaHQ9IjgxMiI+PC9zdmc+)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDhgWDg0NGRgVHR0dJSUZGBYTIhYdHysjGh0oHRUiJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoHig7OzsvOzs7OzsvLzUvNS8vLzUvNTsvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA0AGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAGBQEA/8QAHhAAAQQCAwEAAAAAAAAAAAAAAgABAwQFMRETIQb/xAAWAQEBAQAAAAAAAAAAAAAAAAAEBQH/xAAcEQABAwUAAAAAAAAAAAAAAAADAAECBBEiQVH/2gAMAwEAAhEDEQA/AC9WlAMbETq9DDTkpb0ynTVwGl4kHy2LgtUS7OXV0pIw0tC14ojlI8c4uJF6sVHP4KqNkmbna5CeubiFMeS//9k=)![](https://www.datocms-assets.com/75231/1753388286-unnamed-2.png?fm=webp)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNjAwIiBoZWlnaHQ9IjgxMiI+PC9zdmc+)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDhgWDg0NGRgVHR0dJSUZGBYTIhYdHysjGh0oHRUiJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoHig7OzsvOzs7OzsvLzUvNS8vLzUvNTsvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA0AGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAGBQEA/8QAHhAAAQQCAwEAAAAAAAAAAAAAAgABAwQFMRETIQb/xAAWAQEBAQAAAAAAAAAAAAAAAAAEBQH/xAAcEQABAwUAAAAAAAAAAAAAAAADAAECBBEiQVH/2gAMAwEAAhEDEQA/AC9WlAMbETq9DDTkpb0ynTVwGl4kHy2LgtUS7OXV0pIw0tC14ojlI8c4uJF6sVHP4KqNkmbna5CeubiFMeS//9k=)![](https://www.datocms-assets.com/75231/1753388286-unnamed-2.png?fm=webp)

One of the most profoundly transformed domains in the wake of the LLM revolution has been code generation, especially the rise of vibe coding, where natural language prompts replace traditional programming. This shift has empowered millions of users with little to no technical background to build fully functional applications with ease.  
  
Platforms like Lovable, Bolt, and Base44 are on the front of this movement - they have enabled the creation of millions of applications spanning from personal tools to enterprises that now rely on these platforms to build internal chatbots, create complex automations, and trust them with sensitive corporate data.  
  
In [our mission to find novel AI and cloud risks](https://www.wiz.io/blog/tag/ai "https://www.wiz.io/blog/tag/ai"), Wiz Research has been looking into the security posture of these AI-powered development platforms to identify common vulnerabilities that may impact the industry as a whole – a mission that becomes even more important as these systems and technologies get infused into [governments and other critical infrastructure](https://www.wiz.io/blog/us-ai-action-plan "https://www.wiz.io/blog/us-ai-action-plan").

**Executive Summary**
=====================

Wiz Research has identified a critical vulnerability affecting the popular [vibe coding](https://www.wiz.io/blog/safer-vibe-coding-rules-files "https://www.wiz.io/blog/safer-vibe-coding-rules-files") platform Base44 ([recently acquired by Wix](https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash/ "https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash/") following an amazingly rapid rise) which allowed unauthorized access to private applications built by its users.

The vulnerability we discovered was remarkably simple to exploit - by providing only a non-secret app\_id value to undocumented registration and email verification endpoints, an attacker could have created a verified account for private applications on their platform.  
  
This effectively bypassed all given authentication controls that Base44 provided, including Single Sign-On (SSO), granting full access to what were intended to be private enterprise applications and the sensitive data they might have contained.

Upon discovering the vulnerability, we immediately and responsibly disclosed the issue to both Base44 and Wix who promptly validated our report. The vulnerability was fixed in less than 24 hours, with Wix confirming that there was no evidence of past abuse (see their statement below).

In this blog post, we will detail our discovery process and discuss how the security implications extend beyond the specific platform to the broader AI-powered development ecosystem.

**Vibe Coding Platforms - Shared Infrastructure, Shared Risk**
==============================================================

The term vibe coding was coined by OpenAI co-founder Andrej Karpathy in February 2025 to describe a development approach where users fully trust AI to generate code without manual oversight. Platforms and vendors quickly emerged to offer this capability, democratizing software development by allowing anyone to build applications using plain language.

To grasp the severity of the vulnerability we found and similar ones, it’s essential to understand the shared-risk model of vibe coding platforms. All applications run on the vendor's shared infrastructure, meaning every customer inherits the vendor's security posture. This model introduces a critical single point of failure - a single flaw in the platform’s core, especially in a critical component like authentication, instantly jeopardizes every single application built upon it.  
  
The rapid enterprise adoption of these platforms for critical functions - handling sensitive data through internal chatbots, automations, and business tools - is precisely why we decided to focus our research efforts on this emerging [attack surface](https://www.wiz.io/academy/attack-surface "https://www.wiz.io/academy/attack-surface"). By understanding the potential impact of these systemic risks and by working with vendors to address them, we can help ensure the secure evolution of this transformative technology, helping vendors become more proactive in their quest for security assurance.

**Exposure Walkthrough**
========================

Our reconnaissance began by assessing Base44's publicly accessible domains. By mapping the external attack surface with straightforward reconnaissance techniques (passive and active discovery of subdomains), we identified around five internet facing subdomains. All appeared benign, hosting the main application, documentation, and marketing website - none of which initially suggested an interesting entry point.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBg0ICAgLCgoTDQ4HDQ0NDh0VFhENFxUZGBYTFhUaKysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDw0OHQ4QHC8cFhwvLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA0AGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAAABAECB//EAB4QAAIABwEBAAAAAAAAAAAAAAABAwQREhUxUQUC/8QAFQEBAQAAAAAAAAAAAAAAAAAAAQD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDVsRLLpOIlmOfUNU2yqhrogs/Ll7aAN2JrbAk//9k=)![](https://www.datocms-assets.com/75231/1753397368-unnamed-3.png?fm=webp)

Continuing with the research, we received an alert about two Swagger-UI interfaces that were publicly accessible across [app.base44.com](http://app.base44.com "http://app.base44.com") and [docs.base44.com](http://docs.base44.com "http://docs.base44.com"), providing information of internal documentation & API endpoints.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgTBgoIDQgLCg0LDhgQDgsNDh0VDg0NFxwZGBYVFiEmKzcjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDw0OHA0QEi8dFhw7Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAMAGAMBIgACEQEDEQH/xAAYAAEAAwEAAAAAAAAAAAAAAAAAAwQHAf/EACAQAAIABAcAAAAAAAAAAAAAAAACAQMRMQQiIzKBk9H/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABcRAQADAAAAAAAAAAAAAAAAAAABAzH/2gAMAwEAAhEDEQA/ANSwq6W+Z2N6WpEL5m5aJ0Cs0YSrWt4gAKf/2Q==)![](https://www.datocms-assets.com/75231/1753397407-unnamed-4.png?fm=webp)

Swagger-UI is an open-source tool that provides an interactive interface for visualizing and testing APIs, making it easier to understand and interact with web services.

By leveraging Swagger's interface, we browsed through the API endpoints looking for any endpoint that might leak sensitive data, allow privileged permissions, or be accessible without authentication. The API documentation was well-organized into several segments, but one section immediately caught our attention: the "auth" APIs.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAQAQMAAAA26i3WAAAAA1BMVEX79/2GGlgwAAAAD0lEQVR42mNhYGBgoQADAAjAAEHpWQJpAAAAAElFTkSuQmCC)![](https://www.datocms-assets.com/75231/1753397450-unnamed-5.png?fm=webp)

Given that Base44 is a vibe coding platform used by enterprises, we recognized that any authentication tampering vulnerability would have maximum impact. Before diving into the API specifications, we first examined how Base44 offers different authentication methods to its customers:

1. **Public (requires login)** – Default setting allowing any user to sign up and access the application
2. **Private with Beta authentication** – Still allows self-signup, effectively remaining public
3. **Private with SSO** – The only real private option, restricting access to invited users while enforcing SSO in the authentication flow

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABMAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAAAAv/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK+AlQAAAAAD/9k=)![](https://www.datocms-assets.com/75231/1753397553-unnamed-6.png?fm=webp)

Armed with this knowledge, we wondered if any of the authentication APIs could bypass these restrictions.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAKCAMAAACZt25aAAAAZlBMVEXl8f/l8v/m8v7m8v/n8/zn8/3n8/7n9Pzo9Pro9Pvo9Pzo9frp9fjp9fnp9frp9vjq9vbq9vfq9vjq9/br9/Tr9/Xr9/br+PTs+PLs+PPs+PTs+fLt+fDt+fHt+fLt+vDu+u/u+vCw+Yw4AAAAcUlEQVR42l2PWRLDIAxD5aXp/Q8MqizSj8R4GHiWLWhMRIJNsEqXpYXogSLUkcC2SAT90cYvka7DHTGFC1Lz8hziDJ5ZKiDvklpgNVpZGOWR//m0yIO2jRoutlfIEZ0C05HHgHrUsnnhFdtc/3hGmCt/VPIsft+4ui4AAAAASUVORK5CYII=)![](https://www.datocms-assets.com/75231/1753397582-unnamed-7.png?fm=webp)

After examining the documentation, we discovered an interesting lead which eventually turned into a critical misconfiguration - the `api/apps/{app_id}/auth/register` (registering a new user by providing email address and password) and `api/apps/{app_id}/auth/verify-otp`  (verifying our user by providing one-time-password) endpoints were exposed without authentication, allowing anyone to register for private applications using only the app\_id value it expects - particularly interesting in cases where sign-up is disabled.

The question became - how do we obtain app\_id values? These appeared as random strings like `686d0a751a78bb2608517740`, but we quickly discovered they weren't a secret at all. When we navigate to any application developed on top of Base44, the app\_id is immediately visible in the URI and manifest.json file path, all applications have their app\_ids value hardcoded in their manifest path: `manifests/{app_id}/manifest.json`.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhAPDwgREQ8HDA0NDhINDhEhDREYFxYZGBYVFiEaHysjGikoHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLCg0OFQ4QGi8dFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAwAGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAABBAACB//EAB0QAAEDBQEAAAAAAAAAAAAAAAABAgUDBBIxURH/xAAWAQEBAQAAAAAAAAAAAAAAAAABAgD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwDU0ibH0CxVi1w8tBmWij6LMtCkosXZKQdSizgBZ//Z)![](https://www.datocms-assets.com/75231/1753397686-unnamed-8.png?fm=webp)

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAcAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AK0ARACT/9k=)![](https://www.datocms-assets.com/75231/1753397744-unnamed-9.png?fm=webp)

Using our target application's app\_id, we successfully registered a new user account through the Swagger-UI interface, received an OTP verification code via email, and verified our new account - all for an application we didn't own and that was configured for SSO-only access.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLGhUYDg0NDh0gFhEVFxUZHRYVGh4mKysjGh0oHRUWJDUlLS0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OFg4OHDsdFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA0AGAMBIgACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAAFAwD/xAAeEAABBAIDAQAAAAAAAAAAAAACAAEDBQYRBxIhFv/EABYBAQEBAAAAAAAAAAAAAAAAAAMBAP/EABcRAQEBAQAAAAAAAAAAAAAAAAACIgH/2gAMAwEAAhEDEQA/AErTGrp5ddUeWJXet9UrkeaWUE7DGwMzISTkC3YfHFHlEfj7wpd9VlA+RLkT8cVknKln/9k=)![](https://www.datocms-assets.com/75231/1753397770-unnamed-10.png?fm=webp)

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAsAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/ALEAQgCT/9k=)![](https://www.datocms-assets.com/75231/1753397797-unnamed-11.png?fm=webp)

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCg8LDhUNDg0ODh0eDQ4YFxUZGBYVFhUaKysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHA0QHDscFh0vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAoAGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAGAAQH/8QAIhAAAQMDAwUAAAAAAAAAAAAAAgADkQEFMgQREwYSFCEi/8QAFgEBAQEAAAAAAAAAAAAAAAAAAgMB/8QAFxEBAQEBAAAAAAAAAAAAAAAAAAExIf/aAAwDAQACEQMRAD8AcXLwdK/9HRVXNTbC2rVwZR7qsi58qyjjhn2ZVlELp1qH7WXrlGVFnDjh75lKi1eTj//Z)![](https://www.datocms-assets.com/75231/1753397825-unnamed-12.png?fm=webp)

After confirming our email address, we could just login via the SSO within the application page, and successfully bypass the authentication.

We used 2 different methods to discover Base44 applications in the wild, which helped us proactively notify a couple of our customers who were vulnerable.  
  
1. **Enterprise applications with custom domains** - Base44 allows companies to add custom domains, they all share the same CNAME record - pointing to [base44.onrender.com](http://base44.onrender.com "http://base44.onrender.com"), using this knowledge, we identified several enterprise applications in our reconnaissance data.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoSCAgLCgoNDiQVDQ0NDhYVFhERFx8ZGBYVFhYdHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAOHDUdIigvLy8vLy81Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAsAGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABQYD/8QAHRAAAgICAwEAAAAAAAAAAAAAAQIAAwQREyIyBf/EABcBAAMBAAAAAAAAAAAAAAAAAAEDBAD/xAAXEQADAQAAAAAAAAAAAAAAAAAAAQIh/9oADAMBAAIRAxEAPwCEyxZXUdCJ7Rkup0hlflopXyJklNfAegmKFOEI4cHsCIR19GtA50ohAJcn/9k=)![](https://www.datocms-assets.com/75231/1753398061-unnamed-13.png?fm=webp)

2. **General Reconnaissance** - any Base44 application is presented with the same login page flow, equipped with identifiers that mention the string “base44”, we used platforms such as urlscan that helped us discover additional applications empowered by the vibe coding platform by searching for HTML data.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLEQoNDhUQDg0XDhMVFg0YFxUdGCIVFiYdKysjJh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OGhAQHDsoFhwvLy8vLy87Ly8vLy8vLy8vLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAsAGAMBIgACEQEDEQH/xAAZAAACAwEAAAAAAAAAAAAAAAABBQMEBwD/xAAgEAABAgUFAAAAAAAAAAAAAAABAAIDBBITMgYRFjFR/8QAFQEBAQAAAAAAAAAAAAAAAAAAAQL/xAAYEQEAAwEAAAAAAAAAAAAAAAAAAhESAf/aAAwDAQACEQMRAD8A086elidySgdOSpHZTBr3elQxIr6sim+gs4pL3N6kVfhxH3MiuVbkH//Z)![](https://www.datocms-assets.com/75231/1753398101-unnamed-14.png?fm=webp)

**Impact of the Vulnerability**
===============================

This vulnerability meant that private applications hosted on Base44 could be accessed without authorization. During our research we managed to confirm authentication bypass was available across several enterprise applications that utilized the popular vibe coding platform for internal chatbots, knowledge bases, PII & HR operations - significant sensitive data that could have been leaked to unauthorized attackers.

What made this vulnerability particularly concerning was its simplicity - requiring only basic API knowledge to exploit. This low barrier to entry meant that attackers could systematically compromise multiple applications across the platform with minimal technical sophistication. Fortunately, Wix confirmed that there was no evidence of exploitation in the wild.

**Am I Affected?**
==================

If you or your organization utilize Base44’s platform, especially for business operations or for storing sensitive data, Here's what you need to know:

**The vulnerability has been completely resolved.** Following our responsible disclosure on July 9th, 2025, Wix implemented a fix within 24 hours that properly validates application privacy settings before allowing user registration.

**No evidence of malicious exploitation.** Wix conducted a thorough investigation and confirmed there was no indication of past abuse or compromise across the Base44 user base during the vulnerable period.

**No action required from customers.** Since the fix was implemented platform-wide by Base44/Wix, no additional steps are needed from organizations using the platform.

**Wiz Research verified the fix -** Wiz Research independently verified that the fix completely addresses the vulnerability - Base44 now correctly prevents unauthorized registration attempts on private applications.

While no immediate action is required, organizations may want to:

* Review the data -> analytics section inside your Base44 application settings for any unusual user visits and registrations to any of your private applications during the vulnerable period (July 9th and earlier)
* Implement additional monitoring for third-party platform access as a general security best practice
* Wiz customers can use the inventory page to identify any Base44 applications in their environment, detected by our External Attack Surface.

**Key Takeaways**
=================

This vulnerability highlights a critical gap in how we evaluate AI development platforms. While security discussions often focus on [AI-specific threats](https://www.wiz.io/academy/ai-security-risks "https://www.wiz.io/academy/ai-security-risks") like [model poisonin](https://www.wiz.io/academy/data-poisoning "https://www.wiz.io/academy/data-poisoning")g or [prompt injection](https://www.wiz.io/academy/prompt-injection-attack "https://www.wiz.io/academy/prompt-injection-attack"), the most immediate risks stem from fundamental security controls - proper authentication and secure API design.

Vibe Coding platforms create new attack surfaces that [traditional security frameworks](https://www.wiz.io/academy/application-security-frameworks "https://www.wiz.io/academy/application-security-frameworks") may not adequately address. As they continue to evolve and gain enterprise adoption, the security community, vendors, and organizations must work together to build robust security foundations.  
  
Through responsible disclosure and open dialogue, we can help these transformative platforms strengthen their security posture and develop with security as a core consideration, so enterprises can trust them more without worry and develop at a faster pace than ever before.

**Statement from Base44, part of Wix**
======================================

The security and privacy of our users are paramount. We are committed to maintaining the highest standards of security across all our products and platforms. The recent acquisition of Base44 by Wix was driven in large part by Wix’s commitment to delivering trusted, robust technology backed by the company’s industry-leading infrastructure and security standards.

Immediately upon being notified by the Wiz research team about a potential vulnerability, we conducted a thorough investigation and took swift, decisive action to remediate the issue in the Base44 platform. We’ve investigated and, so far, found no evidence that any customer was impacted by an attacker leveraging the vulnerability. Our investigation is ongoing as we continue to take this matter seriously.

We continue to invest heavily in strengthening the security of all products and potential vulnerabilities are proactively managed. We remain committed to protecting our users and their data.

**Closure**
===========

The AI development landscape is evolving at unprecedented speed, with Vibe Coding platforms transforming how organizations build software. However, this rapid innovation cycle often outpaces security considerations, creating systemic risks that affect entire ecosystems rather than individual applications.

Building security into the foundation of these platforms, not as an afterthought - is essential for realizing their transformative potential while protecting enterprise data. We thank Wix for their prompt collaboration and response to our disclosure.

**Disclosure timeline**
=======================

* July 9th, 2025 - Wiz Research discovers and reports the vulnerability to Wix & Base44
* July 9th, 2025 - Wix acknowledges the recipient of the report, working on a fix.  
  July 10th, 2025 - Wiz researchers verify the fix, external users can no longer register to private applications
* July 13th, 2025 - Wix confirms that the issue is officially resolved, while reporting no indication of compromise across Base44 user-base.
* July 29th, 2025 - Public Disclosure

Tags

[#Research](/blog/tag/research "/blog/tag/research")[#Vulnerabilities](/blog/tag/vulnerabilities "/blog/tag/vulnerabilities")

Table of contents

* [Executive Summary](#executive-summary-2 "#executive-summary-2")
* [Vibe Coding Platforms - Shared Infrastructure, Shared Risk](#vibe-coding-platforms---shared-infrastructure-shared-risk-7 "#vibe-coding-platforms---shared-infrastructure-shared-risk-7")
* [Exposure Walkthrough](#exposure-walkthrough-10 "#exposure-walkthrough-10")
* [Impact of the Vulnerability](#impact-of-the-vulnerability-37 "#impact-of-the-vulnerability-37")
* [Am I Affected?](#am-i-affected-40 "#am-i-affected-40")
* [Key Takeaways](#key-takeaways-48 "#key-takeaways-48")
* [Statement from Base44, part of Wix](#statement-from-base44-part-of-wix-51 "#statement-from-base44-part-of-wix-51")
* [Closure](#closure-55 "#closure-55")
* [Disclosure timeline](#disclosure-timeline-58 "#disclosure-timeline-58")

###### Watch 12-min demo

See how Wiz protects your cloud from code to runtime

[Watch now](https://www.wiz.io/recorded-demo/cloud?cta_source=blog&cta_page=/blog/critical-vulnerability-base44&cta_placement=sidebar "https://www.wiz.io/recorded-demo/cloud?cta_source=blog&cta_page=/blog/critical-vulnerability-base44&cta_placement=sidebar")

Continue reading
----------------

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzODkwIiBoZWlnaHQ9IjIxNzciPjwvc3ZnPg==)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDiQcFRgNDhsVFh0VFx0dHhYWJSQmKysjJh0oHR0WJTUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLAg0OHBAQHDsoIig7Ozs7Lzs7Ozs1Ozs7Oy87OzsvOzsvOzs7LzU7NS8vLzsvOy87Oy8vLy87Ly8vNS8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAXAAADAQAAAAAAAAAAAAAAAAAABQYE/8QAIhAAAQMDAwUAAAAAAAAAAAAAAQACBAUGEQMjMRMhIlGR/8QAFQEBAQAAAAAAAAAAAAAAAAAABgX/xAAeEQABAwQDAAAAAAAAAAAAAAACAAESBAUGMQMRIf/aAAwDAQACEQMRAD8Adst6G6OfIKQuO14L3jcAOfa3RavJdBJLjwom4avLOvjqEd0oqGvwi/bqfSHgUvBVFqWnAFKbuD6hIGVSS+lty88IR83vMkkDlwCOl//Z)![](https://www.datocms-assets.com/75231/1753706510-traitor-2x.png?fm=webp)](/blog/north-korean-tradertraitor-crypto-heist "/blog/north-korean-tradertraitor-crypto-heist")

[### TraderTraitor: Deep Dive](/blog/north-korean-tradertraitor-crypto-heist "/blog/north-korean-tradertraitor-crypto-heist")

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NzQiIGhlaWdodD0iNDM4Ij48L3N2Zz4=)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAXCAIAAACeQxh6AAADqUlEQVR42jVUDXLuOAgDjJ2knb3/gfYSu8dom1/bwIr0bYdxk3yxIgsh/fefv0tRbWttH6qblMVCx4jrntd5X+f13JeNm+wp1Kv0yl35Ej9p7jZ267vNy22oCImwMIpQTKigCI5c6b3+c0Hvr/kaS76dO6kIR3FyBRKeKp68QNjwQniEhVvYu7qxO7PjG+/3WDn3eJRCaqwhBKAXOn8OJqcwShD3OVA2OwoXHMNlBrDEk0eeQCi5qHMN4Am5hEnun0QjQSZj+3ie/lz9zvL5SAwqphXEjNgSDjoULiTAzpOFjQj3VxlnUClPj/ua9/Fc+3keZ79vm1B6mrq0UI+Kt3QUwOEERCXlwAn75Yk8mWdQHyb348c5fn6ufT+P/UTX3Dq2rRqxEk/OIzajMpTzyOQGQfS5DgZBVuIK8frg67af4/n+vn5+jmM/7vuOBPKtka1CH0wb0xKus8oQ6kwzge5zT3ZcgnS6PJ3Oc37v9/f3+fV97IC8r0ib+LOwbSUGSkDNmtcyk9T/QCdBLSqgM4zvJ/YD57q/vo6vr33fIdXrtxJ9keiFrLIJTfYlGuSXiRuC2qM/QRwA8tInQ9nrHOdxQZ5j/wW6AVRLgIiEKtfKgGWGydQTCLIByMyIBFjmZJPm9DnnGKP32XPNAlCUUC69Uu/cO3UVxSa0T0Av2wdjlxcIGsHilMOCJkrJ9S3Kgj0wNa+UDBOiQCjt7+6R00Xa2hovECwG/7ewNkpbqK3eblzD5+I28f22iDbViiqCGYGli+VnfsVets9fRobBwWHh8Rjda586oAHVogtOi66ti2ybrp+lbdJWqtWKzEKDAmKbrh9/AQhdM9IK4WpEmZPWGYvRwmVr6Wz42NcmnxuwyrbS0qLq2/voBE8mo/XzVQEf12mFGwYc+nfjzXlj3SqcPoeg3ZU/Fv5YecHBq71ufKAyeUc8KIimolIJpwglxYBjfBFtC0iRrNoee4GaEswNlKWmFQs/nPOegRAMdqW9baoEMlRVSqWAKovV1atR4/KYwb7YHK1GRWZUE+4ZXJRdQ6phdhXD98YLsBRASCj8L1VrK3WRZpk4gjyCo0sURBiCrMxMTAQeFIAQjrbiMYIogw1/6aI0C24QoEqS2wBKGTwxBckDWNgb9GLCVwinafAwKAUGFc8DOcuczvIkjFdxj1sEmL4r5V/a0t8Ytcx0z2EYAHrTWNOZlFTkN+Yz5fndxjnMf1akqryPIwfzfcmDzH/NjUmJ/wDA7OIZGhSxqQAAAABJRU5ErkJggg==)![](https://www.datocms-assets.com/75231/1721219501-slack.png?fm=webp)](/authors/merav-bar "/authors/merav-bar")

[Merav Bar](/authors/merav-bar "/authors/merav-bar")

July 28, 2025

Inside the Lazarus subgroup that’s hijacking cloud platforms, poisoning supply chains, and stealing billions in digital assets.

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMDAyIiBoZWlnaHQ9IjE2OTAiPjwvc3ZnPg==)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAOCAIAAAC6mkspAAAB7klEQVR42k2Sa3LbQAyD+VzLzlV6r97/V1NLJAuskk40GFn2yt+CWMSv32MuDqVYiLqMSo9U847LdDL1WPJ6yHPJIyVVFKunnJ/n+/PP+f5b1xVuoipmggfbIkj4I0EzZh2meC9coPQNwipeioG0p2QCa3QUEsE7ngcsOBqARqbcOkOPpODoCEnsB0cq1/R7+tIun1h5mVmERW4QpjM6woYzl8gX6LnmtfK1gJPlBE3UZVCf3l0dK06H7fDIuFmMiTMVLOtcAC04AuiQj0c80xZywF7XVV4XlF1XfYMSiUquYOSGhDBWDWevDULM/VrzQV/+cA2CqgnqOuEIGUW5D8yvtMyONMSkOjNgtU67FWZ55rxStuYIgswB6rLuezRsaKZgQREgsgo4FB59Cz5dZ/k8XGDkEX24HK6pPE0Yh2ekPi2IBBdPW02R+t0pfEGBNk9DJVgOEBtGQkGRhe2xZjDMlhDUaJz4ID7xG6ok0ApiVymUTJi6bA1kI8Y/DAuou3eqUfTuLbf2ecEfK030DPZgEbDnT+FScHpj6AwgmGVusRv4pZuEqmwvxSB6unSLVeQ4DFG3ULz5dsSibwojpisMgiGQaUOg8GS0bpYpX4ORDeLZwtHcr8re5L82a9+NsbDodz57tb8SGC7cd/0HBwRkbwwaUHgAAAAASUVORK5CYII=)![](https://www.datocms-assets.com/75231/1753705976-artboard-2.png?fm=webp)](/blog/us-ai-action-plan "/blog/us-ai-action-plan")

[### What the U.S. AI Action Plan Means For Cyber Defenders](/blog/us-ai-action-plan "/blog/us-ai-action-plan")

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIj48L3N2Zz4=)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLDQ8LDiIXDQ0VEhEODQ0VFx8ZGCITFhUmHysjGh0oKRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBANHDscFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy81Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABgAGAMBIgACEQEDEQH/xAAYAAADAQEAAAAAAAAAAAAAAAAABQYBBP/EAB8QAAEEAQUBAAAAAAAAAAAAAAEAAgMEBRETMUFhEv/EABcBAQADAAAAAAAAAAAAAAAAAAMCBAX/xAAZEQADAQEBAAAAAAAAAAAAAAAAAhEDATH/2gAMAwEAAhEDEQA/AEEdOGawAXBUVXAxbBcHDhSM7JqtsaOVDj79ja+STwq+bNB815DhEDamScNe1iyaKSW6XaoUGZqAyrRFFckvZJrT2VeQ4wxUhJ4hC3UyWeAZv2Epcvvr3SPUIQibJb4Az9p//9k=)![](https://www.datocms-assets.com/75231/1711130315-mitch.jpeg?fm=webp)](/authors/mitch-herckis "/authors/mitch-herckis")

[Mitch Herckis](/authors/mitch-herckis "/authors/mitch-herckis")

July 28, 2025

In the race to lead in AI, the U.S. is prioritizing rapid innovation and national security.

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzODkxIiBoZWlnaHQ9IjIxNjIiPjwvc3ZnPg==)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAOCAIAAAC6mkspAAAB+UlEQVR42jWTC7bbMAhEZwDJdl66iu6kW+7mXusIOsinCVE4/lwNA4qfv367RxxzntdxvcZ1jfOMOcydBkMZVtSaXCfzy/Id9Xb8CLwDL8flGISzgjbgAa02ypREMZIBGoFCVhVRq3KBn+Kd+LDurHvhBhwAaxGB8WI4x0RcivKz/MjGGVmoND1YQha1c1WgBvRa50zkqvtRZMeb3iDOE+OsONInWpoESc6ikNmZYEJblWUjIJEmSg1dlCKbGzQnxlGKBo1y6Xiq+ki6nOp8s5piAumvlqVA0mhb0VeDYojFEGjsO3IHqaIYKm8zc5eZXgpYgdu5xQzoukDjpJsJFLJp0Juibkl75i6mXbdFk8jVCncU7moh3DtskCjuvfanEdw9l9GdSJg4bXQje1WwV33356m5wlUw0xSm1fcjuy7JAPbvUV6jMMDJHpydcALdwepXwvDX4C2ievz2Y72XdKg6t6X2ONdATdSpMF7kizjBQzjYY0ZYfjcotaWakArqVrvZV+Wn8eNYE+tgvQw7BGrcARPdYVtyfquIBuUG9eDEU1YPjqUoQVHytLysdCy+/rOOrq4PQZfG/KMjxdayh62nbGmbbWn3xZmDa1oeXucOna+Xt6KTHD277UmwPnugujU7sd0aPOsDUkPiCR1RRXAYhnFsvzcI/wCEGxAFLBW2HwAAAABJRU5ErkJggg==)![](https://www.datocms-assets.com/75231/1753138867-pwc-2x.png?fm=webp)](/blog/wiz-pwc-cloud-security-assessment "/blog/wiz-pwc-cloud-security-assessment")

[### Operationalizing Cloud Security: How PwC and Wiz Help Turn Risk into Resilience](/blog/wiz-pwc-cloud-security-assessment "/blog/wiz-pwc-cloud-security-assessment")

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIj48L3N2Zz4=)![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCxMUDhYPFQ0NFRIODQ0NFx8ZGBYVIhUdHysjGh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoFig7OzsvNTs7LzYvOzUwLy8vLzs7Ly8vLy81Oy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIABgAGAMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAABAYB/8QAIBAAAgIBAwUAAAAAAAAAAAAAAQIAEhEFFDEDBBNCUf/EABkBAAEFAAAAAAAAAAAAAAAAAAYAAQIDBP/EABkRAQADAQEAAAAAAAAAAAAAAAEAAhEhA//aAAwDAQACEQMRAD8AyLEBMAS7xsOwtUwj9oCtsczVX01tG9eIfevqicg1WokwwKuuDOyt9rdq/Ymmt3JF5JGVH6eRK+mx2VbGIivU2LUkgCopJiIloGRw2f/Z)![](https://www.datocms-assets.com/75231/1658183939-1657572482-wiz_logo_star_blue_bg-1.png?fm=webp)](/authors/wiz-team "/authors/wiz-team")

[Wiz Team](/authors/wiz-team "/authors/wiz-team")

July 24, 2025

PwC leverages Wiz to empower secure cloud transformation—bridging strategy, visibility, and execution.

Get a personalized demo

Ready to see Wiz in action?
---------------------------

> "Best User Experience I have ever seen, provides full visibility to cloud workloads."

David EstlickCISO

> "Wiz provides a single pane of glass to see what is going on in our cloud environments."

Adam FletcherChief Security Officer

> "We know that if Wiz identifies something as critical, it actually is."

Greg PoniatowskiHead of Threat and Vulnerability Management

[Get a demo](/demo "/demo")

Footer
------

### Platform

* [Cloud & AI Security](/platform "/platform")
* [Wiz Code](/platform/wiz-code "/platform/wiz-code")
* [Wiz Cloud](/platform/wiz-cloud "/platform/wiz-cloud")
* [Wiz Defend](/platform/wiz-defend "/platform/wiz-defend")
* [Integrations](/integrations "/integrations")
* [Environments](/environments "/environments")
* [Documentation](https://docs.wiz.io "https://docs.wiz.io")

### Learn

* [Customer Stories](/customers "/customers")
* [Cloud Security Courses](/courses "/courses")
* [Blog](/blog "/blog")
* [CloudSec Academy](/academy "/academy")
* [Resources Center](/resources "/resources")
* [Cloud Threat Landscape](/cloud-threat-landscape "/cloud-threat-landscape")
* [Cloud Security Assessment](/cloud-security-assessment "/cloud-security-assessment")
* [Vulnerability Database](/vulnerability-database "/vulnerability-database")

### Company

* [About Wiz](/about "/about")
* [Join the Team](/careers "/careers")
* [Newsroom](/newsroom "/newsroom")
* [Events](/events "/events")
* [Contact Us](/contact "/contact")
* [Trust Center](/trust-center "/trust-center")
* [Wiz Partner Alliance](/partner-alliance "/partner-alliance")

English (US)

[X](https://x.com/intent/user?screen_name=wiz_io "https://x.com/intent/user?screen_name=wiz_io")[LinkedIn](https://linkedin.com/company/wizsecurity "https://linkedin.com/company/wizsecurity")[RSS](/feed/rss.xml "/feed/rss.xml")

© 2026 Wiz, Inc.

[Status](https://status.wiz.io "https://status.wiz.io")[Privacy Policy](https://cloud.google.com/terms/cloud-acquisitions-privacy-notice?hl=en&e=0 "https://cloud.google.com/terms/cloud-acquisitions-privacy-notice?hl=en&e=0")[Terms of Use](https://legal.wiz.io/legal#terms-of-use "https://legal.wiz.io/legal#terms-of-use")[Modern Slavery Statement](https://legal.wiz.io/legal#modern-slavery "https://legal.wiz.io/legal#modern-slavery")Cookie Settings