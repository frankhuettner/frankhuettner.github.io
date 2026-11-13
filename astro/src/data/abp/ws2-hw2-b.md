---
title: "Homework until 16 Nov, Part B: How Claude Code works here"
---


### 7. What Claude Code can do, and what it cannot

| Claude Code can | Claude Code cannot |
|---|---|
| read and write in `~/kingo-pod/claude` | write anywhere else on your laptop |
| read kingo-pod: `compose.yml`, the guides | change kingo-pod, or run `./kingo` |
| change your n8n workflows and data tables, your Langflow flows and your Postgres database | see your keys: it gets stand-ins |
| look things up on the web | see your own Claude Code settings, if you use Claude Code already |

Sometimes, Claude Code wants to execute a command (which we don’t allow), and then it’ll tell you to run a command on its behalf in the terminal.

<div class="quiz">

**Quiz.** Claude Code says that the sandbox blocks a command, and asks you to run it in your own terminal. Should you?

<ul>
<li>Yes: Claude Code needs it to go on</li>
<li data-right>Only if I understand the command</li>
<li>No, never</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Only run a command in your own terminal if you understand it.** Claude Code cannot leave its sandbox, but a command
you type does. When Claude Code says that the sandbox blocks it, that is the sandbox doing its job.

</details>

</div>

<div class="quiz">

**Quiz.** In step 4 you gave `kingo` your n8n key. Does Claude Code know the key now?

<ul>
<li>Yes: it needs the key to reach n8n</li>
<li data-right>No: it gets a stand-in</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**No.** Claude Code gets only a stand-in. nono keeps the real key and puts it into each request that Claude Code sends
to n8n. Hence, your key is not uploaded to the provider of the LLM, but Claude Code can still use it. The Langflow
key and your OpenRouter key are kept the same way.

</details>

</div>

### 8. Claude Code always asks for permission: should we tell it to just do its job?

Claude Code always works in one of four modes. The mode decides who says yes before a command runs: you, the
AI, or nobody. The line under your text shows the mode, for example `⏸ manual mode on`.

**The mode does not decide where Claude Code can write.** The nono sandbox does that, as the table above shows:
Claude Code cannot write into any other folder on your laptop, such as Documents or Desktop, with or without your
permission. The mode only decides whether Claude Code asks you first.

**To change the mode, press Shift+Tab.** Each press takes you one mode further, in this order:

1. <span style="color:#9ca3af;font-weight:700">⏸︎</span> `manual mode on`: Claude Code asks you before it writes a file and before it runs a command. `./kingo claude`
   always starts here.
2. <span style="color:#a855f7;font-weight:700">⏵⏵</span> `accept edits on`: Claude Code writes files in its folder `~/kingo-pod/claude` without asking. Before a command,
   it still asks you.
3. <span style="color:#14b8a6;font-weight:700">⏸︎</span> `plan mode on`: Claude Code changes nothing. It writes a plan and asks for your yes.
4. <span style="color:#d97706;font-weight:700">⏵⏵</span> `auto mode on`: the AI decides itself whether it needs to ask you for permission.

One more press of Shift+Tab, and you are back in manual mode.

<div class="quiz">

**Quiz.** The line under your text says `plan mode on`. You ask Claude Code to rename a workflow. What happens?

<ul>
<li>Claude Code renames the workflow</li>
<li data-right>Claude Code writes a plan and asks for your yes</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Claude Code writes a plan and asks for your yes.** In plan mode, it changes nothing before you agree to the plan.

</details>

</div>

<span style="color:#dc2626;font-weight:700">⏵⏵</span> There is a fifth way, where nobody says yes or no: you start Claude Code with `./kingo yolo` instead of
`./kingo claude`. Then Claude Code never asks for permission.

**The difference, in five examples:**

