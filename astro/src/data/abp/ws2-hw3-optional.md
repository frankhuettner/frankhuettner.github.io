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

So far, all your sessions pay with one OpenRouter key. On openrouter.ai, you see one sum for everything: the course,
your website, and every other project.

Give a project a key of its own. This gives you three things:

- **You see what this project costs.** OpenRouter counts for each key what it used.
- **The project gets a credit limit of its own.** When Claude Code goes in circles in this project, it stops at
  that amount, and the credit of your other key stays.
- **The project can use another provider.** A provider is the company, or the program, that runs the model. In the
  course, the provider is OpenRouter. A project with a key of its own can use another one, for example Anthropic's
  API: Anthropic is the company that makes Claude Code and the Claude models.

**Your turn: a key with the name `website`, for your first website.** Pick one provider, and follow its lines.

<details class="more newhere">
<summary>New here? What is different for you in this step</summary>

- You use your Claude subscription, with `--login`? A subscription does not pay for a key: a key is paid per use, at
  OpenRouter or at Anthropic's API. Without such an account, read this step, and skip the rest.
- You have no folder `~/projects/my-first-project`? Then take your practice folder in 2: write
  `~/projects/practice` in its place.
- Below, <span class="cmd-i cmd-i-t">`kc --key website`</span> is the start for the course. You do not need it.

</details>

1. Make the key, in your browser.
   - **OpenRouter:** open openrouter.ai, and sign in. Open **Settings**, then **Keys**, and make a new key. Name it
     `website`, and give it a small credit limit.
   - **Anthropic's API:** open platform.claude.com, and sign in. Open **API keys**, and click **Create key**. Name it
     `website`, and choose one workspace for it, for example Default: kingo needs a key for one workspace. The API is
     paid per use, with credit of its own: a Claude Pro or Max subscription does not pay for it.

   Copy the key: you see it only once.
2. Is Claude Code still running in your terminal? Type <span class="cmd-i cmd-i-c">`/exit`</span> first. Then start Claude Code for your website, with
   `--key` and the name of the key. With an OpenRouter key:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project --key website
   ```

   </div>

   With a key for Anthropic's API, say the provider too:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project --key website --provider anthropic
   ```

   </div>

   The name is for kingo: small letters, digits and `-`. It can be any name, but the same name as on the provider's
   website is the easiest to remember. You did not make the short commands of [Part E](/abp/ws2/hw3-e/)? Then go into `~/kingo-pod`
   first, and write <span class="cmd-i cmd-i-t">`./kingo claude --in`</span> in place of <span class="cmd-i cmd-i-t">`kc`</span>.
3. kingo asks for the key: `Paste the OpenRouter key "website"`, or `Paste the Anthropic API key "website"`. Paste
   the key that you copied in 1, and press **Enter**. kingo keeps it with your other keys, outside the sandbox.
4. Look at the lines before Claude Code starts. kingo says where the model comes from:
   - **OpenRouter:** `Claude Code's model is paid with your OpenRouter key "website"`. The model is the course's,
     as before.
   - **Anthropic's API:** `Claude Code's model comes from Anthropic's API, paid with your key "website"`, and
     `The model: Claude Code picks one of Anthropic's`. Type <span class="cmd-i cmd-i-c">`/model`</span> in Claude Code to pick another one.
5. Ask Claude Code something, for example: "What is in this folder?" Then look at your key in the browser again: on
   openrouter.ai, **Keys** shows what the key `website` used.
6. Type <span class="cmd-i cmd-i-c">`/exit`</span>, and start again with the short line:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project --key website
   ```

   </div>

   This time, kingo does not ask. It kept the key under this name, and the provider with it: the short line is
   enough for Anthropic's API too.

Four more things to know:

- **Without `--key`, nothing changed.** Start Claude Code as before, and your first OpenRouter key pays, as before.
- **`--key` works in the course too.** <span class="cmd-i cmd-i-t">`kc --key website`</span> starts Claude Code for the course, with the key `website`.
  Your flows in Langflow keep the key that they have.
- **One name, one provider.** The name `website` now belongs to its provider. For a key at another provider, take
  another name, for example `website-api`.
- **Not with `--login`.** `--login` uses your Claude subscription, and `--key` a key that is paid per use: kingo
  takes one of the two.

<details class="more">
<summary>Another model, a model on your own laptop, or another provider</summary>

**Another model.** `--model` and the ID of a model go with `--key`. kingo keeps the model with the name, like the
provider. With Anthropic's API, for example:

<div class="cmd cmd-terminal">

```
kc ~/projects/my-first-project --key website --model claude-sonnet-5-5
```

</div>


With an OpenRouter key, the ID is the one on the model's page on openrouter.ai. In the course, your OpenRouter key
works only for the course's models.

**A model on your own laptop.** Ollama is a program that runs models on your laptop. It needs no key: the name
stands for the provider and the model. Start Ollama first. Then, with a model that you have in Ollama:

<div class="cmd cmd-terminal">

```
kc ~/projects/practice --key local --provider ollama --model qwen3.5
```

</div>


For Claude Code, Ollama asks for a model with a context window of 64,000 tokens or more.

**Another provider.** It works when the provider offers Anthropic's Messages API, the format that Claude Code
speaks. Give its address, the one that the provider names for `ANTHROPIC_BASE_URL`, and a model:

<div class="cmd cmd-terminal">

```
kc ~/projects/practice --key work --provider https://llm.example.com/anthropic --model big-model
```

</div>


We tested these two ways with a stand-in for the provider, not with a real Ollama or a real provider.

<span class="src">From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--provider` and `--model`. Ollama's page
[Claude Code](https://docs.ollama.com/integrations/claude-code): "64k+ context window".</span>

</details>

Done: your website has a key of its own, with its own costs and its own limit.

**Next time.** When you start a project that may cost more than a little, give it a key of its own first.

<span class="src">From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--key` and `--provider`. OpenRouter's page on
[limits](https://openrouter.ai/docs/api/reference/limits): "Per-key credit limits", and what each key used.
Anthropic's page [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication): "Create and use
a key", and "Select a workspace".</span>

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
| `OpenRouter did not accept the key "website"`, or `Anthropic did not accept the key "website"` | kingo deleted this key, and no other. Check it on the provider's website (openrouter.ai: Settings, Keys; platform.claude.com: API keys), or make a new one. Then start again with `--key website`: kingo asks for the key. |
| With Anthropic's API, Claude Code shows an error that names `anthropic-workspace-id` | Your key is not for one workspace. On platform.claude.com, make a new key, and choose one workspace for it. Paste `rm ~/.config/kingo/key-website.key` into your terminal, and start again with `--key website`: kingo asks for the key. |
| `The key "website" is for OpenRouter, not for Anthropic's API` | A name belongs to one provider. Take another name for the other provider, for example `--key website-api --provider anthropic`. |
| `Ollama does not answer on this laptop` | Start Ollama, then start again. On Windows, Ollama must run in Ubuntu, where kingo runs. |
| You want another key under the name `website` | kingo keeps the key in a file. Delete this file. For an OpenRouter key, paste `rm ~/.config/kingo/openrouter-website.key` into your terminal; for another provider, `rm ~/.config/kingo/key-website.key`. Then start again with `--key website`: kingo asks for the key. |

</details>
