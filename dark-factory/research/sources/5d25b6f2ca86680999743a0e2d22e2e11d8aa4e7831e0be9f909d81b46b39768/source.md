# Usage

Run `aider` with the source code files you want to edit.
These files will be “added to the chat session”, so that
aider can see their
contents and edit them for you.
They can be existing files or the name of files you want
aider to create for you.

```
aider <file1> <file2> ...
```

At the aider `>` prompt, ask for code changes and aider
will edit those files to accomplish your request.

```
$ aider factorial.py

Aider v0.37.1-dev
Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo
Git repo: .git with 258 files
Repo-map: using 1024 tokens
Use /help to see in-chat commands, run with --help to see cmd line args
───────────────────────────────────────────────────────────────────────
> Make a program that asks for a number and prints its factorial

...
```

Use `/help <question>` to
[ask for help about using aider](/docs/troubleshooting/support.html "/docs/troubleshooting/support.html"),
customizing settings, troubleshooting, using LLMs, etc.

## Adding files

To edit files, you need to “add them to the chat”.
Do this
by naming them on the aider command line.
Or, you can use the in-chat
`/add` command to add files.

Only add the files that need to be edited for your task.
Don’t add a bunch of extra files.
If you add too many files, the LLM can get overwhelmed
and confused (and it costs more tokens).
Aider will automatically
pull in content from related files so that it can
[understand the rest of your code base](https://aider.chat/docs/repomap.html "https://aider.chat/docs/repomap.html").

You can use aider without adding any files,
and it will try to figure out which files need to be edited based
on your requests.

You’ll get the best results if you think about which files need to be
edited. Add **just** those files to the chat. Aider will include
relevant context from the rest of your repo.

## LLMs

Aider works best with Claude 3.5 Sonnet, DeepSeek R1 & Chat V3, OpenAI o1, o3-mini & GPT-4o. Aider can [connect to almost any LLM, including local models](https://aider.chat/docs/llms.html "https://aider.chat/docs/llms.html").

```
# o3-mini
$ aider --model o3-mini --api-key openai=<key>

# Claude 3.7 Sonnet
$ aider --model sonnet --api-key anthropic=<key>
```

Or you can run `aider --model XXX` to launch aider with
another model.
During your chat you can switch models with the in-chat
`/model` command.

## Making changes

Ask aider to make changes to your code.
It will show you some diffs of the changes it is making to
complete you request.
[Aider will git commit all of its changes](/docs/git.html "/docs/git.html"),
so they are easy to track and undo.

You can always use the `/undo` command to undo AI changes that you don’t
like.

---

## Table of contents

* [Tips](/docs/usage/tips.html "/docs/usage/tips.html")
* [In-chat commands](/docs/usage/commands.html "/docs/usage/commands.html")
* [Chat modes](/docs/usage/modes.html "/docs/usage/modes.html")
* [Tutorial videos](/docs/usage/tutorials.html "/docs/usage/tutorials.html")
* [Voice-to-code with aider](/docs/usage/voice.html "/docs/usage/voice.html")
* [Images & web pages](/docs/usage/images-urls.html "/docs/usage/images-urls.html")
* [Prompt caching](/docs/usage/caching.html "/docs/usage/caching.html")
* [Aider in your IDE](/docs/usage/watch.html "/docs/usage/watch.html")
* [Notifications](/docs/usage/notifications.html "/docs/usage/notifications.html")
* [Aider in your browser](/docs/usage/browser.html "/docs/usage/browser.html")
* [Specifying coding conventions](/docs/usage/conventions.html "/docs/usage/conventions.html")
* [Copy/paste with web chat](/docs/usage/copypaste.html "/docs/usage/copypaste.html")
* [Linting and testing](/docs/usage/lint-test.html "/docs/usage/lint-test.html")
* [Editing config & text files](/docs/usage/not-code.html "/docs/usage/not-code.html")
