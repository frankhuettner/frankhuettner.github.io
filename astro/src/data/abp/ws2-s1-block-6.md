---
title: "Block 6 · Why we put the human in the loop in WS2.4"
---

Nothing to build. You look at what happened to your mail from block 3, and keep one list short.

1. Open `WS2.4 - Reply with Approval`, then the tab **Executions**.
2. Click the run of your mail from block 3.
3. Double-click the nodes, one after the other:

   | Node | What it does |
   |---|---|
   | `get_mail`, `if_draft_given` | the mail from the database; a workflow that calls WS2.4 may bring its own draft |
   | `format_mail_as_text`, `transform_mask_personal_numbers` | the mail as text, personal numbers masked |
   | `fetch_flow_list`, `fetch_draft_reply_flow`, `set_draft_reply_ids` | Langflow gave each part of your flow a new id when you uploaded it, so n8n reads the ids here, from the flow itself: which *Text Input* takes the mail, which the date |
   | `fetch_draft_reply` | the Langflow flow Draft Reply: Kaminski's earlier mails up to the mail's date, never a confidential one; it checks its own draft (*Check Draft*) |
   | `check_draft`, `if_draft_fine` | a draft, and someone to send it to; Draft Reply's verdict goes onto the approval form |
   | `post_proposal_to_outbox` | a row in `outbox`, status `proposed` |
   | `wait_for_approval` | the form, with the draft in a field to edit; the run waits for you |
   | `post_approve`, `post_reject` | your decision into the database; the mail service sends what is approved |

**The agent cannot send.** No Langflow flow has a tool for that. Fixed rules check the draft, a person approves, and
the database allows only that order.

4. Keep the approvals page's list of runs short:
   1. Open `WS2.4 - Approvals Page`.
   2. Open the menu **…** at the top, next to its name, then **Settings**.
   3. Set *Save successful production executions* to **Do not save**, then click **Save**.

   <small>The approvals page is a workflow of its own, so its runs stay out of WS2.4's list. It reloads every 15
   seconds, and each reload is a run: 240 an hour. Does that break the rule that you can show every run and every
   decision later? No: the page only shows, it decides nothing. The decisions stay in WS2.4's runs and in `outbox`,
   with who approved, when, and why. And n8n still keeps the page's failed runs.</small>

   <small>Want to see one run of the page? In `WS2.4 - Approvals Page`, click **Execute workflow**. Then open its Test
   URL once: in the node `webhook_open_approvals`, *Webhook URLs*, then *Test URL*. n8n keeps the runs you start by
   hand.</small>

## If something goes wrong

Still stuck? Ask Frank.

#### Block 6

| What you see | What to do |
|---|---|
| The approvals page shows "No draft waits" although WS2.4 waits | The page shows drafts with the status `proposed`. Open WS2.4, tab *Executions*: did the run reach `wait_for_approval`? |

## Go deeper, in your own time

<div class="fine">

n8n's own courses are free and go further. Two that fit this morning, with a free account on learn.n8n.io:

- [n8n Quickstart](https://learn.n8n.io/courses/course-v1:n8n+QS101+2026H2/about), part *Working with data*: how data
  moves between nodes, expressions such as `$('get_mail').item.json.subject`, and the three ways to handle an error.
- [In Practice: AI, Testing & Best Practices](https://learn.n8n.io/courses/course-v1:n8n+N8N103+2026H2/about), section
  *Testing & Debugging*: *Common Error Types* and *Pinning Data for Testing*. The best tip there: pin the output of the
  last node that works, then *Execute step*.

</div>

**Next: [Appendix · contracts between your tools →](/abp/ws2/s1-appendix/)**
