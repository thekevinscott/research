# Context Engineering for Coding Agents — Martin Fowler
Source: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html

---

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<head><meta charset="UTF-8">
<title>Context Engineering for Coding Agents</title>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8" /><script defer src="https://cloud.umami.is/script.js" data-website-id="eb12527f-b713-4afa-905a-8a50f8a7f157"></script>
<meta content = 'summary' name = 'twitter:card'></meta>

<meta content = '16665197' name = 'twitter:site:id'></meta>

<meta content = '@martinfowler' name = 'twitter:site'></meta>

<meta content = 'Context Engineering for Coding Agents' property = 'og:title'></meta>

<meta content = 'https://martinfowler.com/articles/exploring-gen-ai.html/context-engineering-coding-agents.html' property = 'og:url'></meta>

<meta content = 'Notes from my Thoughtworks colleagues on AI-assisted software delivery' property = 'og:description'></meta>

<meta content = 'https://martinfowler.com/articles/exploring-gen-ai/donkey-card.png' property = 'og:image'></meta>

<meta content = 'martinfowler.com' property = 'og:site_name'></meta>

<meta content = 'article' property = 'og:type'></meta>

<meta content = '05 February 2026' property = 'og:article:modified_time'></meta>

<meta content = 'width=device-width, initial-scale=1' name = 'viewport'></meta>

<link href = 'exploring-gen-ai.css' rel = 'stylesheet' type = 'text/css'></link>
</head>

<body><header id = 'banner' style = 'background-image: url("/banner.png"); background-repeat: no-repeat'>

<div class = 'name-logo'><a href = 'https://martinfowler.com'><img src = '/mf-name-white.png'></img></a></div>
  <div class = 'search'>
    <!-- SiteSearch Google -->
    <form method='GET' action="https://www.google.com/search">
      <input type='hidden' name='ie' value='UTF-8'/>
      <input type='hidden' name='oe' value='UTF-8'/>
      <input class = 'field' type='text' 
             name='q' size='15' maxlength='255' value=""/>
      <button class = 'button' type='submit' 
             name='btnG' value=" " title = "Search"/>
      <input type='hidden' name='domains' value="martinfowler.com"/>
      <input type='hidden' name='sitesearch' value=""/> 
      <input
          type='hidden' name='sitesearch' value="martinfowler.com"/>
    </form>
  </div>

<div class = 'menu-button navmenu-button'><a class = 'icon icon-bars' href = '#navmenu-bottom'></a></div>

<nav class = 'top-menu'>
<ul>
<li><a class = '' href = 'https://refactoring.com'>Refactoring</a></li>

<li><a class = '' href = '/agile.html'>Agile</a></li>

<li><a class = '' href = '/architecture'>Architecture</a></li>

<li><a class = '' href = '/aboutMe.html'>About</a></li>

<li><a class = 'tw' href = 'https://www.thoughtworks.com/engineering'>Thoughtworks</a></li>

<li><a class = 'icon icon-rss' href = '/feed.atom' title = 'feed'></a></li>

<li><a class = 'icon icon-twitter' href = 'https://www.twitter.com/martinfowler' title = 'Twitter stream'></a></li>

<li class = 'icon'><a href = 'https://toot.thoughtworks.com/@mfowler' title = 'Mastodon stream'><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M21.2595 13.9898C20.9852 15.4006 18.8033 16.9446 16.2974 17.2439C14.9907 17.3998 13.7041 17.5431 12.3321 17.4802C10.0885 17.3774 8.31809 16.9446 8.31809 16.9446C8.31809 17.163 8.33156 17.371 8.3585 17.5655C8.65019 19.7797 10.5541 19.9124 12.3576 19.9742C14.1779 20.0365 15.7987 19.5254 15.7987 19.5254L15.8735 21.1711C15.8735 21.1711 14.6003 21.8548 12.3321 21.9805C11.0814 22.0493 9.52849 21.9491 7.71973 21.4703C3.79684 20.432 3.12219 16.2504 3.01896 12.0074C2.98749 10.7477 3.00689 9.55981 3.00689 8.56632C3.00689 4.22771 5.84955 2.95599 5.84955 2.95599C7.2829 2.29772 9.74238 2.0209 12.2993 2H12.3621C14.919 2.0209 17.3801 2.29772 18.8133 2.95599C18.8133 2.95599 21.6559 4.22771 21.6559 8.56632C21.6559 8.56632 21.6916 11.7674 21.2595 13.9898ZM18.3029 8.9029C18.3029 7.82924 18.0295 6.97604 17.4805 6.34482C16.9142 5.71359 16.1726 5.39001 15.2522 5.39001C14.187 5.39001 13.3805 5.79937 12.8473 6.61819L12.3288 7.48723L11.8104 6.61819C11.2771 5.79937 10.4706 5.39001 9.40554 5.39001C8.485 5.39001 7.74344 5.71359 7.17719 6.34482C6.62807 6.97604 6.3547 7.82924 6.3547 8.9029V14.1562H8.43597V9.05731C8.43597 7.98246 8.88822 7.4369 9.79281 7.4369C10.793 7.4369 11.2944 8.08408 11.2944 9.36376V12.1547H13.3634V9.36376C13.3634 8.08408 13.8646 7.4369 14.8648 7.4369C15.7694 7.4369 16.2216 7.98246 16.2216 9.05731V14.1562H18.3029V8.9029Z"></path></svg>
</a></li>

