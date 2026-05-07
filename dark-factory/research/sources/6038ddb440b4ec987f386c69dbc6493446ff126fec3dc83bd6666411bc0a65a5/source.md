# Assessing internal quality while coding with an agent — Martin Fowler
Source: https://martinfowler.com/articles/exploring-gen-ai/ccmenu-quality.html

---

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<head><meta charset="UTF-8">
<title>Assessing internal quality while coding with an agent</title>
<meta http-equiv="Content-type" content="text/html;charset=UTF-8" /><script defer src="https://cloud.umami.is/script.js" data-website-id="eb12527f-b713-4afa-905a-8a50f8a7f157"></script>
<meta content = 'summary' name = 'twitter:card'></meta>

<meta content = '16665197' name = 'twitter:site:id'></meta>

<meta content = '@martinfowler' name = 'twitter:site'></meta>

<meta content = 'Assessing internal quality while coding with an agent' property = 'og:title'></meta>

<meta content = 'https://martinfowler.com/articles/exploring-gen-ai.html/ccmenu-quality.html' property = 'og:url'></meta>

<meta content = 'Notes from my Thoughtworks colleagues on AI-assisted software delivery' property = 'og:description'></meta>

<meta content = 'https://martinfowler.com/articles/exploring-gen-ai/donkey-card.png' property = 'og:image'></meta>

<meta content = 'martinfowler.com' property = 'og:site_name'></meta>

<meta content = 'article' property = 'og:type'></meta>

<meta content = '27 January 2026' property = 'og:article:modified_time'></meta>

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

<main class = 'memo '>
<div class = 'frontMatter'>
<div class = 'main'>
<h1>Assessing internal quality while coding with an agent</h1>

<div class = 'front-grid'>
<div class = 'author-list'>
<div class = 'author'>
<div class = 'photo'><a href = 'https://www.linkedin.com/in/edoernenburg/'><img alt = 'Photo of  Erik Doernenburg' src = 'erik-d.jpg' width = '80'></img></a></div>

<address class = 'name'><a href = 'https://www.linkedin.com/in/edoernenburg/' rel = 'author'> Erik Doernenburg</a></address>

<div class = 'bio'>
<p>Erik is an experienced technologist and software engineer. He's always interested in emerging technologies and software excellence.</p>
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

<p class = 'date'>27 January 2026</p>
</div>
</div>

<div class = 'paperBody'><p>There’s no shortage of reports on how AI coding assistants, agents, and fleets of agents have written vast amounts of code in a short time, code that reportedly implements the features desired. It’s rare that people talk about non-functional requirements like performance or security in that context, maybe because that’s not a concern in many of the use cases the authors have. And it’s even rarer that people assess the quality of the code generated by the agent. I’d argue, though, that internal quality is crucial for development to continue at a sustainable pace over years, rather than collapse under its own weight.</p>

<p>So, let’s take a closer look at how the AI tooling performs when it comes to <a href="https://martinfowler.com/articles/is-quality-worth-cost.html#SoftwareQualityMeansManyThings">internal code quality</a>. We’ll add a feature to an existing application with the help of an agent and look at what’s happening along the way. Of course, this makes it “just” an anecdote. This memo is by no means a study. At the same time, much of what we’ll see falls into patterns and can be extrapolated, at least in my experience.</p>

<h2 id="the-feature-were-implementing">The feature we’re implementing</h2>

<p>We’ll be working with the codebase for <a href="https://ccmenu.org/">CCMenu</a>, a Mac application that shows the status of CI/CD builds in the Mac menu bar. This adds a degree of difficulty to the task because Mac applications are written in Swift, which is a common language, but not quite as common as JavaScript or Python. It’s also a modern programming language with a complex syntax and type system that requires more precision than, again, JavaScript or Python.</p>

<p><img src="ccmenu-screenshot.png" alt="Screenshot of CCMenu showing a list of pipelines and their status" /></p>

<p>CCMenu periodically retrieves the status from the build servers with calls to their APIs. It currently supports servers using a legacy protocol implemented by the likes of Jenkins, and it supports GitHub Actions workflows. The most requested server that’s not currently supported is GitLab. So, that’s our feature: we’ll implement support for GitLab in CCMenu.</p>

<h2 id="the-api-wrapper">The API wrapper</h2>

<p>GitHub provides the <a href="https://docs.github.com/en/rest/actions?apiVersion=2022-11-28">GitHub Actions API</a>, which is stable and well documented. GitLab has the <a href="https://docs.gitlab.com/api/rest/">GitLab API</a>, which is also well documented. Given the nature of the problem space, they are semantically quite similar. They’re not the same, though, and we’ll see how that affects the task later.</p>

<p>Internally, CCMenu has three GitHub-specific files to retrieve the build status from the API: a feed reader, a response parser, and a file that contains Swift functions that wrap the GitHub API, including functions like the following:</p>

