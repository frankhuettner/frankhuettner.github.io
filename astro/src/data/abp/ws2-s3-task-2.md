---
title: "Task 2 · Decide on whose computers your system runs, and what it needs"
---

On 7 December, the faculty team will ask what management must approve for your system. Where your system runs
decides a large part of the answer. A company can run your system in three ways. The picture shows, for each way,
what runs outside the company and what runs on the company's own computers:

<figure class="bp bp-ways" aria-label="Three ways to run your system"><div class="bp-way3"><div class="bp-way"><b>Online</b><span class="bp-sub">everything at providers</span><div class="bp-zone out"><em>outside, at providers</em><span class="bp-chip muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span>n8n</span><span class="bp-chip brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span>Langflow</span><span class="bp-chip db"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span>database</span><span class="bp-chip box"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></span>model</span></div><div class="bp-zone in"><em>your company's own computers</em><i>nothing</i></div></div><div class="bp-way"><b>Partly self-hosted</b><span class="bp-sub">like your laptop: only the model outside</span><div class="bp-zone out"><em>outside, at providers</em><span class="bp-chip box"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></span>model</span></div><div class="bp-zone in"><em>your company's own computers</em><span class="bp-chip muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span>n8n</span><span class="bp-chip brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span>Langflow</span><span class="bp-chip db"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span>database</span></div></div><div class="bp-way"><b>Air-gapped</b><span class="bp-sub">no line to the outside</span><div class="bp-zone out"><em>outside, at providers</em><i>nothing</i></div><div class="bp-zone in"><em>your company's own computers</em><span class="bp-chip muscle"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="9" width="5" height="6" rx="1.2"/><rect x="16.5" y="3" width="5" height="6" rx="1.2"/><rect x="16.5" y="15" width="5" height="6" rx="1.2"/><path d="M7.5 12H11M11 12V6h5.5M11 12v6h5.5"/></svg></span>n8n</span><span class="bp-chip brain"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l1.9 4.6 4.6 1.9-4.6 1.9L12 16l-1.9-4.6-4.6-1.9 4.6-1.9z"/><path d="M18.5 15.5l.8 1.9 1.9.8-1.9.8-.8 1.9-.8-1.9-1.9-.8 1.9-.8z"/></svg></span>Langflow</span><span class="bp-chip db"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></span>database</span><span class="bp-chip box"><span class="bp-disc"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></span>model</span></div></div></div><figcaption>What runs where. Whatever runs outside gets your data.</figcaption></figure>

The three ways differ in what data leaves the company, in cost, and in the quality of the model. (A **GPU** is the
chip that runs a model.)

| | Online | Partly self-hosted | Air-gapped |
|---|---|---|---|
| Compliance: what data leaves | all of it | what goes to the model | none |
| Cost | low: the provider runs it | medium: servers, updates | high: own GPUs, all the work |
| Model quality | the best models | the best models | what your own GPUs can run |

Your laptop is partly self-hosted: n8n, Langflow and the database run on your laptop, but the model runs outside,
through OpenRouter.

### Find out what your flows send to the model

1. Send this request to Claude Code:

   ```
   Look at my team's Langflow flows. In five short lines: what goes to the model in each call, and what text goes out to make embeddings? For example the mail, what a tool found, or a document. Name the kinds of data, not the data itself.
   ```

2. Now you know what leaves your company with each call. This decides which of the three ways fits your company.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **You know what your system sends out.**

<div class="quiz">

**Quiz.** A hospital's patient records must never leave the hospital. Which way fits?

<ul>
<li>Partly self-hosted, like your laptop</li>
<li data-right>Air-gapped</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**Air-gapped.** In the partly self-hosted way, every call sends the record to the model outside. If the records must
stay inside, the model must run inside too. Then the hospital needs GPUs of its own. So read your five lines from
Claude Code: if one kind of data must stay inside your company, write air-gapped in your paragraph.

</details>

</div>

### Try a small model that your company could run itself (optional)

