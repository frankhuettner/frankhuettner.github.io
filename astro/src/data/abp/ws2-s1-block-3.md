---
title: "Block 3 · Your mail AI assistant answers your mail: WS2.3 and WS2.4"
---

You import three ready workflows and turn them on. Then you send a mail from your SKKU account: your mail AI
assistant sorts it, drafts an answer, waits for your OK, and sends it.

1. Import these three workflows from the folder `n8n`:
   - `ws2_4_reply_with_approval.json`
   - `ws2_4_approvals_page.json`
   - `ws2_3_triage_new_mail.json`
2. Check the credentials in WS2.4. n8n should pick them by their name, but check:
   1. Open `WS2.4 - Reply with Approval`.
   2. Double-click the node `fetch_flow_list`. Under *Header Auth*, it should say `Langflow (Run API)`. Another one, or
      none? Pick `Langflow (Run API)`. Close the node with the **✕** at the top right.
   3. Do the same in the nodes `fetch_draft_reply_flow` and `fetch_draft_reply`.
   4. Save.

   <small>A node whose name starts with `fetch_` calls another service, so it needs that service's credential. Any
   other node with a warning: pick the credential with the same name.</small>
3. Check the credential in WS2.3:
   1. Open `WS2.3 - Triage New Mail`.
   2. Double-click the node `fetch_triage`. Under *Header Auth*, it should say `Langflow (Run API)`. If not, pick it.
      Close the node.
4. Connect WS2.3 to WS2.4:
   1. Still in WS2.3, double-click the node `submit_to_reply_with_approval`.
   2. In the field **Workflow**, pick `WS2.4 - Reply with Approval`.
   3. Save.
5. Turn them on, in this order. Open each one, click **Publish** at the top, then **Publish** again in the window:

   <small>A *Production Checklist* may open, also after a reload: close it with **✕**.</small>

   1. `WS2.4 - Reply with Approval`
   2. `WS2.4 - Approvals Page`
   3. `WS2.3 - Triage New Mail`
6. Open the approvals page in a new browser tab, at this address. It says "No draft waits".

   ```
   http://localhost:5678/webhook/approvals
   ```

   <div class="fine">

   The address is in `WS2.4 - Approvals Page` too: double-click its node `webhook_open_approvals`, click *Webhook URLs* at the top, then *Production URL*.

   </div>

   <details class="more fine">
   <summary>Test URL or Production URL?</summary>

   **Production URL**, with `/webhook/`: it works while the workflow is published. Every call starts a run, and you find the run under *Executions*. Publishing is what puts a workflow into production, so the approvals page needs nothing else.

   **Test URL**, with `/webhook-test/`: it works only while you build. Click *Execute workflow*, then open the Test URL once. n8n shows that one run right on the canvas.

   </details>

7. From your SKKU account, send this mail to your test Gmail account:

   The subject:

   ```
   Steve's address
   ```

   The text:

   ```
   Dear Vince, what is Steve Leppard's email address? I need to reach him.
   ```

8. A little later, the draft appears on the approvals page. Open its approval form. The draft stands in the field
   *Text to send*: change it if you like. Then choose *approve* and give your name.
9. Kaminski's answer arrives in your SKKU inbox.

**Done: your mail AI assistant answers mail, and you stay in control.**

<details class="more fine">
<summary>What happens on the way</summary>

kingo-pod's part called Mail copies your mail from Gmail into PostgresDB. The new row wakes WS2.3: it takes the
mail, masks personal numbers, asks the Langflow flow Triage and checks the answer. For `reply` it calls WS2.4: the
Langflow flow Draft Reply drafts from Kaminski's earlier mails, n8n checks the draft, writes it into the table
`outbox` and waits for you. The mail service sends only what you approved.

</details>

<div class="fine">

**Stuck?** [Help for block 3](#block-3)

</div>

## If something goes wrong

Still stuck? Ask Frank.

#### Block 3

| What you see | What to do |
|---|---|
| No draft appears on the approvals page | Open WS2.3, tab *Executions*: which `action` did Triage choose? A mail that only informs is archived. Ask a clearer question, or run WS2.4 by hand: open WS2.4 and click *Execute workflow*. It drafts for the newest mail that WS2.3 sorted as `reply`. For another mail, put its `message_id` (WS2.3's run, node `post_result`) into the node `set_mail_to_try`, in place of `newest`. |
| WS2.3's run failed, you fixed it, and still nothing comes | WS2.3 takes each mail only once, also when its run failed. Send your mail again: a new mail is a new row. |
| In WS2.3, *Execute workflow* stops with "Aborted, no data received within 30secs" | The button started `trigger_new_mail_notify`: by hand, it waits only 30 seconds for a new mail. You need not run WS2.3 by hand: published, it runs by itself. To run it now anyway, click the small arrow next to *Execute workflow*, pick `schedule_every_15_minutes`, then click *Execute workflow*: it takes every new mail at once. |
| WS2.3 shows no run at all | WS2.3 must be published, and the mail must come from the address you allowed in homework step 6, to your test Gmail account's main address. `./kingo mail status` shows whether the mail arrived in the database. Not there? In your test Gmail account, look in *Spam*: Spam is not synced. Click *Not spam*, and the mail comes in. |
| `submit_to_reply_with_approval` gives an error | Pick the called workflow again: double-click the node and choose *WS2.4 - Reply with Approval* in the field **Workflow**. |
| In WS2.4, `get_mail` gives an error about a parameter | `set_mail_to_try` needs `newest` or a `message_id`. |
| In WS2.4, a `fetch_` node gives an error 403 | Its credential: it must be `Langflow (Run API)` (step 2). |
| In WS2.4, `fetch_draft_reply_flow` gives an error | Langflow has no flow with the endpoint `enron-draft-reply`. In Langflow, open your project `WS2 - Mail Assistant (Enron)`: is *Draft Reply (Enron)* there? If not, upload it again (homework step 8.3). |
| No answer in your SKKU inbox | Look in its spam folder first. Then on the approvals page: did you approve? In n8n, WS2.4's run: did `post_approve` run? |

**Next: [Block 4 · Challenge: all five test mails right →](/abp/ws2/s1-block-4/)**
