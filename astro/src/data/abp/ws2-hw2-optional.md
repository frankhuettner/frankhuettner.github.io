---
title: "Homework until 16 Nov, optional: Get ready for SMS"
---


An SMS lets your system reach a person who is not at the laptop, for example the person who approves a draft. You
need an account with a company that sends SMS, for example **Twilio** (or **SOLAPI**). The steps here use Twilio.

**Twilio costs money.** Its free trial account is enough for the two test SMS here, and it needs no credit card: it
has 100 SMS, ends after 30 days, and sends only Twilio's sample texts, not your own.

**An SMS is not a safe channel.** Never send a name or the text of a mail, even with a paid account. An SMS passes
through the SMS company and the phone networks, and it can show up on a locked phone. Send only a short note, such as
"A draft waits for you".

### 15. Make a free Twilio trial account

1. Open <https://www.twilio.com/try-twilio> and sign up with your SKKU address.
2. Confirm your address with the mail Twilio sends you.
3. Twilio asks for your mobile number and sends it a code. Type the code in.
4. Send yourself a first SMS on Twilio's website. This also makes your number a **verified tester**: a trial account
   sends SMS only to verified numbers.
   - On the first page of your Twilio account, under **Try it out**, tab **Communications**, click **Send an SMS**.
     The page *Try out SMS* opens.
   - Under **To**, open the list. Your number is there, with `+82` in front and without the first 0
     (`010-1234-5678` becomes `+821012345678`)? Pick it. If not, pick **Add a verified tester**, type your number
     like that, and type in the code Twilio sends you.
   - Click **Send SMS**. Your phone shows it within a minute: Twilio works. Keep the SMS: you need the number it
     comes from in step 16.

[Stuck? Help for step 15](#step-15)

### 16. Copy three things from Twilio into a note

1. On the first page of your Twilio account (**Home** in the menu on the left), find the box with the name of your
   account, at first *My First Twilio Account*. Next to **Account SID**, click the copy icon, and paste it into a note.
2. Next to **Auth Token**, click the copy icon too, and paste it into the same note. The token stays hidden as dots;
   the eye shows it.
3. Add the number the SMS of step 15 came from, as a `+` and then only digits: `+1 (737) 250-8034` becomes
   `+17372508034`. A trial account has no number of its own: it sends from numbers that Twilio shares among many
   accounts.

### 17. Give n8n the Twilio login: a credential

1. In n8n, click the **+** at the very top left, then **New credential**.
2. Type `Twilio` into the search box, pick **Twilio API**, and click **Continue**.
3. Top left, name it `Twilio`.
4. Paste the **Account SID** and the **Auth Token** from step 16. Click **Save**.

[Stuck? Help for step 17](#step-17)

### 18. Send yourself an SMS from n8n

Build a small n8n workflow with two nodes:

1. Make a new workflow and name it `WS2.4 - TEST - SMS`: a test, as the rules page names tests.
2. Add a first node: the trigger **Trigger manually**. Name it `trigger_manual`.
3. Add a **Twilio** node, the action **Send an SMS/MMS/WhatsApp message**. Name it `send_sms`.
   - Credential: `Twilio`
   - From: the number from step 16, such as `+17372508034`
   - To: your own mobile number with `+82` in front and without the first 0: `010-1234-5678` becomes
     `+821012345678`
   - Message: `sms_internal_alerts`. A trial account sends only Twilio's sample texts; this name picks the alert.
4. Click **Execute workflow**, once.

Within a minute your phone shows Twilio's sample alert, in Korea marked [국제발신]: *Alert: System downtime detected. …*
Well done: your n8n can now reach a phone. Your own text needs a paid Twilio account. SOLAPI seems to give you more
freedom in its trial: from what it writes, the points you get at sign-up already send your own text, from your own
number. For this, you need a Korean phone number in your own name.

[Stuck? Help for step 18](#step-18)

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 15

| What you see | What to do |
|---|---|
| Twilio does not accept your Korean mobile number | Write to Frank, with a screenshot. |
| The SMS from Twilio's website does not come | Check the number under **To**: `+82`, then your number without the first 0. Then open the tab **Logs** on the same page and look at the status of your SMS. |

#### Step 17

| What you see | What to do |
|---|---|
| The credential test fails | Copy the Account SID and the Auth Token again: no space before or after. |

#### Step 18

| What you see | What to do |
|---|---|
| `The number … is unverified` | A trial account sends only to verified numbers. Check the number in **To**: `+82`, then your number without the first 0. Check that the same number is in the list under **To** on Twilio's page *Try out SMS* (step 15). |
| Another error from Twilio in `send_sms` | Check **From**: the number from step 16, a `+` and then only digits. Check **Message**: exactly `sms_internal_alerts`, as a trial account sends only Twilio's sample texts. |
| No SMS after five minutes | On Twilio's page *Try out SMS* (step 15), open the tab **Logs** and look at the status of your SMS. Send Frank a screenshot. |
