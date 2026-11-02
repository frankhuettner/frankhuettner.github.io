---
title: "Homework (3–8 November): get ready for Workshop II"
---

## What you will build in Workshop II

In Workshop II (9, 16 and 23 November), you will build an AI assistant for a real mailbox.

- **The mailbox:** 3,244 real mails of Vince Kaminski. He was head of research at Enron in 2001.
- **Where the mails live:** in a new Gmail account, only for the course. We call it your **test account**.
- **What the AI assistant does:** it reads new mail, sorts it, and drafts answers in Kaminski's words. It sends nothing
  without your OK.

## Your goal for 9 November

At the end of the first morning, this works on your laptop:

1. You will write a mail from your **private mail account** to your test account.
2. Your AI assistant will sort the mail and draft Kaminski's answer.
3. You will read the draft and say OK.
4. The answer will arrive in your private inbox.

Your **private mail account** is the account you already use, for example Gmail, Naver, Daum or Outlook. Your SKKU
address works too. It is not the new test account.

## This homework: three parts

The homework gets your laptop ready for 9 November. It has three parts:

| Part | Steps | What you do | What you see at the end |
|---|---|---|---|
| A | 1–7 | **Set up your test mailbox:** update kingo-pod, make the account, copy Kaminski's mails into it | his mails arrive in your test account in Gmail |
| B | 8 | **Test Langflow:** load the course flows, let Triage sort a mail | the AI's decision: `reply`, then `calendar` |
| C | 9–13 | **Set up n8n and test it:** logins, mail search, a test mail from your private account | your test mail in kingo-pod; answers from Kaminski's mails |

## Before you start

- **Time:** 1 to 2 hours. Some of it is waiting while things load.
- **Deadline:** **Friday, 6 November**.
- **Stuck?** Write to Frank right away. Then we fix it together.
- **You need:**
  - your kingo-pod;
  - the OpenRouter key Yanbo gave you;
  - the file `ws2_hw.zip` from Canvas (Workshop II). You download it in step 8.

## Part A · Set up your test mailbox

### 1. Update kingo-pod: get the new part called 'Mail'

kingo-pod is the course software on your laptop. Langflow and n8n run in it. This update adds a new part called
**Mail**. It connects your test account to kingo-pod. Later, it also sends the answers you approve.

Open a terminal in your kingo-pod folder and run:

```
./kingo update
./kingo mode abp
```

- `./kingo update` gets the newest version.
- `./kingo mode abp` starts the parts we need: Langflow, n8n, the database, CloudBeaver and Mail.

This can take a few minutes. You don't have to wait: go on with steps 2 to 5 in your browser. The update keeps running
in the terminal.

### 2. Make your test account in Gmail

1. Go to <https://accounts.google.com/signup>. Google will ask for your phone number.
2. Use this pattern for the address: **`n8n.<givenname>.<familyname>@gmail.com`**
   - For example, for Min-ji Kim: `n8n.minji.kim@gmail.com` (small letters, no spaces, no hyphens)
   - If the address is taken, add a 2: `n8n.minji.kim2@gmail.com`
3. When Google suggests addresses, click **Create your own Gmail address**. Type the part before `@gmail.com`.

This account is only for the course. Do **not** use your private account or your SKKU account: the AI assistant
you build will read and send mail in this account.

### 3. Set your test account to English

In Gmail, signed in with your test account: gear icon → **See all settings** → **General** → **Language**: *English
(US)* → **Save Changes** (at the bottom of the page). Do this before step 6: then the folders in your test account have
English names, as in this guide.

### 4. Turn on 2-Step Verification (needed for step 5)

Go to <https://myaccount.google.com/security> → **2-Step Verification** → turn it on. Choose text messages, the Google
prompt, or an authenticator app. A security key alone does not work for step 5.

### 5. Make an app password for kingo-pod

1. Go to <https://myaccount.google.com/apppasswords>.
2. Type a name for it, for example `kingo mail`, and click **Create**. The name does not matter; it only helps you
   find the password on this page later.
3. Google shows 16 letters, only once. Copy them.

This is not your Google password. It is a second password, only for kingo-pod: with it, kingo-pod can read your test
account and send the answers you approve. You can delete it any time on the same page.

### 6. Connect your test account to kingo-pod

First check that step 1 is done. In the terminal, in your kingo-pod folder, run:

```
./kingo status
```

You should see **Mail** in the list. Then run:

```
./kingo mail
```

It asks three questions:

1. **The address of your test account.** Type the full address, with `@gmail.com`, for example
   `n8n.minji.kim@gmail.com`.