| What Claude Code wants to do | <span style="color:#9ca3af;font-weight:700">⏸︎</span> In manual mode | <span style="color:#a855f7;font-weight:700">⏵⏵</span> In accept edits mode | <span style="color:#d97706;font-weight:700">⏵⏵</span> In auto mode | <span style="color:#dc2626;font-weight:700">⏵⏵</span> Started with `./kingo yolo` |
|---|---|---|---|---|
| **Write a file:** save its findings in the file `notes.md` in its folder `~/kingo-pod/claude` | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first | Claude Code writes the file <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong> | Claude Code writes the file <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong> | Claude Code writes the file <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong> |
| **Run a command that only reads:** list your n8n workflows | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first | <strong style="background:#bfdbfe;color:#1f2937;padding:0 .3em;border-radius:.25em">The AI checks the command.</strong> If the AI judges it safe, Claude Code runs it <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong>. If not, <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command does not run</strong> | Claude Code runs the command <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong>, and <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the AI does not check it</strong> |
| **Run a command that changes something:** make a copy of a Langflow flow | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first | <strong style="background:#bfdbfe;color:#1f2937;padding:0 .3em;border-radius:.25em">The AI checks the command.</strong> If the AI judges it safe, Claude Code runs it <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong>. If not, <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command does not run</strong> | Claude Code runs the command <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong>, and <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the AI does not check it</strong> |
| **Run a command that you said no to:** you wrote “Do not change the original flow”, but Claude Code gets confused and wants to change the original | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first. If you say yes without reading, <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command runs</strong> | Claude Code <strong style="background:#fde68a;color:#1f2937;padding:0 .3em;border-radius:.25em">asks you for permission</strong> first. If you say yes without reading, <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command runs</strong> | <strong style="background:#bfdbfe;color:#1f2937;padding:0 .3em;border-radius:.25em">The AI checks the command.</strong> It sees that you said no to this: <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command does not run</strong>. But the AI can get it wrong too: then <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the command runs</strong> | Claude Code runs the command <strong style="background:#bbf7d0;color:#1f2937;padding:0 .3em;border-radius:.25em">without asking you</strong>, and <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">the AI does not check it</strong> |
| **Write a file outside its folder:** save a file on your Desktop | <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">The nono sandbox stops it</strong>, with or without permission | <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">The nono sandbox stops it</strong>, with or without permission | <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">The nono sandbox stops it</strong>, with or without permission | <strong style="background:#fecaca;color:#1f2937;padding:0 .3em;border-radius:.25em">The nono sandbox stops it</strong>, with or without permission |

**The fourth example shows the risk.** An AI can get confused, and then it changes or deletes something that nobody
asked for. This happened to a professor: he asked for new page numbers, and lost the lecture notes of a year.

<div class="video" style="margin:1em 0"><iframe src="https://www.youtube-nocookie.com/embed/SzVLwnOlbVA" title="Watch the video: “Claude Just Deleted a Year of Lecture Notes” (Better Stack, 1.5 minutes)" width="315" height="560" style="max-width:100%;border:0;border-radius:12px;display:block" loading="lazy" allowfullscreen allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin"></iframe><p style="font-size:.9em;margin:.4em 0 0"><a class="video" href="https://www.youtube.com/shorts/SzVLwnOlbVA" target="_blank" rel="noopener">Watch the video: “Claude Just Deleted a Year of Lecture Notes” (Better Stack, 1.5 minutes)</a></p></div>

Who stops such a command?

- **In manual mode, only you.** You would have to read a long command and find the mistake in it.
- **In auto mode, the AI.** It reads every command and compares it with what you wrote. That is better than a yes
  without reading, but the AI can get it wrong too.

So no mode makes you safe. Two other things do: the nono sandbox lets Claude Code write in its folder only, and every
start of `./kingo claude` saves a copy of your workflows and flows. There is no such copy of your Postgres database.

