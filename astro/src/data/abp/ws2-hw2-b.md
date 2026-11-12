---
title: "Homework until 16 Nov, Part B: Find out why your mail AI assistant missed the kimchi"
---


Your mail AI assistant drafts answers based on earlier mails. In the preparatory homework, you first sent a mail about
kimchi to your test Gmail account, then asked it about Korean food, and saw the power of semantic search. However, when
you send another mail that asks about Korean food, you see that the mail AI assistant misses the info about the kimchi
in its search. Let's use Claude Code to find out why. Then Claude Code will try to fix the search, and you measure
whether the fix does better.

### 7. See the mistake: ask your mail AI assistant about Korean food

1. In n8n, check that these four workflows are published:
   - **WS2.0 - Embed Mails**
   - **WS2.3 - Triage New Mail**
   - **WS2.4 - Reply with Approval**
   - **WS2.4 - Approvals Page**

   Published means: the dot on the button **Publish** is green.
2. First the kimchi mail. Did you send *Kimchi for Monday* in step 12 of the preparatory homework? If yes, go on with 3.
   If you are not sure, search your test Gmail account for `kimchi`.

   If you did not send it, send it now: from your SKKU account, send this mail to your test Gmail account. Copy the
   subject and the text, then sign with your first name:

   ```
   Kimchi for Monday
   ```

   ```
   Hi,

   This weekend my family makes kimchi for the winter (gimjang).
   I will bring a box of it for everyone at the workshop on Monday.
   ```

   Wait two minutes: kingo-pod copies the mail into its database, and WS2.0 adds it to the search.
3. Now the question. From your SKKU account, send a second mail to your test Gmail account. Copy the subject and
   the text:

   ```
   Is there any Korean home made food?
   ```

   ```
   Hi Vince, I'm getting hungry! Please reply.
   ```
4. Wait two minutes. Then open the page with the drafts that wait for you: <http://localhost:5678/webhook/approvals>
5. Read the draft of the reply to *Is there any Korean home made food?* (A draft of a reply to the kimchi mail may
   wait there too: leave it.) Most likely the draft says that nothing is known about Korean food and that someone will follow up. The
   kimchi mail is in your database, yet the draft does not use it.

Does your draft mention the kimchi? Then the search was lucky this time. Go on anyway: in step 10 you measure it.

<details class="more">
<summary>Side note: the address in sub-step 4 is a webhook</summary>