2. **The app password** from step 5. You will not see it while you type.
3. **Other addresses kingo-pod may send mail to.** Type the address you will write from on 9 November: your private
   address (for example `yourname@naver.com`), your SKKU address, or both, with a comma between them.

   **Why?** kingo-pod sends mail only to your test account and the addresses you type here. A mail to anyone
   else lands in your own test account instead. So neither your AI assistant nor a mistake can send mail to
   anyone else.

kingo-pod then checks the login. It sends nothing. You should see a line that starts with `OK. Folders:`.

### 7. Copy Kaminski's mails into your test account

Your AI assistant will search Kaminski's old mails for facts when it drafts an answer. The update in step 1 brought
all 3,244 mails onto your laptop, inside kingo-pod. Now you copy them from kingo-pod into your test account.

1. In the terminal, in your kingo-pod folder, run:

   ```
   ./kingo mail seed
   ```

   After a short while, you see a line that starts with `Mailbox:` and ends with `Uploading starts now.`
2. The command is done, but the upload goes on inside kingo-pod for about 30 minutes. Keep kingo-pod running and your
   laptop awake.
3. Watch the mails arrive. Open Gmail in your browser, signed in with your test account:
   - **Sent** (in the menu on the left): the mails Kaminski wrote, about 1,500.
   - **All Mail** (in the menu on the left, under **More**): all 3,244 mails.
   - **Inbox**: stays empty. That is right: new mail comes in the workshop.
4. You don't have to wait for the upload: go on with Part B now. The upload keeps running in the background.

Good to know:
- Run `./kingo mail seed` only once. A second time would copy every mail twice, so kingo-pod stops you with
  `already seeded`.
- If your laptop sleeps or kingo-pod stops, start it again with `./kingo up`. The upload goes on by itself.

## Part B · Test Langflow (10 minutes)

### 8. Test Langflow: load the course flows and let Triage sort a mail

This part checks that Langflow works with the OpenRouter key Yanbo gave you, and with the flows of the course.

We prepared a Langflow flow for you: **Triage (Enron)**. It reads one mail and decides what to do with it: `reply`,
`calendar`, `forward` or `archive`. On 9 November, your AI assistant will use this flow for every new mail. Now you
test it by hand.

Open Langflow: <http://localhost:7860>.

