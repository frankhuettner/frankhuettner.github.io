---
title: "Workbook, 9 November"
lede: "The steps of the morning, block by block as on the slides. Start here: the two data tables for block 2."
---

**First, three checks:**

1. kingo-pod runs. In the terminal, in your kingo-pod folder, run `./kingo up`. Then open n8n in your browser:
   <http://localhost:5678>.
2. Your test Gmail account is open in another browser tab.
3. You downloaded [`ws2_s1.zip`](https://huettner.io/abp/ws2/ws2_s1.zip) and unzipped it (double-click it). In the folder `ws2_s1`:
   - `ws2_s1_workbook.html`: these pages, in one file
   - today's slides, as HTML and as PDF
   - two CSV files for the data tables
   - the folder `n8n` with today's workflows

## Block 2 · You must add two data tables before you build your first workflow

**What is a data table?** A table that lives in n8n, like a small spreadsheet.

**Why do I need to add it?** Your first workflow, `WS2.1 - TEST - Triage`, will test the Langflow flow that sorts
mails. To this end, it needs test mails. Those test mails are in the first data table. Then, it needs to write down
the test results. Those go into the second data table.

### Make the two data tables

1. In n8n, click **Overview** at the top left, then the tab **Data tables** in the middle of the page.
2. Click **Create data table**.
3. *Data table name*: paste this name.

   **THE NAMES ARE IMPORTANT BECAUSE YOUR SOLUTION FILES LOOK FOR EXACTLY THESE NAMES.**

   ```
   WS2.1 - TEST - Triage - Cases
   ```

4. Pick **Import CSV**. Drop the file `ws2_1_test_triage_cases.csv` from your folder `ws2_s1` into the box, or click
   the box and pick it.
5. Turn on *My CSV file contains a header row*: the first line of the file holds the names of the columns.
6. n8n shows the columns it found, with their types. Leave them as they are. Click **Create**.
7. The same again for the second table, with this name and the file `ws2_1_test_triage_runs.csv`:

   ```
   WS2.1 - TEST - Triage - Runs
   ```

**Done: your two data tables are ready.** *Cases* holds the five test mails. *Runs* is still empty: in block 4 it gets
one line per run.

**Next: [Block 2 · WS2.1: You build an n8n workflow to test your Langflow Triage flow →](/abp/ws2/s1-block-2/)**
