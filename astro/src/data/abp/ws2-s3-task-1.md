---
title: "Task 1 · Measure your pass rate: with our test bench, or with your own test"
---

On 7 December, the faculty team will ask how often your system is right. Your **pass rate** answers this question.
It is the share of your test cases that your system gets right. For example, if 8 of 10 test cases are right, your
pass rate is 80 %.

Our **test bench** measures your pass rate for you. It is a script in Python, and it shows its results on a page in
your browser. Because it runs the same test every time, you can compare two versions of your flow. It does three
things:

- It sends each test case to your Langflow flow, three times.
- It checks each answer. For each test case, you write down what a right answer must contain: one or more short pieces
  of text. We call them the **expected answer**. The test bench looks for these pieces in the answer. By default, it
  does not understand what the answer means, and no AI judges the answer.
- It shows the results.

<figure class="bp" aria-label="How the test bench measures your pass rate"><ol class="bp-path s5"><li class="bp-stop person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18"/><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/></svg></span><b>Your test cases</b><span>one row each: id, input, expected</span></li><li class="bp-stop muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></svg></span><b>The test bench</b><span>sends each input to your flow, three times</span></li><li class="bp-stop brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span><b>Your Langflow flow</b><span>answers</span></li><li class="bp-stop db"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m16 9-5.5 5.5L8 12"/></svg></span><b>The check</b><span>is each piece of the expected answer in the answer?</span></li><li class="bp-stop person"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg></span><b>Your pass rate</b><span>on a page in your browser</span></li></ol><figcaption>How the test bench measures your pass rate. By default, no AI judges the answers: the bench looks for the expected text.</figcaption></figure>

<div class="quiz multi">

**Quiz.** Here is a mail from the Enron case of 9 November. Paula Corey writes to Vince Kaminski: "you bet - i will
pick you up friday morning . Is 6:15 ok?" Suppose that the Langflow flow Draft Reply (Enron) writes his reply, and
that your test case has the expected answer `6:15; works for me`. These are two pieces of text, separated by `;`.
Which of these five drafts does the test bench count as right? Tick every one that it counts as right.

<ul>
<li data-right>"Paula, thanks. 6:15 works for me. Vince"</li>
<li data-right>"Works for me: 6:15 on Friday. Vince"</li>
<li>"Paula, 6:15 is fine. See you on Friday. Vince"</li>
<li>"Paula, 6:15 is too early for me. Can we say 7:00? Vince"</li>
<li data-right>"Paula, 6:15 works for me on Monday, but not on Friday. Vince"</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**The test bench counts three drafts as right: the first, the second and the last.** It looks for each piece of the
expected answer, exactly as it is written.

- "Paula, thanks. 6:15 works for me. Vince" is right, because both pieces are in it. Kaminski's real reply said the
  same.
- "Works for me: 6:15 on Friday. Vince" is right. The pieces may come in any order, and big and small letters count
  the same.
- "Paula, 6:15 is fine. See you on Friday. Vince" counts as wrong, even though it means the same. The words
  `works for me` are missing, and the test bench does not understand meaning.
- "Paula, 6:15 is too early for me. Can we say 7:00? Vince" counts as wrong, because `works for me` is missing.
- "Paula, 6:15 works for me on Monday, but not on Friday. Vince" counts as right, even though it says no to Friday.
  Both pieces are in it, and that is all that the test bench checks.

An AI as a judge looks at the meaning instead. We tried one: the Langflow flow Judge Draft (Enron), which you loaded
with your homework. It compares a draft with the reply that Kaminski really sent, and it gives a grade from 1 to 5,
with the model GLM 5.3 Flash. We gave it these five drafts, three times each. Every time, it counted the first three
drafts as right and the last two as wrong. By default, our test bench does not use such a judge. You can switch one
on, as in the optional task 3.

So, for a short fact, such as a time, a number or a fixed word, write that fact as the expected answer. For an answer
in free words, such as a reply, no piece of text is in every right answer. Then let the test bench read a fixed field,
as in our test of Triage, or let an AI judge, as in task 3. In both cases, read some of the answers yourself.

</details>

