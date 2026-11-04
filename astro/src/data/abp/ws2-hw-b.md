---
title: "Homework, Part B: Test Langflow"
lede: "Step 8: load the course flows, let Triage sort a mail."
---


<figure class="bp bp-setup bp-mini" aria-label="Where you are: Part B"><div class="bp-sys"><div class="bp-node mail done"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Gmail</b><span>your test Gmail account</span><em>Part A · steps 1–7 ✓</em></div><div class="bp-node box done"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></span><b>Mail</b><span>kingo-pod's service: copies the mails, masks addresses</span><em>Part A · steps 1–7 ✓</em></div><div class="bp-node db done"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span><b>PostgreSQL</b><span>every mail as a row</span><em>Part A · steps 1–7 ✓</em></div><div class="bp-node muscle later"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>does the work</span><em>Part C · steps 9–13</em></div><div class="bp-node brain now"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow</b><span>thinks: sorts and drafts</span><em>Part B · step 8 · you are here</em></div><div class="bp-part pa done">Part A · steps 1–7 ✓</div><div class="bp-part pc later">Part C · steps 9–13</div><div class="bp-part pb now">Part B · step 8 · you are here</div></div></figure>

### 8. Test Langflow: load the course flows and let Triage sort a mail

This part checks that Langflow works with the OpenRouter key Yanbo gave you, and with the flows of the course.

We prepared a Langflow flow for you: **Triage (Enron)**. It reads one mail and decides what to do with it: `reply`,
`calendar`, `forward` or `archive`. On 9 November, your AI assistant will use this flow for every new mail. Now you
test it by hand.

Open Langflow: <http://localhost:7860>.

1. **Check your key.** Langflow needs the OpenRouter key Yanbo gave you. Langflow keeps keys as **global variables**:
   you enter a key once, and every flow can use it.
   - Click your profile icon (top right) → **Settings** → **Global Variables**.
   - Is there a variable called `OPEN_ROUTER_API_KEY`? Then go on with step 8.2.
   - If not, click **Add New**. Name: `OPEN_ROUTER_API_KEY`. Type: **Credential** (then Langflow hides the key on
     screen). Value: your key. Save.
   - More help: [Langflow: Global variables](https://docs.langflow.org/configuration-global-variables)
2. **Get the course files.** Download [`ws2_hw.zip`](https://huettner.io/abp/ws2/ws2_hw.zip) and unzip it. You get
   a folder `ws2_hw` with two folders inside (`langflow` and `n8n`) and a readme. Every name starts with `ws2_`, for
   Workshop II. You need them now and in [Part C](/abp/ws2/hw-c/).
3. **Load the Langflow flows.** Make a new project called `WS2 - Mail Assistant (Enron)`. Open the folder
   `ws2_hw/langflow` (from step 8.2) next to your browser. Select all four files in it and drag them onto the page of
   your new project, where its flows are listed (not into an open flow). Langflow loads all four at once.
   Or use the small button with an arrow pointing up, next to **Projects** in the left column. It says
   *Upload a flow* when you point at it.
4. **Give the flow a mail.** Open the flow `Triage (Enron)`. Copy this mail into the box **Text** of the component
   **Text Input**:

   ```
   From: Thomas Gygax <thomas.gygax@enron.com>
   To: Vince J Kaminski
   Date: Wed, 09 May 2001 03:49:00 GMT
   Subject: Clewlow/Strickland, "Energy Derivatives"

   Dear Vince,

   I'm working in the Continental Power Structured Products group here in London, and we'd like to use the
   Clewlow/Strickland book "Energy Derivatives. Pricing & Risk Management".
   Is there such a thing as an "Enron discount", and if so, how should we purchase the book (two copies) to get it?

   Thanks,
   THOMAS.
   ```

   If you see a yellow note "Legacy" on Text Input or Text Output, ignore it. If Langflow says *Flow needs review*,
   click **Dismiss All**.
5. **Run it.** On the component **Text Output**, click ▶ (*Run component*). Wait a few seconds. Then click the small
   icon next to **Output Text** (*Inspect output*). You see `"action": "reply"` and a short reason after `"why"`.
   Thomas asks a question, so the AI assistant would draft an answer. At the end you see `"checks_ok": true`: the
   component **Check Triage** checked the answer before it left Langflow.
6. **Change the mail.** Replace the whole text in **Text Input** with this mail. Run it again:

   ```
   From: Thomas Gygax <thomas.gygax@enron.com>
   To: Vince J Kaminski
   Date: Wed, 09 May 2001 03:49:00 GMT
   Subject: Meeting next Tuesday

   Dear Vince,

   I'm working in the Continental Power Structured Products group here in London. I will be in Houston next week.
   Could we meet on Tuesday at 10 am in your office?

   Thanks,
   THOMAS.
   ```

   Now the action is `calendar`. Thomas wants a meeting, so the AI assistant would mark the mail for the
   calendar.

   Done testing? You can now delete the mail in **Text Input**. On 9 November, n8n will put in each new mail itself.

**Well done: an AI just sorted a real mail for you.** This flow is the brain of your AI assistant. On 9 November, n8n
will give it hands: n8n will notice new mail, then reach out to this Langflow flow, check the answer, and act in your
test Gmail account.

[Stuck? Help for step 8](#step-8)

**Next: [Part C · Set up n8n and test it →](/abp/ws2/hw-c/)**

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 8

| What you see | What to do |
|---|---|
| Triage shows an error | Check the name `OPEN_ROUTER_API_KEY` in Langflow. Check that your key still has credit. |
| A component says the API key is missing, or its API key field is empty | You loaded the flows before you made `OPEN_ROUTER_API_KEY`. Langflow then empties the key fields. Delete the four flows and load them again (step 8.3). |
| OpenRouter and Check Triage are not connected | At the bottom right of OpenRouter, set the menu to **Model Response**. Then drag a line from its dot to **Answer** on Check Triage. |
