---
title: "Block 4 · Challenge: all five test mails right"
---

Your Triage flow sorts some of the five test mails wrong. A ready workflow gives it a score, three rounds per click.
Then you improve the prompt until all five are right.

| Test mail | Subject | Expected |
|---|---|---|
| 8 | Papers | reply |
| 30 | (no subject) | forward |
| 46 | Market Forecasting Conference | reply |
| 67 | RE: Jump | archive |
| 126 | Contact Info for Conference Call Tomorrow at 10 am EDT | calendar |

1. Import `n8n/ws2_1_test_triage_improved.json` from the folder `n8n`. It gives `WS2.1 - TEST - Triage - Improved`.
2. Check its credential: double-click the node `fetch_flow`. Under *Header Auth*, it should say `Langflow (Run API)`.
   If not, pick it. Close the node, then save.
3. Before you run it, look at its nodes. Double-click each one:

   | Node | What it does |
   |---|---|
   | `trigger_manual` | starts it when you click *Execute workflow* |
   | `webhook_open_runs` | starts it from its page in your browser: opening the page shows the dashboard, its button runs the test |
   | `set_test_settings` | the settings: `rounds` (3), the flow (`enron-triage`, your Triage flow), and the field of its answer to compare (`action`) |
   | `set_settings_from_page`, `if_run_requested` | what the page's form sent, over the settings; a test runs only after a click on **Run the test**, or *Execute workflow* |
   | `get_cases` | the five test mails from *Cases*, as in your WS2.1 |
   | `transform_into_rounds` | each test mail once per round: 15 items |
   | `fetch_flow` | the 15 mails to your Triage flow, five at a time |
   | `set_answer` | Triage's answer as fields, as in your WS2.1 |
   | `set_score` | each action next to the expected one: the score of each round, the seconds, every answer |
   | `post_run_to_runs` | one line into *Runs* |
   | `get_runs`, `transform_runs_into_dashboard` | every line of *Runs* as a dashboard |
   | `format_dashboard_as_html`, `send_dashboard_page` | the dashboard in n8n, and as a page in your browser |

   **Check yourself:** your WS2.1 writes each action into *Cases*. Does this workflow do that too?

   <details class="more fine">
   <summary>The answer</summary>

   No. The one node that writes, `post_run_to_runs`, writes into *Runs*. *Cases* holds the test: the five mails and
   what is expected. A test should not change its test set. The results go into *Runs*, one line per click, so you can compare
   one prompt with the next.

   </details>

   **And:** why does it send each mail several times?

   <details class="more fine">
   <summary>The answer</summary>

   The model does not always give the same answer to the same mail. One round can be lucky, or unlucky. Three rounds
   show whether a prompt holds. Want more? Set more rounds: a clearer picture, a longer wait.

   </details>

4. Run it once here, in n8n:
   1. Click the small arrow next to **Execute workflow** and pick `trigger_manual`.
   2. Click **Execute workflow**.
   3. When all nodes are green, double-click the node `format_dashboard_as_html`. On the right: your dashboard.

   <small>Why pick a trigger? With two triggers, n8n starts from the webhook unless you pick another. The webhook
   would wait for a call of its page, and nothing happens. n8n picks the webhook again after each reload.</small>
5. Open the dashboard as a page, to keep next to Langflow:
   1. Click **Publish** at the top, then **Publish** again in the window. The page works only while the workflow is
      published.
   2. Open this address in a new browser tab:

      ```
      http://localhost:5678/webhook/triage-runs
      ```

   3. At the top, the form: what you changed, the rounds, the flow, the field. Its button **Run the test** runs the
      test. The page comes back when all rounds are done, with the new run.
6. Read the dashboard:
   - **The most recent run:** right answers per round, on average. Is it better than the run before, and than your
     start? Only beyond the spread counts: every round better than every round before.
   - **Every run:** one row per run, one dot per round. The spread of the dots is the model's luck.
   - **Every test mail, run by run:** in how many rounds each mail was right. ▲ or ▼: better or worse than the run
     before. The mails that work worst come first.
   - **Wrong in the most recent run:** what the model answered.
   - **Each run in detail:** click a run, and see every answer of every round.
7. In *Cases*, read the mails it got wrong, in the column `mail`. Why would the model choose that?
8. In Langflow, open **Triage (Enron)**, then the node **Prompt Template**. Change how the actions are described. Only
   the prompt. Save.
9. On the page, write what you changed, and click **Run the test**. Did your fix for one mail break another? The table
   of test mails shows it.

**Done: you test your Triage flow the right way: three rounds per click, one line per run, the test set untouched,
and a dashboard that shows what each change did.**

<details class="more fine">
<summary>Our prompt, for after the challenge: 5 of 5, ten times in a row</summary>

In Langflow, open **Triage (Enron)**, then the node **Prompt Template**. Click into *Template*, select all of it, and paste this in its place. Save the flow, then run `WS2.1 - TEST - Triage - Improved` again.

