---
title: "Homework until 23 Nov, Part C: Stay in control"
---


Claude Code can work alone for a long time. That is its strength, and its risk: it can go in circles, lose the
thread in a long conversation, or change something that you cannot take back. In this part, you learn three moves
that keep you in charge: **Esc**, <span class="cmd-i cmd-i-c">`/clear`</span>, and a copy.

### 6. Watch Claude Code, and press Esc when it goes in circles

Going in circles means: Claude Code tries the same thing again and again, and gets no closer.

<div class="case" data-model="GLM 5.3 Flash · our trial 1">

**A real case from our tests.** We gave Claude Code the two prompts of the kimchi part of the last homework three
times: **trials 1, 2 and 3**.

In every trial, Claude Code was to fix the search in a copy of the Langflow flow
([step 13 of the last homework](/abp/ws2/hw2-recommended/#13-let-claude-code-fix-the-search-in-a-copy-of-the-flow)).
The replay below shows what Claude Code wrote in trial 1.

</div>

**Your turn.** Watch the replay:

1. Click **Play the replay**.
2. Watch for one thing: does Claude Code say something new, or the same again? You do not need to understand every
   line.
3. Click **Esc Stop it here** where you would stop Claude Code.

<figure class="hx hx-term" aria-label="Replay of our trial 1"><div class="hx-term__bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><em>Claude Code · z-ai/glm-5.3-flash · our trial 1, 17 Nov</em></div><ol class="hx-term__log"><li class="you"><s aria-hidden="true">❯</s><span>Make a copy of the Langflow flow Draft Reply (Enron) and name it &quot;Draft Reply (Enron) - Search Fix&quot;. …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 1m 26s</span></li><li class="say"><s aria-hidden="true">⏺</s><span>I&#x27;ll do this in steps: first inspect the pieces I need from the flow JSON …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 1m 58s, ran 2 shell commands</span></li><li class="say"><s aria-hidden="true">⏺</s><span>Now let me look at the related mails&#x27; full texts and measure which stored mails are actually closest to the Kimchi mail …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 42s, ran 2 shell commands</span></li><li class="say"><s aria-hidden="true">⏺</s><span>… Before building anything, let me verify empirically which search input actually brings the Kimchi mail into the top 5. …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 29s, ran 3 shell commands</span></li><li class="rep"><s aria-hidden="true">⏺</s><span>Interesting — the tweaks on MailSearch-mails.search_query were ignored (its input comes through an edge, and edge values win over tweaks). …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 53s, ran 1 shell command</span></li><li class="rep"><s aria-hidden="true">⏺</s><span>The tweaks path doesn&#x27;t reach the search (the edge wins). …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 2m 8s, ran 3 shell commands</span></li><li class="rep"><s aria-hidden="true">⏺</s><span>The tweaks on MailSearch.search_query were ignored — that input comes through an edge, and the edge value wins. …</span></li><li class="think"><s aria-hidden="true"></s><span>Thought for 40s, ran 3 shell commands</span></li><li class="rep"><s aria-hidden="true">⏺</s><span>The tweaks on search_query don&#x27;t apply (the edge wins), but settings like number_of_results are not edge-fed …</span></li><li class="say"><s aria-hidden="true">⏺</s><span>The planned format (subject + body) improves the Kimchi mail&#x27;s rank from 31 to 13, but let me be systematic …</span></li><li class="zh"><s aria-hidden="true">⏺</s><span>现在我来验证组件代码在 Langflow 上的加载情况（仅校验——不修改任何流程）：<em lang="en">Now I check how Langflow loads the code of the component (a check only, no flow is changed):</em></span></li><li class="zh"><s aria-hidden="true">⏺</s><span>代码是有效的。现在我来构建副本的 JSON：…<em lang="en">The code is valid. Now I build the JSON of the copy: …</em></span></li><li class="say"><s aria-hidden="true">⏺</s><span>The copy is created (id f567b653…, same folder). Now the edit: add the Search Query component and rewire. …</span></li><li class="zh"><s aria-hidden="true">⏺</s><span>已完成。以下是我所做工作的总结：<em lang="en">Done. Here is a summary of what I did:</em></span></li><li class="end"><s aria-hidden="true"></s><span>✻ Sautéed for 23m 10s · done 8:21 PM</span></li></ol><div class="hx-term__keys"><button type="button" class="hx-esc" disabled><kbd>Esc</kbd> Stop it here</button><button type="button" class="hx-play">Play the replay</button><span class="hx-term__count" aria-live="polite"></span></div><p class="hx-term__note" aria-live="polite"></p></figure>

**Later, in your own work with Claude Code: after Esc, ask.** The replay above is only for practice: there is nothing
to paste into it. In Claude Code, the key **Esc** stops Claude Code at once and keeps everything that it did so far,
so you lose nothing. Then you could ask it something like:

<div class="cmd cmd-claude">

```
What are you trying now? Why did the last try not work?
```

</div>


And when it writes in another language:

<div class="cmd cmd-claude">

```
Please write in English.
```

</div>


You can also interrupt Claude Code (press **Esc**) when you see no new line for a few minutes, and ask: "What are you
waiting for?" The answer may be simple, for example: Langflow needs a restart (<span class="cmd-i cmd-i-t">`./kingo restart`</span> in a second terminal
tab). Or Claude Code has a good reason to wait. Then you can tell it to continue.

**How often it got lost.** We looked into the logs of our three trials. The task was the same each time: the same
prompt, the same model (GLM 5.3 Flash). The trials differed in one thing: what Claude Code got to read about the
setup, as in `info-for-ai` of step 2. Trial 1 got long instructions, trial 2 nothing, trial 3 the three short files
of [step 2](/abp/ws2/hw3-a/#2-give-claude-code-the-facts-of-your-setup).

<figure class="hx hx-det" aria-label="How often Claude Code got lost in our three trials"><ol class="hx-det__cards"><li class="hot" style="--i:0"><div class="t"><b>Trial 1</b><span>23 min</span></div><span class="who">with long instructions for Claude Code</span><ul><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i><i class="mk" style="--k:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i><i class="mk" style="--k:2"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i><i class="mk" style="--k:3"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i></span><span>said the same thing 4 times</span></li><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i><i class="mk" style="--k:1"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i><i class="mk" style="--k:2"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i><i class="mk" style="--k:3"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i></span><span>4 tries that went nowhere: twice the key files (blocked), a way to change the search that the flow ignores, a long check that it had to stop</span></li><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/></svg></i></span><span>6 messages in Chinese</span></li></ul><p class="end no"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></span>"Kimchi for Monday" not in the sources</p></li><li class="" style="--i:1"><div class="t"><b>Trial 2</b><span>9 min</span></div><span class="who">with no extra instructions</span><ul><li><span class="marks"></span><span>did not say the same thing twice</span></li><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i></span><span>1 try that went nowhere: a run of the flow that took too long</span></li><li><span class="marks"></span><span>English throughout</span></li></ul><p class="end no"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></span>"Kimchi for Monday" not in the sources</p></li><li class="" style="--i:2"><div class="t"><b>Trial 3</b><span>8 min</span></div><span class="who">with the three short files of step 2</span><ul><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i><i class="mk" style="--k:1"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/></svg></i></span><span>said the same thing 2 times</span></li><li><span class="marks"><i class="mk" style="--k:0"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg></i></span><span>1 try that went nowhere: a typo in a command</span></li><li><span class="marks"></span><span>English throughout</span></li></ul><p class="end ok"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg></span>"Kimchi for Monday" in the sources</p></li></ol><p class="hx-det__foot">Orange: trial 1, the run of the replay above. One run each: a hint, not proof. In trial 3, Claude Code could also call OpenRouter (its files said how; the sandbox adds your key), so it could measure the search itself.</p></figure>

<details class="more">
<summary>Why did it write Chinese?</summary>

That is the model, not the tool. Models that learned many languages sometimes switch language in the middle of an
answer; researchers call it code-switching ([Deng et al., 2025](https://arxiv.org/abs/2507.14894)). In our trial 3,
the facts of step 2 said "The student … reads English", and Claude Code wrote English from start to end. So did
trial 2, without that line: one run proves nothing. But the line costs you nothing.

</details>

<div class="fine">

**Why watch at all?** Because the feeling misleads. In 2025, the research group METR measured experienced
programmers: with AI tools, they felt 20% faster, and they were 19% slower
([METR, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). METR says that today's
tools are different, so do not take the numbers as they are. Take the lesson: a feeling is not a measurement.

</div>

Done: you know when to press Esc, and what to ask then.

**Next time.** In your next longer task, watch the first minute. Press **Esc** once and ask what Claude Code is
doing. Then write "continue".

<span class="src">From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#steer-the-session): steer the session.</span>

### 7. Start fresh: after two failed tries, and for a new task

<div class="quiz">

**Quiz.** Say your mail AI assistant starts every reply with "Dear Sir", and you asked Claude Code to fix that. Twice
you told Claude Code what was wrong, and the replies still start with "Dear Sir". What now?

<ul>
<li>Tell Claude Code a third time, more clearly: by now, Claude Code knows the problem well</li>
<li data-right>Type <span class="cmd-i cmd-i-c"><code>/clear</code></span>, and write one new prompt with what you learned</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Type <span class="cmd-i cmd-i-c">`/clear`</span>.** <span class="cmd-i cmd-i-c">`/clear`</span> empties the conversation. Without it, the model reads the whole conversation again at
every step, also the two tries that failed. A third correction only adds to them. After <span class="cmd-i cmd-i-c">`/clear`</span>, one new prompt that
holds what you learned works better almost every time. Your files stay as they are. The picture below visualizes
this (try both buttons):

<figure class="hx hx-ctx" aria-label="What the model reads at every step"><div class="hx-ctx__head"><b>What the model reads again at every step</b><span>room in the course: 200,000 tokens</span></div><ol class="hx-ctx__blocks"><li class="start">AGENTS.md + facts</li><li class="you">Your prompt</li><li class="bad">Try 1 ✗</li><li class="you">Correction</li><li class="bad">Try 2 ✗</li><li class="you">Correction</li></ol><div class="hx-ctx__keys"><button type="button" data-act="more">A third correction</button><button type="button" data-act="clear"><code>/clear</code> and one new prompt</button></div><p class="hx-ctx__say" aria-live="polite">Every step, the model reads all of this again: also the two tries that failed.</p></figure>

</details>

</div>

**Your turn: watch the number.** Start Claude Code as in step 1, if it is not running.

1. Type <span class="cmd-i cmd-i-c">`/context`</span>: it shows how many tokens the model gets at every step. In our trial 2, right at the start, it
   showed `15.8k/200k tokens (8%)`: the start files and the tool's own instructions for the model, before the first
   prompt.
2. Ask Claude Code one question, for example: "Which flows are in my Langflow?" New here? Ask: "What does plan.md
   say?" Then type <span class="cmd-i cmd-i-c">`/context`</span> again: the number grew.
3. Type <span class="cmd-i cmd-i-c">`/clear`</span>, and then <span class="cmd-i cmd-i-c">`/context`</span>: back at the start.

A long conversation has two costs:

- **It costs money.** Every step sends the whole conversation again. On your OpenRouter key, you pay for all of it,
  at every step; with `--login`, it uses up your subscription's limits faster.
- **It gets less reliable.** Researchers who tested 18 models found: the longer the text in front of a model, the
  less reliable its answers, even for simple tasks ([Chroma, 2025](https://research.trychroma.com/context-rot)).

**So start every new task with <span class="cmd-i cmd-i-c">`/clear`</span>.** For example: you worked on your n8n workflow all morning, and now you
want to change a prompt in Langflow. Type <span class="cmd-i cmd-i-c">`/clear`</span> first: the model does not need the morning's conversation for the
new task.

<span class="cmd-i cmd-i-c">`/clear`</span> only empties the conversation. Two things stay:

- **What Claude Code knows about your project.** After <span class="cmd-i cmd-i-c">`/clear`</span>, the model gets the start files of step 2 again,
  and Claude Code's own notes (more on them below).
- **The old conversation.** Type <span class="cmd-i cmd-i-c">`/resume`</span>, and pick it from the list of your earlier conversations.

**Keep what you learned.** What Claude Code found out only in the conversation, for example which file was to blame,
is gone after <span class="cmd-i cmd-i-c">`/clear`</span>. So before <span class="cmd-i cmd-i-c">`/clear`</span>, let Claude Code write it down. Paste:

<div class="cmd cmd-claude">

```
Write what we learned so far into notes.md: what we tried, what failed, what we know now.
```

</div>


After <span class="cmd-i cmd-i-c">`/clear`</span>, begin your new prompt with "Read notes.md first."

<details class="more">
<summary>What about /compact?</summary>

<span class="cmd-i cmd-i-c">`/compact`</span> does not empty the conversation: it puts a summary in its place. That summary still holds the two tries
that failed, so after two failed tries, <span class="cmd-i cmd-i-c">`/clear`</span> with one new prompt is better. <span class="cmd-i cmd-i-c">`/compact`</span> fits a long task that goes
well: you keep the thread, and the model gets fewer tokens at every step. You can tell it what to keep, for example:

<div class="cmd cmd-claude">

```
/compact keep the changes to the flow and the command that tests it
```

</div>


<span class="cmd-i cmd-i-c">`/compact`</span> itself reads the whole conversation once, to write the summary: on a long conversation, that is one big
step.

</details>

**Where its notes are.** While it works, Claude Code writes notes for itself, its memory, and loads them at every
start. Type <span class="cmd-i cmd-i-c">`/memory`</span> in Claude Code to see them. Usually, they are in `~/.claude/projects/`, in a folder for each
project. kingo keeps them in the folder where Claude Code works, in `memory-of-ai/`, where you can read them: in the
course, that is `~/kingo-pod/claude/memory-of-ai/`. Is a note wrong? Ask Claude Code to correct it, or delete it.

Done: you know how to start fresh, and how to keep what you learned.

**Next time.** Before your next new task, type <span class="cmd-i cmd-i-c">`/clear`</span>.

<span class="src">From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#steer-the-session):
steer the session, and [keep cost and context down](https://code.claude.com/docs/en/best-practices#keep-cost-and-context-down);
<span class="cmd-i cmd-i-c">`/resume`</span>: its page on [commands](https://code.claude.com/docs/en/commands); its notes:
[How Claude remembers your project](https://code.claude.com/docs/en/memory#storage-location).</span>

### 8. Work on a copy where there is no undo

Claude Code can undo its own changes: type <span class="cmd-i cmd-i-c">`/rewind`</span>, and pick the point to go back to. But <span class="cmd-i cmd-i-c">`/rewind`</span> undoes only
changes to files that Claude Code edited itself.

<figure class="hx hx-rewind" aria-label="What /rewind can take back"><div class="hx-zone ok"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.7-.9l-.8-1.2A2 2 0 0 0 7.9 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg></span><b>Files in your folder</b><span>that Claude Code edited itself</span><div class="hx-tl" aria-hidden="true"><i>v1</i><i>v2</i><i>v3</i><u></u></div><strong><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 14 4 9l5-5"/><path d="M4 9h11a5 5 0 0 1 0 10h-3"/></svg></span><code>/rewind</code> takes them back</strong></div><div class="hx-zone no"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></span><b>Langflow, n8n, your database</b><span>not files in your folder</span><div class="hx-tl" aria-hidden="true"><i>v1</i><i>v2</i><i>v3</i><u></u><em></em></div><strong>No <code>/rewind</code> here: <em>make a copy first</em></strong></div></figure>

<div class="quiz sort">

**Quiz.** What can <span class="cmd-i cmd-i-c">`/rewind`</span> undo? Sort each change into its box.

| Change | Can <span class="cmd-i cmd-i-c">`/rewind`</span> undo it? |
|---|---|
| Claude Code wrote the file `plan.md`, in your course folder | Yes |
| Claude Code changed a line in `AGENTS.md`, in your course folder | Yes |
| Claude Code changed your flow in Langflow | No |
| Claude Code changed your workflow in n8n | No |
| Claude Code changed a row in your database | No |

<details class="more">
<summary>Why</summary>

<span class="cmd-i cmd-i-c">`/rewind`</span> brings back the files that Claude Code edited itself. Everything else stays as it is:

- in any project: a file that only a command changed, and every change outside your folder, for example in a
  database, through an API, or a mail that went out;
- here: your flows and workflows. They are not files in your folder: they live in Langflow and n8n, and Claude Code
  changes them through their APIs. A change to your flow, or to your published n8n workflow, reaches your mail AI
  assistant at once.

</details>

</div>

**Your turn: undo a change.** In Claude Code, paste:

<div class="cmd cmd-claude">

```
Add a short joke about kimchi to the end of plan.md.
```

</div>


Look at the end of `plan.md` (step 3 shows how to open it). Then type <span class="cmd-i cmd-i-c">`/rewind`</span>, pick your prompt about the joke, and
choose **Restore code**. Look again: the joke is gone, and the rest of `plan.md` is as before.

**Can Claude Code put a flow back?** Ask it, for example: "Put the flow back as it was before your change." Claude Code
knows from the conversation what it changed. Here, it also has backups: `AGENTS.md` asks it to save a flow or a
workflow in `backups/` before it changes it, and kingo saves all your flows and workflows at every start of
<span class="cmd-i cmd-i-t">`./kingo claude`</span>. That can work, but not for sure.

**Where there is no undo, a copy is your undo.** The last homework of the course did this, with the copy *Draft
Reply (Enron) - Search Fix*
([step 13](/abp/ws2/hw2-recommended/#13-let-claude-code-fix-the-search-in-a-copy-of-the-flow)): the original keeps
working, and you can run both and compare. When the copy is better, ask Claude Code to bring the change into the
original.

Done: you know where <span class="cmd-i cmd-i-c">`/rewind`</span> is your undo, and where a copy is.

**Next time.** For your next risky idea, start your prompt with: "Make a copy of … and change only the copy."

<span class="src">From Anthropic's [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#undo-changes-with-checkpoints):
"Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed", and its page on
[checkpointing](https://code.claude.com/docs/en/checkpointing#limitations). That Langflow and n8n are such places
comes from how kingo-pod works.</span>

**Next: [Part D · A project of your own →](/abp/ws2/hw3-d/)**
