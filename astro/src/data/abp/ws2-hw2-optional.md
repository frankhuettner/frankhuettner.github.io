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

The free account has more limits: it ends after 30 days, and it sends only Twilio's sample texts, not your own. That
is enough to see your n8n reach a phone.

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
   - Click **Send SMS**. Your phone shows it within a minute: Twilio works. Keep the SMS: you need the number it
     comes from in step 12.

[Stuck? Help for step 11](#step-11)

### 12. Copy three things from Twilio into a note

1. On the first page of your Twilio account (**Home** in the menu on the left), find the box with the name of your
   account, at first *My First Twilio Account*. Next to **Account SID**, click the copy icon, and paste it into a note.
2. Next to **Auth Token**, click the copy icon too, and paste it into the same note. The token stays hidden as dots;
   the eye shows it.
3. Add the number the SMS of step 11 came from, as a `+` and then only digits: `+1 (737) 250-8034` becomes
   `+17372508034`. A free account has no number of its own: it sends from numbers that Twilio shares among many
   accounts.

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
   - From: the number from step 12, such as `+17372508034`
   - To: your own mobile number with `+82` in front and without the first 0: `010-1234-5678` becomes
     `+821012345678`
   - Message: `sms_internal_alerts`. A free account sends only Twilio's sample texts; this name picks the alert.
4. Click **Execute workflow**, once.

Within a minute your phone shows Twilio's sample alert, in Korea marked [국제발신]: *Alert: System downtime
detected. …* Well done: your n8n can now reach a phone. Your own text needs a paid Twilio account.

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
| Another error from Twilio in `send_sms` | Check **From**: the number from step 12, a `+` and then only digits. Check **Message**: exactly `sms_internal_alerts`, as a free account sends only Twilio's sample texts. |
| No SMS after five minutes | On Twilio's page *Try out SMS* (step 11), open the tab **Logs** and look at the status of your SMS. Send Frank a screenshot. |