An **open model** is a model that anyone can download and run. A small open model, such as **Qwen3.6-35B-A3B**, runs
on one **DGX Spark**, a small AI computer from NVIDIA that costs about 5,000 USD. Your test bench shows whether your
flow still works with such a model.

1. Wait until no other test is running. Then, in the tab **Run** of the test bench, type your endpoint name under **Flow**,
   type `qwen/qwen3.6-35b-a3b` under **Model**, and type `small model` under **A name for the full test**. Click
   **Full test**. The test bench uses the small model only for this test, and your flow in Langflow stays as it is.
2. When the test is done, open the tab **Compare**. Pick `today` under **Before** and `small model` under **After**.
3. In the tab **Run**, empty the field **Model** again, so that your next test uses the model of your flow.

Sometimes the page says **The test did not start. The bench cannot set the model**, or all answers say **no answer**
or **HTTP 500**. In that case, let Claude Code make a
copy of your flow that uses the small model. Send this request to Claude Code, and replace `MY FLOW` in both places
with the name of your flow, as Langflow shows it:

```
Make a copy of my Langflow flow MY FLOW and call it "MY FLOW - small model". In the copy, use the model qwen/qwen3.6-35b-a3b through OpenRouter, and change nothing else. Do not change the original. Then tell me the endpoint name of the copy.
```

Then test the copy. In the tab **Run**, type its endpoint name under **Flow**, leave the field **Model** empty, type `small model` under
**A name for the full test**, and click **Full test**.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg> **What we found on 21 November.** We tested the flow Triage with five test mails and three runs,
and both models ran through OpenRouter. GLM 5.3 Flash, the model of the flow Triage, got 12 of 15 answers right and took 11 seconds per call.
Qwen3.6-35B-A3B got 8 of 15 answers right and took 19 seconds per call. Five test mails are not many, so your own
test cases will tell you more.

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg> **You know whether your company could run the model itself.**

### Write your paragraph for 7 December

Copy this template into your team's notes, and fill it in together:

```
We recommend: online / partly self-hosted / air-gapped, for our company.
Our reason:
What changes in our system (for example, Gmail becomes the company's own mail server):
What we ask management to approve (for example, a server in the company for n8n, Langflow and the database):
With the small model Qwen3.6-35B-A3B, which our company could run itself (if you tried it): __ % instead of __ %
```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M10 14.66V17a1 1 0 0 1-1 1 2 2 0 0 0-2 2v2"/><path d="M14 14.66V17a1 1 0 0 0 1 1 2 2 0 0 1 2 2v2"/><path d="M17.916 10H19.5A2.5 2.5 0 0 0 22 7.5V5a1 1 0 0 0-1-1h-3"/><path d="M4 22h16"/><path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/><path d="M6.084 10H4.5A2.5 2.5 0 0 1 2 7.5V5a1 1 0 0 1 1-1h3"/></svg> **You have your paragraph for management.** On 7 December, it answers the question of what management must approve.

## Write down your results

Copy this template into your team's notes, and fill it in. You will need it for your slides on 7 December.

```
Pass rate: __ % on __ test cases, three runs; with 95 % confidence between __ and __ %; about __ seconds per call
n8n workflow: what it does: __; a person approves: yes / not yet
On whose computers (online / partly self-hosted / air-gapped): __, because __
```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M10 14.66V17a1 1 0 0 1-1 1 2 2 0 0 0-2 2v2"/><path d="M14 14.66V17a1 1 0 0 0 1 1 2 2 0 0 1 2 2v2"/><path d="M17.916 10H19.5A2.5 2.5 0 0 0 22 7.5V5a1 1 0 0 0-1-1h-3"/><path d="M4 22h16"/><path d="M6 9a6 6 0 0 0 12 0V3a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1z"/><path d="M6.084 10H4.5A2.5 2.5 0 0 1 2 7.5V5a1 1 0 0 1 1-1h3"/></svg> **Two wins for 7 December.** Your test measures your flow, and you know on whose computers your
system should run and what you will ask management to approve.

**Next: [Task 3 · Optional: let an AI judge the answers →](/abp/ws2/s3-task-3/)**