<li class = 'icon'><a href = 'https://www.linkedin.com/in/martin-fowler-com/' title = 'LinkedIn'><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M4.00098 3H20.001C20.5533 3 21.001 3.44772 21.001 4V20C21.001 20.5523 20.5533 21 20.001 21H4.00098C3.44869 21 3.00098 20.5523 3.00098 20V4C3.00098 3.44772 3.44869 3 4.00098 3ZM5.00098 5V19H19.001V5H5.00098ZM7.50098 9C6.67255 9 6.00098 8.32843 6.00098 7.5C6.00098 6.67157 6.67255 6 7.50098 6C8.3294 6 9.00098 6.67157 9.00098 7.5C9.00098 8.32843 8.3294 9 7.50098 9ZM6.50098 10H8.50098V17.5H6.50098V10ZM12.001 10.4295C12.5854 9.86534 13.2665 9.5 14.001 9.5C16.072 9.5 17.501 11.1789 17.501 13.25V17.5H15.501V13.25C15.501 12.2835 14.7175 11.5 13.751 11.5C12.7845 11.5 12.001 12.2835 12.001 13.25V17.5H10.001V10H12.001V10.4295Z"></path></svg>
</a></li>

<li class = 'icon'><a href = 'https://bsky.app/profile/martinfowler.com' title = 'BlueSky'><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 11.3884C11.0942 9.62673 8.62833 6.34423 6.335 4.7259C4.13833 3.17506 3.30083 3.4434 2.75167 3.69256C2.11583 3.9784 2 4.95506 2 5.52839C2 6.10339 2.315 10.2367 2.52 10.9276C3.19917 13.2076 5.61417 13.9776 7.83917 13.7309C4.57917 14.2142 1.68333 15.4017 5.48083 19.6292C9.65833 23.9542 11.2058 18.7017 12 16.0392C12.7942 18.7017 13.7083 23.7651 18.4442 19.6292C22 16.0392 19.4208 14.2142 16.1608 13.7309C18.3858 13.9784 20.8008 13.2076 21.48 10.9276C21.685 10.2376 22 6.10256 22 5.52923C22 4.95423 21.8842 3.97839 21.2483 3.6909C20.6992 3.44256 19.8617 3.17423 17.665 4.72423C15.3717 6.34506 12.9058 9.62756 12 11.3884Z"></path></svg></a></li>
</ul>
</nav>
</header>
<nav id = 'top-navmenu'>
<nav class = 'navmenu'>
<div class = 'nav-head'>  <div class = 'search'>
    <!-- SiteSearch Google -->
    <form method='GET' action="https://www.google.com/search">
      <input type='hidden' name='ie' value='UTF-8'/>
      <input type='hidden' name='oe' value='UTF-8'/>
      <input class = 'field' type='text' 
             name='q' size='15' maxlength='255' value=""/>
      <button class = 'button' type='submit' 
             name='btnG' value=" " title = "Search"/>
      <input type='hidden' name='domains' value="martinfowler.com"/>
      <input type='hidden' name='sitesearch' value=""/> 
      <input
          type='hidden' name='sitesearch' value="martinfowler.com"/>
    </form>
  </div>

<div class = 'closediv'>
<span class = 'close' title = 'close'></span>
</div>
</div>

<div class = 'nav-body'>
<div class = 'topics'>
<h2>Topics</h2>

<p><a href = '/architecture'>Architecture</a></p>

