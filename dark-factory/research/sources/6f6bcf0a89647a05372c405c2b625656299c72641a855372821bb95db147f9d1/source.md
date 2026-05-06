# vibe-tools

Give Cursor Agent an AI Team and Advanced Skills

Give AI Agents an AI team and advanced skills
Summary
Prompt it
Essential information to understand what vibe-tools is and how to get started using it
Overview of available commands and their basic functionality
Browser automation commands and capabilities
LLM provider integration and configuration
Model Context Protocol (MCP) commands and tools
Testing framework and capabilities
Configuration options and customization
Telemetry implementation and infrastructure
Example usage
Table of Contents
The AI Team
New Skills
How to Use
Example: Using Perplexity
Example: Using Gemini
What is vibe-tools
Installation
Requirements
Telemetry & Privacy
Tips
Additional Examples
GitHub Skills
Gemini Code Review
Detailed Cursor Usage
Tool Recommendations
Command Nicknames
Web Search
Repository Search
Documentation Generation
GitHub Integration
Browser Automation
Direct Model Queries
Authentication and API Keys
AI Team Features
Perplexity: Web Search & Research
Gemini 2.0: Repository Context & Planning
Stagehand: Browser Automation
Browser Command Options
Video Recording
Console and Network Logging
Complex Actions
Troubleshooting Browser Commands
YouTube Video Analysis
Skills
GitHub Integration
Linear Integration
Xcode Tools
Documentation Generation
Wait Command
Configuration
vibe-tools.config.json
GitHub Authentication
Repomix Configuration
Model Selection
Cursor Configuration
Cursor Agent Configuration
vibe-tools cli
Command Options
Execution Methods
Troubleshooting
Examples
Web Search Examples
Repository Context Examples
Documentation Examples
GitHub Integration Examples
Xcode Command Examples
Browser Command Examples
open subcommand examples
act, extract, observe subcommands examples
YouTube Command Examples
Node Package Manager
Contributing
Sponsors
License
The AI Team
Perplexity to search the web and perform deep research
Gemini 2.0 for huge whole-codebase context window, search grounding and reasoning
Stagehand for browser operation to test and debug web apps (uses Anthropic, OpenAI, Gemini, or OpenRouter models)
OpenRouter for access to a variety of models through a unified API (for MCP commands)
New Skills for your existing Agent
Work with GitHub Issues and Pull Requests
Access Linear issues with full context and comments
Generate local agent-accessible documentation for external dependencies
Analyze YouTube videos to extract insights, summaries, and implementation plans
vibe-tools
is optimized for Cursor Composer Agent but it can be used by any coding agent that can execute commands
How do I use it?
After installation, to see AI teamwork in action just ask Cursor Composer to use Perplexity or Gemini.
Here are two examples:
Asking Perplexity to carry out web research
see what happens next...
see what happens next...
see what happens next...
see the spec composer and perplexity produced together:
pac-man-spec.md
(link out to the example repo)
Asking Gemini for a plan
see what happens next...
see what happens next...
see what happens next...
see the spec composer and perplexity produced together:
pac-man-plan.md
(link out to the example repo)
What is vibe-tools
vibe-tools
provides a CLI that your
AI agent can use
to expand its capabilities.
vibe-tools
is designed to be installed globally, providing system-wide access to its powerful features. When you run
vibe-tools install
, it configures instruction files tailored to your chosen development environment:
Supported IDEs/Environments
: Cursor, Claude Code, Codex, Windsurf, Cline, Roo.
Instruction File Setup
: The installer automatically creates or updates relevant configuration files:
For
Cursor
:
.cursorrules
or
.cursor/rules/vibe-tools.mdc
.
For
Claude Code
:
CLAUDE.md
(local or global
~/.claude/CLAUDE.md
).
For
Codex
:
codex.md
(local or global
~/.codex/instructions.md
).
For
Windsurf
:
.windsurfrules
.
For
Cline/Roo
:
.clinerules
directory (with
vibe-tools.md
) or legacy file.
vibe-tools
supports multiple AI instruction sources including Claude code, Codex, and IDE-specific rules, ensuring compatibility across various AI-powered development setups.
vibe-tools
integrates with multiple AI providers including OpenAI, Anthropic, Gemini, Perplexity, OpenRouter, ModelBox, and xAI (Grok).
vibe-tools
requires a Perplexity API key and a Google AI API key.
vibe-tools
is a node package that should be installed globally.
Installation
Install vibe-tools globally:
npm install -g vibe-tools
Then run the setup:
vibe-tools install
.
This command will:
Guide you through API key configuration for the AI providers you choose.
Automatically install Playwright browsers (Chromium) for browser automation commands.
Create or update AI instruction files based on your selected IDE (e.g., setting up
.cursorrules
for Cursor,
CLAUDE.md
for Claude Code,
.windsurfrules
for Windsurf, etc.).
Non-Interactive Installation (CI/CD)
For automated environments,
vibe-tools install
automatically detects CI environments and runs in non-interactive mode:
#
CI environments - automatically detected and runs without prompts
CI=true vibe-tools install
.
#
Or explicitly set non-interactive mode
NONINTERACTIVE=true vibe-tools install
.
In non-interactive mode, vibe-tools will:
Auto-detect your package manager and IDE environment
Use existing configurations (local takes precedence over global)
Apply sensible defaults for new installations
Skip writing API keys to files (uses environment variables only)
Enable telemetry by default (can be disabled with
VIBE_TOOLS_NO_TELEMETRY=1
)
Requirements
Node.js 18 or later
Perplexity API key
Google Gemini API key
For browser commands:
Playwright browsers are automatically installed during
vibe-tools install
OpenAI API key or Anthropic API key (for
act
,
extract
, and
observe
commands)
vibe-tools
uses Gemini-2.5 models by default, which provide excellent performance with large context windows up to 2 million tokens - enough to handle an entire codebase in one shot. Available Gemini models include
gemini-2.5-flash
(default for speed),
gemini-2.5-pro
(default for quality), and
gemini-2.5-flash-lite-preview-06-17
(lightweight option). Gemini models are currently free to use on Google and you need a Google Cloud project to create an API key.
vibe-tools
uses Perplexity because Perplexity has the best web search api and indexes and it does not hallucinate. Perplexity Pro users can get an API key with their pro account and recieve $5/month of free credits (at time of writing). Support for Google search grounding is coming soon but so far testing has shown it still frequently hallucinates things like APIs and libraries that don't exist.
Telemetry & Privacy
vibe-tools
collects
anonymous usage telemetry
to help improve the tool. You will be prompted during installation to enable or disable telemetry, and you can opt out at any time. No code, queries, file contents, or personal data are ever collected—only high-level command usage and error types (see
TELEMETRY.md
for full details).
Telemetry is
opt-in
: you choose during install.
You can change your choice later by setting the
VIBE_TOOLS_NO_TELEMETRY=1
environment variable.
For details on what is (and is not) collected, and how telemetry works, see
TELEMETRY.md
.
Tips:
Ask Cursor Agent to have Gemini review its work
Ask Cursor Agent to generate documentation for external dependencies and write it to a local-docs/ folder
If you do something cool with
vibe-tools
please let me know on twitter or make a PR to add to this section!
Additional Examples
GitHub Skills
To see vibe-tools GitHub and Perplexity skills: Check out
this example issue that was solved using Cursor agent and vibe-tools
Gemini code review
See cursor get approximately 5x more work done per-prompt with Gemini code review:
Detailed Cursor Usage
Use Cursor Composer in agent mode with command execution (not sure what this means, see section below on Cursor Agent configuration). If you have installed the vibe-tools prompt to your .cursorrules (or equivalent) just ask your AI coding agent/assistant to use "vibe-tools" to do things.
Tool Recommendations
vibe-tools ask
allows direct querying of any model from any provider. It's best for simple questions where you want to use a specific model or compare responses from different models.
vibe-tools web
uses an AI teammate with web search capability to answer questions.
web
is best for finding up-to-date information from the web that is not specific to the repository such as how to use a library to search for known issues and error messages or to get suggestions on how to do something. Web is a teammate who knows tons of stuff and is always up to date.
vibe-tools repo
uses an AI teammate with large context window capability to answer questions.
repo
sends the entire repo as context so it is ideal for questions about how things work or where to find something, it is also great for code review, debugging and planning. With the
--with-diff
flag, it can also include git diff information for focused code review that keeps the AI focused on current changes while maintaining full codebase understanding. is a teammate who knows the entire codebase inside out and understands how everything works together.
vibe-tools plan
uses an AI teammate with reasoning capability to plan complex tasks. Plan uses a two step process. First it does a whole repo search with a large context window model to find relevant files. Then it sends only those files as context to a thinking model to generate a plan it is great for planning complex tasks and for debugging and refactoring. Plan is a teammate who is really smart on a well defined problem, although doesn't consider the bigger picture.
vibe-tools doc
uses an AI teammate with large context window capability to generate documentation for local or github hosted repositories by sending the entire repo as context.
doc
can be given precise documentation tasks or can be asked to generate complete docs from scratch it is great for generating docs updates or for generating local documentation for a libary or API that you use! Doc is a teammate who is great at summarising and explaining code, in this repo or in any other repo!
vibe-tools browser
uses an AI teammate with browser control (aka operator) capability to operate web browsers.
browser
can operate in a hidden (headless) mode to invisibly test and debug web apps or it can be used to connect to an existing browser session to interactively share your browser with Cursor agent it is great for testing and debugging web apps and for carrying out any task that can be done in a browser such as reading information from a bug ticket or even filling out a form. Browser is a teammate who can help you test and debug web apps, and can share control of your browser to perform small browser-based tasks.
vibe-tools youtube
uses an AI teammate with video analysis capability to understand YouTube content.
youtube
can generate summaries, extract transcripts, create implementation plans from tutorials, and answer specific questions about video content. It's great for extracting value from technical talks, tutorials, and presentations without spending time watching the entire video. YouTube is a teammate who can watch and analyze videos for you, distilling the key information.
Note: For repo, doc and plan commands the repository content that is sent as context can be reduced by filtering out files in a .repomixignore file.
Command Nicknames
When using vibe-tools with Cursor Composer, you can use these nicknames:
"Gemini" is a nickname for
vibe-tools repo
"Perplexity" is a nickname for
vibe-tools web
"Stagehand" is a nickname for
vibe-tools browser
Use web search
"Please implement country specific stripe payment pages for the USA, UK, France and Germany. Use vibe-tools web to check the available stripe payment methods in each country."
Note: in most cases you can say "ask Perplexity" instead of "use vibe-tools web" and it will work the same.
Use repo search
"Let's refactor our User class to allow multiple email aliases per user. Use vibe-tools repo to ask for a plan including a list of all files that need to be changed."
"Use vibe-tools repo to analyze how authentication is implemented in the Next.js repository. Use --from-github=vercel/next.js."
"Use vibe-tools repo to explain this React component with documentation from the official React docs. Use --with-doc=
https://react.dev/reference/react/useState
or a local file path"
"Use vibe-tools repo to review my recent changes and suggest improvements. Use --with-diff to include the git diff."
"Use vibe-tools repo to check if my changes are compatible with the main branch. Use --with-diff --base=main."
Note: in most cases you can say "ask Gemini" instead of "use vibe-tools repo" and it will work the same.
Use doc generation
"Use vibe-tools to generate documentation for the Github repo
https://github.com/kait-http/kaito
" and write it to docs/kaito.md"
Note: in most cases you can say "generate documentation" instead of "use vibe-tools doc" and it will work the same.
Use github integration
"Use vibe-tools github to fetch issue 123 and suggest a solution to the user's problem"
"Use vibe-tools github to fetch PR 321 and see if you can fix Andy's latest comment"
Note: in most cases you can say "fetch issue 123" or "fetch PR 321" instead of "use vibe-tools github" and it will work the same.
Use linear integration
"Use vibe-tools linear to set up authentication with Linear"
"Use vibe-tools linear to fetch issue ITE-123 and provide a summary of the current status"
"Use vibe-tools linear to get issue ABC-456 and explain what the team is discussing in the comments"
Note: in most cases you can say "fetch Linear issue ITE-123" or "get Linear issue ABC-456" instead of "use vibe-tools linear" and it will work the same.
Use browser automation
"Use vibe-tools to open the users page and check the error in the console logs, fix it"
"Use vibe-tools to test the form field validation logic. Take screenshots of each state"
"Use vibe-tools to open
https://example.com/foo
the and check the error in the network logs, what could be causing it?"
Note: in most cases you can say "Use Stagehand" instead of "use vibe-tools" and it will work the same.
Use direct model queries
"Use vibe-tools ask to compare how different models answer this question: 'What are the key differences between REST and GraphQL?'"
"Ask OpenAI's o3-mini model to explain the concept of dependency injection."
"Use vibe-tools ask to analyze this complex algorithm with high reasoning effort: 'Explain the time and space complexity of the Boyer-Moore string search algorithm' --provider openai --model o3-mini --reasoning-effort high"
Note: The ask command requires both --provider and --model parameters to be specified. This command is generally less useful than other commands like
repo
or
plan
because it does not include any context from your codebase or repository.
Ask Command Options:
--provider=<provider>
: AI provider to use (openai, anthropic, perplexity, gemini, modelbox, openrouter, xai, or groq)
--model=<model>
: Model to use (required for the ask command)
--max-tokens=<number>
: Maximum tokens for response
--reasoning-effort=<low|medium|high>
: Control the depth of reasoning for supported models (OpenAI o1/o3-mini models, Claude 4 Sonnet, and XAI Grok models). Higher values produce more thorough responses for complex questions.
--with-doc=<doc_url>
: Fetch content from one or more document URLs and include it as context. Can be specified multiple times (e.g.,
--with-doc=<url1> --with-doc=<url2>
).
Authentication and API Keys
vibe-tools
requires API keys for Perplexity AI, Google Gemini, and optionally for OpenAI, Anthropic, OpenRouter, and xAI. These can be configured in two ways:
Interactive Setup
: Run
vibe-tools install
and follow the prompts
Manual Setup
: Create
~/.vibe-tools/.env
in your home directory or
.vibe-tools.env
in your project root:
PERPLEXITY_API_KEY
=
"
your-perplexity-api-key
"
GEMINI_API_KEY
=
"
your-gemini-api-key
"
OPENAI_API_KEY
=
"
your-openai-api-key
"
#
Optional, for Stagehand
ANTHROPIC_API_KEY
=
"
your-anthropic-api-key
"
#
Optional, for Stagehand and MCP
OPENROUTER_API_KEY
=
"
your-openrouter-api-key
"
#
Optional, for MCP
XAI_API_KEY
=
"
your-xai-api-key
"
#
Optional, for xAI Grok models
GROQ_API_KEY
=
"
your-groq-api-key
"
#
Optional, for Groq models
GITHUB_TOKEN
=
"
your-github-token
"
#
Optional, for enhanced GitHub access
LINEAR_API_KEY
=
"
your-linear-api-key
"
#
Optional, for Linear integration
At least one of
ANTHROPIC_API_KEY
and
OPENROUTER_API_KEY
must be provided to use the
mcp
commands.
CI/CD Environments
: In non-interactive mode (automatically detected in CI environments), vibe-tools uses only environment variables for API keys and skips writing them to filesystem for enhanced security.
Google Gemini API Authentication
vibe-tools
supports multiple authentication methods for accessing the Google Gemini API, providing flexibility for different environments and security requirements. You can choose from the following methods:
API Key (Default)
This is the simplest method and continues to be supported for backward compatibility.
Set the
GEMINI_API_KEY
environment variable to your API key string obtained from Google AI Studio.
Example:
GEMINI_API_KEY
=
"
your-api-key-here
"
Service Account JSON Key File
For enhanced security, especially in production environments, use a service account JSON key file.
Set the
GEMINI_API_KEY
environment variable to the
path
of your downloaded service account JSON key file.
Example:
GEMINI_API_KEY
=
"
./path/to/service-account.json
"
This method enables access to the latest Gemini models available through Vertex AI, such as
gemini-2.5-flash
.
Automatic Doppler Secrets Manager Integration
(new in 0.63.x)
If the
Doppler
CLI is installed and your working directory has been configured with
doppler setup
, vibe-tools will automatically run
doppler secrets --json
at startup and load any secrets whose names end with
_API_KEY
into the current process
before
it evaluates which providers are available.
This means you can keep all of your provider keys (e.g.
OPENAI_API_KEY
,
ANTHROPIC_API_KEY
,
GEMINI_API_KEY
, etc.) in Doppler and skip copying them into
.env
files.
Doppler integration is
on by default
. To turn it off add the following to
vibe-tools.config.json
:
{
"disableDoppler"
:
true
}
Doppler secrets are only loaded if the variable is
not already defined
in the environment, so explicit environment variables always win.
The integration is read-only: secrets are never written back to Doppler or logged.
Environment Variable Precedence with VIBE_TOOLS_ Prefix
You can prefix any environment variable with
VIBE_TOOLS_
to ensure it takes precedence over all other sources
Example:
VIBE_TOOLS_OPENAI_API_KEY
will override
OPENAI_API_KEY
from any source (environment, .env files, or Doppler)
This works for all API keys and configuration variables
Useful for CI/CD environments or when you want different API keys specifically for vibe-tools
Example usage:
#
This will use the prefixed key instead of the regular one
VIBE_TOOLS_OPENAI_API_KEY=
"
vibe-specific-key
"
OPENAI_API_KEY=
"
regular-key
"
vibe-tools ask
"
Hello
"
Application Default Credentials (ADC) for Gemini models (Recommended for Google Cloud Environments)
Note:
This is an
alternative
to setting the
GEMINI_API_KEY
environment variable for Gemini models.
ADC is ideal when running
vibe-tools
within Google Cloud environments (e.g., Compute Engine, Kubernetes Engine) or for local development using
gcloud
.
Set the
GEMINI_API_KEY
environment variable to
adc
.
Example:
GEMINI_API_KEY
=
"
adc
"
Setup Instructions:
For Google Cloud environments no further steps are required.
To use vibe-tools locally with ADC, authenticate locally using gcloud:
gcloud auth application-default login
AI Team Features
Perplexity: Web Search & Research
Use Perplexity AI to get up-to-date information directly within Cursor:
vibe-tools web
"
What's new in TypeScript 5.7?
"
Gemini 2.0: Repository Context & Planning
Leverage Google Gemini 2.0 models with 1M+ token context windows for codebase-aware assistance and implementation planning:
#
Get context-aware assistance
vibe-tools repo
"
Explain the authentication flow in this project, which files are involved?
"
#
Generate implementation plans
vibe-tools plan
"
Add user authentication to the login page
"
The plan command uses multiple AI models to:
Identify relevant files in your codebase (using Gemini by default)
Extract content from those files
Generate a detailed implementation plan (using o3-mini by default)
Plan Command Options:
--fileProvider=<provider>
: Provider for file identification (gemini, openai, anthropic, perplexity, modelbox, openrouter, xai, or groq)
--thinkingProvider=<provider>
: Provider for plan generation (gemini, openai, anthropic, perplexity, modelbox, openrouter, xai, or groq)
--fileModel=<model>
: Model to use for file identification
--thinkingModel=<model>
: Model to use for plan generation
--fileMaxTokens=<number>
: Maximum tokens for file identification
--thinkingMaxTokens=<number>
: Maximum tokens for plan generation
--debug
: Show detailed error information
--with-doc=<doc_url>
: Fetch content from one or more web URLs and include it as context during plan generation. Can be specified multiple times (e.g.,
--with-doc=<url1> --with-doc=<url2>
).
Repository context is created using Repomix. See repomix configuration section below for details on how to change repomix behaviour.
Above 1M tokens vibe-tools will always send requests to Gemini 2.0 Pro as it is the only model that supports 1M+ tokens.
The Gemini 2.0 Pro context limit is 2M tokens, you can add filters to .repomixignore if your repomix context is above this limit.
Stagehand: Browser Automation
Automate browser interactions for web scraping, testing, and debugging:
Note:
Playwright browsers are automatically installed when you run
vibe-tools install
. No additional setup is required for browser commands.
open
- Open a URL and capture page content:
#
Open and capture HTML content, console logs and network activity (enabled by default)
vibe-tools browser open
"
https://example.com
"
--html
#
Take a screenshot
vibe-tools browser open
"
https://example.com
"
--screenshot=page.png
#
Debug in an interactive browser session
vibe-tools browser open
"
https://example.com
"
--connect-to=9222
act
- Execute actions using natural language - Agent tells the browser-use agent what to do:
#
Single action
vibe-tools browser act
"
Login as 'user@example.com'
"
--url
"
https://example.com/login
"
#
Multi-step workflow using pipe separator
vibe-tools browser act
"
Click Login | Type 'user@example.com' into email | Click Submit
"
--url
"
https://example.com
"
#
Record interaction video
vibe-tools browser act
"
Fill out registration form
"
--url
"
https://example.com/signup
"
--video=
"
./recordings
"
observe
- Analyze interactive elements:
#
Get overview of interactive elements
vibe-tools browser observe
"
What can I interact with?
"
--url
"
https://example.com
"
#
Find specific elements
vibe-tools browser observe
"
Find the login form
"
--url
"
https://example.com
"
extract
- Extract data using natural language:
#
Extract specific content
vibe-tools browser extract
"
Get all product prices
"
--url
"
https://example.com/products
"
#
Save extracted content
vibe-tools browser extract
"
Get article text
"
--url
"
https://example.com/blog
"
--html
>
article.html
#
Extract with network monitoring
vibe-tools browser extract
"
Get API responses
"
--url
"
https://example.com/api-test
"
--network
mac-chrome
- Start a Chrome instance with remote debugging (macOS only):
#
Launch Chrome with remote debugging on port 9222
vibe-tools browser mac-chrome
#
Launch with debug output to see the full command
vibe-tools browser mac-chrome --debug
#
Fast start-up with a minimal flag set
vibe-tools browser mac-chrome --lite
This command:
Only works on macOS (shows clear error on other platforms)
Creates an isolated temporary profile for clean testing
Launches Chrome with comprehensive automation-optimized flags (or minimal flags with
--lite
)
Enables remote debugging on port 9222
Provides connection instructions for Playwright/CDP tools
Uses proven Chrome configuration for reliable automation
--lite
option launches Chrome with a reduced set of flags for quicker startup and fewer side-effects
Browser Command Options
All browser commands (
open
,
act
,
observe
,
extract
) support these options:
--console
: Capture browser console logs (enabled by default, use
--no-console
to disable)
--html
: Capture page HTML content (disabled by default)
--network
: Capture network activity (enabled by default, use
--no-network
to disable)
--screenshot=<file path>
: Save a screenshot of the page
--timeout=<milliseconds>
: Set navigation timeout (default: 120000ms for Stagehand operations, 30000ms for navigation)
--viewport=<width>x<height>
: Set viewport size (e.g., 1280x720)
--headless
: Run browser in headless mode (default: true)
--no-headless
: Show browser UI (non-headless mode) for debugging
--connect-to=<port>
: Connect to existing Chrome instance. Special values: 'current' (use existing page), 'reload-current' (refresh existing page)
--wait=<time:duration or selector:css-selector>
: Wait after page load (e.g., 'time:5s', 'selector:#element-id')
--video=<directory>
: Save a video recording (1280x720 resolution, timestamped subdirectory). Not available when using --connect-to
--url=<url>
: Required for
act
,
observe
, and
extract
commands
--evaluate=<string>
: JavaScript code to execute in the browser before the main command
Notes on Connecting to an existing browser session with --connect-to
DO NOT ask browser act to "wait" for anything, the wait command is currently disabled in Stagehand.
When using
--connect-to
, viewport is only changed if
--viewport
is explicitly provided
Video recording is not available when using
--connect-to
Special
--connect-to
values:
current
: Use the existing page without reloading
reload-current
: Use the existing page and refresh it (useful in development)
Video Recording
All browser commands support video recording of the browser interaction in headless mode (not supported with --connect-to):
Use
--video=<directory>
to enable recording
Videos are saved at 1280x720 resolution in timestamped subdirectories
Recording starts when the browser opens and ends when it closes
Videos are saved as .webm files
Example:
#
Record a video of filling out a form
vibe-tools browser act
"
Fill out registration form with name John Doe
"
--url
"
http://localhost:3000/signup
"
--video=
"
./recordings
"
Console and Network Logging
Console logs and network activity are captured by default:
Use
--no-console
to disable console logging
Use
--no-network
to disable network logging
Logs are displayed in the command output
Complex Actions
The
act
command supports chaining multiple actions using the pipe (|) separator:
#
Login sequence with console/network logging (enabled by default)
vibe-tools browser act
"
Click Login | Type 'user@example.com' into email | Click Submit
"
--url
"
http://localhost:3000/login
"
#
Form filling with multiple fields
vibe-tools browser act
"
Select 'Mr' from title | Type 'John' into first name | Type 'Doe' into last name | Click Next
"
--url
"
http://localhost:3000/register
"
#
Record complex interaction
vibe-tools browser act
"
Fill form | Submit | Verify success
"
--url
"
http://localhost:3000/signup
"
--video=
"
./recordings
"
Troubleshooting Browser Commands
Common issues and solutions:
Element Not Found Errors
Use
--no-headless
to visually debug the page
Use
browser observe
to see what elements Stagehand can identify
Check if the element is in an iframe or shadow DOM
Ensure the page has fully loaded (try increasing
--timeout
)
Stagehand API Errors
Verify your OpenAI or Anthropic API key is set correctly
Check if you have sufficient API credits
Try switching models using
--model
Network Errors
Check your internet connection
Verify the target website is accessible
Try increasing the timeout with
--timeout
Check if the site blocks automated access
Video Recording Issues
Ensure the target directory exists and is writable
Check disk space
Video recording is not available with
--connect-to
Performance Issues
Use
--headless
mode for better performance (default)
Reduce the viewport size with
--viewport
Consider using
--connect-to
for development
Browser Installation Issues
Playwright browsers are automatically installed during
vibe-tools install
If browser installation fails, you can skip it by setting
SKIP_PLAYWRIGHT=1
and install manually
To manually install browsers:
npx playwright install chromium
Browser installation uses the exact Playwright version that vibe-tools depends on
YouTube Video Analysis
Use Gemini-powered YouTube video analysis to extract insights, summaries, and implementation plans:
#
Generate a video summary
vibe-tools youtube
"
https://www.youtube.com/watch?v=VIDEO_ID
"
--type=summary
#
Get a detailed transcript
vibe-tools youtube
"
https://www.youtube.com/watch?v=VIDEO_ID
"
--type=transcript
#
Create an implementation plan based on tutorial content
vibe-tools youtube
"
https://www.youtube.com/watch?v=VIDEO_ID
"
--type=plan
#
Ask specific questions about the video
vibe-tools youtube
"
https://www.youtube.com/watch?v=VIDEO_ID
"
"
How does the authentication flow work?
"
#
Save summary to a file
vibe-tools youtube
"
https://www.youtube.com/watch?v=VIDEO_ID
"
--type=summary --save-to=video-summary.md
The YouTube command leverages Gemini models' native ability to understand video content, enabling you to:
Extract key insights and summaries from technical talks, tutorials, and presentations
Generate complete transcripts of video content
Create implementation plans based on tutorial videos
Perform quality reviews of educational content
Get answers to specific questions about the video content
YouTube Command Options:
--type=<summary|transcript|plan|custom>
: Type of analysis to perform (default: summary)
Note:
The YouTube command requires a
GEMINI_API_KEY
to be set in your environment or .vibe-tools.env file as the Gemini API is currently the only interface that reliably supports YouTube video analysis.
Skills
GitHub Integration
Access GitHub issues and pull requests directly from the command line with rich formatting and full context:
#
List recent PRs or issues
vibe-tools github pr
vibe-tools github issue
#
View specific PR or issue with full discussion
vibe-tools github pr 123
vibe-tools github issue 456
The GitHub commands provide:
View of 10 most recent open PRs or issues when no number specified
Detailed view of specific PR/issue including:
PR/Issue description and metadata
Code review comments grouped by file (PRs only)
Full discussion thread
Labels, assignees, milestones and reviewers
Support for both local repositories and remote GitHub repositories
Markdown-formatted output for readability
Modular output filtering
with flags like
--review-only
,
--discussion-only
,
--metadata-only
,
--no-links
, and
--hide-resolved
for AI agent optimization
Authentication Methods:
The commands support multiple authentication methods:
GitHub token via environment variable:
GITHUB_TOKEN=your_token_here
GitHub CLI integration (if
gh
is installed and logged in)
Git credentials (stored tokens or Basic Auth)
Without authentication:
Public repositories: Limited to 60 requests per hour
Private repositories: Not accessible
With authentication:
Public repositories: 5,000 requests per hour
Private repositories: Full access (with appropriate token scopes)
Linear Integration
Access Linear issues directly from the command line with rich formatting and full context:
#
Set up authentication (interactive prompts)
vibe-tools linear connect
#
View specific issue with full details
vibe-tools linear get-issue ITE-123
vibe-tools linear issue ABC-456
#
Alternative command name
The Linear commands provide:
Authentication Setup
: Support for both personal API keys and OAuth2 flow with PKCE
Issue Details
: Complete issue information including:
Issue title, description, and status
Priority level and assignee information
Creation and update timestamps
Creator information
Comments
: Full discussion thread with timestamps and authors
Attachments
: List of attached files with links
Flexible Identifiers
: Support for both Linear identifiers (e.g.,
ITE-123
) and UUID format
Authentication Methods:
The Linear integration supports two authentication approaches:
Personal API Key
(Recommended for individual use):
Simple setup with guided browser navigation
Direct API key entry for existing keys
Choice of local or global storage
OAuth2 with PKCE
(Recommended for organizational use):
Secure browser-based authentication flow
Automatic token management
Enhanced security with PKCE (Proof Key for Code Exchange)
Authentication Setup:
Run the interactive setup command:
vibe-tools linear connect
This will guide you through:
Choosing between personal API key or OAuth authentication
Setting up browser access to Linear (if needed)
Configuring token storage (project-local vs global)
Environment Variable:
Alternatively, you can set the
LINEAR_API_KEY
environment variable in your
.vibe-tools.env
file:
LINEAR_API_KEY
=
"
your-linear-api-key
"
Note:
Linear personal API keys should be used directly without a "Bearer" prefix when set as environment variables.
Xcode Tools
Automate iOS app building, testing, and running in the simulator:
#
Available subcommands
vibe-tools xcode build
#
Build Xcode project and report errors
vibe-tools xcode run
#
Build and run app in simulator
vibe-tools xcode lint
#
Analyze code and offer to fix warnings
Build Command Options:
#
Specify custom build path (derived data)
vibe-tools xcode build buildPath=/custom/build/path
#
Specify target device
vibe-tools xcode build destination=
"
platform=iOS Simulator,name=iPhone 15
"
Run Command Options:
#
Run on iPhone simulator (default)
vibe-tools xcode run iphone
#
Run on iPad simulator
vibe-tools xcode run ipad
#
Run on specific device with custom build path
vibe-tools xcode run device=
"
iPhone 16 Pro
"
buildPath=/custom/build/path
The Xcode commands provide:
Automatic project/workspace detection
Dynamic app bundle identification
Build output streaming with error parsing
Simulator device management
Support for both iPhone and iPad simulators
Custom build path specification to control derived data location
Documentation Generation (uses Gemini 2.0)
Generate comprehensive documentation for your repository or any GitHub repository:
#
Document local repository and save to file
vibe-tools doc --save-to=docs.md
#
Document remote GitHub repository (both formats supported)
vibe-tools doc --from-github=username/repo-name@branch
vibe-tools doc --from-github=https://github.com/username/repo-name@branch
#
Save documentation to file (with and without a hint)
#
This is really useful to generate local documentation for libraries and dependencies
vibe-tools doc --from-github=eastlondoner/cursor-tools --save-to=docs/MY_DOCS.md
vibe-tools doc --from-github=eastlondoner/cursor-tools --save-to=docs/MY_DOCS.md --hint=
"
only information about the doc command
"
#
Document dependencies
vibe-tools doc --from-github=expressjs/express --save-to=docs/EXPRESS.md --quiet
#
Document with additional web documentation as context
vibe-tools doc --from-github=reactjs/react-redux --with-doc=https://redux.js.org/tutorials/fundamentals/part-5-ui-and-react --save-to=docs/REACT_REDUX.md
#
Document using multiple web documents as context
vibe-tools doc --from-github=some/repo --with-doc=https://example.com/spec1 --with-doc=https://example.com/spec2 --save-to=docs/MULTI_DOC.md
Wait Command
vibe-tools wait <seconds>
: Pauses execution for the specified number of seconds. Useful for simple timing needs within scripts or chained commands.
Configuration
vibe-tools.config.json
Customize
vibe-tools
behavior by creating a
vibe-tools.config.json
file. This file can be created either globally in
~/.vibe-tools/vibe-tools.config.json
or locally in your project root.
The vibe-tools.config file configures the local default behaviour for each command and provider.
Here is an example of a typical vibe-tools.config.json file, showing some of the most common configuration options:
{
// Commands
"repo"
: {
"provider"
:
"
openrouter
"
,
"model"
:
"
google/gemini-2.5-pro
"
},
"doc"
: {
"provider"
:
"
openrouter
"
,
"model"
:
"
anthropic/claude-sonnet-4
"
,
"maxTokens"
:
4096
},
"web"
: {
"provider"
:
"
gemini
"
,
"model"
:
"
gemini-2.5-pro
"
},
"plan"
: {
"fileProvider"
:
"
gemini
"
,
"thinkingProvider"
:
"
perplexity
"
,
"thinkingModel"
:
"
r1-1776
"
},
"browser"
: {
"headless"
:
false
},
//...
// Providers
"stagehand"
: {
"model"
:
"
claude-sonnet-4-20250514
"
,
// For Anthropic provider
"provider"
:
"
anthropic
"
,
// or "openai"
"timeout"
:
90000
},
"openai"
: {
"model"
:
"
gpt-4o
"
}
//...
}
For details of all configuration options, see
CONFIGURATION.md
. This includes details of all the configuration options and how to use them.
GitHub Authentication
The GitHub commands support several authentication methods:
Environment Variable
: Set
GITHUB_TOKEN
in your environment:
GITHUB_TOKEN
=
your_token_here
GitHub CLI
: If you have the GitHub CLI (
gh
) installed and are logged in, vibe-tools will automatically use it to generate tokens with the necessary scopes.
Git Credentials
: If you have authenticated git with GitHub (via HTTPS), vibe-tools will automatically:
Use your stored GitHub token if available (credentials starting with
ghp_
or
gho_
)
Fall back to using Basic Auth with your git credentials
To set up git credentials:
Configure git to use HTTPS instead of SSH:
git config --global url.
"
https://github.com/
"
.insteadOf git@github.com:
Store your credentials:
git config --global credential.helper store
#
Permanent storage
#
Or for macOS keychain:
git config --global credential.helper osxkeychain
The next time you perform a git operation requiring authentication, your credentials will be stored
Authentication Status:
Without authentication:
Public repositories: Limited to 60 requests per hour
Private repositories: Not accessible
Some features may be restricted
With authentication (any method):
Public repositories: 5,000 requests per hour
Private repositories: Full access (if token has required scopes)
vibe-tools will automatically try these authentication methods in order:
GITHUB_TOKEN
environment variable
GitHub CLI token (if
gh
is installed and logged in)
Git credentials (stored token or Basic Auth)
If no authentication is available, it will fall back to unauthenticated access with rate limits.
Repomix Configuration
When generating documentation, vibe-tools uses Repomix to analyze your repository. By default, it excludes certain files and directories that are typically not relevant for documentation:
Node modules and package directories (
node_modules/
,
packages/
, etc.)
Build output directories (
dist/
,
build/
, etc.)
Version control directories (
.git/
)
Test files and directories (
test/
,
tests/
,
__tests__/
, etc.)
Configuration files (
.env
,
.config
, etc.)
Log files and temporary files
Binary files and media files
You can customize the files and folders to exclude using two methods, both can be combined together:
Create a
.repomixignore
file
in your project root to specify files to exclude.
Example
.repomixignore
file for a Laravel project:
vendor/
public/
database/
storage/
.idea
.env
Create a
repomix.config.json
file
in your project root for more advanced configuration options:
Example
repomix.config.json
to enable compression and specify what to include:
{
"include"
: [
"
src/**/*
"
,
"
README.md
"
,
"
package.json
"
],
"output"
: {
"compress"
:
true
}
}
This configuration will be detected and used automatically by the
repo
,
plan
, and
doc
commands, allowing for precise control over which files are included in the repository analysis.
If both a .repomixignore and an ignore section in
repomix.config.json
are present then the ignore patterns from both are combined.
Model Selection
The
browser
commands support different AI models for processing from multiple providers (Anthropic, OpenAI, Gemini, OpenRouter). You can select the model using the
--model
option:
#
Use gpt-4o
vibe-tools browser act
"
Click Login
"
--url
"
https://example.com
"
--model=gpt-4o
#
Use Claude 4 Sonnet
vibe-tools browser act
"
Click Login
"
--url
"
https://example.com
"
--model=claude-sonnet-4-20250514
#
Use Gemini model
vibe-tools browser act
"
Click Login
"
--url
"
https://example.com
"
--model=gemini-2.5-flash
#
Use OpenRouter model
vibe-tools browser act
"
Click Login
"
--url
"
https://example.com
"
--model=groq-llama-3.3-70b-versatile
You can set a default provider in your
vibe-tools.config.json
file under the
stagehand
section:
{
"stagehand"
: {
"model"
:
"
claude-sonnet-4-20250514
"
,
// For Anthropic provider
"provider"
:
"
anthropic
"
,
// "openai", "gemini", or "openrouter"
"timeout"
:
90000
}
}
You can also set a default model in your
vibe-tools.config.json
file under the
stagehand
section:
{
"stagehand"
: {
"provider"
:
"
openai
"
,
// "anthropic", "gemini", or "openrouter"
"model"
:
"
gpt-4o
"
}
}
If no model is specified (either on the command line or in the config), a default model will be used based on your configured provider:
Anthropic:
anthropic/claude-sonnet-4-20250514
OpenAI:
o3-mini
Gemini:
gemini-2.5-flash
OpenRouter:
groq-llama-3.3-70b-versatile
Available models depend on your configured provider (OpenAI or Anthropic) in
vibe-tools.config.json
and your API key.
Cursor Configuration
vibe-tools
automatically configures Cursor by updating your project rules during installation. This provides:
Command suggestions
Usage examples
Context-aware assistance
For new installations, we use the recommended
.cursor/rules/vibe-tools.mdc
path. For existing installations, we maintain compatibility with the legacy
.cursorrules
file. If both files exist, we prefer the new path and show a warning.
Cursor Agent Configuration:
To get the benefits of vibe-tools you should use Cursor agent in "yolo mode". Ideal settings:
vibe-tools cli
In general you do not need to use the cli directly, your AI coding agent will call the CLI but it is useful to know it exists and this is how it works.
Command Options
All commands support these general options:
--model
: Specify an alternative model
--max-tokens
: Control response length
--reasoning-effort=<low|medium|high>
: Control the depth of reasoning for supported models (OpenAI o1/o3-mini models, Claude 4 Sonnet, and XAI Grok models). Higher values produce more thorough responses at the cost of increased token usage.
--save-to
: Save command output to a file (in addition to displaying it, like tee)
--quiet
: Suppress stdout output (only useful with --save-to)
--debug
: Show detailed error information
--provider
: AI provider to use. Valid values: openai, anthropic, perplexity, gemini, openrouter, modelbox, xai, groq
--web
: Enable web search capabilities for supported models (Gemini models, XAI Grok models, Perplexity models, and ModelBox models) across all commands
Documentation command specific options:
--from-github
: Generate documentation for a remote GitHub repository (supports @branch syntax)
--hint
: Provide additional context or focus for documentation generation
--with-doc=<doc_url>
: Fetch content from one or more document URLs and include it as additional context. Can be specified multiple times.
Repository command specific options:
--from-github=<GitHub username>/<repository name>[@<branch>]
: Analyze a remote GitHub repository without cloning it locally
--subdir=<path>
: Analyze a specific subdirectory instead of the entire repository
--with-doc=<doc_url>
: Fetch content from one or more web URLs and include it as context. Can be specified multiple times.
--with-diff
: Include git diff information along with repository context for focused code review
--base=<branch>
: Specify base branch for diff comparison (used with --with-diff)
Plan command specific options:
--fileProvider
: Provider for file identification (gemini, openai, anthropic, perplexity, modelbox, or openrouter)
--thinkingProvider
: Provider for plan generation (gemini, openai, anthropic, perplexity, modelbox, or openrouter)
--fileModel
: Model to use for file identification
--thinkingModel
: Model to use for plan generation
--fileMaxTokens
: Maximum tokens for file identification
--thinkingMaxTokens
: Maximum tokens for plan generation
--debug
: Show detailed error information
--with-doc=<doc_url>
: Fetch content from one or more web URLs and include it as context during plan generation. Can be specified multiple times.
GitHub command specific options:
--from-github=<GitHub username>/<repository name>[@<branch>]
: Access PRs/issues from a specific GitHub repository.
--repo
is an older, still supported synonym for this option.
--review-only
: Show only code review comments section (PRs only)
--discussion-only
: Show only discussion comments section
--metadata-only
: Show only PR/issue metadata (labels, assignees, etc.)
--no-links
: Hide all "View in GitHub" links from output
--hide-resolved
: Filter out resolved code review comments (PRs only)
Xcode command specific options:
For the build subcommand:
buildPath=<path>
: Set a custom derived data path
destination=<destination string>
: Set a custom simulator destination
For the run subcommand:
iphone
or
ipad
: Select device type
device=<device name>
: Specify a custom device
buildPath=<path>
: Set a custom derived data path
Browser command specific options:
--console
: Capture browser console logs (enabled by default, use
--no-console
to disable)
--html
: Capture page HTML content (disabled by default)
--network
: Capture network activity (enabled by default, use
--no-network
to disable)
--screenshot
: Save a screenshot of the page
--timeout
: Set navigation timeout (default: 120000ms for Stagehand operations, 30000ms for navigation)
--viewport
: Set viewport size (e.g., 1280x720)
--headless
: Run browser in headless mode (default: true)
--no-headless
: Show browser UI (non-headless mode) for debugging
--connect-to
: Connect to existing Chrome instance
--wait
: Wait after page load (e.g., 'time:5s', 'selector:#element-id')
--video
: Save a video recording (1280x720 resolution, timestamped subdirectory)
--url
: Required for
act
,
observe
, and
extract
commands. Url to navigate to on connection or one of the special values: 'current' (use existing page), 'reload-current' (refresh existing page).
--evaluate
: JavaScript code to execute in the browser before the main command
Execution Methods
Execute commands using:
vibe-tools
<
command
>
[options]
For example:
vibe-tools web
"
What's new in TypeScript 5.7?
"
Troubleshooting
Command Not Found
Ensure
vibe-tools
is installed globally using
npm install -g vibe-tools
Check your system's PATH environment variable to ensure it includes npm's global bin directory
On Unix-like systems, the global bin directory is typically
/usr/local/bin
or
~/.npm-global/bin
On Windows, it's typically
%AppData%\npm
Installation Hanging in CI/CD
For automated environments, ensure you set appropriate environment variables:
CI=true vibe-tools install
.
#
or
NONINTERACTIVE=true vibe-tools install
.
Set
SKIP_SETUP=true
to skip API key prompts if keys are already in environment
vibe-tools automatically detects CI environments and skips interactive prompts
API Key Errors
Verify
.vibe-tools.env
exists and contains valid API keys
Run
vibe-tools install
to reconfigure API keys
Check that your API keys have the necessary permissions
For GitHub operations, ensure your token has the required scopes (repo, read:user)
For Google Vertex AI authentication:
If using a JSON key file, verify the file path is correct and the file is readable
If using ADC, ensure you've run
gcloud auth application-default login
and the account has appropriate permissions
Verify your service account has the necessary roles in Google Cloud Console (typically "Vertex AI User")
For troubleshooting ADC: Run
gcloud auth application-default print-access-token
to check if ADC is working
For MCP commands ensure that
either
the
ANTHROPIC_API_KEY
or
the
OPENROUTER_API_KEY
are set.
If using OpenRouter for MCP, ensure
OPENROUTER_API_KEY
is set.
If a provider is not specified for an MCP command, Anthropic will be used by default.
Model Errors
Check your internet connection
Verify API key permissions
Ensure the specified model is available for your API tier
GitHub API Rate Limits
GitHub API has rate limits for unauthenticated requests. For higher limits you must be authenticated.
If you have the gh cli installed and logged in vibe-tools will use that to obtain a short lived auth token. Otherwise you can add a GitHub token to your environment:
GITHUB_TOKEN
=
your_token_here
Private repositories always require authentication
Documentation Generation Issues
Repository too large: Try using
--hint
to focus on specific parts
Token limit exceeded: The tool will automatically switch to a larger model
Network timeouts: The tool includes automatic retries
For very large repositories, consider documenting specific directories or files
Cursor Integration
If .cursorrules is outdated, run
vibe-tools install .
to update
Ensure Cursor is configured to allow command execution
Check that your Cursor version supports AI commands
Examples
Web Search Examples
#
Get information about new technologies
vibe-tools web
"
What are the key features of Bun.js?
"
#
Check API documentation
vibe-tools web
"
How to implement OAuth2 in Express.js?
"
#
Compare technologies
vibe-tools web
"
Compare Vite vs Webpack for modern web development
"
#
Use XAI Grok for web search with reasoning
vibe-tools web
"
What are the latest AI safety developments?
"
--provider xai --reasoning-effort high
Repository Context Examples
#
Architecture understanding
vibe-tools repo
"
Explain the overall architecture of this project
"
#
Find usage examples
vibe-tools repo
"
Show me examples of error handling in this codebase
"
#
Debugging help
vibe-tools repo
"
Why might the authentication be failing in the login flow?
"
#
Analyze specific subdirectory
vibe-tools repo
"
Explain the code structure
"
--subdir=src/components
#
Analyze remote GitHub repository
vibe-tools repo
"
Explain the architecture
"
--from-github=username/repo-name
#
Deep analysis with enhanced reasoning
vibe-tools repo
"
Analyze the security implications of our authentication implementation
"
--reasoning-effort high
#
Include web documentation as context
vibe-tools repo
"
Help me implement useState in my component
"
--with-doc=https://react.dev/reference/react/useState or a
local
file path
"
Direct Model Query Examples
#
Basic question
vibe-tools ask
"
What is the capital of France?
"
--provider openai --model o3-mini
#
Complex algorithm explanation with high reasoning effort
vibe-tools ask
"
Explain the quicksort algorithm and analyze its time complexity in different scenarios
"
--provider openai --model o3-mini --reasoning-effort high
#
Comparative analysis with Claude model and enhanced reasoning
vibe-tools ask
"
Compare and contrast microservices vs monolithic architecture
"
--provider anthropic --model claude-sonnet-4-20250514 --reasoning-effort medium
#
Advanced reasoning with XAI Grok model
vibe-tools ask
"
Analyze the philosophical implications of artificial general intelligence
"
--provider xai --model grok-4-latest --reasoning-effort high
#
Ask with context from multiple documents
vibe-tools ask
"
Based on these specs, what is the main goal?
"
--provider openai --model o3-mini --with-doc=./specA.txt --with-doc=https://example.com/specB.txt
#
Ask Groq's moonshotai/kimi-k2-instruct model
vibe-tools ask
"
Explain quantum computing
"
--provider groq --model moonshotai/kimi-k2-instruct
#
Ask Groq's qwen/qwen3-32b model
vibe-tools ask
"
Summarize the history of AI
"
--provider groq --model qwen/qwen3-32b
Documentation Examples
#
Document specific aspects and save to file without stdout output
vibe-tools doc --save-to=docs/api.md --quiet --hint=
"
Focus on the API endpoints and their usage
"
#
Document with hint to customize the docs output
vibe-tools doc --save-to=docs/architecture.md --quiet --hint=
"
Focus on system architecture
"
#
Document dependencies
vibe-tools doc --from-github=expressjs/express --save-to=docs/EXPRESS.md --quiet
#
Document with additional web documentation as context
vibe-tools doc --from-github=reactjs/react-redux --with-doc=https://redux.js.org/tutorials/fundamentals/part-5-ui-and-react --save-to=docs/REACT_REDUX.md
#
Document using multiple web documents as context
vibe-tools doc --from-github=some/repo --with-doc=https://example.com/spec1 --with-doc=./local-spec.md --save-to=docs/MULTI_DOC.md
GitHub Integration Examples
#
List PRs with specific labels
vibe-tools github pr --from-github facebook/react
#
Check recent issues in a specific repository
vibe-tools github issue --from-github vercel/next.js
#
View PR with code review comments
vibe-tools github pr 123 --from-github microsoft/typescript
#
Track issue discussions
vibe-tools github issue 456 --from-github golang/go
#
Show only code review comments (useful for agents)
vibe-tools github pr 123 --review-only
#
Show only discussion without code review noise
vibe-tools github pr 123 --discussion-only
#
Get just the metadata (labels, assignees, etc.)
vibe-tools github pr 123 --metadata-only
#
Hide GitHub links for cleaner agent output
vibe-tools github pr 123 --no-links
#
Hide resolved code review comments, show only active discussions
vibe-tools github pr 123 --review-only --hide-resolved
#
Combine flags for focused AI agent consumption
vibe-tools github pr 123 --review-only --no-links --hide-resolved
#
Include web documentation as context
vibe-tools repo
"
Help me implement useState in my component
"
--with-doc=./path/to/local/docs.md
#
Include multiple documents as context
vibe-tools repo
"
Summarize these two specifications
"
--with-doc=./spec1.md --with-doc=https://example.com/spec2.pdf
#
Git diff integration for code review
vibe-tools repo
"
Review my recent changes for potential issues
"
--with-diff
#
Compare changes against specific branch
vibe-tools repo
"
Check compatibility with main branch
"
--with-diff --base=main
#
Combine diff with external documentation for comprehensive review
vibe-tools repo
"
Does my implementation follow the API specification?
"
--with-diff --with-doc=./local-api-spec.md
Linear Integration Examples
#
Set up authentication interactively
vibe-tools linear connect
#
View specific Linear issue by identifier
vibe-tools linear get-issue ITE-1850
#
View issue using alternative command name
vibe-tools linear issue ABC-123
#
View issue by UUID (also supported)
vibe-tools linear get-issue 0b906a8e-f8a8-477d-9c98-0986b09ac5f9
Xcode Command Examples
#
Build an iOS app with default settings
vibe-tools xcode build
#
Build with custom derived data path
vibe-tools xcode build buildPath=
~
/custom/derived/data
#
Run in iPhone simulator
vibe-tools xcode run iphone
#
Run on specific iPad model
vibe-tools xcode run device=
"
iPad Pro (12.9-inch) (6th generation)
"
#
Analyze code quality
vibe-tools xcode lint
Browser Command Examples
open
subcommand examples:
#
Open a URL and get HTML
vibe-tools browser open
"
https://example.com
"
--html
#
Open and capture console logs and network activity
vibe-tools browser open
"
https://example.com
"
--console --network
#
Take a screenshot
vibe-tools browser open
"
https://example.com
"
--screenshot=page.png
#
Run in non-headless mode for debugging
vibe-tools browser open
"
https://example.com
"
--no-headless
act
,
extract
,
observe
subcommands examples:
#
AI-powered action
vibe-tools browser act
"
Click on 'Sign Up'
"
--url
"
https://example.com
"
#
AI-powered extraction
vibe-tools browser extract
"
Get the main content
"
--url
"
https://example.com/blog
"
#
AI-powered observation
vibe-tools browser observe
"
What can I do on this page?
"
--url
"
https://example.com
"
YouTube Command Examples
#
Generate a comprehensive summary of a technical talk
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--type=summary
#
Get a complete transcript with speaker annotations
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--type=transcript --save-to=transcript.md
#
Create an implementation plan from a coding tutorial
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--type=plan
#
Generate a critical review of a tutorial's accuracy and quality
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--type=review
#
Ask specific questions about video content
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
"
What libraries does the tutorial use for authentication?
"
#
Use a specific model for analysis
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--model=gemini-2.5-pro
#
Use custom analysis type for specialized insights
vibe-tools youtube
"
https://www.youtube.com/watch?v=dQw4w9WgXcQ
"
--type=custom
"
Extract all code examples and explain them in detail
"
Node Package Manager (npm)
vibe-tools is available on npm
here
Contributing
Contributions are welcome! Please feel free to submit a Pull Request. If you used vibe-tools to make your contribution please include screenshots or videos of vibe-tools in action.
Sponsors
Vinta.app
Optimise your Vinted accounting
with real-time analytics, inventory management, and tax compliance tools.
🔗
Start scaling your Vinted business today
Resoled.it
Automate your Vinted reselling business
with advanced tools like autobuy, custom snipers, and one-click relisting.
🔗
Take Vinted reselling to the next level
iterate.com
Build self-driving startups
with autonomous AI agents that run your company.
🔗
AI Engineer in London? Join the startup revolution
License
MIT License - see
LICENSE
for details.