1. **Check your key.** Langflow needs the OpenRouter key Yanbo gave you. Langflow keeps keys as **global variables**:
   you enter a key once, and every flow can use it.
   - Click your profile icon (top right) → **Settings** → **Global Variables**.
   - Is there a variable called `OPEN_ROUTER_API_KEY`? Then go on with 2.
   - If not, click **Add New**. Name: `OPEN_ROUTER_API_KEY`. Type: **Credential** (then Langflow hides the key on
     screen). Value: your key. Save.
   - More help: [Langflow: Global variables](https://docs.langflow.org/configuration-global-variables)
2. **Get the course files.** Download `ws2_hw.zip` from Canvas (Workshop II) and unzip it. You get a folder
   `ws2_hw` with two folders inside (`langflow` and `n8n`) and a readme. Every name starts with `ws2_`, for
   Workshop II. You need them now and in Part C.
3. **Load the flows.** Make a new project called `WS2 - Mail Assistant (Enron)`. Then click **Upload a flow** and upload these
   four files from the folder `ws2_hw/langflow` (from step 8.2), one by one: `ws2_triage_enron.json`,
   `ws2_draft_reply_enron.json`, `ws2_ask_mailbox_enron.json`, `ws2_judge_draft_enron.json`.
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

   If you see a yellow note "Legacy" on Text Input or Text Output, ignore it.
5. **Run it.** On the component **Text Output**, click ▶ (*Run component*). Wait a few seconds. Then click the small
   icon next to **Output Text** (*Inspect output*). You see `"action": "reply"` and a short reason after `"why"`.
   Thomas asks a question, so the AI assistant would draft an answer.
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
test account.

## Part C · Set up n8n and test it

n8n is the second tool of the course. In n8n you build **workflows**. A workflow is like a flow in Langflow: boxes
(nodes) joined by lines. The difference: Langflow is good for building AI; n8n is good for doing things. An n8n
workflow starts by itself (for example when a new mail arrives), passes data from box to box, asks Langflow, and acts,
for example in Gmail.

We name our workflows `WS2.0`, `WS2.1`, and so on: `WS2` stands for Workshop II, the number for the step of the
course. `WS2.0` is the first one; you import it in step 10. On 9 November, you will build more.

### 9. Open n8n and give it its logins: four credentials

Langflow and n8n each keep their own keys:
- **Langflow** keeps your OpenRouter key as a global variable (step 8.1). With it, Langflow can use the AI.
- **n8n** keeps its keys and passwords as **credentials**. A credential is a login that n8n saves for you. You make it
  once, and every workflow that needs it finds it by its name.

n8n needs four credentials. One of them lets n8n use your Langflow flows: for it, Langflow gives n8n a key of its own.

1. **Open n8n and make your account.** Open <http://localhost:5678>. The first time, n8n asks you to make an account.
   It lives only on your laptop.
   - *Set up owner account*: Email (for example the address of your test account), First Name, Last Name, and a
     Password with 8 or more characters, at least 1 number and 1 capital letter. Write the password down: n8n asks for
     it when you sign in again. Click **Next**.
   - *Customize n8n to you*: answer the questions as you like, then click **Get started**.
   - *Get paid features for free (forever)*: click **Skip**. The course does not need them.
   - n8n shows *Sign in* instead? Then you made an account before: sign in with it.
2. **A key from Langflow, for n8n.** In Langflow: profile icon → **Settings** → **Langflow API Keys** → *Create*. Copy
   the key.
3. **The four credentials in n8n.** In n8n: **Credentials** (in the menu on the left) → **Create credential**. Use
   exactly these names: the workflows you import later look for them by name.

   For each one: search for its type, change the name at the top of the window to the credential name below, then
   fill in the fields.

   - **Give n8n access to kingo-pod's database**
     - Credential name: `Mail (n8n_workshop_mail_n8n)`
     - Type: *Postgres*
     - Host: `postgres`
     - Database: `classroom`
     - User: `n8n_workshop_mail_n8n`
     - Password: `KINGO_PASSWORD` from the file `.env` in your kingo-pod folder
     - Port: `5432`
     - SSL: `disable`
   - **Give n8n access to your Langflow flows**
     - Credential name: `Langflow (Run API)`
     - Type: *Header Auth*
     - Name: `x-api-key`
     - Value: the Langflow key from 2
   - **Give n8n access to OpenRouter, to make the mails searchable (WS2.0)**
     - Credential name: `OpenRouter (embeddings)`
     - Type: *Header Auth*
     - Name: `Authorization`
     - Value: `Bearer ` (with a space), then your OpenRouter key
   - **Give n8n access to OpenRouter's chat models, for the guard on 16 November**
     - Credential name: `OpenRouter (chat)`
     - Type: *OpenRouter*
     - API Key: your OpenRouter key

   **Why two for OpenRouter?** It is the same key twice. WS2.0 and the guard talk to OpenRouter in two different ways,
   and each way needs the key in its own form.

More help: [n8n: Create a credential](https://docs.n8n.io/credentials/add-edit-credentials/)

### 10. Make Kaminski's mails searchable for your AI assistant: import WS2.0

1. In n8n, click **Create workflow**. In the new workflow, open the menu **…** at the top → **Import** → **From file**,
   and pick `ws2_hw/n8n/ws2_0_embed_mails.json` (in the folder from step 8.2).
2. If a node shows a credential warning, pick the credential with the same name.
3. Turn the workflow on: click **Publish** at the top. In the window that opens, click **Publish** again.
   **Publish** means: the workflow now runs by itself, every minute, until you unpublish it.

WS2.0 makes Kaminski's mails searchable, so that your AI assistant finds the right ones (step 13 tests it). Every
minute, it handles up to 320 mails. All 3,244 take about 12 minutes once step 7 is done.

### 11. Check that all mails arrived

When the upload of step 7 is done (about 30 minutes), run this in the terminal, in your kingo-pod folder:

```
./kingo mail status
```

You should see `Mails: 3244 in Postgres` (or a few more) and no `Last error`. In your test account in Gmail, open
**All Mail**: above the list, on the right, Gmail shows *1–50 of 3,244* (or a few more). **Sent** has about 1,500
mails.

**Look into the database.** No code needed, just look. CloudBeaver shows the database in your browser:
<http://localhost:8978>. How to log in: [Using CloudBeaver](https://huettner.io/kingo-pod/cloudbeaver/).

1. On the left, open **Classroom (PostgreSQL)** → **Databases** → **classroom** → **Schemas** →
   **n8n_workshop_mail** → **Tables**.
2. Double-click the table **messages**, then click the tab **Data**.
3. One row is one mail of Kaminski's mailbox. Scroll to the right: who sent it (`from_addr`), to whom (`to_addrs`),
   the subject (`subject`), the text (`body_text`).

The addresses here end in `.com` or `.edu`, not in `.example` as in Gmail: kingo-pod shows your AI assistant the real
addresses, and makes sure no mail ever reaches these people. On 9 November, your n8n workflows work with exactly
these rows.

### 12. Check that new mail arrives: a test mail from your private account

From your **private mail account**, send a mail to your test account. Within a minute, it is in the inbox of your test
account. kingo-pod also copies it into its database: `./kingo mail status` now shows one mail more.

**It works: the mail from your private account just arrived in kingo-pod on your laptop.**

### 13. Test the mail search: ask the mailbox

We also prepared a Langflow component for you: **Mail Search**. It finds the mails that fit a question, among all
3,244 mails. On 9 November, your AI assistant will use it to find facts for its drafts. The flow **Ask Mailbox (Enron)**
uses it, so you test Mail Search through this flow.

1. In Langflow, open the flow `Ask Mailbox (Enron)` → **Playground**, as usual.
2. Ask: *What is Steve Leppard's email address?* The answer gives steven.leppard@… and names the mail it comes from.
3. Ask three questions of your own about Kaminski's work in spring 2001.

**That's it: your laptop is ready for 9 November.** There you will build your first n8n workflow, WS2.1, and then
your AI assistant.

## If something goes wrong

| What you see | What to do |
|---|---|
| Triage shows an error (step 8) | Check the name `OPEN_ROUTER_API_KEY` in Langflow. Check that your key still has credit. |
| No app passwords page (step 5) | Turn on 2-Step Verification with text messages or the Google prompt. A security key alone is not enough. |
| `Sign-in failed` (step 6) | Paste the app password again (not your Google password). Check that 2-Step Verification is on. |
| `the mail service is off` | Run `./kingo mode abp`, then step 6 again. |
| `already seeded` (step 7) | Your account already has the mails. Look in Sent and All Mail. |
| WS2.0 fails at `fetch_embeddings_bge_m3` | In the credential `OpenRouter (embeddings)`, the value must be `Bearer `, a space, then your key. |
| Ask Mailbox gives no answer | WS2.0 is not finished yet (it needs about 12 minutes after step 7), or `OPEN_ROUTER_API_KEY` is missing in Langflow. |
| The Postgres credential fails | Host `postgres` (not `localhost`), SSL `disable`, the password from `.env`. |
| The mail from your private account does not arrive (step 12) | Wait a minute. Check the address. Look into the inbox of your test account in Gmail. |
| `./kingo mail status` shows an error | Copy the error into a mail to Frank. |
| You want to start again with another account | Run `./kingo mail reset`, then step 6 again. |

## The files in ws2_hw.zip

The Enron mail case. Every name starts with `ws2_`, for Workshop II.

The homework says when you need which file (step 8 and Part C).

### Langflow: upload all four in step 8

| File | Langflow flow | What it does |
|---|---|---|
| `langflow/ws2_triage_enron.json` | Triage (Enron) | sorts one mail: MailEx events, action (calendar, reply, forward, archive), deadline |
| `langflow/ws2_draft_reply_enron.json` | Draft Reply (Enron) | drafts Vince Kaminski's reply from his earlier mails, as of the mail's date; never from a confidential mail |
| `langflow/ws2_ask_mailbox_enron.json` | Ask Mailbox (Enron) | answers questions about the mailbox, with sources |
| `langflow/ws2_judge_draft_enron.json` | Judge Draft (Enron) | grades a draft against the reply really sent, 1 to 5 (right from 4); for the test bench of 16 November |

### n8n

| File | n8n workflow | What it does |
|---|---|---|
| `n8n/ws2_0_embed_mails.json` | WS2.0 - Embed Mails | embeds every mail of your mailbox into `n8n_workshop_mail.chunks`, so the search finds it |

### Setting up (short version)

The homework walks you through all of this step by step. The short version, to look things up later:

- Your pod runs in mode `abp`, and your test account is connected and holds Kaminski's mails (`./kingo mail`,
  `./kingo mail seed`).
- In Langflow, your OpenRouter key is a global variable named `OPEN_ROUTER_API_KEY`, with the key Yanbo gave you.

1. **Langflow:** make a project "WS2 - Mail Assistant (Enron)" and upload the four files from `langflow/`. In Settings →
   Langflow API Keys, create a key and copy it.
2. **n8n, credentials:** create four, with exactly these names:
   - `Mail (n8n_workshop_mail_n8n)`, type Postgres: host `postgres`, database `classroom`, user
     `n8n_workshop_mail_n8n`, password: the class password (`KINGO_PASSWORD` in your kingo-pod's `.env`), port
     `5432`, SSL `disable`.
   - `OpenRouter (embeddings)`, type Header Auth: name `Authorization`, value `Bearer ` followed by your OpenRouter key.
   - `Langflow (Run API)`, type Header Auth: name `x-api-key`, value your Langflow API key.
   - `OpenRouter (chat)`, type OpenRouter: your OpenRouter key (the guard's model).
3. **n8n, WS2.0:** *Import from File* `n8n/ws2_0_embed_mails.json`; where a node asks for a credential, pick the one of
   the same name. Publish it: it embeds your mailbox, in our test in about 12 minutes.
