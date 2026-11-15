---
title: "Block 3 · Let Claude Code improve the search flow"
---

Your page asks the Langflow flow Ask Mailbox, through WS2.11. Now Claude Code makes that flow better. It works on a
copy, so that the original keeps running while you test.

### Choose what to improve

Think of the answer your page gave in block 2. What should be better? Take one of these ideas, or your own:

- **Shorter, with sources:** at most three sentences, then the mails it used, one line each: date, sender, subject.
- **Search wider:** the search returns twice as many mail threads.
- **Search again:** if the first search finds little, search again with other words. At most three searches, then
  answer.

### Let Claude Code make the copy and change it

1. Copy this request into Claude Code, but do not press Enter yet. Claude Code shows a long paste as one short line,
   for example `[Pasted text #1 +11 lines]`: that is fine. Type your change after it, for example
   *Search wider: the search returns twice as many mail threads.* Then press Enter. The request has four parts: which
   flow, what must stay, how you check, and at the end your change.

   ```
   Make a copy of the Langflow flow Ask Mailbox (Enron) and name it
   "Ask Mailbox (Enron) - v2", with the endpoint name enron-ask-mailbox-v2.
   Put the copy into the same Langflow project (folder) as the original.

   In the copy, check every component that needs an OpenRouter API key: it must use
   the global variable OPEN_ROUTER_API_KEY. If the key is missing, set it.

   Do not change the original flow, and do not change n8n yet.
   Tell me how to test the copy in the Playground.

   In the copy only, change this:
   ```

2. Claude Code asks before each step. Read what it wants to do, then agree.

### Test the copy

1. Reload Langflow in your browser. Open your project `WS2 - Mail Assistant (Enron)`. The copy *Ask Mailbox (Enron) - v2* is next to the original.
2. Open the copy, click **Playground**, and ask the same question:

   ```
   Who arranges tours of the Enron trading floor?
   ```

3. Is the answer better than on your page? If not, tell Claude Code what is still wrong. Then test again.

### Switch it on

Your page still asks the original flow. Now let it ask the copy.

1. In Claude Code, send this:

   ```
   Point my n8n workflow WS2.11 - Ask to the copy: in its node fetch_ask_mailbox,
   call the endpoint enron-ask-mailbox-v2 in place of enron-ask-mailbox.
   Change nothing else.
   ```

2. Claude Code changes the workflow and asks you to publish it. Only Publish changes what runs. Publish it yourself:
   in n8n, reload the page and open `WS2.11 - Ask`. Click **Publish** at the top. In the window that opens, click
   **Publish** again. Or tell Claude Code: `Publish WS2.11 - Ask.`
3. Reload your page, <http://localhost:8080/ask.html>, and ask the same question.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **Your page answers with your better flow, and the original is unchanged.** You improved an AI flow without risk:
Claude Code changed a copy, you tested it, and you switched it on. This is how you change anything that already runs.
Before Claude Code changes a flow or a workflow, it also saves a copy as a file in `~/kingo-pod/claude/backups/`.

<div class="quiz">

**Quiz.** The copy is better. Who decides that it runs?

<ul>
<li>Claude Code, by itself</li>
<li data-right>You</li>
<li>Langflow, when you save the copy</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**You.** You tested the copy, so you decide. You click **Publish** in n8n, or you tell Claude Code to publish. Claude
Code does not publish by itself: it asks you. Until you publish WS2.11 again, n8n keeps calling the original.

</details>

</div>

**Next: [Block 4 · Write your team's rules, together with Claude Code →](/abp/ws2/s2-block-4/)**
