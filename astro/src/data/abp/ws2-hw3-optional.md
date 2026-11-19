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

### 14. Give a project a key of its own

So far, all your sessions pay with one OpenRouter key. In the course, it is the key that Yanbo gave you. One key
means one credit and one sum for everything: the course, your website, and every other project.

**Make a key of your own.** The key from Yanbo is for the course. For a project of your own, make your own key: then
you see on openrouter.ai what the project costs, and you set its limit yourself. On
[openrouter.ai](https://openrouter.ai), make an account and add credits. Then open Settings, then Keys, make a key,
and give it a credit limit: the key stops at that amount. You pay for these credits yourself, so this is your choice.

kingo has one command to give a project such a key. You start Claude Code as you know it, and you add `--key` and a
name: <span class="cmd-i cmd-i-t">`kc ~/projects/my-first-project --key website`</span>. Then the key with the name `website` pays for this session,
and not your first key. Before Claude Code starts, kingo says so:
`Claude Code's model is paid with your OpenRouter key "website"`. This gives you three things:

- **You see what this project costs.** OpenRouter counts for each key what it used.
- **The project gets a credit limit of its own.** When Claude Code goes in circles in this project, it stops at
  that amount, and the credit of your other key stays.
- **The project can use another provider.** A provider is the service that Claude Code sends the conversation to.
  It runs the model itself, or it passes the conversation on to a server that does. In the course, the provider is
  OpenRouter. With a key of its own, a project can use another one: for example Anthropic's API, or a model on your
  own laptop. Anthropic is the company that makes Claude Code and the Claude models.

**The command, piece by piece.** In its longest form, it has four pieces:

| You write | What it means |
|---|---|
| <span class="cmd-i cmd-i-t">`kc ~/projects/my-first-project`</span> | Start Claude Code in this folder, as before. |
| `--key website` | The key with the name `website` pays. You choose the name. |
| `--provider anthropic` | Which provider: `anthropic` is Anthropic's API, `ollama` is a model on your laptop, and an address that starts with `https://` is any other provider. For OpenRouter, you leave this piece out. |
| `--model sonnet` | Which model. For OpenRouter and for Anthropic's API, you can leave this piece out: then you get their usual model. |

You did not make the short commands of [Part E](/abp/ws2/hw3-e/)? Then go into `~/kingo-pod` first. Write <span class="cmd-i cmd-i-t">`./kingo claude --in`</span> in place
of <span class="cmd-i cmd-i-t">`kc`</span> when a folder follows, <span class="cmd-i cmd-i-t">`./kingo claude`</span> when no folder follows, and <span class="cmd-i cmd-i-t">`./kingo`</span> in place of <span class="cmd-i cmd-i-t">`kingo`</span>.

**About the name.**

- **What is the name?** A word that you choose: small letters, digits and `-`. It is kingo's name for the key. It
  need not be the name that the key has on the provider's website, but the same name is the easiest to remember.
- **What does kingo keep under a name?** Three things: the key, its provider, and its model. The first start with a
  new name asks for the key, and takes the provider and the model from your line. From then on, `--key` and the name
  are enough.
- **Where does kingo keep them?** On your laptop, in the folder `~/.config/kingo/`, with your other keys. This
  folder is outside the sandbox: Claude Code cannot read your key. <span class="cmd-i cmd-i-t">`kingo claude key list`</span> shows your names, and
  never a key.
- **Does the name live in my project?** No. kingo writes nothing about the key into your project folder. The name
  belongs to your laptop, not to one project.
- **Can I use a name again?** Yes, for every folder: write another folder in the line, and the same key pays there.
  Without a folder, <span class="cmd-i cmd-i-t">`kc --key website`</span> starts Claude Code for the course with this key; your flows in Langflow keep
  the key that they have.
- **What if I leave `--key` out?** Then the start is as before, and your first OpenRouter key pays. A project does
  not remember its name: write `--key` and the name at every start of this project.
- **Can I change what is under a name?** The model, yes: write `--model` again. The key, yes:
  <span class="cmd-i cmd-i-t">`kingo claude key add website`</span> asks whether another key shall take its place. The provider, no: one name, one
  provider. For a key at another provider, take another name.
- **And my first OpenRouter key?** <span class="cmd-i cmd-i-t">`kingo claude key add --first`</span> puts another key in its place. Your first key
  stays until OpenRouter has accepted the new one.
- **Does it work with `--login`?** No. `--login` uses your Claude subscription, and `--key` uses a key: kingo takes
  one of the two.

**Your keys without a start.** kingo also takes care of your keys when no Claude Code starts. So you can add a key
once, and start every project with the short line, `--key` and the name:

| You write | What it does |
|---|---|
| <span class="cmd-i cmd-i-t">`kingo claude key add website`</span> | It asks for the key and keeps it under the name, as the first start with `--key` does. `--provider` and `--model` go with it. No Claude Code starts. |
| <span class="cmd-i cmd-i-t">`kingo claude key list`</span> | It shows your names, each with its provider and its model. It never shows a key. |
| <span class="cmd-i cmd-i-t">`kingo claude key remove website`</span> | It deletes the key of this name from your laptop, with its provider and its model. At the provider, the key is as it was. |

**Three examples.** Each one starts with something that you already have: a key, or a model on your laptop. In
examples 2 and 3, write your own model and your own address into the line before you press **Enter**.

<details class="more newhere">
<summary>New here? What is different for you in the examples</summary>

- You have no folder `~/projects/my-first-project`? Then write `~/projects/practice` in its place.
- You use your Claude subscription with `--login`, and you have no key? Then your subscription pays already: read
  the examples, and try none.
- <span class="cmd-i cmd-i-t">`kc --key website`</span>, without a folder, is the start for the course. You do not need it.

</details>

**Example 1: a key for Anthropic's API.** You have a key from platform.claude.com. A workspace is a part of your
account there that keeps the use of one project apart; every account has one, the Default Workspace. You choose
the workspace when you make a key. The key must be for one workspace: kingo cannot use a key for all workspaces.

<div class="cmd cmd-terminal">

```
kc ~/projects/my-first-project --key api --provider anthropic --model sonnet
```

</div>


kingo asks for the key: `Paste the Anthropic API key "api"`. Then it says where the model comes from:
`Claude Code's model comes from Anthropic's API, paid with your key "api"`, and `The model: sonnet`. Sonnet is
Anthropic's model for everyday coding. Without `--model`, Claude Code takes Opus, a larger model that costs more.
In Claude Code, <span class="cmd-i cmd-i-c">`/model haiku`</span> changes to Haiku, Anthropic's fast model for simple tasks, and <span class="cmd-i cmd-i-c">`/model sonnet`</span>
changes back.

**You have a Claude Pro or Max subscription? Then the subscription is usually the cheaper way.** It has a fixed price
per month, and Claude Code is included, up to the limits of your plan.
[Use your Claude subscription](/abp/ws2/s2-model/#use-your-claude-subscription) shows how.

**Example 2: a model on your own laptop.** You have Ollama, a program that runs models on your laptop, and a model
in it. Ollama needs no key, so kingo asks for none: here, the name stands for the provider and the model. Start
Ollama first, and write the name of your model in place of `qwen3.5`:

<div class="cmd cmd-terminal">

```
kc ~/projects/my-first-project --key local --provider ollama --model qwen3.5
```

</div>


kingo says: `Claude Code's model comes from Ollama on this laptop ("local")`. The model runs on your laptop, so no
provider bills you. For Claude Code, Ollama asks for a model with a context window of 64,000 tokens or more. Your
model holds fewer than 200,000 tokens? Then tell kingo once, with your number:
<span class="cmd-i cmd-i-t">`kingo claude key add local --context 64000`</span>. kingo keeps the number with the name, and Claude Code keeps the
conversation below it.

**Example 3: a key from another provider, by its address.** You have a key from a provider that you trust, and the
address that this provider names for Claude Code. It works when the provider offers Anthropic's Messages API, the
format that Claude Code speaks. You write the address in place of a provider's name, and you name the model. In
this line, write the address of your provider and its name for the model in place of ours:

<div class="cmd cmd-terminal">

```
kc ~/projects/my-first-project --key work --provider https://yourtrustedkey.example.com --model big-model
```

</div>


The address is the one that the provider names for `ANTHROPIC_BASE_URL`. It ends in `/v1` or in `/v1/messages`?
kingo leaves this ending out, and says so: Claude Code adds `/v1/messages` itself. kingo asks for the key:
`Paste the key "work" for https://yourtrustedkey.example.com`. kingo cannot check this key before the start. Your
key, and everything that Claude Code sends to the model, go to this address: take only a provider that you trust.

Some providers need two more things, and <span class="cmd-i cmd-i-t">`kingo claude key add`</span> takes them: `--context` and a number of tokens,
when the model holds fewer than 200,000 tokens, and `--ca` and a file, when the provider signs with a certificate of
its own. <span class="cmd-i cmd-i-t">`kingo claude key help`</span> shows both.

We tested the three examples with a stand-in for the provider: not yet with a real key of Anthropic, a real Ollama,
or a real provider.

**Next time.** When you start a project that may cost more than a little, give it a key of its own first.

<span class="src">From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--key`, `--provider`, `--model` and `key`. OpenRouter's page on
[limits](https://openrouter.ai/docs/api/reference/limits): "Per-key credit limits", and what each key used.
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
| <span class="cmd-i cmd-i-t">`kingo claude key list`</span> starts Claude Code, or kingo says `n8n and Langflow must be running first` | Your kingo-pod is older than this step: it does not know `key` yet. Update it, as in the line above. |
| Before Claude Code starts, kingo prints no line that begins with `Claude Code's model` | You left `--key` out, so your first OpenRouter key pays. A project does not remember its name: type <span class="cmd-i cmd-i-c">`/exit`</span>, and start again with `--key` and the name. |
| `OpenRouter did not accept the key "website"`, or `Anthropic did not accept the key "api"` | kingo deleted this key, and no other. Check it on the provider's website (openrouter.ai: Settings, Keys; platform.claude.com: API keys), or make a new one. Then start again with `--key` and the name: kingo asks for the key. |
| With Anthropic's API, Claude Code shows an error that names `anthropic-workspace-id` | Your key is not for one workspace. On platform.claude.com, make a new key, and choose one workspace for it. Then paste <span class="cmd-i cmd-i-t">`kingo claude key add api`</span> into your terminal: kingo asks for the new key, and puts it in the place of the old one. |
| `The key "website" is for OpenRouter, not for Anthropic's API` | A name belongs to one provider. Take another name for the other provider, for example `--key api --provider anthropic`. |
| `Ollama does not answer on this laptop` | Start Ollama, then start again. On Windows, Ollama must run in Ubuntu, where kingo runs. |
| With a provider's address, Claude Code shows an error at your first question, for example with the number `404` | Check the address with your provider: it is the one for `ANTHROPIC_BASE_URL`. A name keeps its address. For another address, take a new name, or paste <span class="cmd-i cmd-i-t">`kingo claude key remove work`</span> into your terminal and start again with the whole line: kingo asks for the key. |
| You want another key under a name | Paste <span class="cmd-i cmd-i-t">`kingo claude key add website`</span> into your terminal, with your name in place of `website`: kingo asks for the new key. Your first OpenRouter key has no name: for it, paste <span class="cmd-i cmd-i-t">`kingo claude key add --first`</span>. |
| You do not know your names any more | Paste <span class="cmd-i cmd-i-t">`kingo claude key list`</span> into your terminal. It shows each name with its provider and its model, and never a key. |

</details>