<pre><code class="language-Swift">  func requestForAllPublicRepositories(user: String, token: String?) -&gt; URLRequest
  func requestForAllPrivateRepositories(token: String) -&gt; URLRequest
  func requestForWorkflows(owner: String, repository: String, token: String?) -&gt; URLRequest
</code></pre>

<p>The functions return <code>URLRequest</code> objects, which are part of the Swift SDK and are used to make the actual network request. Because these functions are structurally quite similar they delegate the construction of the <code>URLRequest</code> object to one shared, internal function:</p>

<pre><code class="language-Swift">  func makeRequest(method: String = "GET", baseUrl: URL, path: String,
        params: Dictionary&lt;String, String&gt; = [:], token: String? = nil) -&gt; URLRequest
</code></pre>

<p>Don’t worry if you’re not familiar with Swift, as long as you recognise the arguments and their types you’re fine.</p>

<h2 id="optional-tokens">Optional tokens</h2>

<p>Next, we should look at the <code>token</code> argument in a little more detail. Requests to the API’s can be authenticated. They don’t have to be authenticated but they can be authenticated. This allows applications like CCMenu to access information that’s restricted to certain users. For most API’s, GitHub and GitLab included, the token is simply a long string that needs to be passed in an HTTP header.</p>

<p>In its implementation CCMenu uses an optional string for the token, which in Swift is denoted by a question mark following the type, <code>String?</code> in this case. This is idiomatic use, and Swift forces recipients of such optional values to deal with the optionality in a safe way, avoiding the classic null pointer problems. There are also special language features to make this easier.</p>

<p>Some functions are nonsensical in an unauthenticated context, like <code>requestForAllPrivateRepositories</code>. These declare the token as non-optional, signalling to the caller that a token must be provided.</p>

<h2 id="lets-go">Let’s go</h2>

<p>I’ve tried this experiment a couple of times, during the summer using Windsurf and Sonnet 3.5, and now, recently, with Claude Code and Sonnet 4.5. The approach remained similar: break down the task into smaller chunks. For each of the chunks I asked Windsurf to come up with a plan first before asking for an implementation. With Claude Code I went straight for the implementation, relying on its internal planning; and on Git when something ended up going in the wrong direction.</p>

<p>As a first step I asked the agent, more or less verbatim: <em>“Based on the GitHub files for API, feed reader, and response parser, implement the same functionality for GitLab. Only write the equivalent for these three files. Do not make changes to the UI.”</em></p>

<p>This sounded like a reasonable request, and by and large it was. Even Windsurf, with the less capable model, picked up on  key differences and handled them, e.g. it recognised that what GitHub calls a repository is a project in GitLab; it saw the difference in the JSON response, where GitLab returns the array of runs at the top level while GitHub has this array as a property in a top-level object.</p>

<p>I hadn’t looked at the GitLab API docs myself at this stage and just from a cursory scan of the generated code everything looked pretty okay, the code compiled and even the complex function types were generated correctly, or were they?</p>

<h2 id="first-surprise">First surprise</h2>

<p>In the next step, I asked the agent to implement the UI to add new pipelines/workflows. I deliberately asked it not to worry about authentication yet, to just implement the flow for publicly accessible information. The discussion of that step is maybe for another memo, but the new code somehow needs to acknowledge that a token might be present in the future</p>

<pre><code class="language-Swift">  var apiToken: String? = nil
</code></pre>

<p>and then it can use the variable in the call the wrapper function</p>

<pre><code class="language-Swift">  let req = GitLabAPI.requestForGroupProjects(group: name, token: apiToken)
  var projects = await fetchProjects(request: req)
</code></pre>

<p>The <code>apiToken</code> variable is correctly declared as an optional String, initialised to <code>nil</code> for now. Later, some code could retrieve the token from another place depending on whether the user has decided to sign in. This code led to the first compiler error:</p>

<p><img src="ccmenu-error.jpg" alt="Screenshot of Xcode panel showing a compiler error in GitLabProjectList.swift. The error reads &quot;Value of optional type 'String?' must be unwrapped to a value of type 'String'&quot;." width="50%" /></p>

<p>What’s going on here? Well, it turns out that the code for the API wrapper in the first step had a bit of a subtle problem: it declared the tokens as non-optional in <em>all</em> the wrapper functions, e.g.</p>

<pre><code class="language-Swift">  func requestForGroupProjects(group: String, token: String) -&gt; URLRequest
</code></pre>

<p>The underlying <code>makeRequest</code> function, for one reason or another, was created correctly, with the token declared as optional.</p>

<p>The code compiled because in the way the functions were written, the wrapper functions definitely have a string and that can of course be passed to a function that takes an optional string, an argument that may be  a string or nothing (<code>nil</code>). But now, in the code above, we have an optional string and that can’t be passed to a function that needs a (definite) string.</p>

<h2 id="the-vibe-fix">The vibe fix</h2>

<p>Being lazy I simply copy-pasted the error message back to Windsurf. (Building a Swift app in anything but Xcode is a whole different story, and I remember an experiment with Cline where it alternated between adding and removing explicit imports, at about 20¢ per iteration.) The fix proposed by the AI for this problem worked: it changed the call-site and inserted an empty string as a default value for when no token was present, using Swift’s <code>??</code> operator.</p>