**What does this mean for you?** In this homework, Claude Code rarely writes files. It mostly runs commands to
search, and to talk to n8n, Langflow and your Postgres database. In accept edits mode, Claude Code still asks you
before each of these commands. The requests stop only in auto mode, or with `./kingo yolo`.

**Which mode should you use? Auto mode is okay.** Claude Code runs inside the nono sandbox, so the sandbox protects
your laptop in every mode. And every start of `./kingo claude` saves your n8n workflows and your Langflow flows. In
manual mode, you get many requests, and the commands are hard to read. So feel free to switch to auto mode: press
Shift+Tab until the line under your text says `auto mode on`.

**In manual mode,** Claude Code asks before each command. **Yes** runs the command. **No** stops Claude Code: then
tell it what to do instead, or type `continue`.

<div class="quiz">

**Quiz.** You are in auto mode. Claude Code tells you that a request was blocked, and asks whether it may try again. It is the change you asked for. What do you do?

<ul>
<li>Type <code>/exit</code> and start again</li>
<li data-right>Say yes, and name what it may do</li>
<li>Nothing: Claude Code finds another way</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Say yes, and name what it may do,** for example: `Yes, retry saving the change to the copy.` In auto mode, the AI
may refuse a command that you asked for. Is it blocked again? Press Shift+Tab until the line under your text says
`manual mode on`, and say it again.

</details>

</div>

### 9. You decide: `./kingo yolo` starts Claude Code without any check

In each of the four modes, someone checks a command before it runs: you, or the AI. You can also start Claude Code
with no check at all. To this end, you start it with this line:

```
./kingo yolo
```

The first time, Claude Code asks whether you accept this mode. Choose **Yes, I accept**.

| | <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg> ./kingo claude | <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15.914 4a1.5 1.5 0 00-2.474-1.561l-9 9A1.5 1.5 0 005.5 14h4.002a.5.5 0 01.471.666L8.086 20a1.5 1.5 0 002.475 1.56l9-9A1.5 1.5 0 0018.5 10h-3.997a.5.5 0 01-.472-.667z"/></svg> ./kingo yolo | <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m2 2 20 20"/><path d="M5 5a1 1 0 0 0-1 1v7c0 5 3.5 7.5 7.67 8.94a1 1 0 0 0 .67.01c2.35-.82 4.48-1.97 5.9-3.71"/><path d="M9.309 3.652A12.252 12.252 0 0 0 11.24 2.28a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1v7a9.784 9.784 0 0 1-.08 1.264"/></svg> claude (without kingo) |
|---|---|---|---|
| <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M18 5a2 2 0 0 1 2 2v8.526a2 2 0 0 0 .212.897l1.068 2.127a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45l1.068-2.127A2 2 0 0 0 4 15.526V7a2 2 0 0 1 2-2z"/><path d="M20.054 15.987H3.946"/></svg> Your laptop is | protected by the nono sandbox and by Claude Code’s hesitations | protected by the nono sandbox | protected only by Claude Code’s hesitations: no sandbox |
| <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> Your workflows, flows and database | you see every change before it happens | Claude Code changes them at once, mistakes too | out of reach at first, as Claude Code has no keys for them; but it can read every file you can, your keys too |
| <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M14 4.1 12 6"/><path d="m5.1 8-2.9-.8"/><path d="m6 12-1.9 2"/><path d="M7.2 2.2 8 5.1"/><path d="M9.037 9.69a.498.498 0 0 1 .653-.653l11 4.5a.5.5 0 0 1-.074.949l-4.349 1.041a1 1 0 0 0-.74.739l-1.04 4.35a.5.5 0 0 1-.95.074z"/></svg> Your user experience | many requests for permissions, often the same ones | Claude Code works on by itself | Anthropic's standard Claude Code: your own Anthropic login and bill, and the usual requests for permissions |

The requests for permission protect your project from Claude Code's mistakes. If you let Claude Code work without asking, save your work first. This line saves your
n8n workflows and your Langflow flows into `~/kingo-pod/backups/` (not your own tables in the database):