</div>

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Does your team already have its own test, for example an n8n test workflow?** Then keep it.
Still, read through this task, because it shows a simple test system that you could use instead. The last steps of
this task also work with your own test: the three runs, the test of your Demo Day flow, and the fix in a copy.

### Get the test bench

1. Open a second terminal for the test bench. We call it your **bench terminal**. On a Mac, press Command-T in
   Terminal. On Windows, open the app **Ubuntu** a second time. Leave Claude Code open in the first terminal.
2. In the bench terminal, run this command. It downloads the test bench and our five test mails into the folder of
   Claude Code:

   ```
   mkdir -p ~/kingo-pod/claude/test && cd ~/kingo-pod/claude/test && curl -fsSLO https://huettner.io/abp/ws2/test_bench.py && curl -fsSLO https://huettner.io/abp/ws2/triage_cases.csv
   ```

### First, run our test: the Triage flow and five test mails

Before you test your own flow, run our test from the demo. You only need to copy and paste. Afterwards, you know that
the test bench works on your laptop. For this test, you need the Langflow flow Triage (Enron) from 9 November. If you
do not have it, skip this part.

1. In the bench terminal, start the test bench on Triage:

   ```
   python3 test_bench.py --flow enron-triage --field action --cases triage_cases.csv
   ```

   The terminal now shows this line: `Test bench: open http://localhost:8765 in your browser. Stop it with Ctrl+C.`
   Leave the bench terminal open, because the page works only while it is open. Ctrl+C means: hold the key Control
   and press C. This is the same on a Mac.
2. Open <http://localhost:8765> in your browser. Under **A name for the full test**, type `triage`. Then click
   **Full test**. The test bench now sends the five test mails to Triage, three times each. The page counts the calls.
   When the test is done, the page shows the tab **Results**.
3. In the tab **Results**, each test mail is a column of three squares, one square per run. A square is green when
   Triage chose the expected action, and light red when it did not. Click a square. A window opens with the mail. Click
   **Read the answers** in it to see Triage's answers.

Each test mail is one row of the file `triage_cases.csv`. Its column `input` holds the mail, and its column `expected`
holds the action that Triage must choose. Because the command says `--field action`, the test bench reads only the
field `action` in Triage's answer, and a case is right when this field is exactly the expected action. Your own test
cases also say what goes in and what must come out. Without `--field`, the test bench looks for the pieces of
`expected` in the whole answer, as in the quiz.

Under the pass rate, the page shows the **95 % confidence interval**. This is the range in which the true pass rate
lies, with 95 % confidence. With only five mails, this range is wide, for example from 57 to 100 %, because five cases
say little. This is why your own test needs more cases.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **The test bench works on your laptop.** Now do the same for your own flow.

### Get your test cases ready

1. Open the test set that your team made for Demo Day, in Excel or Google Sheets. If you have no test set, you will
   write ten new cases in step 2.
2. Make a new sheet. In its first row, type these three column names as the table header, one name per cell. Below
   the header, write one test case per row.
   - `id`: a number, such as 1, 2 or 3.
   - `input`: what goes into your flow, in the form in which your flow gets it, for example a question or a mail.
   - `expected`: the **expected answer**. This is what must appear in the answer: one or more short pieces of text,
     separated by `;`.
3. Write each expected answer so that the test bench can find it. As in the quiz at the start of this task, a case
   counts as right when every piece of `expected` appears in the answer, exactly as you wrote it. Every letter, number
   and comma counts, but big and small letters count the same. A piece also counts inside a longer word: `no` is found
   in "not".

   So write short pieces that every right answer contains, such as an ID, a number or a fixed word. Do not write a
   whole sentence: the model words a sentence differently each time, so the test bench would never find it. Also be
   careful with words that a wrong answer can contain too. If the expected answer is only `6:15`, the draft "6:15 is
   too early for me" also counts as right, because it contains `6:15`.

   <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Does your flow give right answers in different words?** Then a fixed field helps, as in our
   test of Triage, which reads the field `action`. Let a copy of your flow end each answer with one field in JSON, for
   example `{"result": "yes"}`. Then add `--field result` to the command that starts the test bench, and write the one
   right value as the expected answer, for example `yes`. Every flow that you compare needs this field, also your Demo
   Day flow. To get the copy, send this request to Claude Code, and replace `MY FLOW` in both places with the name of
   your flow:

   ```
   Make a copy of my Langflow flow MY FLOW and call it "MY FLOW - field". In the copy, let every answer end with one line of JSON with the field result, for example {"result": "yes"}. Change nothing else, and do not change the original. Then tell me the endpoint name of the copy.
   ```
