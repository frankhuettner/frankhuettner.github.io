---
title: "Homework until 23 Nov, optional: More room for Claude Code"
---


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

*From nono's page on [Claude Code](https://nono.sh/docs/cli/clients/claude#overriding-profile-settings): "add extra
directory access", and from its
[security model](https://nono.sh/docs/cli/internals/security-model#capability-expansion-and-irreversibility): a
program in the sandbox "cannot expand its own kernel policy". Anthropic's page on
[permissions](https://code.claude.com/docs/en/permissions#working-directories): working directories and <span class="cmd-i cmd-i-c">`/add-dir`</span>.
kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>.*

[Stuck? Help for step 12](#step-12)

### 13. Work in two sessions at once

Claude Code can work in two terminal tabs at once: for example on your website in one tab, while you ask about your
flow in the other. Each tab is a session of its own, in a sandbox of its own.

**Your turn.** Open a second terminal tab ([how](/abp/ws2/hw3/#your-terminal-in-short)).

<details class="more">
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

*From Anthropic's page [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees): each session
gets a copy of its own, "so changes don't collide". kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--login`.*

[Stuck? Help for step 13](#step-13)

### 14. Give a project a key of its own

So far, all your sessions pay with one OpenRouter key. On openrouter.ai, you see one sum for everything: the course,
your website, and every other project.

Give a project a key of its own. This gives you two things:

- **You see what this project costs.** OpenRouter counts for each key what it used.
- **The project gets a credit limit of its own.** When Claude Code goes in circles in this project, it stops at
  that amount, and the credit of your other key stays.

**Your turn: a key with the name `website`, for your first website.**

<details class="more">
<summary>New here? What is different for you in this step</summary>

- You use your Claude subscription, with `--login`? Then this step is not for you: `--key` needs an OpenRouter
  account with credit. You can read it, and skip the rest.
- You have no folder `~/projects/my-first-project`? Then take your practice folder in 2:
  <div class="cmd cmd-terminal">

  ```
  kc ~/projects/practice --key website
  ```

  </div>

- Below, <span class="cmd-i cmd-i-t">`kc --key website`</span> is the start for the course. You do not need it.

</details>

1. Make the key. Open openrouter.ai in your browser, and sign in. Open **Settings**, then **Keys**, and make a new
   key. Name it `website`, and give it a small credit limit. Copy the key: OpenRouter shows it only once.
2. Is Claude Code still running in your terminal? Type <span class="cmd-i cmd-i-c">`/exit`</span> first. Then start Claude Code for your website,
   with `--key` and the name of the key:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project --key website
   ```

   </div>

   The name is for kingo: small letters, digits and `-`. It can be any name, but the same name as on openrouter.ai
   is the easiest to remember. You did not make the short commands of [Part E](/abp/ws2/hw3-e/)? Then go into `~/kingo-pod` first, and
   start it with <span class="cmd-i cmd-i-t">`./kingo claude --in ~/projects/my-first-project --key website`</span>.
3. kingo asks: `Paste the OpenRouter key "website"`. Paste the key that you copied in 1, and press **Enter**. kingo
   keeps it with your other keys, outside the sandbox.
4. Look at the lines before Claude Code starts. kingo says which key pays:
   `Claude Code's model is paid with your OpenRouter key "website"`.
5. Ask Claude Code something, for example: "What is in this folder?" Then look at **Keys** on openrouter.ai again:
   the key `website` shows what it used.
6. Type <span class="cmd-i cmd-i-c">`/exit`</span>, and paste the line of 2 again. This time, kingo does not ask: it has the key of this name.

Three more things to know:

- **Without `--key`, nothing changed.** Start Claude Code as before, and your first OpenRouter key pays, as before.
- **`--key` works in the course too.** <span class="cmd-i cmd-i-t">`kc --key website`</span> starts Claude Code for the course, paid with the key
  `website`. Your flows in Langflow keep the key that they have.
- **Not with `--login`.** `--login` uses your Claude subscription, and `--key` an OpenRouter key: kingo takes one
  of the two.

Done: your website has a key of its own, with its own costs and its own limit.

**Next time.** When you start a project that may cost more than a little, give it a key of its own first.

*From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--key`. OpenRouter's page on
[limits](https://openrouter.ai/docs/api/reference/limits): "Per-key credit limits", and what each key used.*

[Stuck? Help for step 14](#step-14)

## If something goes wrong

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
| `unknown option '--key'` | Your kingo-pod is older than `--key`. Paste <span class="cmd-i cmd-i-t">`kingo update`</span>, or <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo update`</span>, and start again. New here? Paste <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && git pull`</span>. |
| `OpenRouter did not accept the key "website"` | kingo deleted this key, and no other. Check it on openrouter.ai (Settings, Keys), or make a new one. Then start again with `--key website`: kingo asks for the key. |
| You want another key under the name `website` | kingo keeps the key in a file. Delete this file: paste `rm ~/.config/kingo/openrouter-website.key` into your terminal. Then start again with `--key website`: kingo asks for the key. |
