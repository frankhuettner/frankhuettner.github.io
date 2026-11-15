---
title: "Workbook, 16 November"
lede: "The steps of the morning, block by block. Start here: the three checks."
---

**The terminal** in this workbook: on Windows the app **Ubuntu**, on a Mac the app **Terminal**. On Windows, never
PowerShell: its line starts with `PS C:\`, and our commands do not work there.

**First, three checks:**

1. Start kingo-pod. In the terminal, run:

   ```
   cd ~/kingo-pod && ./kingo up
   ```

   Then open n8n in your browser at <http://localhost:5678>, and Langflow at <http://localhost:7860>.
2. Check that Claude Code starts, as in your homework:

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

   Leave it with `/exit`. Then check your version of kingo-pod:

   ```
   cd ~/kingo-pod && ./kingo version
   ```

   You need 1.4.15 or newer (with Kingo 1.5: 1.5.14 or newer). Older? Run:

   ```
   cd ~/kingo-pod && ./kingo update
   ```

3. Download [`ws2_s2.zip`](https://huettner.io/abp/ws2/ws2_s2.zip) and unzip it (double-click it). The folder `ws2_s2` holds:
   - `ws2_s2_workbook.html`: these pages, in one file
   - today's slides, as HTML and as PDF
   - `ws2_s2_team_a_ksmc.html`, `ws2_s2_team_b_kgoda.html`, `ws2_s2_team_c_k_motor.html`: one page per team, for
     this afternoon
   - `ws2_claude_model.html`: how to change the model that Claude Code uses
   - the folder `n8n`: the workflows you import
   - the folders `langflow`, `data` and `pages`: for this afternoon
   - the folder `contracts`: what the Langflow flows take in and give back, in a technical format

**Stuck at a step?** Ask Claude Code. Start it, then tell it what you did and what you see:

```
cd ~/kingo-pod && ./kingo claude
```

On a Mac, you can even drag a screenshot into the terminal.

**Next: [Block 1 · Build and use a simple webhook →](/abp/ws2/s2-block-1/)**
