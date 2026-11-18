---
title: "Homework until 23 Nov, Part B: Ask well"
---


### 3. Plan first when you are not sure what you want

Not every task needs a plan. Which way is best depends on how well you know what you want.

<div class="quiz match">

**Quiz.** Which way for which task? Match each task with the way that fits it.

| Task | The way |
|---|---|
| The draft of your flow greets every customer with "Dear Sir". You know which flow it is. | One prompt: what goes wrong, where, and how you will know that it is fixed |
| Your team wants a new feature: your form asks for the order number, your flow uses it, and n8n sends urgent orders to a person. You have not thought it through yet. | Let Claude Code ask you questions and write a plan, then let it build the plan |
| Three small changes that have nothing to do with each other | One prompt for each, and <span class="cmd-i cmd-i-c">`/clear`</span> in between |

<details class="more">
<summary>Why</summary>

For the greeting, you know what is wrong and where: one clear prompt is enough. Three changes that have nothing to
do with each other go one by one, with <span class="cmd-i cmd-i-c">`/clear`</span> in between: each starts with a clean conversation.

A new feature has questions that only you can answer: which field, what counts as urgent, who gets the mail. Claude
Code cannot see your answers. Without the interview, Claude Code answers the questions itself, and you find out at
the end. When Claude Code asks you first, you catch a wrong idea in the plan, where it is quick to fix, and not later
in the work.

</details>

</div>

**Your turn: plan one small thing.** Here you only plan it; you do not build it. The thing: a short page for a new
member of your team, which says what your project does, which flow does what, and how to try it. The plan also says
how you will know that the page is done.

<details class="more">
<summary>New here? Plan a page about a team of yours</summary>

You have no team project of the course. So plan a page about a team or a group that you are in, at work or
elsewhere. Start Claude Code in your folder `~/projects/practice`, and paste this prompt in place of the one in 1:

<div class="cmd cmd-claude">

```
I want a short page for a new member of my team: what we do, who does what, and how to start. I have not thought it through yet. Interview me until you could write a plan, then write the plan to plan.md. End the plan with how we will know that the page is done. Do not build anything yet.
```

</div>


Claude Code writes `plan.md` into your folder. To open it in 3, paste this line on a Mac:

<div class="cmd cmd-terminal">

```
open -e ~/projects/practice/plan.md
```

</div>


On Windows:

<div class="cmd cmd-terminal">

```
cd ~/projects/practice && notepad.exe plan.md
```

</div>


</details>

1. Start Claude Code and paste this prompt. The sparkles before it stand for Claude Code: they are not part of the
   prompt.
   <div class="cmd cmd-claude">

   ```
   I want a short page for a new member of my team: what our project does, which flow does what, and how to try it. I have not thought it through yet. Interview me until you could write a plan, then write the plan to plan.md. End the plan with how we will know that the page is done. Do not build anything yet.
   ```

   </div>

2. Answer its questions, until Claude Code has written `plan.md` into your course folder. Count the questions that
   you had not thought about yourself. Does Claude Code ask whether it should build now? Say no: here you only plan.