<pre><code class="language-Swift">  let req = GitLabAPI.requestForGroupProjects(group: name, token: apiToken ?? "")
  var projects = await fetchProjects(request: req)
</code></pre>

<p>This compiles, and it kinda works: if there’s no token an empty string is substituted, which means that the argument passed to the function is either the token or the empty string, it’s always a string and never <code>nil</code>.</p>

<p>So, what’s wrong? The whole point of declaring the token as optional was to signal that the token is optional. The AI ignored this and introduced new semantics: an empty string now signals that no token is available. This is</p>
<ul>
  <li>not idiomatic,</li>
  <li>not self-documenting,</li>
  <li>unsupported by Swift’s type system.</li>
</ul>

<p>It also required changes in every place where this function is called.</p>

<h2 id="the-real-fix">The real fix</h2>

<p>Of course, what the agent should’ve done is to simply change the function declaration of the wrapper function to make the token optional. With that change everything works as expected, the semantics remain intact, and the change is limited to adding a single <code>?</code> to the function argument’s type, rather than spraying <code>?? ""</code> all over the code.</p>

<h2 id="does-it-really-matter">Does it really matter?</h2>

<p>You might ask whether I’m splitting hair here. I don’t think I am. I think this is a clear example where an AI agent left to their own would have changed the codebase for the worse, and it took a developer with experience to notice the issue and to direct the agent to the correct implementation.</p>

<p>Also, this is just one of many examples I encountered. At some point the agent wanted to introduce a completely unnecessary cache, and, of course, couldn’t explain why it had even suggested the cache.</p>

<p>It also failed to realise that the user/org overlap in GitHub doesn’t exist in the GitLab, and went to implement some complicated logic to handle a non-existing problem. It took more than nudging the agent towards the correct places in the documentation to talk it down from insisting that the logic was needed.</p>

<p>It also “forgot” to use existing functions to construct URLs, replicating such logic in multiple places, often without implementing all functionality, e.g. the option to overwrite the base URL for testing purposes using the defaults system on macOS.</p>

<p>So, in those cases, and there were more, the generated code worked. It implemented the functionality required. But the new code also would’ve added completely unnecessary complexity and it missed non-obvious functionality, decreasing the quality of the codebase and introducing subtle issues.</p>

<p>If working on large software systems has taught me one thing it’s that investing in the internal quality of the software, the quality of the codebase, is a worthwhile investment. Don’t get overwhelmed by technical debt. Humans and agents find it more difficult to work with a complicated codebase. Without careful oversight, though, the AI agents seem to have a strong tendency to introduce technical debt, making future development harder, for humans and agents.</p>

<h2 id="one-more-thing">One more thing</h2>

<p>If possible, CCMenu shows the avatar of the person/actor that triggered the build. In GitHub the avatar URL is part of the response to the build status API call. GitLab has a “cleaner”, more RESTful design and keeps additional user information out of the build response. The avatar URL must be retrieved with a separate API call to a <code>/user</code> endpoint.</p>

<p>Both Windsurf and Claude Code stumbled over this in a major way. I remember a longish conversation where Claude Code wanted to convince me that the URL was in the response. (It probably got mixed up because multiple endpoints were described on the same page of the documentation.) In the end I found it easier to implement that functionality without agent support.</p>

<h2 id="my-conclusions">My conclusions</h2>

<p>During the experiments in the summer I was on the fence. The Windsurf / Sonnet 3.5 combo did speed up writing code, but it required careful planning with prompts, and I had to switch back and forth between Windsurf and Xcode (for building, running tests, and debugging), which always felt somewhat disorientating and got tiring quickly. The quality of the generated code had significant issues, and the agent had a tendency to get stuck trying to fix a problem. So, on the whole it felt like I wasn’t getting much out of using the agent. And I traded doing what I like, writing code, for overseeing an AI with a tendency to write sloppy code.</p>

<p>With Claude Code and Sonnet 4.5 the story is somewhat different. It needs less prompting, and the code has better quality. It’s by no means high quality code, but it’s better, requiring less rework and less prompting to improve quality. Also, running a conversation with Claude Code in a terminal window alongside Xcode felt more natural than switching between two IDEs. For me this has tilted the scales enough to use Claude Code regularly.</p>

</div>

<div class = 'series-nav'>
<div class = 'latest'>
<p class = 'label'>latest article (Mar 04):</p>

<p><a href = 'humans-and-agents.html'>Humans and Agents in Software Engineering Loops</a></p>
</div>

<div class = 'prev'>
<p class = 'label'>previous article:</p>

<p><a href = 'sdd-3-tools.html'>Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl</a></p>
</div>

<div class = 'next'>
<p class = 'label'>next article:</p>

<p><a href = 'context-engineering-coding-agents.html'>Context Engineering for Coding Agents</a></p>
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
