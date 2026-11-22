---
title: "Workbook, 23 November"
lede: "The tasks, one page each. Start here: why it matters, and how to start your tools."
---

**Why this matters.** On 7 December, the faculty team will ask you two questions. Every manager asks them about an AI
system:

- How often is your system right, and how has it improved since Demo Day? Task 1 answers this question with your pass
  rate.
- What must management approve for your system? Task 2 gives you part of the answer: it shows on whose computers your
  system should run. For example, Korea's data protection law, PIPA (Personal Information Protection Act), may require
  that your data stays on the company's own computers. Then management must approve those computers.

With this workbook, you answer both questions with your own numbers and reasons, not just with "it works well". If
your n8n workflow does not run yet, start with task 0.

**The terminal.** On Windows, use the app **Ubuntu**. On a Mac, use the app **Terminal**. On Windows, never use
PowerShell, because our commands do not work there. You can recognise PowerShell by its line, which starts with
`PS C:\`.

**First, start your tools:**

1. Start kingo-pod. In the terminal, run this command:

   ```
   cd ~/kingo-pod && ./kingo up
   ```

   Then open n8n in your browser at <http://localhost:5678>, and open Langflow at <http://localhost:7860>.
2. Start Claude Code, as you did in your homework:

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

   Leave Claude Code open. You will use it in task 1.

**Stuck at a step?** Ask Claude Code for help. Tell it what you did and what you see.

**Next: [Task 0 · Only if your n8n workflow does not run yet →](/abp/ws2/s3-task-0/)**
