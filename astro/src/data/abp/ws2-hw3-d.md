---
title: "Homework until 23 Nov, Part D: A project of your own"
---


So far, Claude Code worked for the course. Now it works for you: you build a small website of your own, in a folder
of its own. After this part, you can use Claude Code for any project of yours, and the course stays clean.

### 9. Know where Claude Code may work

<div class="quiz">

**Quiz.** In the course, you start Claude Code with <span class="cmd-i cmd-i-t">`./kingo claude`</span>. In which of your folders can Claude Code create
and change files?

<ul>
<li>In every folder on your laptop that you can write to</li>
<li>In all of <code>~/kingo-pod</code></li>
<li data-right>Only in <code>~/kingo-pod/claude</code>, your course folder</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Only in `~/kingo-pod/claude`.** Claude Code may read all of kingo-pod, but it can write only in the course folder.
The sandbox decides that, not the model: so a mistake of the model cannot change the rest of your laptop. In any
setup: before you start a project, know where Claude Code may write.

The course folder is for the course: there Claude Code reaches n8n, Langflow and your database, and it reads your
team's rules. For anything else, for example your thesis or a small tool for yourself, Claude Code gets a folder of
its own. You do that in the next step.

</details>

</div>

<figure class="hx hx-box" data-mode="course" aria-label="Where Claude Code may read and write"><div class="hx-switch" role="group" aria-label="How you start Claude Code"><button type="button" data-mode="course" aria-pressed="true"><code>./kingo claude</code></button><button type="button" data-mode="in" aria-pressed="false"><code>./kingo claude --in ~/projects/my-first-project</code></button></div><ul class="hx-tree"><li style="--i:0"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~/kingo-pod/claude</code><small>your course folder</small><span class="acc course write"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg><span>reads and writes</span></span><span class="acc in none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span></li><li style="--i:1"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~/kingo-pod</code><small>the rest of kingo-pod</small><span class="acc course read"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg><span>reads only</span></span><span class="acc in read"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg><span>reads only its helpers</span></span></li><li style="--i:2"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~/projects/my-first-project</code><small>a folder of your own (step 10)</small><span class="acc course none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span><span class="acc in write"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg><span>reads and writes</span></span></li><li style="--i:3"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>~</code><small>your other folders</small><span class="acc course none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span><span class="acc in none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span></li><li style="--i:4"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg><code>/mnt/c</code><small>Windows: your drive C:</small><span class="acc course none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span><span class="acc in none"><svg class="hx-i" viewBox="0 0 24 24" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg><span>no access</span></span></li></ul><p class="hx-pick" data-for="course"><code>./kingo claude</code>: Claude Code writes only in your course folder. It reads the rest of kingo-pod, and nothing else of yours.</p><p class="hx-pick" data-for="in"><code>./kingo claude --in ~/projects/my-first-project</code>: Claude Code writes only in that folder. Of kingo-pod, it reads only its own helpers, in <code>~/kingo-pod/setup/claude</code>.</p></figure>

Done: you know where Claude Code may write, with each way to start it.

**Next time.** When you start Claude Code in a new setup, find out first where it may write.

### 10. Give each project a folder of its own

Make a new folder and start Claude Code there:

1. Make the folder. Is Claude Code still running in your terminal? Type <span class="cmd-i cmd-i-c">`/exit`</span> first. Then paste this line into
   your terminal:
   <div class="cmd cmd-terminal">

   ```
   mkdir -p ~/projects/my-first-project
   ```

   </div>

   <span class="cmd-i cmd-i-t">`mkdir`</span> makes a folder: here `my-first-project`, inside a folder `projects` in your home folder (`~`). With
   `-p`, it also makes `projects` when that folder is not there yet. Check it: this line lists your new folder.
   <div class="cmd cmd-terminal">

   ```
   ls ~/projects
   ```

   </div>

