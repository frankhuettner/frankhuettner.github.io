---
title: "Homework until 16 Nov, Part B: Find out why your mail AI assistant missed the kimchi"
lede: "Steps 7 to 10. At the end: a fix, measured on three mails."
---


Your mail AI assistant answers from earlier mails. Here you first send it a mail about kimchi, then ask it about
Korean food, see that it misses the kimchi, and let Claude find out why.

### 7. See the mistake: ask your mail AI assistant about Korean food

1. In n8n, check that **WS2.0 - Embed Mails**, **WS2.3 - Triage New Mail** and **WS2.4 - Reply with Approval** are
   published: the dot on the button **Publish** is green.
2. First the kimchi mail. You sent *Kimchi for Monday* in step 12 of the preparatory homework? Then go on with 3. Not
   sure? Search your test Gmail account for `kimchi`.

   Otherwise, from your SKKU account, send this mail to your test Gmail account. Copy the subject and the text, then
   sign with your first name:

   ```
   Kimchi for Monday
   ```

   ```
   Hi,

   This weekend my family makes kimchi for the winter (gimjang).
   I will bring a box of it for everyone at the workshop on Monday.
   ```

   Wait two minutes: kingo-pod copies the mail into its database, and WS2.0 adds it to the search.
3. Now the question. From your SKKU account, send a second mail to your test Gmail account:
   - Subject: `Is there any Korean home made food?`
   - Text: `I'm getting hungry!`
4. Wait two minutes. Then open the page with the drafts that wait for you: <http://localhost:5678/webhook/approvals>
5. Read the draft for *Is there any Korean home made food?* (A draft for the kimchi mail may wait there too: leave
   it.) Most likely the draft says that nothing is known about Korean food and that someone will follow up. The
   kimchi mail is in your database, yet the draft does not use it.

Your draft does mention the kimchi? Then the search was lucky this time. Go on anyway: in step 10 you see how close
it was.

<details class="more">
<summary>What just happened: a webhook</summary>

The page you just opened is a **webhook**: an address where someone else calls n8n. Here your browser called the
address `/webhook/approvals`, and the n8n workflow *WS2.4 - Approvals Page* answered with the page. An **HTTP Request**
node is the other way round: there n8n calls someone else, as WS2.4 calls the Langflow flow Draft Reply. The form
behind **Review** has an address of its own, made for this one run of WS2.4: when you send the form, that run goes on.

<figure class="bp bp-calls" aria-label="Who calls whom"><div class="bp-call"><em>A webhook: someone else calls n8n</em><div class="bp-end person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/></svg></span><b>Your browser</b><span>you open the page</span></div><div class="bp-arrow"><span>calls <code>/webhook/approvals</code></span><i></i><span>← the page</span></div><div class="bp-end muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>WS2.4 - Approvals Page</span></div></div><div class="bp-call"><em>An HTTP Request node: n8n calls someone else</em><div class="bp-end muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>WS2.4 - Reply with Approval</span></div><div class="bp-arrow"><span>calls Langflow's Run API</span><i></i><span>← the draft</span></div><div class="bp-end brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow</b><span>Draft Reply</span></div></div><div class="bp-call"><em>The form behind Review: an address for one run</em><div class="bp-end person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/></svg></span><b>You</b><span>approve or reject</span></div><div class="bp-arrow"><span>send the form to this run's own address</span><i></i></div><div class="bp-end muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>this one run of WS2.4 goes on</span></div></div><figcaption>Who calls whom: the left side calls, the right side answers.</figcaption></figure>

</details>

