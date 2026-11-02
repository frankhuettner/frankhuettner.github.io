---
title: "Session 1 (9 November): snippets to copy"
---

Everything the slides ask you to type, in the order of the slides. Click *Copy* next to a box, then paste it into n8n. What is in `ws2_s1.zip`, and how to set it up: [at the end of this page](#the-files-in-ws2_s1zip).

## WS2.1 - TEST - Triage: your AI, tested

First the two data tables. In n8n, on the page *Overview*, the tab *Data tables* (in the middle of the page): import `ws2_1_test_triage_cases.csv` with this name:

```
WS2.1 - TEST - Triage - Cases
```

and `ws2_1_test_triage_runs.csv` with this name:

```
WS2.1 - TEST - Triage - Runs
```

The n8n workflow's name:

```
WS2.1 - TEST - Triage
```

Node `get_cases` (Data table, *Get row(s)*): the table *By Name*, *Return All* on:

```
WS2.1 - TEST - Triage - Cases
```

Node `fetch_triage` (HTTP Request), method POST, the URL:

```
http://langflow:7860/api/v1/run/enron-triage?stream=false
```

Authentication: *Generic Credential Type* → *Header Auth* → `Langflow (Run API)`. *Send Body* on, *JSON*, *Using JSON*, the body:

```
{{ JSON.stringify({ input_type: 'text', output_type: 'text', tweaks: { 'TextInput-mail': { input_value: $json.mail } } }) }}
```

Node `set_action` (Edit Fields), a field named `action` with this value:

````
{{ JSON.parse(($json.outputs[0].outputs[0].results.text.text || '').replace(/^```(?:json)?\s*|\s*```$/g, '')).action }}
````

Node `post_action_to_cases` (Data table, *Update row(s)*), the table Cases. The condition: `id` *equals*

```
{{ $('get_cases').item.json.id }}
```

and the column `action`:

```
{{ $json.action }}
```

**Stuck?** The n8n workflow as far as this is the file `ws2_1_test_triage_without_score.json` in the folder `n8n`. In n8n: *Create workflow* → **⋯** (top right) → *Import from File*.

## WS2.2 - Ask Mailbox

The n8n workflow's name:

```
WS2.2 - Ask Mailbox
```

Node `fetch_ask_mailbox` (HTTP Request), method POST, the URL:

```
http://langflow:7860/api/v1/run/enron-ask-mailbox?stream=false
```

Authentication: *Generic Credential Type* → *Header Auth* → `Langflow (Run API)`. *Send Body* on, *JSON*, *Using JSON*, the body:

```
{{ JSON.stringify({ input_value: $json.chatInput, input_type: 'chat', output_type: 'chat', session_id: $json.sessionId }) }}
```

Node `set_answer` (Edit Fields), a field named `output` with this value:

```
{{ $json.outputs[0].outputs[0].results.message.text }}
```

Questions to ask in the chat:

```
What is Steve Leppard's email address?
```

```
Who arranges tours of the Enron trading floor?
```

**Stuck?** The finished n8n workflow is the file `ws2_2_ask_mailbox.json` in the folder `n8n`.

## Extra, if you are fast: let an AI write the SQL

Give this to an AI chat, then paste its answer into a node **Postgres** (credential `Mail (n8n_workshop_mail_n8n)`, *Execute Query*):

```
Write a PostgreSQL query for me. The table n8n_workshop_mail.messages holds one mail per row, with
the columns message_id, sent_at, from_name, from_addr, to_addrs (text[]), cc_addrs (text[]), subject, body_text,
folders (text[]: INBOX, Sent, ...) and deleted_at. Who wrote to Vince Kaminski most often? Leave out the mails in the
folder Sent and the deleted ones. One row per sender (from_addr) with the number of mails, the ten largest first.
```

## WS2.3 and WS2.4: your AI assistant

The approvals page, in a new browser tab:

```
http://localhost:5678/webhook/approvals
```

A mail from your private account to your test account:

```
Dear Vince, what is Steve Leppard's email address? I need to reach him.
```

## Your own rule in WS2.3

Node `if_urgent` (If), the value on the left. Then *String* → *contains* → `urgent`, and in the options *Ignore Case* on.

```
{{ $json.subject }}
```

Node `post_star` (Postgres, *Execute Query*), the query:

```sql
INSERT INTO n8n_workshop_mail.changes (message_id, action, label) VALUES ($1, 'star', NULL);
```

In the options, *Query Parameters*:

```
{{ $json.message_id }}
```

In place of `'star', NULL` the mail service also knows `'label', 'Urgent'` (a label under `Assistant/`), `'archive', NULL` and `'read', NULL`.

The subject of your test mail:

```
Urgent: call me back
```

## Challenge: WS2.1 gets a score

Node `keep_right` (Filter): the value on the left, *is equal to*, the value on the right. In the node's *Settings*: *Always Output Data* on.

```
{{ $json.action }}
```

```
{{ $json.expected }}
```

Node `count_right` (Summarize): *Count* of `test_mail`.

Node `post_score_to_runs` (Data table, *Insert row*), the table Runs, the column `ran_at`:

```
{{ $now.toFormat('dd LLL yyyy, HH:mm') }}
```

and the column `score`:

```
{{ $json.count_test_mail }} of 5
```

**Stuck?** The finished n8n workflow is the file `ws2_1_test_triage.json` in the folder `n8n`.

## Any time

One of the test mails of May 2001 into your inbox, here test mail 67 (CloudBeaver, database `classroom`):

```sql
SELECT n8n_workshop_mail.deliver_test(67);
```

## The files in ws2_s1.zip

The Enron mail case. Every name starts with `ws2_`, for Workshop II.

The n8n workflows are numbered in the order the course builds them up: `WS2.<step> - <purpose>`. Workflows
of one step share its number. A workflow that tests another one is called `WS2.<step> - TEST - <what it tests>`. Its
data tables add what one row is: `- Cases` (one test case: the input and the expected answer) and `- Runs` (one run:
when, and the score). Files carry the same names in small letters and `_`.

### n8n

| File | n8n workflow | What it does |
|---|---|---|
| `n8n/ws2_1_test_triage.json` | WS2.1 - TEST - Triage | your first workflow: each of the five test mails to the Langflow flow Triage, its answer next to the expected one; with the score per run from block 5 |
| `n8n/ws2_1_test_triage_without_score.json` | WS2.1 - TEST - Triage | the same as far as block 2 builds it, to go on from (Stuck?) |
| `n8n/ws2_2_ask_mailbox.json` | WS2.2 - Ask Mailbox | a chat in n8n, answered by Langflow from the mailbox |
| `n8n/ws2_3_triage_new_mail.json` | WS2.3 - Triage New Mail | sorts every new mail and acts in Gmail: archive, label, star; a mail to answer goes to WS2.4 |
| `n8n/ws2_4_reply_with_approval.json` | WS2.4 - Reply with Approval | the draft, your approval in a form, the answer in Gmail; drafts waiting for you at <http://localhost:5678/webhook/approvals> |
| `n8n/ws2_5_team_intake_by_mail_a_c.json` | WS2.5 - Team - Intake by Mail (A, C) | your project: mail to your plus address (`name+project@gmail.com`) → your system → a draft reply (WS2.4) or an approval ticket |
| `n8n/ws2_5_team_intake_by_form_b.json` | WS2.5 - Team - Intake by Form (B) | your project: a form → your system → an HTML document to download |
| `n8n/ws2_5_team_your_agent_template.json` | WS2.5 - Team - Your Agent (Template) | your project: your agent behind the core's inputs and outputs, so the test bench and your ways in can call it |

The mail case's workflows and WS2.0 leave out mail to a plus address: that is your team's.

### Data tables and snippets

- `ws2_1_test_triage_cases.csv` and `ws2_1_test_triage_runs.csv`: in n8n, on the page *Overview*, the tab *Data
  tables*, import them once as "WS2.1 - TEST - Triage - Cases" and "WS2.1 - TEST - Triage - Runs" (exactly these
  names: the workflow finds its tables by name). In block 2 you build WS2.1 up to the table Cases; in block 5 it gets
  the score in Runs.
- `ws2_s1_snippets.md`: everything the slides ask you to type, in their order, ready to copy: the boxes above.

### Setting up (short version)

1. **Import** a step's file from `n8n/` when the course gets there (*Import from File*). Where a node asks for a
   credential, pick the one of the same name.
2. **Calls between workflows:** every n8n gives an imported workflow a new id, so pick the called workflow by name:
   - in WS2.3, node "submit_to_reply_with_approval": "WS2.4 - Reply with Approval";
   - in the team templates, node "submit_to_your_system": your copy of WS2.5 - Team - Your Agent (Template); in
     WS2.5 - Team - Intake by Mail, node "submit_to_reply_with_approval": WS2.4.
3. **Publish** WS2.4, then WS2.3.
4. **Try it:** send a mail from your private mail account to your test account, or in CloudBeaver run
   `SELECT n8n_workshop_mail.deliver_test(67);`. A little later WS2.3 sorts it; test mail 67 should end up archived.
