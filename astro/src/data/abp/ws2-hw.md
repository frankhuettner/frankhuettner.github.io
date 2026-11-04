---
title: "Preparatory homework (3–8 November): get ready for Workshop II"
lede: "Three parts, 13 steps: your test mailbox, Langflow and n8n. At the end, your laptop is ready for 9 November. One more step, if you like, shows your mails in the database."
---

## What you will build in Workshop II

In Workshop II (9, 16 and 23 November), you will build an AI assistant for a real mailbox.

- **The mailbox:** 3,244 real mails of Vince Kaminski. He was head of research at Enron in 2001.
- **Where the mails live:** in a new Gmail account, only for the course. We call it your **test Gmail account**.
- **What the AI assistant does:** it reads new mail, sorts it, and drafts answers in Kaminski's words. It sends nothing
  without your OK.

## Your goal for 9 November

At the end of the first morning, this works on your laptop:

1. You will write a mail from your **SKKU mail account** to your test Gmail account.
2. Your AI assistant will sort the mail and draft Kaminski's answer.
3. You will read the draft and say OK.
4. The answer will arrive in your SKKU inbox.

<figure class="bp" aria-label="The path of one mail on 9 November"><ol class="bp-path"><li class="bp-stop mail"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Your SKKU account</b><span>you write to your test Gmail account</span></li><li class="bp-stop mail"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Your test Gmail account</b><span>the mail arrives</span></li><li class="bp-stop muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>picks it up, checks it</span></li><li class="bp-stop brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow: Triage</b><span>decides: reply</span></li><li class="bp-stop brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow: Draft Reply</b><span>writes in Kaminski's words, checks it</span></li><li class="bp-stop muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>checks the rules, asks you</span></li><li class="bp-stop person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/></svg></span><b>You</b><span>say OK</span></li><li class="bp-stop hot"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Your SKKU inbox</b><span>the answer arrives, from your test Gmail account</span></li></ol><figcaption><span><i class="bp-key brain"></i>Langflow thinks.</span> <span><i class="bp-key muscle"></i>n8n does the work.</span> <span><i class="bp-key person"></i>You say OK.</span></figcaption></figure>

So you work with two mail accounts: your **SKKU mail account**, which you already have, and a new
**test Gmail account**, which you make in step 2.

<details class="more">
<summary>Two ideas you know from Yanbo's workshop</summary>

- **Decomposition.** Your AI assistant is not one big AI that does everything. The job is cut into small steps, and
  each step has one task: n8n picks up the mail, Triage only sorts it, Draft Reply only writes the answer, n8n checks
  the rules, and you decide. Small steps are easy to test and to fix. On 9 November you will test Triage on its own
  first.
- **Guardrails.** Every step is checked before the next one acts. n8n looks at each new mail first: it hides personal
  numbers, and a mail that tries to trick your AI assistant goes to you instead. Langflow checks its own answer: in
  step 8 you will see `"checks_ok": true`. And nothing leaves without your OK.

</details>

## This homework: three parts, and one optional

The homework gets your laptop ready for 9 November. It has three parts, and one optional:

| Part | Steps | What you do |
|---|---|---|
| A | 1–7 | **[Set up your test mailbox](/abp/ws2/hw-a/):** update kingo-pod, make the account, copy Kaminski's mails into it |
| B | 8 | **[Test Langflow](/abp/ws2/hw-b/):** load the course flows, let Triage sort a mail |
| C | 9–13 | **[Set up n8n and test it](/abp/ws2/hw-c/):** logins, mail search, a test mail from your SKKU account |
| Optional | 14 | **[Look into the database](/abp/ws2/hw-optional/):** see Kaminski's mails and your test mail as rows, in CloudBeaver |

<figure class="bp bp-setup" aria-label="What this homework sets up"><div class="bp-sys"><div class="bp-node mail "><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Gmail</b><span>your test Gmail account</span><em>Part A · steps 1–7</em></div><div class="bp-node box "><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></span><b>Mail</b><span>kingo-pod's service: copies the mails, masks addresses</span><em>Part A · steps 1–7</em></div><div class="bp-node db "><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span><b>PostgreSQL</b><span>every mail as a row</span><em>Part A · steps 1–7</em></div><div class="bp-node muscle "><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>does the work</span><em>Part C · steps 9–13</em></div><div class="bp-node brain "><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow</b><span>thinks: sorts and drafts</span><em>Part B · step 8</em></div><div class="bp-part pa ">Part A · steps 1–7</div><div class="bp-part pc ">Part C · steps 9–13</div><div class="bp-part pb ">Part B · step 8</div></div><figcaption>What this homework sets up on your laptop: the mails go from Gmail into your database, and n8n and Langflow work with them there.</figcaption></figure>

## Before you start

- **Time:** 1 to 2 hours. Some of it is waiting while things load. You can do this with breaks or in chunks.
- **Deadline:** **Sunday, 8 November**, the day before Workshop II.
- **Want help?** Finish by **Friday, 6 November**. Then there is still time to fix problems together.
- **Stuck?** Write to Frank right away. Then we fix it together.
- **You need:**
  - your kingo-pod;
  - the OpenRouter key Yanbo gave you;
  - the file `ws2_hw.zip` from <https://huettner.io/abp/ws2/ws2_hw.zip>. You download it in step 8.

**Ready? [Start with Part A: Set up your test mailbox →](/abp/ws2/hw-a/)**