<p><a href = 'https://refactoring.com'>Refactoring</a></p>

<p><a href = '/agile.html'>Agile</a></p>

<p><a href = '/delivery.html'>Delivery</a></p>

<p><a href = '/microservices'>Microservices</a></p>

<p><a href = '/data'>Data</a></p>

<p><a href = '/testing'>Testing</a></p>

<p><a href = '/dsl.html'>DSL</a></p>
</div>

<div class = 'about'>
<h2>about me</h2>

<p><a href = '/aboutMe.html'>About</a></p>

<p><a href = '/books'>Books</a></p>

<p><a href = '/faq.html'>FAQ</a></p>
</div>

<div class = 'content'>
<h2>content</h2>

<p><a href = '/videos.html'>Videos</a></p>

<p><a href = '/tags'>Content Index</a></p>

<p><a href = '/fragments'>Fragments</a></p>

<p><a href = '/boardgames'>Board Games</a></p>

<p><a href = '/photos'>Photography</a></p>
</div>

<div class = 'tw'>
<h2>Thoughtworks</h2>

<p><a href = 'https://thoughtworks.com'>Home</a></p>

<p><a href = 'https://thoughtworks.com/insights'>Insights</a></p>

<p><a href = 'https://thoughtworks.com/careers'>Careers</a></p>

<p><a href = 'https://thoughtworks.com/radar'>Radar</a></p>

<p><a href = 'https://www.thoughtworks.com/engineering'>Engineering</a></p>
</div>

<div class = 'feeds'>
<h2>follow</h2>

<p><a href = '/feed.atom'>RSS</a></p>

<p><a href = 'https://toot.thoughtworks.com/@mfowler'>Mastodon</a></p>

<p><a href = 'https://www.linkedin.com/in/martin-fowler-com/'>LinkedIn</a></p>

<p><a href = 'https://bsky.app/profile/martinfowler.com'>Bluesky</a></p>

<p><a href = 'https://www.twitter.com/martinfowler'>X</a></p>

<p><a href = 'https://boardgamegeek.com/blog/13064/martins-7th-decade'>BGG</a></p>
</div>
</div>
</nav>
</nav>

<main class = 'memo context-engineering'>
<div class = 'frontMatter'>
<div class = 'main'>
<h1>Context Engineering for Coding Agents</h1>

<div class = 'front-grid'>
<div class = 'author-list'>
<div class = 'author'>
<div class = 'photo'><a href = 'https://birgitta.info'><img alt = 'Photo of Birgitta Böckeler' src = 'bb.jpg' width = '80'></img></a></div>

<address class = 'name'><a href = 'https://birgitta.info' rel = 'author'>Birgitta Böckeler</a></address>

<div class = 'bio'>
<p>Birgitta is a Distinguished Engineer and AI-assisted delivery
    expert at Thoughtworks. She has over 20 years of experience as a software
    developer, architect and technical leader.</p>
</div>
</div>
</div>
</div>
</div>

<div class = 'right'>
<div class = 'catalog-notice'>
<p><a href = '../exploring-gen-ai.html'><img src = 'donkey-card.png'></img></a></p>

<p>This article is part of <a href = '../exploring-gen-ai.html'>“Exploring Gen
  AI”</a>. A series capturing Thoughtworks technologists' explorations of using gen ai technology for
  software development.</p>
</div>

<p class = 'date'>05 February 2026</p>
</div>
</div>

<div class = 'paperBody'><p>The number of options we have to configure and enrich a coding agent’s context has exploded over the past few months. Claude Code is leading the charge with innovations in this space, but other coding assistants are quickly following suit. Powerful context engineering is becoming a huge part of the developer experience of these tools.</p>

<p>Context engineering is relevant for all types of agents and LLM usage of course. My colleague <a href="https://www.thoughtworks.com/insights/podcasts/technology-podcasts/talking-context-engineering">Bharani Subramaniam’s simple definition</a> is: “Context engineering is curating what the model sees so that you get a better result.”</p>

<p>For coding agents, there is an emerging set of context engineering approaches and terms. The foundation of it are the configuration features offered by the tools (e.g. “rules”, “skills”), and then the nitty gritty of part is how we conceptually use those features (“specs”, various workflows).</p>

<p>This memo is a primer about the current state of context configuration features, using Claude Code as an example at the end.</p>

<h2 id="what-is-context-in-coding-agents">What is context in coding agents?</h2>

