---
title: "Block 4 · Write your team's rules, together with Claude Code"
---

Now, or this afternoon.

Claude Code reads the file `AGENTS.md` at every start. Its last part, *Your team's rules*, holds no rules yet, only three
steps as a placeholder. Now you fill it in, together with Claude Code. Claude Code interviews you, you answer,
Claude Code writes.

### Let Claude Code interview you

1. In Claude Code, send this:

   ```
   Interview us, one question at a time, and write our team's rules into AGENTS.md,
   under the heading "Your team's rules". Ask, then wait for our answer.
   First ask which project we have. Then look at our workflows in n8n and our flows in Langflow.
   Then go through these six principles, one at a time. For each, suggest our rule in one or
   two sentences, and ask us whether it fits or what to change:
   1. One task per piece: each flow does one job.
   2. A contract for each flow: which fields go in, which come out.
   3. One place for the data.
   4. A fixed rule decides; the model only proposes.
   5. Each part may do only what its job needs.
   6. Where a person decides.
   At the end, show us the whole text before you save it. Replace only the three steps under
   the heading. Leave everything above the heading as it is.
   ```

2. Claude Code interviews you, one question at a time. Answer in a few words.
3. Claude Code shows the whole text before it saves. Is it right? Say what to change, then agree.

### Check that Claude Code knows your rules

1. Leave Claude Code with `/exit`, and start it again:

   ```
   cd ~/kingo-pod && ./kingo claude
   ```

2. Send this:

   ```
   What are our team's rules? Answer in six short lines.
   ```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5.8 11.3 2 22l10.7-3.79"/><path d="M4 3h.01"/><path d="M22 8h.01"/><path d="M15 2h.01"/><path d="M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/><path d="m22 13-.82-.33c-.86-.34-1.82.2-1.98 1.11c-.11.7-.72 1.22-1.43 1.22H17"/><path d="m11 2 .33.82c.34.86-.2 1.82-1.11 1.98C9.52 4.9 9 5.52 9 6.23V7"/><path d="M11 13c1.93 1.93 2.83 4.17 2 5-.83.83-3.07-.07-5-2-1.93-1.93-2.83-4.17-2-5 .83-.83 3.07.07 5 2Z"/></svg> **Claude Code names your team's rules.** From now on, every teammate's Claude Code builds the same way: your
names, your contracts, where a person decides. Nobody has to explain it again in each session. Your teammates want the
same rules? Send them the text under *Your team's rules*. Each pastes it into their own
`~/kingo-pod/claude/AGENTS.md`, under that heading (open the file as in the homework).

<div class="quiz match">

**How do you start Claude Code?** Match each situation with its command. All four start Claude Code inside the
sandbox, nono.

| Situation | Command |
|---|---|
| Claude Code asks you before every command | `./kingo claude` |
| Claude Code works without asking you | `./kingo yolo` |
| Your own folder, for example for your thesis: no n8n, no Langflow | `./kingo claude --in ~/projects/thesis` |
| Your own Claude subscription pays, with Anthropic's models | `./kingo claude --login` |

<details class="more">
<summary>More about the four</summary>

- In `./kingo claude`, **Shift+Tab** switches the mode. In plan mode, for example, Claude Code first makes a plan and
  changes nothing until you agree.
- `./kingo yolo` asks nothing, but the sandbox stays. Your laptop stays protected.
- `--in` takes a folder inside your home folder: not a Windows folder, and not kingo-pod. Claude Code can write only
  there. There it reads that folder's own `CLAUDE.md` or `AGENTS.md`, not your team's.
- `--login` asks you to log in once, at the first start. You need no OpenRouter key.

</details>

</div>

<div class="quiz">

**Quiz.** Which model does Claude Code use in the course, and where is that written?

<ul>
<li>Claude, from Anthropic, always</li>
<li data-right>GLM 5.3 Flash through OpenRouter, written in <code>claude/.claude/settings.json</code></li>
<li>The model of your Langflow flows</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**GLM 5.3 Flash, through OpenRouter.** It is written in `~/kingo-pod/claude/.claude/settings.json`. Want another
model? The page `ws2_claude_model.html` in your download shows how.

An example: Anthropic's Claude Sonnet 5.5, with an Anthropic API key. The page shows it in four steps, under
*Use Anthropic's API, or another provider*:

1. Save the key in `~/.config/kingo/anthropic.key`.
2. Give the sandbox the route to Anthropic, in `~/kingo-pod/my-nono-profile.json`.
3. In `settings.json`, delete the line `"ANTHROPIC_API_KEY": "",`, and let the lines that name the model say
   Anthropic's models, for example `claude-sonnet-5-5`.
4. Start `./kingo claude` again.

</details>

</div>

**This afternoon, your team's page: [Team A · KSMC](/abp/ws2/s2-team-a/) · [Team B · Kgoda](/abp/ws2/s2-team-b/) · [Team C · K-Motor](/abp/ws2/s2-team-c/)**