3. Read `plan.md`. Open a second terminal tab ([how](/abp/ws2/hw3/#your-terminal-in-short)) and paste, on a Mac:
   <div class="cmd cmd-terminal">

   ```
   open -e ~/kingo-pod/claude/plan.md
   ```

   </div>

   On Windows:
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod/claude && notepad.exe plan.md
   ```

   </div>

   Does its end say how you will know that the page is done? Is something missing or wrong? Tell Claude Code, and
   let it change `plan.md`.

<details class="more">
<summary>Claude Code asks to switch to plan mode?</summary>

Plan mode is for exploring: Claude Code searches and reads, but it changes nothing. It may still ask for your OK to
search or to read something.

You do not need plan mode here: the prompt already asks for a plan, in a file. So you can say no. Did you say yes?
Then, when its plan is ready, Claude Code asks whether it should go ahead and build. Choose **Yes, manually approve
edits**: then Claude Code asks you before each change. Say yes when it writes `plan.md`, and no to everything else:
here you only plan. No `plan.md` yet? Ask: "Write the plan to plan.md."

</details>

Done: you have a plan, and maybe some questions that you had not thought about.

**Next time.** When you are not sure what you want, start with this interview. To build a plan, start fresh: type
<span class="cmd-i cmd-i-c">`/clear`</span>, so that Claude Code begins with the plan and nothing else, and then ask it to build what `plan.md` says. You
do that in step 10.

<figure class="hx hx-plan" aria-label="Plan first, then build"><ol class="hx-stages"><li style="--i:0"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M9.5 8.5a2.5 2.5 0 0 1 4.9.7c0 1.6-2.4 2-2.4 3.3"/><path d="M12 15h.01"/></svg></span><b>Interview</b><span>Claude Code asks, you answer</span></li><li style="--i:1"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><b>plan.md</b><span>the answers, in a file</span></li><li style="--i:2"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m7 21-4.3-4.3a1 1 0 0 1 0-1.4l10-10a1 1 0 0 1 1.4 0l5.6 5.6a1 1 0 0 1 0 1.4L13 21"/><path d="M22 21H7"/><path d="m5 11 9 9"/></svg></span><b>/clear</b><span>the conversation goes, the file stays</span></li><li style="--i:3"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg></span><b>Build</b><span>from plan.md, until it is done</span></li></ol><div class="hx-plan__track" aria-hidden="true"><span class="talk"><i></i><i></i><i></i></span><span class="doc"><code>plan.md</code></span></div><figcaption>The bubbles are your conversation with Claude Code. <code>/clear</code> empties the conversation; <code>plan.md</code> stays, because it is a file.</figcaption></figure>

*From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first):
brainstorm with Claude first; on plan mode: [permission modes](https://code.claude.com/docs/en/permission-modes).*

[Stuck? Help for step 3](#step-3)

### 4. Say what "done" looks like

A finish line is one sentence that says how you will know that a task is done.

<div class="case" data-model="GLM 5.3 Flash">

**A real case from our tests.** In the last homework, the mail AI assistant drafted a reply to the mail "Is there any
Korean home made food?" and did not use the information from an older mail, "Kimchi for Monday". We asked Claude Code to
make a copy of the Langflow flow *Draft Reply (Enron)* and to improve the search in the mail database in the copied
flow. We gave Claude Code no finish line.

We were not lucky. This is what happened:

1. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **Claude Code** set its own finish line:

   > Run the copy once with the same mail and check that "Kimchi for Monday" now appears in the sources.

   The sources are the mails that the search finds for the draft.

2. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **Claude Code** ran the copy. "Kimchi for Monday" was among the sources.

3. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg> **The mail AI assistant** wrote the new draft. Claude Code read it and told us what it said:

   > I am afraid I still don't have any information about Korean home made food.

</div>

<div class="quiz">

**Quiz.** Claude Code reached its own finish line. Is the job done?

<ul>
<li>Yes: "Kimchi for Monday" is among the sources, as Claude Code checked</li>
<li data-right>Not for you: you wanted a reply that uses the kimchi mail</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Not for you.** You decide what "done" means. Claude Code kept its word: it checked what it said it would check.
But its finish line was smaller than yours. With your finish line, Claude Code can check its work against what you
want: when the check fails, Claude Code fixes and checks again.

</details>

</div>

<div class="quiz">

**Quiz.** Which finish line should we have given Claude Code?

<ul>
<li>You are done when "Kimchi for Monday" is among the sources.</li>
<li>You are done when the search works better.</li>
<li>You are done when the copy of the flow runs without an error.</li>
<li data-right>You are done when the draft for my mail "Is there any Korean home made food?" mentions the kimchi from the mail "Kimchi for Monday".</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**The draft mentions the kimchi.** This finish line names one input, your mail, and what should come out: a draft
that mentions the kimchi. Claude Code can run the copy and check that by itself. The other three are not enough:

- "Among the sources" is the finish line that Claude Code set itself: the draft still had no kimchi in it.
- "Works better" gives Claude Code nothing to check.
- "Without an error" says that the flow runs, not that the draft is right.

</details>

</div>

<figure class="hx hx-loop" data-mode="none" aria-label="Work, check, fix"><div class="hx-switch" role="group" aria-label="Finish line"><button type="button" data-mode="none" aria-pressed="true">Claude Code’s finish line</button><button type="button" data-mode="line" aria-pressed="false">Your finish line</button></div><div class="hx-loop__body"><div class="hx-ring" aria-hidden="true"><span class="n n1">Work</span><span class="n n2">Check</span><span class="n n3">Fix</span><span class="exit">Stop</span><i class="dot"></i></div><div class="hx-loop__text"><p class="hx-pick" data-for="none"><strong>Claude Code’s finish line:</strong> "Kimchi for Monday appears in the sources." The check passes, and Claude Code stops. The draft still says that there is no information about Korean food.</p><p class="hx-pick" data-for="line"><strong>Your finish line:</strong> "The draft mentions the kimchi." Now the same run fails the check, so Claude Code is not done yet: it fixes and checks again.</p></div></div><figcaption>Click the two finish lines. The dot is Claude Code at work. The check decides: stop, or fix and go round again.</figcaption></figure>

**Ask for proof.** When Claude Code says that it is done, ask: "Show me what you ran and what came out." "It works"
alone tells you little, and reading the output is faster than checking the work yourself.

Done: you can tell Claude Code's finish line from yours.

**Next time.** Add two sentences to your next prompt: "You are done when …", with one input and what should come
out, and "Show me what you ran and what came out."

*From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run): give Claude a check to run, and ask for evidence.*

### 5. Tell Claude Code what it cannot see

Claude Code can read your files, and in the course also your flows, your workflows and your database. It cannot
read your head: what went wrong, where to look, what must stay as it is, and what you want back.

In the last homework, [step 12](/abp/ws2/hw2-recommended/#12-let-claude-code-find-the-cause) gave Claude Code this
prompt:

> My mail AI assistant drafted a reply to my mail "Is there any Korean home made food?" without the mail "Kimchi for
> Monday", which is in the database. Find out why.
>
> Look at:
>
> - the last run of WS2.4 - Reply with Approval in n8n: what it sent to the Langflow flow Draft Reply (Enron), and
>   what came back as sources;
> - the code of the component Mail Search in that flow.
>
> Do not change anything. Then explain the cause to me in plain words.

This prompt tells Claude Code what it cannot see. Look at its pieces:

<div class="quiz match">

**Quiz.** What does each piece tell Claude Code? Match each piece of the prompt with what it says.

| Piece of the prompt | What it tells Claude Code |
|---|---|
| "drafted a reply to my mail … without the mail 'Kimchi for Monday', which is in the database" | What went wrong |
| "the last run of WS2.4 - Reply with Approval in n8n", "the code of the component Mail Search in that flow" | Where to look, with full names |
| "Do not change anything." | What must stay as it is |
| "explain the cause to me in plain words" | What you want back |

<details class="more">
<summary>Why</summary>

Each piece is something that Claude Code cannot see by itself. With all four, Claude Code knows what went wrong,
where to look, what to leave alone, and what to give you back. The recipe below has the same pieces. Its last piece,
the finish line, says what you want back, in a way that Claude Code can check.

</details>

</div>

**Your turn.** Make the prompt "Fix the reply." as good as the one above: in the picture below, add the four pieces,
one after the other.

<figure class="hx hx-build" aria-label="A better prompt, piece by piece"><div class="hx-build__keys" role="group" aria-label="Add a piece"><button type="button" data-k="0" aria-pressed="false">+ What goes wrong</button><button type="button" data-k="1" aria-pressed="false">+ Where to look</button><button type="button" data-k="2" aria-pressed="false">+ What must stay</button><button type="button" data-k="3" aria-pressed="false">+ Your finish line</button></div><div class="hx-build__prompt"><p>Fix the reply.</p><ol><li data-k="0"><b>What goes wrong</b> The draft for my mail "Is there any Korean home made food?" says that there is no information about Korean food, but the mail "Kimchi for Monday" is in the database.</li><li data-k="1"><b>Where to look</b> Look at the Langflow flow Draft Reply (Enron), and at the last run of WS2.4 - Reply with Approval in n8n.</li><li data-k="2"><b>What must stay</b> Do not change the original flow: work on a copy.</li><li data-k="3"><b>Your finish line</b> You are done when the draft for that mail mentions the kimchi from the mail "Kimchi for Monday". Show me what you ran and what came out.</li></ol></div><div class="hx-build__meter"><span>How much Claude Code has to guess</span><i><u></u></i><em aria-live="polite">a lot</em></div><figcaption>An example, from the kimchi case. Click the four pieces: each one tells Claude Code something that it cannot see.</figcaption></figure>

<details class="more">
<summary>A recipe for your own prompts</summary>

<div class="cmd cmd-claude">

```
<What goes wrong, with one example>.
Look at <the full name of the file, or of the flow or workflow and whether it is in Langflow or in n8n>.
Do not change <what must stay as it is>.
You are done when <how you will know that it worked>.
```

</div>


Is there a file that Claude Code should read, for example `plan.md` from step 3? Type `@` and the file's name in
your prompt: the tool adds the file to your prompt.

</details>

<details class="more">
<summary>Side note: first the smallest version, then the next step</summary>

Claude Code reads a request carefully and builds the smallest thing that does the job: it cannot see how much you
hoped for. Often that is just right: you check the small version, then you ask for the next step, and so on. When
you know from the start that you want more, say so, for example: "be ambitious: also handle mails without a
signature".

</details>

Done: you turned "Fix the reply." into a prompt that tells Claude Code what it cannot see.

**Next time.** In your next prompt, write what went wrong with one example, and the full name of the file, flow or
workflow.

*From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt): write a specific prompt.*

**Next: [Part C · Stay in control →](/abp/ws2/hw3-c/)**

## If something goes wrong

Find your step. Still stuck? In the course, write to Frank: then we fix it together.

#### Step 3

| What you see | What to do |
|---|---|
| Claude Code starts to build the page, not only the plan | Press **Esc**, and write: "Only plan: write plan.md, and build nothing." |
| After the interview, there is no `plan.md` | Ask Claude Code: "Write the plan to plan.md." |
