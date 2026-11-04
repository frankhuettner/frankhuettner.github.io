---
title: "Homework, Part A: Set up your test mailbox"
lede: "Steps 1 to 7: update kingo-pod, make the account, copy Kaminski's mails into it."
---


<figure class="bp bp-setup bp-mini" aria-label="Where you are: Part A"><div class="bp-sys"><div class="bp-node mail now"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><b>Gmail</b><span>your test Gmail account</span><em>Part A · steps 1–7 · you are here</em></div><div class="bp-node box now"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="7" rx="1.5"/><rect x="3" y="13" width="18" height="7" rx="1.5"/><path d="M7 7.5h.01M7 16.5h.01"/></svg></span><b>Mail</b><span>kingo-pod's service: copies the mails, masks addresses</span><em>Part A · steps 1–7 · you are here</em></div><div class="bp-node db now"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span><b>PostgreSQL</b><span>every mail as a row</span><em>Part A · steps 1–7 · you are here</em></div><div class="bp-node muscle later"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span><b>n8n</b><span>does the work</span><em>Part C · steps 9–13</em></div><div class="bp-node brain later"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Langflow</b><span>thinks: sorts and drafts</span><em>Part B · step 8</em></div><div class="bp-part pa now">Part A · steps 1–7 · you are here</div><div class="bp-part pc later">Part C · steps 9–13</div><div class="bp-part pb later">Part B · step 8</div></div></figure>

### 1. Update kingo-pod: get the new part called 'Mail'

kingo-pod is the course software on your laptop. Langflow and n8n run in it. This update adds a new part called
**Mail**. It connects your test Gmail account to kingo-pod. Later, it also sends the answers you approve.

Open a terminal (on a Mac: the **Terminal** app; on Windows: the **Ubuntu** app) and run this one line:

```
cd ~/kingo-pod && git checkout -- . && git pull --ff-only && ./kingo backup && ./kingo update && ./kingo mode abp
```

Near the end, you should see a line that starts with `Stack updated — kingo-pod 1.4.3` (or a higher number).

This can take a few minutes. You don't have to wait: go on with steps 2 to 5 in your browser. The update keeps running
in the terminal.

<details class="more">
<summary>In case you care about what this does</summary>

- `&&` just connects the commands: each one starts when the one before it worked. If one fails, the line stops
  there.
- `cd ~/kingo-pod` goes to your kingo-pod folder.
- `git checkout -- .` undoes changes in your kingo-pod folder. For Workshop I, many of you added `nemoguardrails` to
  `langflow/requirements.txt`. That change stopped every update since. kingo-pod now has `nemoguardrails` built in.
- `git pull --ff-only` gets the newest version.
- `./kingo backup` saves your Langflow flows and n8n workflows first.
- `./kingo update` builds the new version.
- `./kingo mode abp` starts the parts we need: Langflow, n8n, the PostgreSQL database, CloudBeaver and a service
  called Mail.

</details>

