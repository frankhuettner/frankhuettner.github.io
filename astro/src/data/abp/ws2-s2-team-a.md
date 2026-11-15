---
title: "This afternoon · Team A · KSMC: a sales engineer approves every quote"
---

Today, you play the sales engineer. Your system does the routine work. You approve every quote before it leaves.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg> your page shows · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> n8n runs the steps · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> Langflow thinks · <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> you decide

## What happens to a mail that asks for a price

1. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg> **A customer asks for a price,** by mail to your test Gmail account.
2. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n picks up the mail** and passes it to Langflow.
3. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> **Langflow sorts and reads it.** The flow *Triage with Projects (Enron)* gives the mail the action
   `quote_request`. The flow *Read Quote Request (KSMC)* finds the part number, the quantity and what the customer
   needs.
4. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n calculates the price** from your price tiers: a table with the price per unit for each range of quantities. It also
   checks fixed rules, for example: never below cost. n8n never guesses a price.
5. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n saves the quote** as a new row in the Data table `WS2.12 - KSMC - Quotes`. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/></svg> The quote waits for you.
6. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg> **Your page shows the quote.** It gets the waiting quotes from n8n.
7. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> **You decide:** **Approve and send**, or **Reject**, with a short note. Your page sends your click to n8n.
8. <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M4 22V4a1 1 0 0 1 .4-.8A6 6 0 0 1 8 2c3 0 5 2 7.333 2q2 0 3.067-.8A1 1 0 0 1 20 4v10a1 1 0 0 1-.4.8A6 6 0 0 1 16 16c-3 0-5-2-8-2a6 6 0 0 0-4 1.528"/></svg> **The result:**
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1E7B4D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><circle cx="12" cy="12" r="10"/><path d="m16 9-5.5 5.5L8 12"/></svg> Approve and send: n8n sends the quote to the customer, as a reply to their mail.
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B3261E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><circle cx="12" cy="12" r="10"/><path d="m15 9-6 6"/><path d="m9 9 6 6"/></svg> Reject: nothing is sent.

   Either way, n8n writes your decision into the row: by whom, when, and why. The templates stop here. What could
   come next? See *Ideas* in section 3.

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

The *templates* are a ready-made version of this system: two Langflow flows, three n8n workflows, two Data tables and
your page.

**Before you start**, check that you have this from the homework:

- kingo-pod runs in mode `abp`.
- Your test Gmail account is connected.
- n8n has the credentials `Langflow (Run API)`, `Mail (n8n_workshop_mail_n8n)` and `OpenRouter (chat)`.

