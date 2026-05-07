# browser-use/browser-use

browser-use is a Python framework for letting LLM agents drive a real browser via accessibility-tree extraction and structured action emission. It claims 78k+ GitHub stars and a custom ChatBrowserUse() model tuned for browser tasks (3-5x faster than general-purpose models). Browser Use Cloud adds stealth browsers and CAPTCHA handling.

browser-use is the closest open-source analog to a piece of StrongDM's Digital Twin Universe — it lets agents drive third-party services (Okta, Jira, Slack, Drive UIs) without a typed API, which is exactly the hole DTU fills with behavioral clones. In Dark Factory builds, browser-use is what you reach for when you need real-service interaction; DTU-style cloning replaces it once you need volume and determinism.
