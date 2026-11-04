---
title: "Homework, optional: Look into the database"
lede: "Step 14: see Kaminski's mails and your test mail as rows, in CloudBeaver."
---


### 14. Look into the database with CloudBeaver

This part is optional: skip it if you like. CloudBeaver shows kingo-pod's database in your browser:
<http://localhost:8978>. In Workshop II, it shows you what your AI assistant did, row by row.

**First time in CloudBeaver? Open [Using CloudBeaver](https://huettner.io/kingo-pod/cloudbeaver/) first and do its
steps 1 and 2.** This page is not just extra help: without it, you cannot get in. CloudBeaver has two logins, one for
CloudBeaver and one for the database, with different passwords. The page shows both. You do it only once.

1. On the left, open **Classroom (PostgreSQL)** → **Databases** → **classroom** → **Schemas** →
   **n8n_workshop_mail** → **Tables**.
2. Double-click the table **messages**, then click the tab **Data**.
3. One row is one mail of Kaminski's mailbox. Scroll to the right: who sent it (`from_addr`), to whom (`to_addrs`),
   the subject (`subject`), the text (`body_text`).
4. Find your test mail from step 12: sort the table by the column `sent_at`, newest first. To sort, move the mouse over
   the head of the column `sent_at`: small arrows appear. Click them until the newest mail is at the top. Your mail is
   the first row.

On 9 November, your n8n workflows work with exactly these rows.

[Stuck? Help for step 14](#step-14)

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 14

| What you see | What to do |
|---|---|
| CloudBeaver shows `No Connections`, or **Classroom (PostgreSQL)** does not open | You are not logged in yet. Do steps 1 and 2 of [Using CloudBeaver](https://huettner.io/kingo-pod/cloudbeaver/): two logins, with two different passwords. |
