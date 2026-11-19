---
title: "Homework until 23 Nov, optional: More room for Claude Code"
---


You do not need this part for the course. It is for the day when one folder, one session or one API key is not
enough any more: then you know that there is a way, and where to find it.

### 12. Give Claude Code one more folder

Claude Code works in a sandbox, nono: a fence around Claude Code, as in the last homework
([Better safe than sorry](/abp/ws2/hw2-a/#better-safe-than-sorry)). Inside the fence, it works as it likes. Outside,
it can read nothing and change nothing. Usually, that is just right. But say you start a second website, and Claude
Code should take over the colours of your first one. Your first website is outside the fence.

<div class="quiz">

**Quiz.** Say Claude Code writes: "I cannot read `~/projects/my-first-project`. Type
<span class="cmd-i cmd-i-c">`/add-dir ~/projects/my-first-project`</span>, and I can." You type it. What happens?

<ul>
<li>Claude Code can now read your first website</li>
<li data-right>Claude Code still cannot read it</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**It still cannot.** Two things decide what Claude Code may read:

- **Claude Code's own list** of the folders that it works in. Outside them, it asks you first. <span class="cmd-i cmd-i-c">`/add-dir`</span> puts one
  more folder on the list.
- **The sandbox**, the fence. kingo sets it up when Claude Code starts, and nothing inside can move it: not Claude
  Code, not <span class="cmd-i cmd-i-c">`/add-dir`</span>, not your "yes".

So <span class="cmd-i cmd-i-c">`/add-dir`</span> changes only the list. Claude Code then tries to read the folder, and the sandbox says no:
`Operation not permitted` on a Mac, `Permission denied` on Windows. To give Claude Code one more folder, you start it
again, with that folder. Claude Code gives you the line for it.

</details>

</div>

<figure class="hx hx-box hx-fence" data-mode="adddir" aria-label="What /add-dir changes, and what --read changes"><div class="hx-switch" role="group" aria-label="What you type"><button type="button" data-mode="adddir" aria-pressed="true"><code>/add-dir ~/projects/my-first-project</code></button><button type="button" data-mode="start" aria-pressed="false"><code>kc ~/projects/my-second-project --read ~/projects/my-first-project</code></button></div><ul class="hx-tree"><li style="--i:0"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~/projects/my-second-project</code><small>where you started Claude Code</small><span class="acc adddir write"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg><span>reads and writes</span></span><span class="acc start write"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg><span>reads and writes</span></span></li><li style="--i:1"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~/projects/my-first-project</code><small>your first website</small><span class="acc adddir none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>blocked by the sandbox</span></span><span class="acc start read"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg><span>reads only</span></span></li><li style="--i:2"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~</code><small>your other folders</small><span class="acc adddir none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span><span class="acc start none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span></li></ul><p class="hx-pick" data-for="adddir">Typed into Claude Code: <code>/add-dir</code> puts your first website on Claude Code's own list. The sandbox stays as kingo set it up at the start, and says no: <code>Operation not permitted</code>.</p><p class="hx-pick" data-for="start">Typed into the terminal: kingo sets up the sandbox with your first website, and tells Claude Code too. Claude Code reads it, and cannot change it.</p></figure>

**For a file or two: copy them in.** For example, Claude Code shall read a report that is in your Downloads:

1. Open the folder where Claude Code works, as in step 10. For your first website on a Mac, paste this line into a
   second terminal tab:
   <div class="cmd cmd-terminal">

   ```
   open ~/projects/my-first-project
   ```

   </div>

   On Windows:
   <div class="cmd cmd-terminal">

   ```
   cd ~/projects/my-first-project && explorer.exe .
   ```

   </div>

2. Copy the file into this folder. Click the file where it is now, and press **Cmd+C** on a Mac or **Ctrl+C** on
   Windows. Then click into the folder that you opened, and press **Cmd+V** or **Ctrl+V**. On Windows, you can also
   drag the file from a Windows folder into it.
3. Tell Claude Code the name of the file, for example: "Read report.pdf in this folder, and tell me its three main
   points."

That is all: you do not start Claude Code again, and the fence stays as it is. Claude Code works with the copy.
Your file in Downloads stays as it is: Claude Code cannot read it or change it.

**Want to give access to an entire other folder? Then use `--read`.** **Your turn:** start a second website that reads your first one.

1. Make its folder. Is Claude Code still running? Type <span class="cmd-i cmd-i-c">`/exit`</span> first. Then paste this line into your terminal:
   <div class="cmd cmd-terminal">

   ```
   mkdir -p ~/projects/my-second-project
   ```

   </div>

2. Start Claude Code there, with your first website to read:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-second-project --read ~/projects/my-first-project
   ```

   </div>

   Before Claude Code starts, kingo names the folder that Claude Code may also read. You did not make the short
   commands of [Part E](/abp/ws2/hw3-e/)? Then go into `~/kingo-pod` first, and start it with
   <span class="cmd-i cmd-i-t">`./kingo claude --in ~/projects/my-second-project --read ~/projects/my-first-project`</span>.
3. Paste this prompt into Claude Code:
   <div class="cmd cmd-claude">

   ```
   Read my first website in ~/projects/my-first-project. Make a one-page website here about me, in the same colours and fonts. Ask me three questions about me first. You are done when index.html opens in a browser and looks like a sister of my first website. Look at both pages before you say that you are done.
   ```

   </div>

4. Test the fence. Paste:
   <div class="cmd cmd-claude">

   ```
   Change the title of my first website to "Hello".
   ```

   </div>

   Claude Code says that it cannot, or it asks for your OK: then say yes, and watch the sandbox say no. Claude Code
   may read your first website, not change it.

The folder is open for this one start. Start Claude Code without `--read`, and the fence is where it was before: no
folder stays open by accident.

Done: you gave Claude Code one more folder, and you saw the fence hold.

<details class="more">
<summary>Claude Code should change the files there, too?</summary>

Then start it with `--write` in place of `--read`. Claude Code may then read, change and delete everything in that
folder: give `--write` only to a folder that has a copy (step 8). In the course, for example, Claude Code can then
put a file where your Langflow flows find it: Langflow sees your folder `~/kingo-pod/shared` as `/app/shared`.

<div class="cmd cmd-terminal">

```
kc --write ~/kingo-pod/shared
```

</div>


</details>

**What kingo takes.** A folder inside your home folder, and not too much of it: not your home folder itself, not
Desktop, Documents, Downloads or Library as a whole, no hidden folder (there, programs keep their keys), no Windows
folder. A folder inside one of them is fine, also in Library: on a Mac, Dropbox, OneDrive and iCloud Drive keep their
files there. Is your file somewhere else? Copy it in, as above.

**Before you open a folder, ask two things.** Does Claude Code need all of it? And may these files go to the company
that runs the model? What Claude Code reads goes into the conversation, and with it out of your laptop (step 1).

**Next time.** When Claude Code needs files from elsewhere, copy them in, or start it with `--read` and the smallest
folder that holds them.

<span class="src">From nono's page on [Claude Code](https://nono.sh/docs/cli/clients/claude#overriding-profile-settings): "add extra
directory access", and from its
[security model](https://nono.sh/docs/cli/internals/security-model#capability-expansion-and-irreversibility): a
program in the sandbox "cannot expand its own kernel policy". Anthropic's page on
[permissions](https://code.claude.com/docs/en/permissions#working-directories): working directories and <span class="cmd-i cmd-i-c">`/add-dir`</span>.
kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>.</span>

[Stuck? Help for step 12](#step-12)

### 13. Work in two sessions at once

Claude Code can work in two terminal tabs at once: for example on your website in one tab, while you ask about your
flow in the other. Each tab is a session of its own, in a sandbox of its own.

**Your turn.** Open a second terminal tab ([how](/abp/ws2/hw3/#your-terminal-in-short)).

<details class="more newhere">
<summary>New here? What is different for you in 2 and 3</summary>

In 2, start the second session for your practice folder. Paste this line in place of the one there:

<div class="cmd cmd-terminal">

```
kc ~/projects/practice
```

</div>


In 3, ask it: "What does plan.md say?"

</details>

1. In the first tab, start Claude Code for your website:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project
   ```

   </div>

2. In the second tab, start it for the course:
   <div class="cmd cmd-terminal">

   ```
   kc
   ```

   </div>

3. Ask each one something different. Ask the one of the course, for example: "Which flows are in my Langflow?" Both
   answer, each on its own.

<div class="quiz">

**Quiz.** You ask both sessions to change the greeting of the same Langflow flow, at the same time. What happens?

<ul>
<li>The second session sees the first one at work, and waits</li>
<li data-right>The two do not know about each other: one change can be lost</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**One change can be lost.** Each session takes the flow, changes it, and puts the whole flow back. The one that comes
second puts back its own version, without the change of the first, and nobody gets a warning. So give each session
its own thing: its own folder, its own flow or workflow. Both should change one flow? Then one after the other.

</details>

</div>

<details class="more">
<summary>Do you use Git? Two sessions in one repository</summary>

Two sessions in one repository share more than the files: they share the branch, and each commit and each push.
So one session may commit or push the half-done work of the other.

- **The simple rule:** only one session commits and pushes. The other one only reads, or works in another folder.
- **Two tasks in one repository at the same time?** Give each session a worktree. A worktree is a second folder of
  the same repository, with its own files and its own branch. Each session changes only its own folder. When both
  are done, you bring the two branches together, as with any branch.

<span class="src">From Anthropic's page [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees): the page
also shows how to start one.</span>

</details>

**With your OpenRouter key: as many as you like.** You can start Claude Code in three tabs, in four, or in more:
open one more terminal tab, and start it there with <span class="cmd-i cmd-i-t">`kc`</span> and a folder. Each session is a conversation of its own:
it does not know what you said in the other tabs. All of them pay with your one OpenRouter key, and you pay for each
session. So the credit limit of your key counts for all of them together.

**With `--login`: one at a time.** kingo starts no second <span class="cmd-i cmd-i-t">`kcl`</span> while one runs: two at once break the login, because
of a bug in nono, the sandbox that keeps your login. For a second session at the same time, start it with <span class="cmd-i cmd-i-t">`kc`</span>, with
your OpenRouter key.

Done: two sessions at once, each with its own thing.

**Next time.** When you work in two sessions at once, give each its own folder or its own flow.

<span class="src">From Anthropic's page [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees): each session
gets a copy of its own, "so changes don't collide". kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--login`.</span>

[Stuck? Help for step 13](#step-13)

### 14. Use other API keys for Claude Code

**You decide where your data goes.** So far, every session sends the conversation to OpenRouter, and pays with one
key: in the course, the key from Yanbo. For the course, that is fine. Its data is made up.

Now imagine your mail AI assistant at work, with the mails of real customers. Step 1 showed what leaves your laptop:
the whole conversation, with every file that Claude Code read. All of it goes to the provider. The provider is the
service that runs the model, or that passes the conversation on to a server that does.

With another API key, a project can do three things:

- **Keep sensitive data with a provider that you trust.** For example an API that your company runs itself, or a
  model on your own laptop.
- **Use another provider**, for example Anthropic's API. Anthropic is the company that makes Claude Code and the
  Claude models.
- **Keep its costs apart.** A second OpenRouter key shows on openrouter.ai what this one project costs. It also gets
  a credit limit of its own. If Claude Code goes in circles, it stops at that limit, and your other key keeps its
  credit.

**Two lines, and you are done.** You add a key once. Then you start Claude Code with the key's name, as often as you
like. You choose the name. Pick one that says what the key is for, for example `trusted`.

You did not make the short commands of [Part E](/abp/ws2/hw3-e/)? Then go into `~/kingo-pod` first. Write <span class="cmd-i cmd-i-t">`./kingo claude --in`</span> in place
of <span class="cmd-i cmd-i-t">`kc`</span> when a folder follows, <span class="cmd-i cmd-i-t">`./kingo claude`</span> when no folder follows, and <span class="cmd-i cmd-i-t">`./kingo`</span> in place of <span class="cmd-i cmd-i-t">`kingo`</span>.

<details class="more newhere">
<summary>New here? What is different for you in this step</summary>

- You have no folder `~/projects/my-first-project`? Then write `~/projects/practice` in its place.
- You use your Claude subscription with `--login`, and you have no key? Then your subscription pays already: read
  this step, and try none of its lines.
- <span class="cmd-i cmd-i-t">`kc --key trusted`</span>, without a folder, is the start for the course. You do not need it.

</details>

**Once: add the key.** Paste this line into your terminal:

<div class="cmd cmd-terminal">

```
kingo key add
```

</div>


kingo now asks you a few short questions, one at a time:

1. **The name.** For example `trusted`. Use small letters, digits and `-`.
2. **The provider.** Type a number: `1` for OpenRouter, `2` for Anthropic's API, `3` for Ollama on your laptop, or
   `4` for any other provider. With `4`, kingo also asks for the address. Your provider gives you this address for
   Claude Code. It is often called `ANTHROPIC_BASE_URL`.
3. **The model.** Use the name that your provider gives it.
4. **How much the model can hold, in tokens.** kingo asks this only for Ollama and for an address. Your provider
   names the number. Press **Enter** if it is 200,000 or more.
5. **The key.** Paste it. You do not see it as you paste it: that is on purpose, so that nobody reads it over your
   shoulder. Ollama needs no key, so kingo skips this question.

Did you type something that kingo cannot use, such as a name with a space? Then kingo asks again. At the end, kingo
keeps it all on your laptop. Claude Code does not start yet.

**At every start: call its name.** Start Claude Code as you always do, and add `--key` and the name:

<div class="cmd cmd-terminal">

```
kc ~/projects/my-first-project --key trusted
```

</div>


Before Claude Code starts, kingo tells you where the model comes from, for example:
`Claude Code's model comes from https://trusted-api.example.com, with your key "trusted"`.

That is all: one line once, and one short line at every start.

**Your names at a glance.** The next line shows your names, each with its provider and its model. It never shows a
key's secret:

<div class="cmd cmd-terminal">

```
kingo key list
```

</div>


The next line shows your names too, and asks which one to delete. It deletes the key from your laptop only. At the
provider, the key stays as it was:

<div class="cmd cmd-terminal">

```
kingo key remove
```

</div>


**What to answer, provider by provider.** Open the one that you need.

<details class="more">
<summary>A provider that you trust, by its address</summary>

You need two things from your provider: a key and an address. Ask for the address "for Claude Code", or "for
`ANTHROPIC_BASE_URL`". The provider must speak Anthropic's Messages API: that is the language of Claude Code.

Your answers: a name such as `trusted`, then `4`, the address, the provider's name for the model, the number of
tokens, and the key.

- Does the address end in `/v1` or in `/v1/messages`? Paste it anyway. kingo cuts the ending off and tells you so:
  Claude Code adds it itself.
- kingo cannot test this key before the start. At your first question to Claude Code, you see whether it works.
- Your key, and everything that Claude Code sends, go to this address. So take only a provider that you trust.
- Some providers sign with a certificate of their own. Then <span class="cmd-i cmd-i-t">`kingo key help`</span> shows how to add it.

</details>

<details class="more">
<summary>A model on your own laptop, with Ollama</summary>

Ollama is a free program that runs models on your laptop. You need Ollama, and a model in it.

Your answers: a name such as `local`, then `3`, the name of your model (for example `qwen3.5`), and the number of
tokens. For Claude Code, Ollama asks for a model that holds 64,000 tokens or more. kingo asks for no key.

Start Ollama before you start Claude Code with <span class="cmd-i cmd-i-t">`kc ~/projects/my-first-project --key local`</span>.

The best part: the conversation stays on your laptop, and nobody sends you a bill.

</details>

<details class="more">
<summary>Anthropic's API</summary>

You need a key from platform.claude.com. There, your account has workspaces: each one keeps the use of one project
apart. Every account has one, the Default Workspace. When you make a key, you choose a workspace for it. kingo needs
a key for one workspace, not for all of them.

Your answers: a name such as `anthropic`, then `2`, then `sonnet` as the model, and the key.

- Sonnet is Anthropic's model for everyday coding. If you press **Enter** instead, Claude Code takes Opus: a larger
  model that costs more.
- kingo keeps the key only if Anthropic accepts it.
- In Claude Code, <span class="cmd-i cmd-i-c">`/model haiku`</span> switches to Haiku, Anthropic's fast model for simple tasks. <span class="cmd-i cmd-i-c">`/model sonnet`</span>
  switches back.

Do you have a Claude Pro or Max subscription? Then the subscription is usually cheaper. It has a fixed price per
month, and Claude Code is included, up to the limits of your plan.
[Use your Claude subscription](/abp/ws2/s2-model/#use-your-claude-subscription) shows how.

</details>

<details class="more">
<summary>A second OpenRouter key</summary>

The key from Yanbo is for the course. For a project of your own, you can make your own key:

1. On [openrouter.ai](https://openrouter.ai), make an account and add credits. You pay for these credits yourself,
   so this is your choice.
2. Open Settings, then Keys, and make a key.
3. Give the key a credit limit. The key stops at that amount.

Your answers: a name such as `website`, then `1`, then **Enter** for the course's model, and the key. kingo keeps
the key only if OpenRouter accepts it.

</details>

**About the name.**

- **What is the name?** A word that you choose, just for kingo. It can differ from the key's name on the provider's
  website, but the same name is the easiest to remember. Under the name, kingo keeps three things: the key, its
  provider, and its model.
- **Where does kingo keep all this?** On your laptop, in the folder `~/.config/kingo/`. This folder is outside the
  sandbox, so Claude Code cannot read your key.
- **Does the name live in my project?** No. kingo writes nothing about the key into your project folder. The name
  belongs to your laptop.
- **Can I use one name for many projects?** Yes. Write another folder in the line, and the same key pays there.
  Without a folder, <span class="cmd-i cmd-i-t">`kc --key trusted`</span> starts Claude Code for the course with this key. Your flows in Langflow keep
  their own key.
- **What if I forget `--key`?** Then your first OpenRouter key pays, as before. A project does not remember its
  name, so add `--key` and the name at every start.
- **Can I change a name later?** Yes, its model and its key. Paste <span class="cmd-i cmd-i-t">`kingo key add`</span> and give the same name. kingo
  asks for the new model and the new key, and **Enter** keeps the old one. The provider cannot change: one name, one
  provider. For another provider, take another name.
- **And my first OpenRouter key?** <span class="cmd-i cmd-i-t">`kingo key add --first`</span> puts a new key in its place. The old key stays until
  OpenRouter accepts the new one.
- **Does this work with `--login`?** No. `--login` uses your Claude subscription, and `--key` uses a key. kingo
  takes one of the two.

Done: you decide which provider gets the conversation of each project.

**Next time.** Before Claude Code reads sensitive data in a project, give the project a key for a provider that you
trust.

<span class="src">From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--key`, and <span class="cmd-i cmd-i-t">`./kingo key help`</span>. Anthropic's page [Data usage](https://code.claude.com/docs/en/data-usage): to work with
the model, "Claude Code sends data over the network. This data includes all user prompts and model outputs".
OpenRouter's page on [limits](https://openrouter.ai/docs/api/reference/limits): "Per-key credit limits", and what each key used.
Anthropic's pages [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication): "Select a
workspace"; [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces): "Every organization has a
Default Workspace"; [Model configuration](https://code.claude.com/docs/en/model-config): the names `sonnet`, `opus` and
`haiku`, and that Claude Code with the Anthropic API "defaults to Opus 5.5";
[Manage costs effectively](https://code.claude.com/docs/en/costs): subscribers "have usage included in their
subscription", and "Sonnet handles most coding tasks well and costs less than Opus";
[Connect Claude Code to an LLM gateway](https://code.claude.com/docs/en/llm-gateway-connect): its test request goes
to the address of `ANTHROPIC_BASE_URL` plus `/v1/messages`. Ollama's page
[Claude Code](https://docs.ollama.com/integrations/claude-code): "64k+ context window".</span>

[Stuck? Help for step 14](#step-14)

<details class="more help" id="help">
<summary>If something goes wrong</summary>

Find your step.

#### Step 12

| What you see | What to do |
|---|---|
| `Operation not permitted` (Mac) or `Permission denied` (Windows), when Claude Code reads or changes a folder | The folder is outside the sandbox, or open for reading only. <span class="cmd-i cmd-i-c">`/add-dir`</span> does not help here. Type <span class="cmd-i cmd-i-c">`/exit`</span>, and start Claude Code again with `--read` (or `--write`) and the folder. |
| `unknown option '--read'` | Your kingo-pod is older than this step. Paste <span class="cmd-i cmd-i-t">`kingo update`</span>, or <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo update`</span>, and start again. New here? Paste <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && git pull`</span>. |
| kingo says the folder is too wide | Make a folder inside it for what Claude Code needs, for example <span class="cmd-i cmd-i-t">`mkdir -p ~/Documents/for-claude`</span>, move the files there, and give that folder. |
| kingo says that there is no such folder | Check its name with <span class="cmd-i cmd-i-t">`ls`</span>. Or make it first: <span class="cmd-i cmd-i-t">`mkdir -p`</span> and the folder. |

#### Step 13

| What you see | What to do |
|---|---|
| kingo says that another <span class="cmd-i cmd-i-t">`./kingo claude --login`</span> is running | Only one session with `--login` runs at a time. Type <span class="cmd-i cmd-i-c">`/exit`</span> in the other one first, or start this one with <span class="cmd-i cmd-i-t">`kc`</span>, with your OpenRouter key. No other session runs? Then paste the line `rm …` that kingo names. |

#### Step 14

| What you see | What to do |
|---|---|
| `unknown option '--key'`, or `unknown option '--provider'` | Your kingo-pod is older than this step. Paste <span class="cmd-i cmd-i-t">`kingo update`</span>, or <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo update`</span>, and start again. New here? Paste <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && git pull`</span>. |
| `unknown command 'key'`, after <span class="cmd-i cmd-i-t">`kingo key add`</span> | Your kingo-pod is older than this step: it does not know <span class="cmd-i cmd-i-t">`kingo key`</span> yet. Update it, as in the line above. |
| Before Claude Code starts, kingo prints no line that begins with `Claude Code's model` | You left `--key` out, so your first OpenRouter key pays. A project does not remember its name: type <span class="cmd-i cmd-i-c">`/exit`</span>, and start again with `--key` and the name. |
| `OpenRouter did not accept …`, or `Anthropic did not accept …` | kingo kept no key that the provider refused, and your other keys stay. Check the key on the provider's website (openrouter.ai: Settings, Keys; platform.claude.com: API keys), or make a new one. Then paste <span class="cmd-i cmd-i-t">`kingo key add`</span> again, with the same name: kingo asks for the key. |
| With Anthropic's API, Claude Code shows an error that names `anthropic-workspace-id` | Your key is not for one workspace. On platform.claude.com, make a new key, and choose one workspace for it. Then paste <span class="cmd-i cmd-i-t">`kingo key add`</span> into your terminal, and give the same name: kingo asks for the new key, and puts it in the place of the old one. |
| `The key "website" is for OpenRouter, not for Anthropic's API` | A name belongs to one provider. Take another name for the other provider, and paste <span class="cmd-i cmd-i-t">`kingo key add`</span> again. |
| `Ollama does not answer on this laptop` | Start Ollama, then start again. On Windows, Ollama must run in Ubuntu, where kingo runs. |
| With a provider's address, Claude Code shows an error at your first question, for example with the number `404` | Check the address with your provider: it is the one for `ANTHROPIC_BASE_URL`. A name keeps its address. For another address, take a new name, or paste <span class="cmd-i cmd-i-t">`kingo key remove`</span>, delete the name, and add it again with <span class="cmd-i cmd-i-t">`kingo key add`</span>. |
| You want another key under a name | Paste <span class="cmd-i cmd-i-t">`kingo key add`</span> into your terminal, and give the name: kingo asks for the new key. Your first OpenRouter key has no name: for it, paste <span class="cmd-i cmd-i-t">`kingo key add --first`</span>. |
| You do not know your names any more | Paste <span class="cmd-i cmd-i-t">`kingo key list`</span> into your terminal. It shows each name with its provider and its model, and never a key's secret. |

</details>