```
You sort the incoming mail of Vince J Kaminski, head of the research group at Enron in Houston, in 2001.
Read the mail below and answer with one JSON object and nothing else: no explanation, no code fence.

The object has four keys:
  "events"    a list of strings: the names of every MailEx event in the mail's own text that is addressed to
              Kaminski or to all recipients, for example ["Request_Data", "Deliver_Data"]; [] if none. The names:
  Request_Data           asks for information
  Request_Action         asks someone to do something
  Request_Meeting        asks for a meeting or call
  Request_Action_Data    asks about an action (has it been done, when will it be)
  Request_Meeting_Data   asks about a meeting (time, place, who comes)
  Deliver_Data           gives information
  Deliver_Action_Data    says an action is done, will be done, or will not be
  Deliver_Meeting_Data   gives a meeting's time, place, agenda or outcome
  Amend_Data, Amend_Action_Data, Amend_Meeting_Data   corrects or changes something given before
  "action"    what his assistant does with the mail, one of:
                "calendar"  a meeting, call, visit or interview is asked for or set, or how it will take place
                            (time, place, who calls whom): to Shirley Crenshaw (his assistant) or into the calendar
                "reply"     someone wants information, an answer or a decision from Kaminski himself: draft a reply in
                            his name
                "forward"   someone wants work done that his assistant or his team can do: send documents or slides,
                            make copies, fill in a form, book, register; forward it to whoever does it, or note it as
                            a task
                "archive"   it only delivers, informs or announces (reports, newsletters, FYI, thanks, spam): file it
              Pick the one that matters most if several apply. Work to be done by a date matters more than a
              request to confirm receipt.
  "deadline"  a date or time by which something is wanted, as written in the mail; "" if none
  "why"       one short sentence

The mail:
{mail}
```

What changed: *reply* only for what Kaminski himself must answer; *forward* for work his assistant or his team can do; *calendar* also for how a call will take place; and work to be done by a date matters more than a request to confirm receipt.

Five mails are not enough to know it is better overall. On all 140 test mails of the case, it got about as many right as the prompt as it comes.

</details>

### Test your project's Langflow flows from n8n, too

The same works for every Langflow flow of your team's project: a copy of `WS2.1 - TEST - Triage - Improved`, with
your test cases and your flow. You see every answer, and you can run the test again after each change.

It also avoids the Langflow 1.8 memory bug ([what it is](https://huettner.io/kingo-pod/upgrade/)). In the Playground,
chats with the same name share one memory across flows, so a test can see another flow's chat. A call from n8n never
does: each call of the workflow has its own session id, so a flow with memory starts fresh for every case.

1. Write your test cases. Open `ws2_1_test_triage_cases.csv` in Excel or Numbers and keep its first line, the names
   of the columns. Below it, one test case per line:
   - `test_mail`: a number for the case
   - `subject`: a short title
   - `mail`: what your flow gets, the text you would type into its Playground
   - `expected`: what it should answer
   - `action`: leave it empty

   Save it as CSV, with a new name.
2. Make two data tables, as in block 2, with your team's name and what you test, for example:
   - `Blue - TEST - Intake - Cases`, from your new file
   - `Blue - TEST - Intake - Runs`, from `ws2_1_test_triage_runs.csv`
3. Open `WS2.1 - TEST - Triage - Improved`. Open the menu **…** at the top, next to its name, then **Duplicate**.
   Name the copy after your test, for example `Blue - TEST - Intake`.
4. In the copy, pick your tables: double-click `get_cases` and pick your Cases table in the field **Data table**.
   Do the same in `post_run_to_runs` and `get_runs`, with your Runs table.
5. Give the page an address of its own: double-click `webhook_open_runs` and change *Path*, for example to
   `blue-intake-runs`. Two published workflows cannot share a path.
6. Double-click `set_test_settings` and change the values:
   - `flow_endpoint`: your flow. In Langflow, open it, click **Share** at the top right, then **API access**. Copy what
     comes after `/run/` in the address, up to `?` if there is one.
   - `answer_field`: does your flow answer with JSON, as Triage does? Then the field to compare with `expected`, for
     example `action`. Does it answer with text? Then leave it empty: a case counts as right when the answer
     contains `expected`.
   - `rounds`: how often each case goes to the flow.

   The page's form can change all three for one run.
7. Click **Publish**. Open your page, for example `http://localhost:5678/webhook/blue-intake-runs`, and click **Run
   the test**.

<div class="fine">

**Stuck?** [Help for block 4](#block-4)

</div>

## If something goes wrong

Still stuck? Ask Frank.

#### Block 4

| What you see | What to do |
|---|---|
| `fetch_flow` gives an error 403 | Its credential: it must be `Langflow (Run API)` (step 2). |
| `fetch_flow` gives a timeout | Langflow is busy: 15 mails, five at a time. Wait a minute, then click *Execute workflow* again. |
| `fetch_flow` gives an error 404 | Langflow has no flow by the name in `flow_endpoint`, in `set_test_settings`. For Triage: `enron-triage`. |
| The page says that the webhook is not registered | Publish `WS2.1 - TEST - Triage - Improved` (step 5). Its page works only while it is published. |
| After **Run the test**, the page seems to hang | It waits until all rounds are done. Do not click again: each click is a run of its own. |
| Your project's copy will not publish | Give `webhook_open_runs` in the copy a path of its own. |
| In your project's test, every case counts as wrong | Look at `set_answer`'s output. JSON with your field? Then `answer_field` must name it exactly. Plain text? Then leave `answer_field` empty. |
| `get_cases` gives no items | As in block 2: the table's name must be exactly `WS2.1 - TEST - Triage - Cases`. |
| *Execute workflow* says "Waiting for trigger event" | It started from `webhook_open_runs`. Click the stop button, then the small arrow next to *Execute workflow*, and pick `trigger_manual` (step 4). |
| `post_run_to_runs` gives an error | Your table *Runs* needs the columns of `ws2_1_test_triage_runs.csv`: `ran_at`, `note`, `flow`, `score`, `rounds`, `seconds`, `wrong`, `detail`. Make it again from that file, as in block 2. |
| Your change in Langflow does nothing | Save the flow (the flow must say it is saved). Then click *Execute workflow* in n8n again. |

**Next: [Block 5 · Let's look inside WS2.3, and make it ours →](/abp/ws2/s1-block-5/)**
