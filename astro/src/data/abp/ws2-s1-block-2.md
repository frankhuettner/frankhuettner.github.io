---
title: "Block 2 · WS2.1: You build an n8n workflow to test your Langflow Triage flow"
---

<details class="more fine">
<summary>What the workflow does</summary>

It takes the five test mails from the data table *Cases*. Each goes to your Langflow flow Triage, by HTTP. The action
in Triage's answer goes back into *Cases*, next to the expected one. In block 4, a second workflow gives it a score.

</details>

1. Click **Create workflow**. Click its name at the top and give it this name:

   ```
   WS2.1 - TEST - Triage
   ```

2. Add a first node: a **Manual Trigger** (in the list: *Trigger manually*). It starts the workflow when you click
   **Execute workflow**. Rename it `trigger_manual`.
3. Add a **Data table** node and name it `get_cases`. It reads the five test mails. Set it like this:

   Pick *Get row(s)*. Under *Data table*, choose *From list* and pick this table:

   ```
   WS2.1 - TEST - Triage - Cases
   ```

   Turn *Return All* on.

   Click **Execute step**: on the right, five items.
4. Add an **HTTP Request** node and name it `fetch_triage`. It sends each mail to your Triage flow in Langflow. Set
   it like this:

   Choose method POST and paste the URL:

   ```
   http://langflow:7860/api/v1/run/enron-triage?stream=false
   ```

   For *Authentication*, choose *Generic Credential Type*, then *Header Auth*, then `Langflow (Run API)`. Turn *Send Body* on. *Body Content Type*: *JSON*. *Specify Body*: *Using Fields Below*.

   Under *Body Parameters*, add three. The first: *Name* `input_value`, and as *Value* paste this:

   ```
   {{ $json.mail }}
   ```

   The second: *Name* `input_type`, *Value* `text`. The third: *Name* `output_type`, *Value* `text`.

   <details class="more fine">
   <summary>What it does</summary>

   n8n sends one request per test mail, five in all. Each is one JSON object with three fields:

   ```json
   {
     "input_value": "From: Jason Sokolov ... (the whole mail)",
     "input_type": "text",
     "output_type": "text"
   }
   ```

   `input_value` is the mail, from the column `mail` of *Cases*. Langflow puts it into the flow's one *Text Input*, the box you pasted a mail into in homework step 8. Text goes in, text comes out.

   What Langflow expects, in its own words: in Langflow, open the flow *Triage (Enron)*, then **Share** at the top right, then **API access**.

   </details>

5. Add an **Edit Fields** node and name it `set_answer`. It turns Triage's answer into fields n8n can read. Set it
   like this:

   Click *Add Field* and name it `answer`. Next to the name, change its type from *String* to *Object*. Then paste this as its value:

   ```
   {{ $json.outputs[0].outputs[0].results.text.text }}
   ```

   Click **Execute step**. On the right, each item now has `answer` with Triage's fields: `action`, `why`, `checks_ok` and more.

   <details class="more fine">
   <summary>What it does</summary>

   Langflow answers with one object. `outputs[0].outputs[0]` is the flow's first output, and `results.text.text` its text: Triage's answer, as JSON text.

   The type *Object* makes n8n read that text as JSON, so each of its fields becomes a field of its own. That works because Triage keeps its contract: its answer is always JSON, with these fields.

   </details>

6. Add a **Data table** node and name it `post_action_to_cases`. It writes the action into the table *Cases*. Set it
   like this:

   Pick *Update row(s)* and, from the list as in `get_cases`, the table Cases. Add a condition: the column `id`, *Equals*, and paste this value:

   ```
   {{ $('get_cases').item.json.id }}
   ```

   <details class="more fine">
   <summary>What it does</summary>

   `$('get_cases')` is the node `get_cases`. `.item` is its item that belongs to this one: the same test mail. `.json.id` is that mail's column `id`. So each action goes into the row of its own test mail.

   n8n writes the same when you drag the field `id` of `get_cases` from the left into the box.

   </details>

   Under *Values to update*, fill the column `action`: on the left, open `answer` and drag its field `action` into the box. n8n writes this:

   ```
   {{ $json.answer.action }}
   ```

7. Click **Execute workflow**.
8. Open the table: click **Overview**, then the tab **Data tables**, then `WS2.1 - TEST - Triage - Cases`. Triage's
   answer now stands next to the expected one.
9. Tidy up:
   - Give the workflow the tags `WS2`, `mail case` and `9 Nov`: click the three dots **…** at the top, next to its
     name, then *Edit description and tags*.
   - Add a sticky note (<kbd>Shift</kbd>+<kbd>S</kbd>).

     Paste this into the sticky note, and put your name in place of *Your Name*:

     ```
     ## WS2.1 - TEST - Triage
     **Created by:** Your Name · **Date:** 9 Nov 2026

     Tests the Langflow flow Triage: the five test mails from the table Cases go to Triage, one by one. Triage's action goes back into Cases, next to the expected one.
     ```

**Done: your first n8n workflow tests your Triage flow.**

<div class="fine">