The address you opened in sub-step 4 (<http://localhost:5678/webhook/approvals>) is a **webhook**, that is, an address where
someone (here, that is you) can call n8n. In other words, n8n hands out a hook that you can pull. In this case, your
browser pulled the hook by calling the address, and the n8n workflow *WS2.4 - Approvals Page* answered: it read the
drafts that wait for you from the database, made a web page of them, and sent this page back to your browser. The
page carries a little sticker that you do not see: "pull the hook again in 15 seconds". So your browser does that for
you, and the page is never more than 15 seconds old. n8n looks into the database only when someone pulls the hook:
close the page, and *WS2.4 - Approvals Page* rests.

A webhook is how someone else calls n8n. The other way round, n8n calls someone else, often with an **HTTP Request**
node: *WS2.4 - Reply with Approval*, for example, calls the Langflow flow *Draft Reply (Enron)* with one.

<figure class="bp bp-calls" aria-label="Who calls whom"><div class="bp-call"><em>A webhook: someone else calls n8n</em><div class="bp-end person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/></svg></span><b>Your browser</b><span>you open the page</span></div><div class="bp-arrow"><span>calls <code>/webhook/approvals</code></span><i></i><span>← the page</span></div><div class="bp-end muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>WS2.4 - Approvals Page</span></div></div><div class="bp-call"><em>An HTTP Request node: n8n calls someone else</em><div class="bp-end muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>WS2.4 - Reply with Approval</span></div><div class="bp-arrow"><span>calls Langflow's Run API</span><i></i><span>← the draft</span></div><div class="bp-end brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow</b><span>Draft Reply (Enron)</span></div></div><figcaption>Who calls whom: the left side calls, the right side answers.</figcaption></figure>

</details>

[Stuck? Help for step 7](#step-7)

### 8. Let Claude Code find the cause

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

Claude Code reads the run, the flow and the code. To this end, it runs several commands to dig deeper and to find
the reason. Before running a command, it asks you for permission. Most of these requests are searches: Claude Code
looks into your database, or into the runs that n8n keeps. A search changes nothing, so you can approve it.

So many requests in a row are tiring, right? Did you switch to auto mode? Press Shift+Tab until the line under your
text says `auto mode on`. Then a model checks each command and runs what it judges safe, without asking you. More
about your choices:
[You decide: should Claude Code ask before every command?](#you-decide-should-claude-code-ask-before-every-command)

Did you stop Claude Code by accident, or say no to a request? Type `continue`, and Claude Code goes on.

At the end, Claude Code answers your question: it explains why the search did not find the kimchi. Read this answer
twice (the answer at the end, not the reasons Claude Code gives for its requests): this is the most important finding
of this part.

Feel free to ask Claude Code to say the answer in simple words if you find it too complicated:

```
Say this again in simple words.
```

[Stuck? Help for step 8](#step-8)

### 9. Let Claude Code fix the search, in a copy of the flow

The fix goes into Langflow only, not into n8n: n8n builds the mail text, and the prompt and the check of the draft
still need all of it. Only the search should get less.

```
Make a copy of the Langflow flow Draft Reply (Enron) and name it
"Draft Reply (Enron) - Search Fix". Put the copy into the same Langflow project
(folder) as the original.

In the copy only, change what goes into the search of Mail Search, following the cause
you found. The prompt and Check Draft keep the whole mail.

Do not change the original flow, and do not change n8n.
```

You should see the new flow *Draft Reply (Enron) - Search Fix* in your Langflow, next to the original. The original
is unchanged, and Claude Code saved its JSON in `~/kingo-pod/claude/backups/`.

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
1. "Is there any Korean home made food?" (my own mail):
   "Kimchi for Monday"
2. "Re: FW: Wharton Resume Submission - Summer Intern" (from Kristin Gandy, 26 January 2001):
   "FW: Wharton Resume Submission - Summer Intern"
3. "Dr. Michelle Foss- Energy Institute" (from Aisha Jamal, 23 April 2001): one of
   "Re: Tiger Team Event", "Re: Leonard Hilton Reception-DIRECTIONS-PARKING",
   "Wharton Business Plan Competition", "@Jones: News and Information from the Jones School",
   "Invitation-WhartonETEvent-Apr20/PlsRSVP"

Show me a table: for each mail and each flow, was an expected source among the sources?
```

You should see a table with six answers. When we measured the search alone on 10 November, our table looked like this:

| Mail | Draft Reply (Enron) | Draft Reply (Enron) - Search Fix |
|---|---|---|
| Korean home made food | not found | found |
| Wharton Resume Submission | found | found |
| Energy Institute | found | not found |

In our table, the fix brings in the kimchi, and the Energy Institute drops out: the fix helped one mail and hurt
another.

Your table may look different. Your mailbox holds other mails than ours, and Claude Code may have built your fix in
another way. Read your own table:

- Where did the fix help?
- Where did it change nothing?
- Did it hurt anywhere?

That is the lesson of this part: **a change is better only when you measured it on more than one case.**

[Stuck? Help for step 10](#step-10)

**Want more? [Optional · Get ready for SMS →](/abp/ws2/hw2-optional/)**

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 7

| What you see | What to do |
|---|---|
| No draft for your mail on the page | Check in Gmail that the mail arrived (look in Spam too). Check that WS2.3 and WS2.4 are published. In n8n, open *Executions* and look for a run of WS2.3 with your mail. |
| No draft, and the mail has left the inbox of your test Gmail account (you find it under *All Mail*) | Your mail AI assistant filed the mail instead of answering it. Triage decides for every mail, and for a short mail not always the same way. Send the mail of sub-step 3 again, with exactly the text given there, and wait two minutes. |
| The page does not open | Check that WS2.4 - Approvals Page is published. |
| Claude Code says in step 8 that the kimchi mail is not in the search | WS2.0 - Embed Mails was not published when the kimchi mail came. Publish it, wait two minutes, then send the question again (sub-step 3). |

#### Step 8

| What you see | What to do |
|---|---|
| Claude Code does not find the cause | Ask it: `What exactly does Mail Search get as its search query? Show me the text.` Then: `Which lines of that text help to find the kimchi mail, and which do not?` |
| Claude Code cannot find the run | Ask it for the newest run of WS2.4 - Reply with Approval, with its data. |

#### Step 9

| What you see | What to do |
|---|---|
| No new flow in Langflow | Reload the page of Langflow. Still none? Ask Claude Code: `Did you save the copy? Show me its name and id.` |
| Claude Code changed the original flow | Ask Claude Code to put the original back from its backup in `~/kingo-pod/claude/backups/`. |
| The new flow is in another Langflow project, for example *Starter Project* | Ask Claude Code: `Move the flow Draft Reply (Enron) - Search Fix into the same Langflow project as Draft Reply (Enron).` |
| Claude Code says that the permission system refuses to change your Langflow, and the line under your text says `auto mode on` | Your kingo-pod is too old: there, a newer Claude Code starts in auto mode, where a model decides which commands run. Type `/exit`, run `./kingo update`, then `./kingo claude`, and send the text of step 9 again. `./kingo version` then shows 1.4.9 or newer (on Kingo 1.5: 1.5.8 or newer). |

#### Step 10

| What you see | What to do |
|---|---|
| Claude Code says that it cannot reach your database (Mac) | Your kingo-pod may be too old. Type `/exit`, run `./kingo update`, then `./kingo claude`, and send the text of step 10 again. After the update, `./kingo version` shows 1.4.6 or newer (on Kingo 1.5: 1.5.5 or newer). |
| Claude Code cannot find one of the mails | Ask it to search `n8n_workshop_mail.messages` by the subject, with `ILIKE`. |
| A flow fails because the API key is missing | The key field of *Draft Reply (Enron)* is empty, and the copy took that over. Repair the original as in the preparatory homework (its help row "A component says the API key is missing"). Then ask Claude Code to make the copy again, as in step 9. |
| Both flows find the same sources for every mail | Check with Claude Code that the copy really is a changed copy: `Show me what you changed in the copy.` |