[Stuck? Help for step 1](#step-1)

### 2. Make your test Gmail account

1. Go to <https://accounts.google.com/signup>. Google will ask for your phone number.
2. Use this pattern for the address: **`n8n.<givenname>.<familyname>@gmail.com`**
   - For example, for Min-ji Kim: `n8n.minji.kim@gmail.com` (small letters, no spaces, no hyphens)
   - If the address is taken, add a 2: `n8n.minji.kim2@gmail.com`
3. When Google suggests addresses, click **Create your own Gmail address**. Type the part before `@gmail.com`.

This account is only for the course. Do **not** use your private account or your SKKU account: the AI assistant
you build will read and send mail in this account.

### 3. Set your test Gmail account to English

In Gmail, signed in with your test Gmail account: gear icon → **See all settings** → **General** → **Language**:
*English (US)* → **Save Changes** (at the bottom of the page). Do this before step 6: then the folders in your test
Gmail account have English names, as in this guide.

### 4. Turn on 2-Step Verification (needed for step 5)

Go to <https://myaccount.google.com/security> → **2-Step Verification** → turn it on. Choose text messages, the Google
prompt, or an authenticator app. A security key alone does not work for step 5.

### 5. Make an app password for kingo-pod

1. Go to <https://myaccount.google.com/apppasswords>.
2. Type a name for it, for example `kingo mail`, and click **Create**. The name does not matter; it only helps you
   find the password on this page later.
3. Google shows 16 letters, only once. Copy them.

This is not your Google password. It is a second password, only for kingo-pod: with it, kingo-pod can read your test
Gmail account and send the answers you approve. You can delete it any time on the same page.

[Stuck? Help for step 5](#step-5)

### 6. Connect your test Gmail account to kingo-pod

First check that step 1 is done. In the terminal, in your kingo-pod folder, run:

```
./kingo status
```

You should see **Mail** in the list. Then run:

```
./kingo mail
```

It asks three questions:

1. **The address of your test Gmail account.** Type the full address, with `@gmail.com`, for example
   `n8n.minji.kim@gmail.com`.
2. **The app password** from step 5. You will not see it while you type.
3. **Other addresses kingo-pod may send mail to.** Type your SKKU address. On 9 November you will write from your
   SKKU address, and your AI assistant's answers go back to it.

   <details class="more">
   <summary>Why kingo-pod asks for these addresses</summary>

   kingo-pod sends mail only to your test Gmail account and the addresses you type here. A mail to someone in
   Kaminski's mails lands in your own test Gmail account instead. A mail to any other address is not sent at all. So
   neither your AI assistant nor a mistake can send mail to anyone else.

   </details>

   **Forgot your SKKU address, or want to add another one later?** Run `./kingo mail` again. Press Enter to keep
   your test Gmail account, paste the app password again (or make a new one as in step 5), then type the addresses.

kingo-pod then checks the login. It sends nothing. You should see a line that starts with `OK. Folders:`.

[Stuck? Help for step 6](#step-6)

### 7. Copy Kaminski's mails into your test Gmail account

Your AI assistant will search Kaminski's old mails for facts when it drafts an answer. The update in step 1 brought
all 3,244 mails onto your laptop, inside kingo-pod. Now you copy them from kingo-pod into your test Gmail account.

1. In the terminal, in your kingo-pod folder, run:

   ```
   ./kingo mail seed
   ```

   After a short while, you see a line that starts with `Mailbox:` and ends with `Uploading starts now.`

   <details class="more">
   <summary>What happens</summary>

   In a few seconds, the command puts all mails into kingo-pod's service called Mail, on your laptop. Mail keeps this
   copy: with it, Mail knows what is new on each side. From there, kingo-pod copies the mails into its PostgreSQL
   database and uploads them to your test Gmail account, round by round. In the end, every mail is in three places: in
   Gmail, in Mail, and in PostgreSQL, where n8n and your AI assistant read it.

   </details>
2. The command is done, but the upload goes on inside kingo-pod for about 30 minutes, sometimes longer. Be patient.
   Keep kingo-pod running and your laptop awake.
3. Watch the mails arrive. They come step by step over the 30 minutes, so the numbers in Gmail grow while you
   watch. Open Gmail in your browser, signed in with your test Gmail account. When the upload is done, you see:
   - **Sent** (in the menu on the left): the mails Kaminski wrote, about 870 conversations.
   - **All Mail** (in the menu on the left, under **More**): about 1,600 conversations.
   - **Inbox**: stays empty for now. That is right: new mail comes in step 12 and in the workshop.

   <details class="more">
   <summary>Why not 3,244?</summary>

   Gmail counts conversations, not mails: a mail and all its answers are one conversation. So Gmail shows smaller
   numbers, but all 3,244 mails are there.

   </details>

   To count the mails, ask kingo-pod: run `./kingo mail status`. It shows each folder twice, here and at Gmail. When
   the numbers are the same in every row, the upload is done. (No such rows? Run `./kingo update` first.)
4. You don't have to wait for the upload: go on with [Part B](/abp/ws2/hw-b/) now. The upload keeps running in the background.

Good to know:
- `./kingo mail seed` copies every mail only once. If you run it again, kingo-pod answers `already seeded` and gives
  the upload a push.
- If your laptop sleeps or kingo-pod stops, start it again with `./kingo up`. The upload goes on by itself.

[Stuck? Help for step 7](#step-7)

**Next: [Part B · Test Langflow →](/abp/ws2/hw-b/)**

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 1

| What you see | What to do |
|---|---|
| The line stops with `fatal: not a git repository` | Your kingo-pod folder came from the old ZIP download. Run `./kingo update`, then `./kingo mode abp`. |
| The line stops with another error | Send Frank a screenshot of the error and of what `git status` shows (run it in your kingo-pod folder). |

#### Step 5

| What you see | What to do |
|---|---|
| No app passwords page | Turn on 2-Step Verification with text messages or the Google prompt. A security key alone is not enough. |

#### Step 6

| What you see | What to do |
|---|---|
| `Sign-in failed` | Paste the app password again (not your Google password). Check that 2-Step Verification is on. |
| `the mail service is off` | Run `./kingo mode abp`, then step 6 again. |
| You want to start again with another account | Run `./kingo mail reset`, then step 6 again. |

#### Step 7

| What you see | What to do |
|---|---|
| `already seeded` | Your account already has the mails. Look in Sent and All Mail. |
| The numbers in Gmail stop growing | Be patient: kingo-pod uploads in rounds, and Gmail's numbers can stand still for up to 10 minutes. Reload Gmail. Keep your laptop awake. Still no change after 20 minutes? Run `./kingo update`, then `./kingo mail seed` again: it copies nothing twice and gives the upload a push. Still stuck? Send Frank everything that `./kingo mail status` shows. |
| Gmail shows about 1,600 in All Mail, not 3,244 | That is right: Gmail counts conversations, not mails. `./kingo mail status` counts the mails. |
| `./kingo mail status` shows an error | Copy the error into a mail to Frank. |