<p>“Everything is context” - however, these are the main categories I think of as context configuration in coding agents.</p>

<h3 id="reusable-prompts">Reusable Prompts</h3>

<p>Almost all forms of AI coding context engineering ultimately involve a bunch of markdown files with prompts. I use “prompt” in the broadest sense here, like it’s 2023: A prompt is text that we send to an LLM to get a response back. To me there are two main categories of intentions behind these prompts, I will call them:</p>

<ul>
  <li>
    <p><strong>Instructions</strong>: Prompts that tell an agent to do something, e.g. “Write an E2E test in the following way: …”</p>
  </li>
  <li>
    <p><strong>Guidance</strong>: (aka rules, guardrails) General conventions that the agent should follow, e.g. “Always write tests that are independent of each other.”</p>
  </li>
</ul>

<p>These two categories often blend into each other, but I’ve still found it useful to distinguish them.</p>

<h3 id="context-interfaces">Context interfaces</h3>

<p>I couldn’t really find an established term for what I’d call <strong>context interfaces</strong>: Descriptions for the LLM of how it can get even more context, should it decide to.</p>

<ul>
  <li>
    <p><strong>Tools</strong>: Built-in capabilities like calling bash commands, searching files, etc.</p>
  </li>
  <li>
    <p><strong>MCP Servers</strong>: Custom programs or scripts that run on your machine (or on a server) and give the agent access to data sources and other actions.</p>
  </li>
  <li>
    <p><strong>Skills</strong>: These newest entrants into coding context engineering are descriptions of additional resources, instructions, documentation, scripts, etc. that the LLM can load on demand when it thinks it’s relevant for the task at hand.</p>
  </li>
</ul>

<p>The more of these you configure, the more space they take up in the context. So it’s prudent to think strategically about what context interfaces are necessary for a particular task.</p>

<p><img src="coding-context-overview.png" alt="Coding context visual overview, showing system prompt, context interfaces, instructions and guidance, conversation history" /></p>

<p><strong>Files in your workspace</strong></p>

<p>The most basic and powerful context interfaces in coding agents are file reading and searching, to understand your current codebase, so I’m giving them a special mention here. It’s worth reflecting on how well your existing code serves as context, basically if you have <a href="https://www.thoughtworks.com/radar/techniques/ai-friendly-code-design">AI-friendly codebase design</a>.</p>

<h2 id="if-and-when-who-decides-to-load-context">If and when: Who decides to load context?</h2>

<ul>
  <li>
    <p><strong>LLM</strong>: Allowing the LLM to decide when to load context is a prerequisite for running agents in an unsupervised way. But there always remains some uncertainty (dare I say non-determinism) <em>if</em> the LLM will actually load the context when we would expect it to. Example: Skills</p>
  </li>
  <li>
    <p><strong>Human</strong>: A human invocation of context gives us control, but reduces the level of automation overall. Example: Slash commands</p>
  </li>
  <li>
    <p><strong>Agent software</strong>: Some context features are triggered by the agent software itself, at deterministic points in time. Example: Claude Code hooks</p>
  </li>
</ul>

<h2 id="how-much-keeping-the-context-as-small-as-possible">How much: Keeping the context as small as possible</h2>

<p>One of the goals of context engineering is to balance the amount of context given - not too little, not too much. Even though context windows have technically gotten really big, that doesn’t mean that it’s a good idea to indiscriminately dump information in there. An agent’s effectiveness goes down when it gets too much context, and too much context is a cost factor as well of course.</p>

<p>Some of this size management is up to the developer: How much context configuration we create, and how much text we put in there. My recommendation would be to build context like rules files up gradually, and not pump too much stuff in there right from the start. The models have gotten quite powerful, so what you might have had to put into the context half a year ago might not even be necessary anymore.</p>

<p>Transparency about how full the context is, and what is taking up how much space, is a crucial feature in the tools to help us navigate this balance.</p>

<p><img src="claude-code-context.png" alt="Example of Claude Code's /context command result, giving transparency about what is taking up how much space in the context" /></p>

<p>But it’s not all up to us, some coding agent tools are also better at optimising context under the hood than others. They compact the conversation history periodically, or optimise the way tools are represented (like <a href="https://www.anthropic.com/engineering/advanced-tool-use">Claude Code’s Tool Search Tool</a>).</p>

<h2 id="example-claude-code">Example: Claude Code</h2>

