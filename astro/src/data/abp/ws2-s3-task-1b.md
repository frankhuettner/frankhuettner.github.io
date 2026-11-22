---
title: "Task 1 · Check your pass rate, and improve your flow"
---

### Check your expected answers: look at three cases yourself

When the full test is done, check whether the test bench checked your cases correctly:

1. In the tab **Results**, click a light red square, and read the answer. Decide whether the answer is really wrong,
   or whether only the expected answer did not match, for example `10 am` against `10:00 AM`.
   - If the answer is really wrong, keep the case. It tells you something about your flow.
   - If the answer is right and the expected answer was too strict, change the expected answer (see step 3).
2. Click two green squares. Are those answers really right? If one of them is wrong, its expected answer was too
   loose. Change it (see step 3).
3. To change an expected answer, first change it in your sheet, and write down why you changed it. Then send this
   request to Claude Code, with the changed row at the end:

   ```
   Update this test case in test/cases.csv, the row with the same id. Change nothing else:
   ```

   The test bench reads the test cases only when it starts. So press Ctrl+C in the bench terminal. Then press the arrow
   key Up, which brings back your last command, and press Enter. Run the full test `today` again.

<div class="quiz">

**Quiz.** Our test mail 126 says "Conference Call Tomorrow at 10 am EDT". A case fails. Its expected answer is
`10 am`, and the answer says `10:00 AM EDT`. What do you change?

<ul>
<li>The expected answer, so that it says 10:00</li>
<li>The prompt of your flow, so that it writes 10 am</li>
<li data-right>First, decide what you need: does a later step, such as your n8n workflow, need the form 10 am?</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**It depends on what you need, and you decide.** If only the time matters, the answer is right. Then change the
expected answer, for example to `10:00`, and write down why. If a later step needs the form 10 am, the answer is
wrong. Then improve your flow, as in the optional step at the end of this task.

</details>

</div>

### Read your pass rate

The tab **Results** shows four things:

- your **pass rate**, with one bar per run;
- its **95 % confidence interval**: the range in which your true pass rate lies, with 95 % confidence. More test
  cases make this range narrower;
- how many cases were right in all three runs;
- the **seconds per call**. One call is one test case, sent to your flow once.

The tab **Errors** lists the cases that you should look at first.

<div class="quiz">

**Quiz.** A case is wrong in all three runs, the same way each time. What does that tell you?

<ul>
<li>Bad luck: run it again, and it will be right</li>
<li data-right>Not bad luck: read the answer, then fix your flow or the expected answer</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Not bad luck.** Bad luck would change from run to run. So read the answer. If it is wrong, improve your flow, as in
the optional step at the end of this task. If it is right, fix the expected answer.

</details>

</div>

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M10 14.66V17a1 1 0 0 1-1 1 2 2 0 0 0-2 2v2"/><path d="M14 14.66V17a1 1 0 0 0 1 1 2 2 0 0 1 2 2v2"/><path d="M17.916 10H19.5A2.5 2.5 0 0 0 22 7.5V5a1 1 0 0 0-1-1h-3"/><path d="M4 22h16"/><path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/><path d="M6.084 10H4.5A2.5 2.5 0 0 1 2 7.5V5a1 1 0 0 1 1-1h3"/></svg> **You have your pass rate, measured three times.** On 7 December, you can say it like this: "On our 30
test cases, over three runs, our pass rate was 77 %. With 95 % confidence, it lies between 59 and 88 %. Each call took
about 40 seconds."

### Measure your Demo Day flow too, if you still have it

The faculty team asks how your flow has improved since Demo Day. The fairest way to show this is to run the same test
cases on both versions of your flow.

1. In Langflow, open the page of your project, and drag the file of your Demo Day flow onto it. This is the JSON file
   that you exported for Demo Day.
2. Send this request to Claude Code:

   ```
   I just loaded my Demo Day flow into Langflow; it is my newest flow. Rename it so that its name ends with " - Demo Day", and tell me its endpoint name.
   ```

3. On the page of the test bench, click the tab **Run**. Type that endpoint name under **Flow**, and type `demo day`
   under **A name for the full test**. Then click **Full test**.
4. When the test is done, open the tab **Compare**. Pick `demo day` under **Before** and `today` under **After**. The
   tab shows which cases got better and which got worse. It also says whether the change is bigger than chance:
   *measurably better*, *measurably worse*, or *no measurable difference*. This needs at least 20 test cases in both
   tests. With fewer, the tab shows the change and says *Too few test cases for an interval*. That is normal, and it is
   not a failure.
5. In the tab **Run**, type your own endpoint name under **Flow** again, so that your next test uses your current flow.

If you no longer have your Demo Day flow, your test `today` is your starting point.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **You can show in numbers how your flow has changed since Demo Day.**

### Optional: improve your flow with Claude Code

Has your test found cases that your flow gets wrong? Then you can improve your flow with Claude Code. Use the habits
from your homework until 23 November:

- **Plan first.** Let Claude Code find out why the cases failed, and let it propose a change before it changes
  anything.
- **Work on a copy.** Let Claude Code change a copy of your flow, not the flow that your n8n workflow calls. A change in
  Langflow has no undo.
- **Say what "done" looks like.** The copy must be better on the failed cases and no worse on the others. Run the full
  test on the copy, with the same test cases, and compare it with `today` in the tab **Compare**.
- **Keep the test honest.** Claude Code must not change your test cases, and it must not put a test case into the
  prompt of the copy. Otherwise, the test only measures itself.

If the copy is better, you decide whether your n8n workflow should call it.

When you are done with the test bench, you can keep its page as one file. Press Ctrl+C in the bench terminal, and run
`python3 test_bench.py --report`. This writes the file `report.html` in the folder `test`, with the same tabs as the
page. To open it on a Mac, run `open report.html`. On Windows, run `explorer.exe .`, and double-click `report.html`.

**Next: [Task 2 · Decide on whose computers your system runs, and what it needs →](/abp/ws2/s3-task-2/)**