[Stuck? Help for step 7](#step-7)

### 8. Let Claude find the cause

Start Claude Code (you find `cd ~/kingo-pod && ./kingo claude` in your terminal's command history with the up arrow)
and paste this:

```
My mail AI assistant drafted a reply to my mail "Is there any Korean home made food?"
without the mail "Kimchi for Monday", which is in the database. Find out why.

Look at:
- the last run of WS2.4 - Reply with Approval in n8n: what it sent to the Langflow flow
  Draft Reply (Enron), and what came back as sources;
- the code of the component Mail Search in that flow.

Do not change anything. Then explain the cause to me in plain words.
```

Claude reads the run, the flow and the code, and asks you before each command. At the end it explains why the search
did not find the kimchi. Read the explanation twice: this is the most important finding of this part.

[Stuck? Help for step 8](#step-8)

### 9. Let Claude fix the search, in a copy of the flow

The fix goes into Langflow only, not into n8n: n8n builds the mail text, and the prompt and the check of the draft
still need all of it. Only the search should get less.

```
Make a copy of the Langflow flow Draft Reply (Enron) and name it
"Draft Reply (Enron) - Search Fix".

In the copy only, change what goes into the search of Mail Search, following the cause
you found. The prompt and Check Draft keep the whole mail.

Do not change the original flow, and do not change n8n.
```

You should see the new flow *Draft Reply (Enron) - Search Fix* in your Langflow, next to the original. The original
is unchanged, and Claude saved its JSON in `~/kingo-pod/claude/backups/`.

[Stuck? Help for step 9](#step-9)

### 10. Measure: three mails, two flows

One mail proves nothing: a fix for one mail can break another. So you test both flows on three mails. All three are
in your database.

```
Run both flows, Draft Reply (Enron) and Draft Reply (Enron) - Search Fix,
on three mails from the table n8n_workshop_mail.messages.

Give each mail to the flow as WS2.4 does (From, To, Date and Subject lines, then the text),
and as its date one second before the mail was sent, so that the search does not find
the mail itself.

The mails, by subject, and the sources I expect:
1. "Is there any Korean home made food?" (my mail of today):
   "Kimchi for Monday"
2. "Re: FW: Wharton Resume Submission - Summer Intern" (from Kristin Gandy, 26 January 2001):
   "FW: Wharton Resume Submission - Summer Intern"
3. "Dr. Michelle Foss- Energy Institute" (from Aisha Jamal, 23 April 2001): one of
   "Re: Tiger Team Event", "Re: Leonard Hilton Reception-DIRECTIONS-PARKING",
   "Wharton Business Plan Competition", "@Jones: News and Information from the Jones School",
   "Invitation-WhartonETEvent-Apr20/PlsRSVP"

Show me a table: for each mail and each flow, was an expected source among the sources?
```

You should see a table with six answers. When we measured the search alone on 10 November, it looked like this:

| Mail | Draft Reply (Enron) | Draft Reply (Enron) - Search Fix |
|---|---|---|
| Korean home made food | not found | found |
| Wharton Resume Submission | found | found |
| Energy Institute | found | not found |

The fix brings in the kimchi, and the Energy Institute drops out. That is the lesson of this part: **a change is
better only when you measured it on more than one case.**

Your table looks a little different? That is fine. What counts is that you measured both flows on the same mails.

[Stuck? Help for step 10](#step-10)

**Want more? [Optional · Get ready for SMS →](/abp/ws2/hw2-optional/)**

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 7

| What you see | What to do |
|---|---|
| No draft for your mail on the page | Check in Gmail that the mail arrived (look in Spam too). Check that WS2.3 and WS2.4 are published. In n8n, open *Executions* and look for a run of WS2.3 with your mail. |
| The page does not open | Check that WS2.4 - Approvals Page is published. |
| Claude says in step 8 that the kimchi mail is not in the search | WS2.0 - Embed Mails was not published when the kimchi mail came. Publish it, wait two minutes, then send the question again (sub-step 3). |

#### Step 8

| What you see | What to do |
|---|---|
| Claude does not find the cause | Ask it: `What exactly does Mail Search get as its search query? Show me the text.` Then: `Which lines of that text help to find the kimchi mail, and which do not?` |
| Claude cannot find the run | Ask it for the newest run of WS2.4 - Reply with Approval, with its data. |

#### Step 9

| What you see | What to do |
|---|---|
| No new flow in Langflow | Reload the page of Langflow. Still none? Ask Claude: `Did you save the copy? Show me its name and id.` |
| Claude changed the original flow | Ask Claude to put the original back from its backup in `backups/`. |

#### Step 10

| What you see | What to do |
|---|---|
| Claude cannot find one of the mails | Ask it to search `n8n_workshop_mail.messages` by the subject, with `ILIKE`. |
| Both flows find the same sources for every mail | Check with Claude that the copy really is a changed copy: `Show me what you changed in the copy.` |