```
cd ~/kingo-pod && ./kingo backup
```

<div class="quiz">

**Quiz.** Claude Code changed your n8n workflow *WS2.3 - Triage New Mail*, and now it does not work. Where is the version from before?

<ul>
<li>It is gone</li>
<li data-right>In <code>~/kingo-pod/backups/flows/</code></li>
<li>In Claude Code's memory</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**In `~/kingo-pod/backups/flows/`.** Every start of `./kingo claude` or `./kingo yolo` saves each n8n workflow and each
Langflow flow there as one JSON file, in a folder per start. The newest 10 starts stay. You can import such a file
again in n8n or in Langflow.

</details>

</div>

### 10. What is different from a standard Claude Code, and where it is configured

The Claude Code you started with `./kingo claude` is set up for the course.

<div class="quiz">

**Quiz.** You are in the folder `~/kingo-pod/claude` and type `claude`. Are you in the sandbox?

<ul>
<li>Yes: the folder belongs to kingo-pod</li>
<li data-right>No</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**No.** Then you get a standard Claude Code with Anthropic's settings: no sandbox, your own `~/.claude`, your own
Anthropic login. Even in `~/kingo-pod/claude`, a plain `claude` runs without the sandbox and without the keys.
**Here, you're on your own, kid.**

The course setup holds only when you start Claude Code with `./kingo claude` or `./kingo yolo`.

</details>

</div>

<details class="more">
<summary>In detail: what <code>./kingo claude</code> changes, and where</summary>

What is different from a Claude Code you install and start with `claude`, and the file where each
part is configured:

