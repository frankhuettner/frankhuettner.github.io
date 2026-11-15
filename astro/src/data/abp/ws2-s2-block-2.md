---
title: "Block 2 · Let Claude Code build your page"
---

You import a second workflow, *Ask*. It takes a question, asks Langflow, and sends the answer back. Then Claude Code
writes a web page that sends your question to *Ask*.

### Import WS2.11 - Ask

1. In n8n, import `ws2_11_ask.json` from the folder `n8n`. You get the workflow `WS2.11 - Ask`.
2. Look at its three nodes, from left to right:
   - `webhook_ask`: your page calls n8n here (a **Webhook**).
   - `fetch_ask_mailbox`: n8n calls your Langflow flow Ask Mailbox (an **HTTP Request**).
   - `send_answer`: n8n sends the answer back to your page (**Respond to Webhook**).

   Double-click `fetch_ask_mailbox`. Under *Header Auth*, it should say `Langflow (Run API)`. If not, pick it. Close
   the node.
3. Publish the workflow: click **Publish** at the top. In the window that opens, click **Publish** again.
4. Try it. Open a second terminal window:
   - **On Windows:** open the Start menu, type `Ubuntu`, and open the app **Ubuntu**. Its line ends with `$`, for
     example `mina@laptop:~$`. Does it start with `PS C:\`? That is PowerShell: close it. (The **+** in the tab bar
     opens PowerShell too.)
   - **On a Mac:** in the Terminal, press **Cmd+N**.

   Run this line in the new window. It sends a question to n8n, as your page will do later:

   ```bash
   curl -s -X POST http://localhost:5678/webhook/ask -H 'Content-Type: application/json' -d '{"question": "Who arranges tours of the Enron trading floor?"}'
   ```

   After a few seconds, you see the answer. In n8n, open the tab *Executions* of WS2.11 and click the run.
   Double-click a node to see what came in and what went out.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **Great: n8n takes a question, asks Langflow, and answers.** This is the pattern of the whole course: n8n runs the
steps, Langflow thinks. The Webhook takes the call, the HTTP Request asks Langflow. Your page only needs to know one
address.

<div class="quiz match">

**Webhook or HTTP Request?** For each case: does someone call n8n (a Webhook), or does n8n call someone (an HTTP
Request)?

| Case | Answer |
|---|---|
| A customer clicks *Send* on your page | Webhook |
| n8n asks your Langflow flow Triage what to do with a mail | HTTP Request |
| Another app tells n8n about a new order | Webhook |
| n8n asks a bank for today's exchange rate | HTTP Request |
| You open the approvals page of WS2.4 in your browser | Webhook |

<details class="more">
<summary>Why</summary>

Webhook: someone calls n8n. That is the customer's page, the other app, and your browser with the approvals page.
HTTP Request: n8n calls someone. That is Langflow, and the bank.

</details>

</div>

### If you like: three searches at once

The lecture's demo page asks three workflows at the same time. One answers at once, without AI. One answers
briefly. One searches thoroughly. You can import them too.

1. Import these three from the folder `n8n`:
   - `ws2_11_ask_peek.json`
   - `ws2_11_ask_quick.json`
   - `ws2_11_ask_deeper.json`
2. Check their credentials. In `WS2.11 - Ask - Peek`, the node `find_mails_with_the_words` needs
   `Mail (n8n_workshop_mail_n8n)`. In the other two, `fetch_ask_mailbox` needs `Langflow (Run API)`.
3. Publish all three, as above. Claude Code explains them to you in a moment.

<small>The thorough one can take up to five minutes. It also uses more of your OpenRouter credit.</small>

### Start Claude Code, and see what it can reach

1. In your first terminal window, start Claude Code:

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

2. Send this:

   ```
   What can you reach from your sandbox, and what not? Answer in five short lines:
   my files, my n8n, my Langflow, my database, the internet.
   ```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Good to know: Claude Code told you what it can reach.** It can write only in `~/kingo-pod/claude`. It can read
the rest of kingo-pod. It reaches n8n, Langflow, your database and the internet. This fence is why you can let it work:
it changes your tools, never the rest of your laptop.

### If you imported the three searches: let Claude Code explain them

1. Send this:

   ```
   Look at my n8n workflows WS2.11 - Ask - Peek, WS2.11 - Ask - Quick and WS2.11 - Ask - Deeper.
   In five short lines: what does each one do, which answers first, and which answers best?
   ```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Now you know what each search does, without opening a node.** That is the point: Claude Code reads workflows and
flows for you and explains them in plain words. Use it whenever you meet a workflow you do not know.

### Let Claude Code write the page

1. In n8n, check that `WS2.11 - Ask` is published: the **Publish** button shows a green dot.
2. Claude Code checks pages with two tools: `look` takes a picture of a page, and `clickthrough` clicks through it
   in a browser of its own. That browser cannot reach n8n, so the request asks only for `look`. In Claude Code,
   send this:

   ```
   Write a web page: site/ask.html in your folder (~/kingo-pod/claude/site/ask.html).
   I open it myself in my browser, at http://localhost:8080/ask.html, through a
   web server that I start. So do not start a server, and do not open the page.

   The page:
   - has the title "Ask your mailbox", a box for a question, a button "Ask",
     and a place for the answer; Enter in the box asks too;
   - sends the question as JSON {"question": "..."} with POST to
     http://localhost:5678/webhook/ask; the reply is JSON {"answer": "..."};
   - shows "Thinking ..." while it waits, and turns the button off until the
     answer is there; an answer may take up to three minutes;
   - shows the answer as plain text, with its line breaks, never as HTML:
     it comes from mails;
   - says in plain words when n8n does not answer.
   One file, nothing loaded from the internet.

   Then check: look at the page with look. Call my n8n workflow WS2.11 - Ask
   once yourself, with one question. Do not try the page with clickthrough:
   there it cannot reach n8n. Tell me in three short lines what you checked.
   ```

3. Claude Code writes the page, takes a picture of it with `look`, and calls your workflow once. Read its three
   lines.

### Open your page

1. You do this step, not Claude Code: Claude Code cannot open your browser, and the web server must keep running
   when Claude Code stops. In your second terminal window (on Windows: Ubuntu, not PowerShell), run this line. It starts a small web server: a program that hands your page to the browser.

   ```
   cd ~/kingo-pod && python3 -m http.server 8080 --bind 127.0.0.1 --directory claude/site
   ```

   It says *Serving HTTP on 127.0.0.1 port 8080*. Leave this window open. You need it in block 3 too.
2. In your browser, open:

   ```
   http://localhost:8080/ask.html
   ```

3. Ask your page:

   ```
   Who arranges tours of the Enron trading floor?
   ```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M10 14.66V17a1 1 0 0 1-1 1 2 2 0 0 0-2 2v2"/><path d="M14 14.66V17a1 1 0 0 0 1 1 2 2 0 0 1 2 2v2"/><path d="M17.916 10H19.5A2.5 2.5 0 0 0 22 7.5V5a1 1 0 0 0-1-1h-3"/><path d="M4 22h16"/><path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/><path d="M6.084 10H4.5A2.5 2.5 0 0 1 2 7.5V5a1 1 0 0 1 1-1h3"/></svg> **Your own page asks your mailbox!** The page shows the answer, n8n runs the steps, Langflow thinks. Claude Code
built the page in minutes. This is how you give people a simple way to use your AI: a page in front, n8n behind it.
You decide what runs.

**Want a change?** Tell Claude Code, for example: `Show my last three questions under the answer.` Then reload the
page in the browser.

<small>Why a web server, and not a double-click on the file? A browser may block a page that was opened as a file
when it calls `localhost`. A page that comes from `localhost` may call `localhost`.</small>

<div class="quiz">

**Quiz.** Your page opens, but says that n8n does not answer. What do you check first?

<ul>
<li>Whether Claude Code is still running</li>
<li data-right>Whether <code>WS2.11 - Ask</code> is published</li>
<li>Whether the web server on port 8080 runs</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Whether `WS2.11 - Ask` is published.** The page opened, so the web server runs. Claude Code only wrote the page: it
does not need to run. The address `/webhook/ask` works only while the workflow is published.

</details>

</div>

**Next: [Block 3 · Let Claude Code improve the search flow →](/abp/ws2/s2-block-3/)**
