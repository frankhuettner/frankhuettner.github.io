---
title: "Homework until 16 Nov, optional: Get ready for SMS"
---


This part is optional: skip it if you like.

An SMS lets your system reach a person who is not at the laptop, for example the person who approves a draft. You
need a free account at **Twilio**, a company that sends SMS for programs.

ONLY SHORT, MASKED TEXT GOES INTO AN SMS: NEVER A NAME OR THE TEXT OF A MAIL. Twilio is outside your laptop, and an
SMS goes through many hands.

**The free account has 100 SMS, and no more.** Send only the two test SMS in steps 11 and 14, and never put the Twilio node
into a workflow that runs on its own many times, such as every minute on a schedule or for every new mail: it can
use them all up before you notice.

### 11. Make a free Twilio account

1. Open <https://www.twilio.com/try-twilio> and sign up with your SKKU address.
2. Confirm your address with the mail Twilio sends you.
3. Twilio asks for your mobile number and sends it a code. Type the code in.
4. Send yourself a first SMS on Twilio's website. This also makes your number a **verified tester**: a free account
   sends SMS only to verified numbers.
   - On the first page of your Twilio account, under **Try it out**, tab **Communications**, click **Send an SMS**.
   - Under **To**, open the list. Your number is there, with `+82` in front and without the first 0
     (`010-1234-5678` becomes `+821012345678`)? Pick it. If not, pick **Add a verified tester**, type your number
     like that, and type in the code Twilio sends you.
   - Click **Send SMS**. Your phone shows it within a minute: Twilio works.

[Stuck? Help for step 11](#step-11)

### 12. Copy three things from Twilio

On the first page of your Twilio account (the *Console*), find the box *Account Info*:

1. Click **Get phone number** if there is no number yet. This is the number your SMS come from.
2. Copy into a note: the **Account SID**, the **Auth Token** (click **Show** first), and **My Twilio phone number**.

### 13. Give n8n the Twilio login: a credential

1. In n8n, click the **+** at the very top left, then **New credential**.
2. Type `Twilio` into the search box, pick **Twilio API**, and click **Continue**.
3. Top left, name it `Twilio`.
4. Paste the **Account SID** and the **Auth Token** from step 12. Click **Save**.

[Stuck? Help for step 13](#step-13)

### 14. Send yourself an SMS from n8n

Build a small n8n workflow with two nodes:

1. Make a new workflow and name it `WS2.4 - TEST - SMS`: a test, as the rules page names tests.
2. Add a first node: the trigger **Trigger manually**. Name it `trigger_manual`.
3. Add a **Twilio** node, the action **Send an SMS/MMS/WhatsApp message**. Name it `send_sms`.
   - Credential: `Twilio`
   - From: your Twilio phone number from step 12
   - To: your own mobile number with `+82` in front and without the first 0: `010-1234-5678` becomes
     `+821012345678`
   - Message: `Hello from my mail AI assistant`
4. Click **Execute workflow**, once.

Within a minute your phone shows the SMS. It starts with *Sent from your Twilio trial account*, and in Korea it may
be marked [국제발신] or [Web 발신]. You cannot reply to it. Well done: your n8n can now reach a phone.

[Stuck? Help for step 14](#step-14)

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 11

| What you see | What to do |
|---|---|
| Twilio does not accept your Korean mobile number | Write to Frank, with a screenshot. |
| The SMS from Twilio's website does not come | Check the number under **To**: `+82`, then your number without the first 0. Then open the tab **Logs** on the same page and look at the status of your SMS. |

#### Step 13

| What you see | What to do |
|---|---|
| The credential test fails | Copy the Account SID and the Auth Token again: no space before or after. |

#### Step 14

| What you see | What to do |
|---|---|
| `The number … is unverified` | A free account sends only to verified numbers. Check the number in **To**: `+82`, then your number without the first 0. Check that the same number is in the list under **To** on Twilio's page *Try out SMS* (step 11). |
| No SMS after five minutes | In Twilio, open **Monitor**, then **Logs**, then **Messaging**, and look at the status of your SMS. Send Frank a screenshot. |