2. Go into your kingo-pod folder, where the command <span class="cmd-i cmd-i-t">`./kingo`</span> is. Paste this line into your terminal:
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod
   ```

   </div>

3. Start Claude Code in the sandbox, as before, but in your new folder:
   <div class="cmd cmd-terminal">

   ```
   ./kingo claude --in ~/projects/my-first-project
   ```

   </div>


Claude Code writes only in `~/projects/my-first-project`. It does not see n8n, Langflow or your database there, and
it does not read your team's rules. Its notes (step 7) are then in that folder, in `memory-of-ai/`.

To see what Claude Code writes there, open the folder in a second terminal tab
([how](/abp/ws2/hw3/#your-terminal-in-short)). On a Mac, paste this line:

<div class="cmd cmd-terminal">

```
open ~/projects/my-first-project
```

</div>


On Windows, paste this line:

<div class="cmd cmd-terminal">

```
cd ~/projects/my-first-project && explorer.exe .
```

</div>


Or click through the File Explorer: **Linux** in the left column, then **Ubuntu**, **home**, your name, **projects**.
Pin the folder `projects`, as in step 2: right-click it and choose **Pin to Quick access**.

**Your turn: build your own website.** A one-page website about this homework, with a little animation: for
example, the nine habits, one card each, that come in one after the other. On the way, you use the habits.

<div class="checklist">

1. **Plan first** (step 3). In Claude Code, paste:
   <div class="cmd cmd-claude">

   ```
   I want a one-page website about the habits of my current homework, with a little animation. I have not thought it through yet. Interview me until you could write a plan, then write the plan to plan.md. Do not build anything yet.
   ```

   </div>

   Answer its questions: you decide who the page is for, what it shows, and how it moves. When Claude Code asks
   what the habits are, copy them from [Your habits on one page](/abp/ws2/hw3-e/#your-habits-on-one-page), at the end of this
   homework.
2. **Start fresh, then build, with a finish line** (steps 7 and 4). Type:
   <div class="cmd cmd-claude">

   ```
   /clear
   ```

   </div>

   Then paste:
   <div class="cmd cmd-claude">

   ```
   Build what plan.md says, as one file index.html. You are done when index.html opens in a browser and shows everything that plan.md asks for. Look at the page before you say that you are done.
   ```

   </div>

3. **Open your page.** On a Mac, paste this line into your second terminal tab:
   <div class="cmd cmd-terminal">

   ```
   open ~/projects/my-first-project/index.html
   ```

   </div>

   On Windows, double-click `index.html` in the folder that you opened above.
4. **One step at a time** (step 5). Ask for one change, look at the page, then ask for the next improvement, for example: "Let
   each card come in from the left when I scroll to it." Does Claude Code go in circles? Press **Esc** (step 6).
5. **Let it remember** (step 2). Do you tell Claude Code the same thing in every session, for example which colours
   your page has? Ask it: "Write this into AGENTS.md, as a rule for this project." At every start, Claude Code reads
   that file, and other coding agents do too.

</div>

Done: you planned and built a website with Claude Code. Show it to your team.

<div class="quiz">

**Quiz.** You started Claude Code in `~/projects/my-first-project`. Next week you want to continue. What do you type?

<ul>
<li><span class="cmd-i cmd-i-t"><code>cd ~/kingo-pod && ./kingo claude</code></span></li>
<li><span class="cmd-i cmd-i-t"><code>cd ~/projects/my-first-project && claude</code></span></li>
<li data-right><span class="cmd-i cmd-i-t"><code>cd ~/kingo-pod && ./kingo claude --in ~/projects/my-first-project</code></span></li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**With `--in` and the folder.** Without `--in`, Claude Code starts in the course folder. A plain `claude` does not go
through kingo: no sandbox, no keys, no way to OpenRouter. To pick up last week's conversation too, type <span class="cmd-i cmd-i-c">`/resume`</span>
in Claude Code. A shorter way to start comes in [Part E](/abp/ws2/hw3-e/).

</details>

</div>

<span class="src">From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo claude help`</span>, its lines on `--in` and on <span class="cmd-i cmd-i-t">`./kingo shortcuts`</span>.</span>

[Stuck? Help for step 10](#step-10)

**Next: [Part E · Shorter commands →](/abp/ws2/hw3-e/)**

<details class="more help" id="help">
<summary>If something goes wrong</summary>

Find your step.

#### Step 10

| What you see | What to do |
|---|---|
| kingo says the folder is not inside your home folder | Use a folder under `~`, as in the box. Not a Windows folder (`/mnt/c/...`). |
| `index.html` opens in a text editor, not in your browser | Right-click it, choose *Open with*, and pick your browser. |

</details>