<p>Here is an overview of Claude Code’s context configuration features as of January 2026, and where they fall in the dimensions described above:</p>

<div class="compact">

  <h3 id="claudemd"><a href="http://Claude.md">CLAUDE.md</a></h3>

  <p><strong>What:</strong> Guidance</p>

  <p><strong>Who decides to load:</strong> Claude Code - Always used at start of a session</p>

  <p><strong>When to use:</strong> For most frequently repeated general conventions that apply to the whole project</p>

  <p><strong>Example use cases:</strong></p>
  <ul>
    <li>“we use yarn, not npm”</li>
    <li>“don’t forget to activate the virtual environment before running anything”</li>
    <li>“when we refactor, we don’t care about backwards compatibility”</li>
  </ul>

  <p><strong>Other coding assistants:</strong> Basically all coding assistants have this feature of a main “rules file”; There are attempts to standardise it as <a href="https://agents.md/"><code>AGENTS.md</code></a></p>

  <h3 id="rules"><a href="https://code.claude.com/docs/en/memory#modular-rules-with-claude/rules/">Rules</a></h3>

  <p><strong>What:</strong> Guidance</p>

  <p><strong>Who decides to load:</strong> Claude Code, when files at the configured paths have been loaded</p>

  <p><strong>When to use:</strong> Helps organise and modularise guidance, and therefore limit size of the always loaded CLAUDE.md. Rules can be scoped to files (e.g. *.ts for all TypeScript files), which means they will then only be loaded when relevant.</p>

  <p><strong>Example use cases:</strong> “When writing bash scripts, variables should be referred to as ${var} not $var.” paths: **/*.sh</p>

  <p><strong>Other coding assistants:</strong> More and more coding assistants allow this path-based rules configuration, e.g. GH Copilot and Cursor</p>

  <h3 id="slash-commands"><a href="https://code.claude.com/docs/en/slash-commands">Slash commands</a></h3>

  <p><strong>What:</strong> Instructions</p>

  <p><strong>Who decides to load:</strong> Human</p>

  <p><strong>When to use:</strong> Common tasks (review, commit, test, …) that you have a specific longer prompt for, and that you want to trigger yourself, inside the main context <em>DEPRECATED in Claude Code, superceded by Skills</em></p>

  <p><strong>Example use cases:</strong> <code>/code-review</code> · <code>/e2e-test</code> · <code>/prep-commit</code></p>

  <p><strong>Other coding assistants:</strong> Common feature, e.g. GH Copilot and Cursor</p>

  <h3 id="skills"><a href="https://code.claude.com/docs/en/skills">Skills</a></h3>

  <p><strong>What:</strong> Guidance, instructions, documentation, scripts, …</p>

  <p><strong>Who decides to load:</strong> LLM (based on skill description) or Human</p>

  <p><strong>When to use:</strong> In its simplest form, this is for guidance or instructions that you only want to “lazy load” when relevant for the task at hand. But you can put whatever additional resources and scripts you want into a skill’s folder, and reference them from the main <code>SKILL.md</code> to be loaded.</p>

  <p><strong>Example use cases:</strong></p>
  <ul>
    <li>JIRA access (skill e.g. describes how agent can use CLI to access JIRA)</li>
    <li>“Conventions to follow for React components”</li>
    <li>“How to integrate the XYZ API”</li>
  </ul>

  <p><strong>Other coding assistants:</strong> Cursor’s “Apply intelligently” rules were always a bit like this, but they’re now also switching to Claude Code style Skills</p>

  <h3 id="subagents"><a href="https://code.claude.com/docs/en/sub-agents">Subagents</a></h3>

  <p><strong>What:</strong> Instructions + Configuration of model and set of available tools; Will run in its own context window, can be parallelised</p>

  <p><strong>Who decides to load:</strong> LLM or Human</p>

  <p><strong>When to use:</strong></p>
  <ul>
    <li>Common larger tasks that are suitable for and worth running in their own context for efficiency (to improve results with more intentional context), or to reduce costs).</li>
    <li>Tasks for which you usually want to use a model other than your default model</li>
    <li>Tasks that need specific tools / MCP servers that you don’t want to always have available in your default context</li>
    <li>Orchestratable workflows</li>
  </ul>

  <p><strong>Example use cases:</strong></p>
  <ul>
    <li>Create an E2E test for everything that was just built</li>
    <li>Code review done by a separate context and with a different model to give you a “second opinion” without the baggage of your original session</li>
    <li>subagents are foundational for swarm experiments like claude-flow or Gas Town</li>
  </ul>

  <p><strong>Other coding assistants:</strong> <a href="https://martinfowler.com/articles/pushing-ai-autonomy.html#MultipleAgents">Roo Code has had subagents for quite a while</a>, they call them “modes”; <a href="https://cursor.com/docs/context/subagents">Cursor just got them</a>; <a href="https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents">GH Copilot allows agent configuration</a>, but they can only be triggered by humans for now</p>

  <h3 id="mcp-servers"><a href="https://code.claude.com/docs/en/mcp">MCP Servers</a></h3>

  <p><strong>What:</strong> A program that runs on your machine (or on a server) and gives the agent access to data sources and other actions via the Model Context Protocol</p>

  <p><strong>Who decides to load:</strong> LLM</p>

  <p><strong>When to use:</strong> Use when you want to give your agent access to an API, or to a tool running on your machine. Think of it as a script on your machine with lots of options, and those options are exposed to the agent in a structured way. Once the LLM decides to call this, the tool call itself is usually a deterministic thing. There is a trend now to supercede some MCP server functionality with skills that describe how to use scripts and CLIs.</p>

  <p><strong>Example use cases:</strong> JIRA access (MCP server that can execute API calls to Atlassian) · Browser navigation (e.g. Playwright MCP) · Access to a knowledge base on your machine</p>

  <p><strong>Other coding assistants:</strong> All common coding assistants support MCP servers at this point</p>

  <h3 id="hooks"><a href="https://code.claude.com/docs/en/hooks-guide">Hooks</a></h3>

  <p><strong>What:</strong> Scripts</p>

  <p><strong>Who decides to load:</strong> Claude Code lifecycle events</p>

  <p><strong>When to use:</strong> When you want something to happen deterministically every single time you edit a file, execute a command, call an MCP server, etc.</p>

  <p><strong>Example use cases:</strong></p>
  <ul>
    <li>Custom notifications</li>
    <li>After every file edit, check if it’s a JS file and if so, then run prettier on it</li>
    <li>Claude Code observability use cases, like logging all executed commands somewhere</li>
  </ul>

  <p><strong>Other coding assistants:</strong> Hooks are a feature that is still quite rare. Cursor has just started supporting them.</p>

  <h3 id="plugins"><a href="https://code.claude.com/docs/en/plugins">Plugins</a></h3>

  <p><strong>What:</strong> A way to distribute all or any of these things</p>

  <p><strong>Example use cases:</strong> Distribute a common set of commands, skills and hooks to teams in an organisation</p>

</div>

<p>This is quite a long list! However, we’re in a “storming” phase right now and will surely converge on a simpler set of features. I expect e.g. Skills to not only absorb slash commands, but also rules, which would reduce this list by two entries.</p>

<h2 id="sharing-context-configurations">Sharing context configurations</h2>

<p>As I said in the beginning, these features are just the foundation for humans to do the actual work and filling these with reasonable context. It takes quite a bit of time to build up a good setup, because you have to use a configuration for a while to be able to say if it’s working well or not - there are no unit tests for context engineering. Therefore, people are keen to share good setups with each other.</p>

<p>Challenges for sharing:</p>

<ul>
  <li>The context of the sharer and the receiver has to be as similar as possible - it works a lot better inside of a team than between strangers on the internet</li>
  <li>There is a tendency to overengineer the context with unnecessary, copied &amp; pasted instructions up front, in my experience it’s best to build this up iteratively</li>
  <li>Different experience levels might need different rules and instructions</li>
  <li>If you have low awareness of what’s in your context because you copied a lot from a stranger, you might inadvertently repeat instructions or contradict existing ones, or blame the poor coding agent for being useless when it’s just following <em>your</em> instructions</li>
</ul>

<h2 id="beware-illusion-of-control">Beware: Illusion of control</h2>

<p>In spite of the name, ultimately this is not <em>really</em> engineering… Once the agent gets all these instructions and guidance, execution still depends on how well the LLM interprets them! Context engineering can definitely make a coding agent more effective and increase the probability of useful results quite a bit. However, sometimes people talk about these features with phrases like “ensure it does X”, or “prevent hallucinations”. But as long as LLMs are involved, we can never be <em>certain</em> of anything, <a href="/articles/exploring-gen-ai/to-vibe-or-not-vibe.html">we still need to think in probabilities</a> and choose the right level of human oversight for the job.</p>

</div>

<div class = 'series-nav'>
<div class = 'latest'>
<p class = 'label'>latest article (Mar 04):</p>

<p><a href = 'humans-and-agents.html'>Humans and Agents in Software Engineering Loops</a></p>
</div>

<div class = 'prev'>
<p class = 'label'>previous article:</p>

<p><a href = 'ccmenu-quality.html'>Assessing internal quality while coding with an agent</a></p>
</div>

<div class = 'next'>
<p class = 'label'>next article:</p>

<p><a href = 'harness-engineering-memo.html'>Harness Engineering - first thoughts</a></p>
</div>

<div class = 'index'>
<p><a href = '/articles/exploring-gen-ai.html'><img src = 'donkey-card.png'></img></a></p>
</div>
</div>
</main>

<nav id = 'bottom-navmenu'>
<nav class = 'navmenu'>
<div class = 'nav-head'>  <div class = 'search'>
    <!-- SiteSearch Google -->
    <form method='GET' action="https://www.google.com/search">
      <input type='hidden' name='ie' value='UTF-8'/>
      <input type='hidden' name='oe' value='UTF-8'/>
      <input class = 'field' type='text' 
             name='q' size='15' maxlength='255' value=""/>
      <button class = 'button' type='submit' 
             name='btnG' value=" " title = "Search"/>
      <input type='hidden' name='domains' value="martinfowler.com"/>
      <input type='hidden' name='sitesearch' value=""/> 
      <input
          type='hidden' name='sitesearch' value="martinfowler.com"/>
    </form>
  </div>

<div class = 'closediv'>
<span class = 'close' title = 'close'></span>
</div>
</div>

<div class = 'nav-body'>
<div class = 'topics'>
<h2>Topics</h2>

<p><a href = '/architecture'>Architecture</a></p>

<p><a href = 'https://refactoring.com'>Refactoring</a></p>

<p><a href = '/agile.html'>Agile</a></p>

<p><a href = '/delivery.html'>Delivery</a></p>

<p><a href = '/microservices'>Microservices</a></p>

<p><a href = '/data'>Data</a></p>

<p><a href = '/testing'>Testing</a></p>

<p><a href = '/dsl.html'>DSL</a></p>
</div>

<div class = 'about'>
<h2>about me</h2>

<p><a href = '/aboutMe.html'>About</a></p>

<p><a href = '/books'>Books</a></p>

<p><a href = '/faq.html'>FAQ</a></p>
</div>

<div class = 'content'>
<h2>content</h2>

<p><a href = '/videos.html'>Videos</a></p>

<p><a href = '/tags'>Content Index</a></p>

<p><a href = '/fragments'>Fragments</a></p>

<p><a href = '/boardgames'>Board Games</a></p>

<p><a href = '/photos'>Photography</a></p>
</div>

<div class = 'tw'>
<h2>Thoughtworks</h2>

<p><a href = 'https://thoughtworks.com'>Home</a></p>

<p><a href = 'https://thoughtworks.com/insights'>Insights</a></p>

<p><a href = 'https://thoughtworks.com/careers'>Careers</a></p>

<p><a href = 'https://thoughtworks.com/radar'>Radar</a></p>

<p><a href = 'https://www.thoughtworks.com/engineering'>Engineering</a></p>
</div>

<div class = 'feeds'>
<h2>follow</h2>

<p><a href = '/feed.atom'>RSS</a></p>

<p><a href = 'https://toot.thoughtworks.com/@mfowler'>Mastodon</a></p>

<p><a href = 'https://www.linkedin.com/in/martin-fowler-com/'>LinkedIn</a></p>

<p><a href = 'https://bsky.app/profile/martinfowler.com'>Bluesky</a></p>

<p><a href = 'https://www.twitter.com/martinfowler'>X</a></p>

<p><a href = 'https://boardgamegeek.com/blog/13064/martins-7th-decade'>BGG</a></p>
</div>
</div>
</nav>
</nav>
<footer id='page-footer'>
<div class='tw-logo'>
<a href='https://www.thoughtworks.com/engineering'>
<img src='/thoughtworks_white.png'>
</a>
</div>
<div class='menu-button'>
<div class='icon-bars navmenu-button'></div>
</div>
<div class='copyright'>
<p>© Martin Fowler | <a href="/aboutMe.html#disclosures">Disclosures</a></p>
</div>
</footer>
</body>
</html>