**Stuck?** Import `n8n/ws2_1_test_triage_solution.json`. It gives the finished workflow `WS2.1 - TEST - Triage - SOLUTION`. [Help for block 2](#block-2)

</div>

### Extra, if you are fast: build WS2.2 - Ask Mailbox

This becomes a chat that allows you to search your mail. It's like the playground from your homework step 13, just
in n8n. It contains:

- a **Chat Trigger** `trigger_chat`
- an **HTTP Request** `fetch_ask_mailbox`
- an **Edit Fields** node `set_answer`

Make an n8n workflow with the name:

```
WS2.2 - Ask Mailbox
```

Add a **Chat Trigger** node and name it `trigger_chat`.

Open the chat at the bottom and send this question. Now `trigger_chat` has an item, and the next node shows it on its left:

```
Who is sharing homemade Korean food?
```

Add an **HTTP Request** node, name it `fetch_ask_mailbox`, choose method POST, and paste the URL:

```
http://langflow:7860/api/v1/run/enron-ask-mailbox?stream=false
```

For *Authentication*, choose *Generic Credential Type*, then *Header Auth*, then `Langflow (Run API)`. Turn *Send Body* on, choose *JSON* and *Using JSON*, and paste the body:

```
{{ JSON.stringify({ input_value: $json.chatInput, input_type: 'chat', output_type: 'chat', session_id: $json.sessionId }) }}
```

Add an **Edit Fields** node and name it `set_answer`. Click *Add Field*, name it `output`, and paste this as its value:

```
{{ $json.outputs[0].outputs[0].results.message.text }}
```

Then open the chat at the bottom, and ask:

```
What is Steve Leppard's email address?
```

```
Who arranges tours of the Enron trading floor?
```

<div class="fine">

Between two questions, you may need to reset the chat: click the curved arrow at the top of the chat.

</div>

<div class="fine">

**Stuck?** Import `n8n/ws2_2_ask_mailbox_solution.json`. It gives the finished workflow `WS2.2 - Ask Mailbox - SOLUTION`.

</div>

### Extra, if you are fast: let an AI chat write the SQL

This becomes a workflow that answers one question: who wrote to Kaminski most often? It contains:

- a **Manual Trigger** `trigger_manual`
- a **Postgres** node `get_top_senders`

<small>The credential may only read and write what n8n needs: a wrong query cannot break the mailbox.</small>

Make an n8n workflow with the name:

```
WS2.2 - Top Senders
```

Add a **Manual Trigger** node (in the list: *Trigger manually*) and name it `trigger_manual`.

Give this to an AI chat like ChatGPT:

```
Write a PostgreSQL query for me.

The table: n8n_workshop_mail.messages, one mail per row. Its columns:
- message_id
- sent_at
- from_name
- from_addr
- to_addrs (text[])
- cc_addrs (text[])
- subject
- body_text
- folders (text[]: INBOX, Sent, ...)
- deleted_at

The question: who sent the most mails?

Leave out:
- the mails in the folder Sent
- the deleted mails

The result:
- one row per sender (from_addr), with the number of mails
- the ten largest first
```

Add a **Postgres** node, name it `get_top_senders`, pick the credential `Mail (n8n_workshop_mail_n8n)` and *Execute Query*, and paste the AI chat's answer as the query. Then click **Execute workflow**: the ten senders appear on the right.

<details class="more fine">
<summary>A solution, just in case</summary>

```sql
SELECT from_addr, count(*) AS mails
FROM n8n_workshop_mail.messages
WHERE deleted_at IS NULL AND NOT 'Sent' = ANY(folders)
GROUP BY from_addr
ORDER BY mails DESC
LIMIT 10;
```

</details>

<div class="fine">

**Stuck?** Import `n8n/ws2_2_top_senders_solution.json`. It gives the finished workflow `WS2.2 - Top Senders - SOLUTION`: *Execute workflow*, then open `get_top_senders`.

</div>

## If something goes wrong

Still stuck? Ask Frank.

#### Block 2

| What you see | What to do |
|---|---|
| `fetch_triage` gives an error 403 | The credential `Langflow (Run API)` holds the wrong key. In Langflow, open *Settings*, then *Langflow API Keys*, and make a new one. Put it into the credential. |
| `fetch_triage` gives no answer, or a timeout | WS2.0 may still be embedding, or Langflow is busy. Wait a minute, then click *Execute step* again. The URL must say `langflow`, not `localhost`: inside kingo-pod, n8n reaches Langflow by its name. |
| `get_cases` gives no items | The table's name must be exactly `WS2.1 - TEST - Triage - Cases`. Check it: click *Overview*, then the tab *Data tables*. |
| `set_answer` gives an error, or the column `action` stays empty | Is the type of the field `answer` *Object*? Then open `fetch_triage`'s output: under `text` you should see Triage's answer as JSON, with `"checks_ok": true`. An empty mail in its `why`? Then `fetch_triage` sends no `input_value`: check its three *Body Parameters*. |
| You are behind | Import `n8n/ws2_1_test_triage_solution.json`. It gives the finished workflow `WS2.1 - TEST - Triage - SOLUTION`. Go on in it. |

**Next: [Block 3 · Your mail AI assistant answers your mail: WS2.3 and WS2.4 →](/abp/ws2/s1-block-3/)**
