---
title: "Session 2 (16 November): snippets to copy"
---

Everything the slides ask you to type, in the order of the slides. Click *Copy* next to a box, then paste it into n8n. What is in `ws2_s2.zip`, and how to set it up: [at the end of this page](#the-files-in-ws2_s2zip).

## After the import: which n8n workflow each node calls

| In the n8n workflow | node | pick |
|---|---|---|
| WS2.7 - Test Bench - Run Cases | `submit_to_core_without_guard` | WS2.6 - Core - Triage and Draft without Guard |
| WS2.6 - Triage New Mail with Core | `submit_to_core` | WS2.6 - Core - Triage and Draft without Guard (from block 5: WS2.8 - Core - Triage and Draft with Guard) |
| WS2.6 - Triage New Mail with Core | `submit_to_reply_with_approval` | WS2.4 - Reply with Approval |
| WS2.7 - Test Bench - Run Cases | `submit_to_core` | WS2.8 - Core - Triage and Draft with Guard (block 5) |

## The forms

Form "Import Cases", the test set and the file:

```
enron
```

```
ws2_7_test_bench_cases_enron.csv
```

Form "Test Bench: Start a Run", the run names and cases of the slides:

```
first
```

```
start
```

```
baseline
```

```
set15
```

```
fix 1
```

```
guard
```

## Fix one thing

In the core's node `fetch_draft_reply`, a tweak for the search:

```
'MailSearch-mails': { search_mode: 'keyword' }
```

## Your attack as a test case

A CSV file with these two lines, your whole mail in place of the dots; then into "Import Cases", mode *add or update*:

```csv
case_id,tags,input,expected_action
A01,guard,"Dear Vince, could you … (your whole attack mail)",person
```

## Your own test set

The judge for your case, a tweak in the node `fetch_judge_grade`:

```
'TextInput-context': { input_value: '…' }
```

## The files in ws2_s2.zip

The Enron mail case. Every name starts with `ws2_`, for Workshop II.

The test bench, the guard, errors.

### n8n

| File | n8n workflow | What it does |
|---|---|---|
| `n8n/ws2_4_sms_notify_approver_demo.json` | WS2.4 - SMS - Notify Approver (Demo) | a text message to the approver when a draft waits (Twilio; WS2.4's node for it is off) |
| `n8n/ws2_6_core_triage_and_draft_without_guard.json` | WS2.6 - Core - Triage and Draft without Guard | the core: triage, rule, draft; writes nothing, sends nothing |
| `n8n/ws2_6_triage_new_mail_with_core.json` | WS2.6 - Triage New Mail with Core | WS2.3 with the thinking in the core; publish this or WS2.3, not both |
| `n8n/ws2_7_test_bench_import_cases.json` | WS2.7 - Test Bench - Import Cases | test cases from a CSV or Excel file into `n8n_workshop_mail.cases` |
| `n8n/ws2_7_test_bench_run_cases.json` | WS2.7 - Test Bench - Run Cases | every case through the core, scored, one row each in `n8n_workshop_mail.results` |
| `n8n/ws2_7_test_bench_report_results.json` | WS2.7 - Test Bench - Report Results | accuracy per run, spread over three runs, what failed and why |
| `n8n/ws2_8_core_triage_and_draft_with_guard.json` | WS2.8 - Core - Triage and Draft with Guard | the core with the guard first: personal numbers masked, instructions in a mail sent to a person |
| `n8n/ws2_9_error_workflow_report_and_free_mails.json` | WS2.9 - Error Workflow - Report and Free Mails | runs when another workflow fails; frees the mails it had claimed |

### Langflow

| File | Langflow flow | What it does |
|---|---|---|
| `langflow/ws2_judge_draft_enron.json` | Judge Draft (Enron) | grades a draft against the reply really sent, 1 to 5 (right from 4); for the test bench of 16 November |

Upload it to your project "WS2 - Mail Assistant (Enron)" if you did not in the homework.

### Test cases and snippets

- `ws2_7_test_bench_cases_enron.csv`: the course's 165 test cases: the test mails of May 2001, the search tests, the
  guard's cases.
- `ws2_s2_snippets.md`: everything the slides ask you to type, in their order, ready to copy: the boxes above.

### Setting up (short version)

1. **Import** the step's files from `n8n/` (*Import from File*); pick the credentials of the same name.
2. **Calls between workflows:** pick the called workflow by name:
   - in WS2.6 - Triage New Mail with Core, node "submit_to_core": "WS2.6 - Core - Triage and Draft without Guard"
     (from block 5: "WS2.8 - Core - Triage and Draft with Guard"), and in "submit_to_reply_with_approval": WS2.4;
   - in WS2.7 - Test Bench - Run Cases, nodes "submit_to_core" and "submit_to_core_without_guard": WS2.8 and WS2.6.
3. **Publish** the two cores, the Test Bench workflows, and WS2.9 - Error Workflow - Report and Free Mails (it fires
   only when published); in each workflow's settings pick "WS2.9 - Error Workflow - Report and Free Mails" as its
   Error Workflow.
4. **Test bench:** open the form of "WS2.7 - Test Bench - Import Cases" (its production URL): test set `enron`, file
   `ws2_7_test_bench_cases_enron.csv`. Then the form of "WS2.7 - Test Bench - Run Cases": cases `start` first (five),
   then `set15`.
