---
title: "This afternoon · Team C · K-Motor: the buyer decides on every bid"
---

Today, you play the buyer. Your system does the routine work. You decide on every bid.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg> your page shows · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> n8n runs the steps · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> Langflow thinks · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> you decide

## What happens to a bid

1. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg> **A supplier sends a bid,** by mail to your test Gmail account.
2. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n picks up the mail** and passes it to Langflow.
3. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> **Langflow sorts and reads it.** The flow *Triage with Projects (Enron)* gives the mail the action `bid`. The
   flow *Read Bid (K-Motor)* finds the supplier (its vendor ID, for example V-0015), the part, the unit price, the
   minimum order and the lead time.
4. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n checks the bid** against fixed rules. Is the supplier on the approved-vendor list for this part (the
   roster), active, and with a contract that has not ended? Is the price at most 20 % above the median of past bids for
   this part? n8n does not guess.
5. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n saves the bid** as a new row in the Data table `WS2.12 - K-Motor - Bids`. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg> The bid waits for you.
6. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg> **Your page shows the bid,** with every rule it breaks. It gets the waiting bids from n8n.
7. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> **You decide:** **Approve** or **Reject**, with a short note. Your page sends your click to n8n.
8. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M4 22V4a1 1 0 0 1 .4-.8A6 6 0 0 1 8 2c3 0 5 2 7.333 2q2 0 3.067-.8A1 1 0 0 1 20 4v10a1 1 0 0 1-.4.8A6 6 0 0 1 16 16c-3 0-5-2-8-2a6 6 0 0 0-4 1.528"/></svg> **The result:** n8n writes your decision into the row: approved or rejected, by whom, when, and why. The
   templates stop here: no mail goes to the supplier, and nothing is ordered. What could come next? See *Ideas* in
   section 3.

## New to n8n? Four words

You built most of your work in Langflow. These n8n words you need today:

- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **Workflow:** a chain of steps in n8n. Each step is a *node*. Like a flow in Langflow.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1E7B4D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 2v10"/><path d="M18.4 6.6a9 9 0 1 1-12.77.04"/></svg> **Publish:** switches a workflow on. A Langflow flow answers whenever someone calls it. An n8n workflow is
  different: it runs by itself only once you publish it. Then it waits for new mails, or for your page, all day.
  **Unpublish** switches it off. Changed a published workflow? Publish it again: n8n runs only the published version.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 3v18"/><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/></svg> **Data table:** a simple table inside n8n, like a spreadsheet. Workflows read and write its rows.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M18 16.98h-5.99c-1.1 0-1.95.94-2.48 1.9A4 4 0 0 1 2 17c.01-.7.2-1.4.57-2"/><path d="m6 17 3.13-5.78c.53-.97.1-2.18-.5-3.1a4 4 0 1 1 6.89-4.06"/><path d="m12 6 3.13 5.73C15.66 12.7 16.9 13 18 13a4 4 0 0 1 0 8"/></svg> **Webhook:** a node with a web address. It waits until your page sends something, as *WS2.11 - Ask* did
  for your page this morning.

## 1 · Set up the templates

The *templates* are a ready-made version of this system: two Langflow flows, three n8n workflows, three Data tables
and your page.

**Before you start**, check that you have this from the homework:

- kingo-pod runs in mode `abp`.
- Your test Gmail account is connected.
- n8n has the credentials `Langflow (Run API)`, `Mail (n8n_workshop_mail_n8n)` and `OpenRouter (chat)`.