All files you need are in your folder `ws2_s2` from this morning ([`ws2_s2.zip`](https://huettner.io/abp/ws2/ws2_s2.zip)).

1. **Langflow:** open your project `WS2 - Mail Assistant (Enron)`. Drag these two files from the folder
   `ws2_s2/langflow` onto its list of flows, as in the homework:
   - `ws2_triage_with_projects_enron.json`. In Langflow, it is called *Triage with Projects (Enron)*: a copy of your
     flow Triage (Enron) that also knows the action `quote_request`. Your own Triage (Enron) does not
     change.
   - `ws2_read_quote_request_ksmc.json`. In Langflow, it is called *Read Quote Request (KSMC)*.
2. **n8n, Data tables:** make two tables, as in Session 1. For each of them:
   1. In n8n, click **Overview** at the top left, then the tab **Data tables**. Click **Create data table**.
   2. *Data table name*: paste its name from below. Use it exactly: the workflows look for their tables by name.
   3. Pick **Import CSV**. Drop its file from the folder `ws2_s2/data` into the box.
   4. Turn on *My CSV file contains a header row*. Click **Create**.

   The first table, with the file `ws2_12_ksmc_quotes.csv`:

   ```
   WS2.12 - KSMC - Quotes
   ```

   The second, with the file `ws2_12_ksmc_price_tiers.csv`:

   ```
   WS2.12 - KSMC - Price Tiers
   ```

   The price tiers hold three made-up rows, so that you can try the workflows.
3. **n8n, workflows:** import these three from the folder `ws2_s2/n8n`:
   - `ws2_12_ksmc_quote_intake.json`
   - `ws2_12_ksmc_quote_queue.json`
   - `ws2_12_triage_new_mail_with_projects.json`

   Does a node with a credential show a warning sign? Double-click it and pick its credential: one of the three
   from *Before you start*. The three `submit_to_…` nodes show a warning too: you fix them next.

   Then open *WS2.12 - Triage New Mail with Projects*. It hands each mail to the right workflow. After the import, it
   does not know your workflows yet. Change three of its nodes:
   - Double-click `submit_to_quote_request_workflow`. In the field **Workflow**, pick *WS2.12 - KSMC - Quote Intake*.
   - Double-click `submit_to_reply_with_approval`. In the field **Workflow**, pick *WS2.4 - Reply with Approval*.
   - `submit_to_bid_workflow` is for team C. Right-click it and click **Deactivate**.
4. **n8n, switch on:**
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B3261E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M18.36 6.64A9 9 0 0 1 20.77 15"/><path d="M6.16 6.16a9 9 0 1 0 12.68 12.68"/><path d="M12 2v4"/><path d="m2 2 20 20"/></svg> Switch off the triage workflow of Session 1: open *WS2.3 - Triage New Mail*, or *WS2.3 - Triage New
     Mail - SOLUTION* if you published that one. Click the small arrow next to **Publish** at the top, then
     **Unpublish**. Why: only one triage workflow takes each new mail. The old one does not know quotes, so a request for a price
     would never reach your page.
   - <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1E7B4D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 2v10"/><path d="M18.4 6.6a9 9 0 1 1-12.77.04"/></svg> Switch on your three new workflows: in each, click **Publish** at the top. In the window that opens, click
     **Publish** again.
5. **Your page:** copy the file `ksmc_quotes.html` into the folder `claude/site` of kingo-pod.
   1. Open a new terminal window: on Windows, the app **Ubuntu** from the Start menu; on a Mac, **Cmd+N** in the
      Terminal. In it, run this line. It opens the folder `claude/site` in a window. On Windows:

      ```
      cd ~/kingo-pod && mkdir -p claude/site && cd claude/site && explorer.exe .
      ```

      On a Mac:

      ```
      cd ~/kingo-pod && mkdir -p claude/site && open claude/site
      ```

   2. Drag the file `ksmc_quotes.html` from your folder `ws2_s2/pages` into that window.
6. **Open your page:** <http://localhost:8080/ksmc_quotes.html>. Does the browser say that it cannot connect? Then the
   web server from this morning has stopped. Start it again in your second terminal window (on Windows: the app
   **Ubuntu** from the Start menu, not PowerShell), then reload the page:

   ```
   cd ~/kingo-pod && python3 -m http.server 8080 --bind 127.0.0.1 --directory claude/site
   ```

7. At the top of your page, type your name into the box *Your name*. The page saves it with every decision.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09"/><path d="M9 12a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.4 22.4 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 .05 5 .05"/></svg> **Your system is set up: your page says "No quote waits", and shows no red error message.** Your page
already talks to n8n. The test in section 2 checks the rest: your mail, Langflow and the workflows.

## 2 · Understand the templates

1. Start Claude Code in the terminal. Is it still running from this morning? Then skip this line.

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

2. Send this to Claude Code:

   ```
   Look at our n8n workflows "WS2.12 - KSMC - Quote Intake" and "WS2.12 - KSMC - Quote Queue".
   In five short lines: what happens to a mail that asks for a price, and where does a person decide?
   Change nothing.
   ```

3. Try it with a mail. From your SKKU account, send a mail to your test Gmail account. Copy the subject and the text:

   ```
   Quote for EXAMPLE-001
   ```

   ```
   Hello KSMC,
   please send us a quote for 500 units of EXAMPLE-001. They must work from -40 to 85 C.

   Ana Lopez, Acme Devices
   ```

   Wait two minutes, then click **Reload** on your page. The quote waits there, with its price and "All rules kept."
4. Decide, as the sales engineer. Type a short note (why), then click **Approve and send**. The quote moves to the tab
   *Decided*. A little later, it arrives in your SKKU inbox, as a reply to your mail.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5.8 11.3 2 22l10.7-3.79"/><path d="M4 3h.01"/><path d="M22 8h.01"/><path d="M15 2h.01"/><path d="M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/><path d="m22 13-.82-.33c-.86-.34-1.82.2-1.98 1.11c-.11.7-.72 1.22-1.43 1.22H17"/><path d="m11 2 .33.82c.34.86-.2 1.82-1.11 1.98C9.52 4.9 9 5.52 9 6.23V7"/><path d="M11 13c1.93 1.93 2.83 4.17 2 5-.83.83-3.07-.07-5-2-1.93-1.93-2.83-4.17-2-5 .83-.83 3.07.07 5 2Z"/></svg> **Your first quote went out, and you approved it.** Your system did the routine work: it read the mail, found the
part and calculated the price. The decision stayed with a person: nothing left without the sales engineer's OK.

<div class="quiz match">

**Who does what?** For each step: Langflow, n8n, or a person on your page?

| Step | Who |
|---|---|
| Picks up each new mail | n8n |
| Decides that the mail asks for a price | Langflow |
| Finds the part number and the quantity in the mail | Langflow |
| Calculates the price from your price tiers | n8n |
| Approves the quote, so that it is sent | A person, on your page |

<details class="more">
<summary>Why</summary>

n8n picks up each mail and follows fixed rules: it calculates the price the same way every time. Langflow reads the
text: it sorts the mail and finds the values. Before anything leaves the company, a person decides.

</details>

</div>

## 3 · Change the templates for your team

**Why these tools?**

- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3864" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/></svg> **n8n for the fixed rules.** They need no AI. A fixed rule gives the same answer every time. You can test it.
  And it shows why it decided, for example "price 1 USD is below cost (1.2 USD): never quote it".
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 01-3-4 4.17 4.17 0 01-3 4"/><path d="M17.707 6.294A3 3 0 1012 5a3 3 0 10-5.707 1.294"/><path d="M17.996 5.125a4 4 0 012.526 5.77"/><path d="M18 18a4 4 0 002-7.465"/><path d="M19.967 17.482a4 4 0 11-7.967.517 4 4 0 11-7.967-.517"/><path d="M6 18a4 4 0 01-2-7.465"/><path d="M6.004 5.125a4 4 0 00-2.526 5.77"/></svg> **Langflow for the reading.** A customer writes in their own words. Only an AI model turns that into a part
  number, a quantity and what they need.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="m16 11 2 2 4-4"/><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> **A person for the decision.** A quote is a promise to a customer: a person takes responsibility for it.

You can split the work differently. Some rules need judgement, for example "Does the chip fit what the customer
needs, like -40 to 85 C?" A fixed rule cannot check that well. For such a rule, let Langflow judge and write a note
on your page. The sales engineer still decides.

Now make the templates fit your team's process. Claude Code changes copies of your workflows and flows, and the
originals keep running. You test a copy. Then you switch to it, as in block 3 this morning: Claude Code tells you how.

Copy this request into Claude Code, but do not press Enter yet. Claude Code shows a long paste as one short line:
that is fine. Type after it what is different in your team: a rule, a field, a step, or who decides. For example:
*A quote above 10,000 USD also needs the head of sales.* Then press Enter.

```
Our project is KSMC Semiconductor Sales. Change copies of our workflows and flows, one step at a time.
Before each change, show me what you will change. Then tell me how to test a copy, and how to
switch from the original to the copy. We publish ourselves.
Our process differs from the templates like this:
```

**Ideas**, if you need one. The first two go on where the templates stop:

- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></svg> **A polite no:** on **Reject**, n8n mails the customer a short answer. Langflow writes it, and you approve it.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#124633" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg> **Into a database:** n8n also writes each approved quote into a table in Postgres, the database in kingo-pod.
  Other programs can read it there. Claude Code helps you set up the connection.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2"/><path d="M5 3 2 6"/><path d="m22 6-3-3"/><path d="M6.38 18.7 4 21"/><path d="M17.64 18.67 20 21"/></svg> **A morning mail:** every morning, n8n mails the sales engineer the quotes that have waited longer than two days.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M13.172 2a2 2 0 0 1 1.414.586l6.71 6.71a2.4 2.4 0 0 1 0 3.408l-4.592 4.592a2.4 2.4 0 0 1-3.408 0l-6.71-6.71A2 2 0 0 1 6 9.172V3a1 1 0 0 1 1-1z"/><path d="M2 7v6.172a2 2 0 0 0 .586 1.414l6.71 6.71a2.4 2.4 0 0 0 3.191.193"/><circle cx="10.5" cy="6.5" r=".5" fill="currentColor"/></svg> **Your real price tiers,** from your project data: `ksmc_pricing_tiers.csv`. First copy the file into
  `~/kingo-pod/claude`: Claude Code reads only kingo-pod. Then ask Claude Code how to load it into the Data table.
- <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg> **A chip finder:** a customer names no part number? A Langflow agent of your own suggests the right chip.