4. Start with about ten cases. You can add more later. More cases make the confidence interval narrower, and 30 cases
   are a good aim.
5. Every Langflow flow has an address, for example `http://localhost:7860/api/v1/run/my-flow`. The last part of this
   address, here `my-flow`, is the **endpoint name** of the flow. Paste this request into Claude Code, but do not press
   Enter yet:

   ```
   Below are my team's test cases, with the columns id, input and expected. In expected, the pieces of text are separated by ";". Save them as test/cases.csv in your folder, as a CSV file with exactly these three columns. Then list my Langflow flows with the name of each in its address (its endpoint name), and ask me which one my test cases are for. My test cases:
   ```

6. In your sheet, select your cells, including the first row, and copy them. In Claude Code, paste them after the
   request, and press Enter. Claude Code shows a long paste as one short line, and that is fine.
7. Claude Code now lists your flows with their endpoint names. Tell Claude Code which flow your test cases are for,
   and write down its endpoint name.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Would you rather let Claude Code build a test bench for you?** That also works, as long as Claude
Code keeps the script, so that you can run the same test again. Paste this request into Claude Code, and add the
endpoint name of your flow at the end:

```
Build me a test bench for my Langflow flow, with my test cases in test/cases.csv: every case three times, a new session for every call (so that no case sees another case's chat). Keep the script in test/, every answer in test/results/, and a report as an HTML page, test/report.html. Write test/README.md: what the script checks, the exact command to run it again, the model and the date. Do not change my flow or the test cases. My flow:
```

### Start the test bench on your flow, and make a quick check

1. In the bench terminal, press Ctrl+C to stop the test bench. Then paste this command, but do not press Enter yet.
   Replace `my-flow` with your endpoint name, and then press Enter:

   ```
   cd ~/kingo-pod/claude/test && python3 test_bench.py --flow my-flow
   ```

   Because this command has no `--cases`, the test bench uses the file `cases.csv`, which Claude Code saved for you.
2. Reload <http://localhost:8765> in your browser, and click **Quick check**. The test bench now sends your first
   three test cases to your flow, once each. When it is done, the page shows the tab **Results**.
3. In the tab **Results**, each test case is a square. A square is green when the answer was right, and light red when
   it was not. Click a square to read the answer. If it looks like the answers that your flow gives in its
   Playground, the test bench reads your flow correctly.

If the answer says **HTTP 404**, the endpoint name is wrong. Click the tab **Run**, type the endpoint name again under
**Flow**, and click **Quick check** again.

If the answers say **no answer** or **HTTP 500**, if a red box says **calls failed**, or if an answer looks strange,
your flow probably needs something that the test bench does not send yet, for example a second input. Send this
request to Claude Code, and describe what you see at the end:

```
The test bench in test/test_bench.py does not read my Langflow flow right. Find out why from my flow and from the newest file in test/results/. Make a copy of the bench, test/test_bench_ours.py, that works with my flow, and tell me the command to start it. Do not change my flow, and do not change test/cases.csv. What I see:
```

Then press Ctrl+C in the bench terminal, and start the new copy of the test bench with the command that Claude Code
gives you.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **The test bench reads your own flow.** Now run the full test.

### Run the full test

1. Click the tab **Run** at the top of the page. Under **A name for the full test**, type `today`, and click **Full
   test**. The test bench now sends every test case to your flow, three times each.
2. Until the test is done, keep your laptop open, because a sleeping laptop stops the test. Also keep the bench
   terminal open. You can close the page and open it again at any time.
3. While the test runs, do not change your flow in Langflow. Go on with task 2 instead. When the test is done, come
   back here to the next step.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Each full test costs a little money.** The test bench calls your flow once per test case and run,
with the OpenRouter key that Yanbo gave you, just as when you chat with your flow. So start a full test only when you
need one.

**Next: [Task 1 · Check your pass rate, and improve your flow →](/abp/ws2/s3-task-1b/)**