All files you need are in your folder `ws2_s2` from this morning ([`ws2_s2.zip`](https://huettner.io/abp/ws2/ws2_s2.zip)).

1. **Langflow:** open your project `WS2 - Mail Assistant (Enron)`. Drag these two files from the folder
   `ws2_s2/langflow` onto its list of flows, as in the homework:
   - `ws2_triage_with_projects_enron.json`. In Langflow, it is called *Triage with Projects (Enron)*: a copy of your
     flow Triage (Enron) that also knows the action `bid`. Your own Triage (Enron) does not change.
   - `ws2_read_bid_k_motor.json`. In Langflow, it is called *Read Bid (K-Motor)*.
2. **n8n, Data tables:** make three tables, as in Session 1. For each of them:
   1. In n8n, click **Overview** at the top left, then the tab **Data tables**. Click **Create data table**.
   2. *Data table name*: paste its name from below. Use it exactly: the workflows look for their tables by name.
   3. Pick **Import CSV**. Drop its file from the folder `ws2_s2/data` into the box.
   4. Turn on *My CSV file contains a header row*. Click **Create**.

   The first table, with the file `ws2_12_k_motor_bids.csv`:

   ```
   WS2.12 - K-Motor - Bids
   ```

   The second, with the file `ws2_12_k_motor_roster.csv`:

   ```
   WS2.12 - K-Motor - Roster
   ```

   The third, with the file `ws2_12_k_motor_prices.csv`:

   ```
   WS2.12 - K-Motor - Prices
   ```

   Roster and Prices come from your project data: the list of approved suppliers, and the median price of each part
   in the 2,500 past bids. Most contracts in the roster have already ended: most bids break that rule.
3. **n8n, workflows:** import these three from the folder `ws2_s2/n8n`:
   - `ws2_12_k_motor_bid_intake.json`
   - `ws2_12_k_motor_bid_queue.json`
   - `ws2_12_triage_new_mail_with_projects.json`

   Does a node with a credential show a warning sign? Double-click it and pick its credential: one of the three
   from *Before you start*. The three `submit_to_…` nodes show a warning too: you fix them next.

   Then open *WS2.12 - Triage New Mail with Projects*. It hands each mail to the right workflow. After the import, it
   does not know your workflows yet. Change three of its nodes:
   - Double-click `submit_to_bid_workflow`. In the field **Workflow**, pick *WS2.12 - K-Motor - Bid Intake*.
   - Double-click `submit_to_reply_with_approval`. In the field **Workflow**, pick *WS2.4 - Reply with Approval*.
   - `submit_to_quote_request_workflow` is for team A. Right-click it and click **Deactivate**.
4. **n8n, switch on:**
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B3261E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M18.36 6.64A9 9 0 0 1 20.77 15"/><path d="M6.16 6.16a9 9 0 1 0 12.68 12.68"/><path d="M12 2v4"/><path d="m2 2 20 20"/></svg> Switch off the triage workflow of Session 1: open *WS2.3 - Triage New Mail*, or *WS2.3 - Triage New
     Mail - SOLUTION* if you published that one. Click the small arrow next to **Publish** at the top, then
     **Unpublish**. Why: only one triage workflow takes each new mail. The old one does not know bids, so a bid
     would never reach your page.
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1E7B4D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 2v10"/><path d="M18.4 6.6a9 9 0 1 1-12.77.04"/></svg> Switch on your three new workflows: in each, click **Publish** at the top. In the window that opens, click
     **Publish** again.
5. **Your page:** copy the file `kmotor_bids.html` into the folder `claude/site` of kingo-pod.
   1. Open a new terminal window: on Windows, the app **Ubuntu** from the Start menu; on a Mac, **Cmd+N** in the
      Terminal. In it, run this line. It opens the folder `claude/site` in a window. On Windows:

      ```
      cd ~/kingo-pod && mkdir -p claude/site && cd claude/site && explorer.exe .
      ```

      On a Mac:

      ```
      cd ~/kingo-pod && mkdir -p claude/site && open claude/site
      ```

   2. Drag the file `kmotor_bids.html` from your folder `ws2_s2/pages` into that window.
6. **Open your page:** <http://localhost:8080/kmotor_bids.html>. Does the browser say that it cannot connect? Then the
   web server from this morning has stopped. Start it again in your second terminal window (on Windows: the app
   **Ubuntu** from the Start menu, not PowerShell), then reload the page:

   ```
   cd ~/kingo-pod && python3 -m http.server 8080 --bind 127.0.0.1 --directory claude/site
   ```

7. At the top of your page, type your name into the box *Your name*. The page saves it with every decision.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09"/><path d="M9 12a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 .05 5 .05"/></svg> **Your system is set up: your page says "No bid waits", and shows no red error message.** Your page
already talks to n8n. The test in section 2 checks the rest: your mail, Langflow and the workflows.

## 2 · Understand the templates

1. Start Claude Code in the terminal. Is it still running from this morning? Then skip this line.

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

2. Send this to Claude Code:

   ```
   Look at our n8n workflows "WS2.12 - K-Motor - Bid Intake" and "WS2.12 - K-Motor - Bid Queue".
   In five short lines: what happens to a bid that arrives by mail, and where does a person decide?
   Change nothing.
   ```

3. Try it with a mail. From your SKKU account, send a mail to your test Gmail account. Copy the subject and the text:

   ```
   Offer P-0001
   ```

   ```
   Vendor V-0015 offers P-0001 at 7,900 USD per unit, minimum order 100, lead time 30 days.
   ```

   Wait two minutes, then click **Reload** on your page. The bid waits there. It lists the rules it breaks: the
   supplier is not approved for P-0001, and the price is far above the median.
4. Decide, as the buyer. Type a short note (why), then click **Approve** or **Reject**. The bid moves to the tab
   *Decided*, with your name and your note.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5.8 11.3 2 22l10.7-3.79"/><path d="M4 3h.01"/><path d="M22 8h.01"/><path d="M15 2h.01"/><path d="M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/><path d="m22 13-.82-.33c-.86-.34-1.82.2-1.98 1.11c-.11.7-.72 1.22-1.43 1.22H17"/><path d="m11 2 .33.82c.34.86-.2 1.82-1.11 1.98C9.52 4.9 9 5.52 9 6.23V7"/><path d="M11 13c1.93 1.93 2.83 4.17 2 5-.83.83-3.07-.07-5-2-1.93-1.93-2.83-4.17-2-5 .83-.83 3.07.07 5 2Z"/></svg> **You decided on your first bid, with all the facts on one page.** Your system did the routine work: it read the
mail and checked the roster and the price. The buyer did one thing: decide.

<div class="quiz match">

**Who does what?** For each step: Langflow, n8n, or a person on your page?

| Step | Who |
|---|---|
| Picks up each new mail | n8n |
| Decides that the mail is a bid | Langflow |
| Finds the supplier, the part and the price in the mail | Langflow |
| Checks the bid against the roster and the median price | n8n |
| Approves or rejects the bid | A person, on your page |

<details class="more">
<summary>Why</summary>

n8n picks up each mail and follows fixed rules: it checks the roster and the price the same way every time.
Langflow reads the text: it sorts the mail and finds the values. The buyer decides on every bid.

</details>

</div>

## 3 · Change the templates for your team

**Why these tools?**

- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n for the fixed rules.** They need no AI. A fixed rule gives the same answer every time. You can test it.
  And it shows why it decided, for example "V-0015 is not on the approved-vendor list for P-0001".
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> **Langflow for the reading.** A supplier writes in their own words. Only an AI model turns that into supplier,
  part, price, minimum order and lead time.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> **A person for the decision.** A bid can become a contract: a buyer takes responsibility for it.

You can split the work differently. Some rules need judgement, for example "Are the supplier's payment or warranty
terms unusual?" A fixed rule cannot check that well. For such a rule, let Langflow judge and write a note on your
page. The buyer still decides.

Now make the templates fit your team's process. Claude Code changes copies of your workflows and flows, and the
originals keep running. You test a copy. Then you switch to it, as in block 3 this morning: Claude Code tells you how.

Copy this request into Claude Code, but do not press Enter yet. Claude Code shows a long paste as one short line:
that is fine. Type after it what is different in your team: a rule, a field, a step, or who decides. For example:
*A bid above 100,000 USD also needs the head of procurement.* Then press Enter.

```
Our project is K-Motor Procurement. Change copies of our workflows and flows, one step at a time.
Before each change, show me what you will change. Then tell me how to test a copy, and how to
switch from the original to the copy. We publish ourselves.
Our process differs from the templates like this:
```

**Ideas**, if you need one. The first two go on where the templates stop:

- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></svg> **Answer the supplier:** after your decision, n8n mails the supplier, as a reply to their bid. Langflow writes
  the text, and you approve it.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#124633" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg> **Into a database:** n8n also writes each approved bid as an order into a table in Postgres, the database in
  kingo-pod. Other programs can read it there. Claude Code helps you set up the connection.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2"/><path d="M5 3 2 6"/><path d="m22 6-3-3"/><path d="M6.38 18.7 4 21"/><path d="M17.64 18.67 20 21"/></svg> **A morning mail:** every morning, n8n mails the buyer the approved suppliers whose contracts end within 30 days.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m16 9-5.5 5.5L8 12"/></svg> **Certificates:** your project data names the certificates a supplier needs, in the folder
  `3_part_specifications`. First copy it into `~/kingo-pod/claude`: Claude Code reads only kingo-pod. Then ask Claude
  Code for a rule that checks them.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg> **A question back:** a bid names no minimum order? A Langflow agent of your own writes the supplier a short
  question.