| | A standard Claude Code | Here, started with `./kingo claude` | Configured for the course in |
|---|---|---|---|
| Start | `claude`, in any folder | `./kingo claude` in the kingo-pod folder; `./kingo yolo` is the same without requests for permission. Claude Code works in `kingo-pod/claude` | `kingo-pod/kingo`, the script behind every `./kingo` command. Before Claude Code starts, it checks that n8n and Langflow run, asks for your keys the first time, copies `AGENTS.md`, `CLAUDE.md` and `.claude/settings.json` into `kingo-pod/claude/` the first time, and writes the nono profile. Then it starts Claude Code inside nono. |
| Model and bill | Claude models, with an Anthropic account or key | GLM 5.3 Flash through OpenRouter, paid with your OpenRouter key | `kingo-pod/claude/.claude/settings.json` names the model, for every role (`ANTHROPIC_MODEL` and the lines `ANTHROPIC_DEFAULT_…_MODEL`). The nono profile sends Claude Code's requests to OpenRouter instead of Anthropic, and puts your OpenRouter key into them. Claude Code does not know this model: `kingo-pod/kingo` tells it the context size to work with (`CLAUDE_CODE_MAX_CONTEXT_TOKENS`), 200,000 tokens. |
| Keys | kept by Claude Code itself | kept in `~/.config/kingo/`; Claude Code sees only stand-ins | `kingo-pod/kingo` asks for your OpenRouter and n8n keys, makes the Langflow key itself, and keeps them in `~/.config/kingo/`, readable only by you. nono reads them from these files when it starts; they are never in an environment variable. The nono profile says, for OpenRouter, n8n and Langflow, which file holds the key and where nono's proxy puts it into a request. |
| Files | Claude Code reads and writes wherever you may, after asking | Claude Code writes only in `kingo-pod/claude` and `~/.kingo-claude`, reads `kingo-pod`, and nothing else; the operating system enforces it | The nono profile `~/.config/nono/profiles/kingo-claude.json` lists the folders Claude Code may read and write, and the few environment variables that reach Claude Code: other keys on your laptop do not. `kingo` writes it anew at every start from `kingo-pod/setup/claude/nono-profile.json`, so a change to it does not last. On top, `kingo-pod/claude/.claude/settings.json` forbids Claude Code to read `.env` files, `~/.ssh` and `~/.aws`. |
| Sandbox | Claude Code's own sandbox, for commands only, if you turn it on | nono, around all of Claude Code: its commands, and its own tools for files too | the nono profile. `kingo-pod/claude/.claude/settings.json` turns Claude Code's own sandbox off (`sandbox.enabled`): nono covers more. |
| Settings and history | `~/.claude` | `~/.kingo-claude`; your own `~/.claude` stays untouched | `kingo-pod/kingo` starts Claude Code with `CLAUDE_CONFIG_DIR=~/.kingo-claude`: Claude Code keeps its settings, sessions and history there. An Anthropic login stored there, `kingo` removes at every start: the course does not use it, and Claude Code could read it. |
| Instructions | a `CLAUDE.md` that you write | `AGENTS.md`: the part about kingo-pod and your team's rules; `CLAUDE.md` only points to it | `kingo-pod/claude/AGENTS.md`, yours to change, and `kingo-pod/claude/CLAUDE.md`, which holds only `@AGENTS.md`. `settings.json` makes Claude Code skip the `CLAUDE.md` of kingo-pod itself, which is for kingo-pod's developers (`claudeMdExcludes`). |
| Memory | hidden in `~/.claude/projects/` | in `kingo-pod/claude/memory/`, where you can read it | `kingo-pod/claude/.claude/settings.json` (`autoMemoryDirectory`) |
| What leaves the laptop | the model's requests and the web pages Claude Code looks up, plus usage data, error reports and feedback to Anthropic; pages on claude.ai (artifacts) and Remote Control, if you use them | the model's requests, to OpenRouter only, and the web pages Claude Code looks up; usage data, error reports, feedback, pages on claude.ai and Remote Control are off | `kingo-pod/kingo` turns off pages on claude.ai, usage data, error reports and all traffic that is not needed, when it starts Claude Code. `kingo-pod/claude/.claude/settings.json` turns off the same, and also feedback (`DISABLE_FEEDBACK_COMMAND`), Remote Control (`disableRemoteControl`), pages on claude.ai (`enableArtifact`) and the check of each web address at Anthropic before Claude Code reads a page (`skipWebFetchPreflight`). |
| A way back | none | every start saves each n8n workflow and Langflow flow as a JSON file in `kingo-pod/backups/flows/`, a folder per start; the newest 10 stay. Claude Code can read them but not change them. A file can be imported again in n8n or in Langflow | `kingo-pod/kingo`, before it starts Claude Code. It needs `psql`. |
| Requests for permission | since version 2.1.283, Claude Code starts in auto mode: a model checks each command, runs what it judges safe and blocks the rest, without asking | Claude Code asks before a command (manual mode). Shift+Tab switches the mode, to auto mode too: there, GLM 5.3 Flash is the judge. `./kingo yolo` turns the requests off | `kingo-pod/kingo` starts Claude Code with `--permission-mode default`, and `./kingo yolo` starts it with `--dangerously-skip-permissions`. The sandbox stays the same. |
| Updates | Claude Code updates itself | no self-update: run the install line again | `kingo-pod/claude/.claude/settings.json`: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also turns off the self-update. |

</details>

**Claude Code's memory.** Claude Code writes down for itself what it learns about your project, so that it still knows it
in the next session: for example a name your team chose, or a mistake it should not make again. Usually this memory
is hidden in Claude Code's own folder. Here it lies in `~/kingo-pod/claude/memory/`, so you can read what Claude Code remembers,
and correct or delete it. The file `MEMORY.md` there lists everything it keeps.

Claude Code can explain all of this itself. Ask it:

```
How are you set up here, and what is different from a standard Claude Code?
```

**Next: [Recommended · Find out why your mail AI assistant missed the kimchi →](/abp/ws2/hw2-recommended/)**
