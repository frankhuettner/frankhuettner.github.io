---
title: "Block 5 · Let's look inside WS2.3, and make it ours"
---

### Look inside WS2.3

1. Open `WS2.3 - Triage New Mail`, then the tab **Executions** at the top: one line per run.
2. Click the run of your mail. Double-click a node: on the left what came in, on the right what went out.

   | Step | Node | What it does |
   |---|---|---|
   | Wake up | `trigger_new_mail_notify` | PostgresDB tells n8n at once: a new mail is here |
   | | `schedule_every_15_minutes` | looks every 15 minutes too, in case that message got lost |
   | Take it once | `fetch_and_claim_new_mails` | notes each new mail as taken, in the table `processed`; a mail already there is skipped, so no mail gets two answers |
   | Protect | `format_mail_as_text` | the mail as one text: sender, date, subject, body |
   | | `transform_mask_personal_numbers` | masks card and bank numbers before any model sees the mail |
   | | `check_injection` | a model asks: does the mail try to give the assistant orders? If so, a person looks at it |
   | Ask Triage | `fetch_triage` | sends the mail to your Langflow flow Triage and gets its answer |
   | | `check_triage` | n8n goes on only with an answer in order: `checks_ok` is true, and the action is one of the four. Anything else: a person looks at it |
   | Act | `post_result` | writes Triage's answer into `processed`, next to the mail |
   | | `if_confidential` | the fixed rule: a mail marked confidential only gets its label, whatever Triage proposed |
   | | `switch_by_action` | one way out per action: a label, the archive, or WS2.4 for a draft. A person looks at anything else: label *Assistant/Check* |

   <details class="more fine">
   <summary>How the wake-up call works</summary>

   When kingo-pod's part called Mail writes a new mail into PostgresDB, the database itself sends a short message on
   a channel named `n8n_workshop_mail_new`. `trigger_new_mail_notify` listens on that channel: double-click it, and
   you see *Listen For* set to *Advanced* and the *Channel Name*. So WS2.3 starts within seconds, and nobody has to
   ask every minute whether something is new.

   It listens only while WS2.3 is published. When you click *Execute workflow*, it waits only 30 seconds for a new
   mail. If a message gets lost, for example while n8n restarts,
   `schedule_every_15_minutes` takes the mail a little later. Either way, `fetch_and_claim_new_mails` takes each mail
   only once.

   </details>

### Your own rule: an urgent mail gets a star

A mail whose subject says "urgent" gets a star in Gmail.

1. Go back to the tab **Editor**.
2. From the small dot on the right of the node `check_triage`, drag a line to an empty spot: n8n opens the list of
   nodes. Pick an **If** node and name it `if_urgent`. Set it like this:

   Paste this as the value on the left:

   ```
   {{ $json.subject }}
   ```

   Choose *String*, then *contains*, and type `urgent` on the right. Under *Options*, turn *Ignore Case* on.

3. From its *true* output, add a **Postgres** node and name it `post_star`. Set it like this:

   Pick the credential `Mail (n8n_workshop_mail_n8n)` and *Execute Query*, and paste the query:

   ```sql
   INSERT INTO n8n_workshop_mail.changes (message_id, action, label) VALUES ($1, 'star', NULL);
   ```

   Under *Options*, add *Query Parameters* and paste this:

   ```
   {{ $json.message_id }}
   ```

   <details class="more fine">
   <summary>What else your rule can do in Gmail</summary>

   `post_star` writes one row into the table `changes`. kingo-pod's part called Mail reads it, makes the change in your mailbox, and Gmail shows it seconds later. The row says what to do in two words: the action, then a label. `NULL` means: no label.

   | In place of `'star', NULL` | What Gmail shows |
   |---|---|
   | `'star', NULL` | a star |
   | `'unstar', NULL` | the star taken off |
   | `'read', NULL` | the mail as read |
   | `'unread', NULL` | the mail as unread, in bold |
   | `'label', 'Urgent'` | the label *Assistant/Urgent* |
   | `'unlabel', 'Urgent'` | that label taken off |
   | `'archive', NULL` | the mail out of the inbox; it stays in *All Mail* |
   | `'inbox', NULL` | the mail back in the inbox |

   For example, the label *Assistant/Urgent* in place of the star:

   ```sql
   INSERT INTO n8n_workshop_mail.changes (message_id, action, label) VALUES ($1, 'label', 'Urgent');
   ```

   The label is a word of your own: letters, digits, spaces, `-` and `_`, up to 40 characters. Gmail shows it under *Assistant*, next to the labels WS2.3 gives.

   No change deletes a mail or sends one. A change that failed keeps its row in `changes`, with the status `failed` and the reason in the column `error`.

   </details>

4. Click **Publish** again: n8n runs only the published version.
5. From your SKKU account, send a mail with this subject. A little later it has a star in Gmail.

   ```
   Urgent: call me back
   ```

**Done: your own rule runs in a real system. A rule decides here, not the model: the same every time.**

<div class="fine">

**Stuck?** Import `n8n/ws2_3_triage_new_mail_solution.json`. It gives the finished workflow `WS2.3 - Triage New Mail - SOLUTION`, with the rule. In its node `fetch_triage`, check that `Langflow (Run API)` is picked; in its node `submit_to_reply_with_approval`, pick `WS2.4 - Reply with Approval`. Unpublish your WS2.3, then publish the solution: never both, or each new mail goes to only one of them. [Help for block 5](#block-5)

</div>

## If something goes wrong

Still stuck? Ask Frank.

#### Block 5

| What you see | What to do |
|---|---|
| No star in Gmail | In `if_urgent`: *Ignore Case* on, and the line comes from `check_triage`. In `post_star`: the parameter under *Options*, then *Query Parameters*. Did you publish WS2.3 again after the change? |
| The mail is not in WS2.3's runs | See block 3: the allowed address, the main address of your test account. |
| You are behind | Import `n8n/ws2_3_triage_new_mail_solution.json`. It gives the finished workflow `WS2.3 - Triage New Mail - SOLUTION`, with the rule. Check its credential in `fetch_triage` and pick WS2.4 in its node `submit_to_reply_with_approval` (block 3, steps 3 and 4). Unpublish your `WS2.3 - Triage New Mail`, then publish the solution. Never both: each new mail goes to only one of them. |

**Next: [Block 6 · Why we put the human in the loop in WS2.4 →](/abp/ws2/s1-block-6/)**
