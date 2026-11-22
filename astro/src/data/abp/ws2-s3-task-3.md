---
title: "Task 3 · Optional: let an AI judge the answers"
---

The test bench checks words, not meaning. You saw this in the quiz at the start of task 1. When your flow writes free
text, for example a reply to a mail, a right answer can come in many different words. Then a second flow can judge
each answer. It reads the input, the expected answer and your flow's answer, and it gives a grade from 1 to 5 with a
reason. We call this flow a **judge**. A grade of 4 or more counts as right.

First, you try a judge on Kaminski's mails, with the flow that writes his replies. Then you can use the judge on your
own flow.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **A judge doubles the calls.** For each test case, the test bench calls your flow and then the
judge. Both use the OpenRouter key that Yanbo gave you.

### Test Draft Reply with the judge

You need two Langflow flows from your homework before 9 November: **Draft Reply (Enron)** and **Judge Draft
(Enron)**. Both are in your Langflow project **WS2 - Mail Assistant (Enron)**. If one of them is missing, download
[`ws2_hw.zip`](https://huettner.io/abp/ws2/ws2_hw.zip) and unzip it. Then upload the missing file from its folder
`ws2_hw/langflow` into this project, as in your homework.

1. In the bench terminal, press Ctrl+C to stop the test bench. Then run this command. It downloads our five test
   mails for Draft Reply:

   ```
   cd ~/kingo-pod/claude/test && curl -fsSLO https://huettner.io/abp/ws2/draft_cases.csv
   ```

   Each row is a real mail to Kaminski. The column `expected` holds the reply that was really sent. The column
   `as_of` holds the date of the mail, because Draft Reply reads only the mails up to that date. The test bench gives
   this date to Draft Reply's second input.
2. Start the test bench on Draft Reply, with the judge:

   ```
   python3 test_bench.py --flow enron-draft-reply --judge enron-judge --cases draft_cases.csv
   ```

3. Reload <http://localhost:8765> in your browser, and click **Quick check**. The test bench now sends the first three
   mails to Draft Reply, once each, and the judge grades each draft. When it is done, the page shows the tab
   **Results**.
4. In the tab **Results**, each square shows the judge's grade, for example `grade 4`. Click a square. A window opens
   with the mail and, below it, the expected answer: the reply that Kaminski really sent. Click **Read the answers**.
   For each run, you see the judge's grade and its reason, and below them the draft.
5. Click the tab **Run**. Under **A name for the full test**, type `judge`, and click **Full test**. The test bench
   now sends all five mails to Draft Reply, three times each.

### Check the judge

A judge is a model too, so it can be wrong. Here, it even uses the same model as Draft Reply, GLM 5.3 Flash. In our
test of 22 November, the judge gave grade 1 to one draft and grade 4 to an almost identical one (case S01). The judge
sees only the mail, the expected answer and the draft, not the earlier mails that Draft Reply read. So check the judge
as you checked your expected answers in task 1:

1. Open three cases, and read the judge's reasons.
2. For each one, decide whether you agree with the grade. Write down the cases where you disagree, and why.

If you disagree with the judge on more than one case of three, do not trust its pass rate yet.

### Use the judge on your own flow

If your own flow writes free text, the judge can grade its answers too.

1. In your test cases, write into `expected` what a right answer says. With a judge, this can be a whole answer, for
   example an answer that a person in your team checked.
2. The judge's setting describes the Enron case. Describe your own case instead, after `--judge-context`. Start the
   test bench like this, with your endpoint name in place of `my-flow`, and with your own words in the quotes:

   ```
   python3 test_bench.py --flow my-flow --judge enron-judge --judge-context "An assistant of our company answers mails from customers. The reference is the answer that a person in our team checked."
   ```

3. Make a quick check, and then run the full test, as in task 1.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **Does your flow have a second input, like the date of Draft Reply?** Then add a column to your test
cases, named after the field that this input feeds, like `as_of` in `draft_cases.csv`. Ask Claude Code for the name of
that field in your flow.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M10 14.66V17a1 1 0 0 1-1 1 2 2 0 0 0-2 2v2"/><path d="M14 14.66V17a1 1 0 0 0 1 1 2 2 0 0 1 2 2v2"/><path d="M17.916 10H19.5A2.5 2.5 0 0 0 22 7.5V5a1 1 0 0 0-1-1h-3"/><path d="M4 22h16"/><path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/><path d="M6.084 10H4.5A2.5 2.5 0 0 1 2 7.5V5a1 1 0 0 1 1-1h3"/></svg> **You let an AI judge free text, and you checked the judge.** On 7 December, you can show how you know
that your flow's answers are right, even when they come in other words.
