---
title: "Homework until 23 Nov, Part E: Shorter commands"
---


### 11. Start Claude Code with one short command

So far, you went into `~/kingo-pod` before each start of Claude Code. After this step, two letters start it, from any
folder: <span class="cmd-i cmd-i-t">`kc`</span>.

**Your turn.**

<details class="more">
<summary>New here? What is different for you in 4 and 5</summary>

In 4, <span class="cmd-i cmd-i-t">`kingo status`</span> needs n8n and Langflow. Paste this line in its place: it shows the version of your kingo-pod.

<div class="cmd cmd-terminal">

```
kingo version
```

</div>


Skip 5: <span class="cmd-i cmd-i-t">`kc`</span> alone starts Claude Code for the course.

</details>

1. Go into your kingo-pod folder. Paste this line into your terminal:
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod
   ```

   </div>

2. Let kingo add the short commands:
   <div class="cmd cmd-terminal">

   ```
   ./kingo shortcuts
   ```

   </div>

   kingo shows a list of five and asks: "Which ones?" Type `1 5` and press **Enter**: that is <span class="cmd-i cmd-i-t">`kc`</span> and <span class="cmd-i cmd-i-t">`kingo`</span>.
   kingo says where it wrote them, and: "They work in every new terminal."
3. Open a new terminal tab ([how](/abp/ws2/hw3/#your-terminal-in-short)). There, go to your home folder, away from
   kingo-pod:
   <div class="cmd cmd-terminal">

   ```
   cd
   ```

   </div>

4. Try the first short command there. It shows the state of your kingo-pod:
   <div class="cmd cmd-terminal">

   ```
   kingo status
   ```

   </div>

5. Start Claude Code for the course, as <span class="cmd-i cmd-i-t">`./kingo claude`</span> does:
   <div class="cmd cmd-terminal">

   ```
   kc
   ```

   </div>

   Type <span class="cmd-i cmd-i-c">`/exit`</span>.
6. Start Claude Code in the folder of your website:
   <div class="cmd cmd-terminal">

   ```
   kc ~/projects/my-first-project
   ```

   </div>

   Type <span class="cmd-i cmd-i-c">`/exit`</span>.
7. Are you in the right folder already? Then a dot is enough: it stands for the folder that you are in. Go into the
   folder of your website, and start Claude Code there:
   <div class="cmd cmd-terminal">

   ```
   cd ~/projects/my-first-project
   ```

   </div>

   <div class="cmd cmd-terminal">

   ```
   kc .
   ```

   </div>


<details class="more">
<summary>Why a dot? And why the dot in ./kingo?</summary>

In the terminal, a dot means "here": the folder that you are in. So <span class="cmd-i cmd-i-t">`kc .`</span> starts Claude Code here. Two dots mean the
folder above: <span class="cmd-i cmd-i-t">`cd ..`</span> goes one folder up.

<span class="cmd-i cmd-i-t">`./kingo claude`</span> reads the same way. <span class="cmd-i cmd-i-t">`./kingo`</span> is the file kingo here, in the folder that you are in: that is why you
went into `~/kingo-pod` first. Without `./`, i.e. if you type just <span class="cmd-i cmd-i-t">`kingo`</span>, then the terminal would not look for it
here: it looks for programs that are written in a central registry. The word `claude` after it tells kingo what to
do: start Claude Code.

The short command <span class="cmd-i cmd-i-t">`kingo`</span> needs no `./` and works from any folder: it knows where the file is.

</details>

Keep in mind: without the dot, <span class="cmd-i cmd-i-t">`kc`</span> starts Claude Code for the course, wherever you are. <span class="cmd-i cmd-i-t">`kc`</span> alone is the same as
<span class="cmd-i cmd-i-t">`kc ~/kingo-pod`</span>.

Done: from now on, <span class="cmd-i cmd-i-t">`kc`</span> is all you type to start Claude Code, from any folder.

**The five short commands.** The number is the one in kingo's list.

| Number | Short command | What it does |
|---|---|---|
| 1 | <span class="cmd-i cmd-i-t">`kc`</span> | Alone: Claude Code for the course, as <span class="cmd-i cmd-i-t">`./kingo claude`</span>. <span class="cmd-i cmd-i-t">`kc .`</span>: in the folder that you are in. <span class="cmd-i cmd-i-t">`kc ~/projects/my-first-project`</span>: in that folder |
| 2 | <span class="cmd-i cmd-i-t">`kcl`</span> | the same as <span class="cmd-i cmd-i-t">`kc`</span>, with `--login`: your Claude subscription pays (step 1) |
| 3 | <span class="cmd-i cmd-i-t">`ky`</span> | the same as <span class="cmd-i cmd-i-t">`kc`</span>, but Claude Code does not ask for your OK before it runs a command or changes a file. The sandbox still decides where it may write (step 9). Use it only when you watch (step 6) |
| 4 | <span class="cmd-i cmd-i-t">`kyl`</span> | the same as <span class="cmd-i cmd-i-t">`ky`</span>, with `--login` |
| 5 | <span class="cmd-i cmd-i-t">`kingo`</span> | <span class="cmd-i cmd-i-t">`./kingo`</span> from any folder, for example <span class="cmd-i cmd-i-t">`kingo status`</span> or <span class="cmd-i cmd-i-t">`kingo update`</span> |

**Want more of them later?** Run <span class="cmd-i cmd-i-t">`./kingo shortcuts`</span> again, and type all the numbers that you want, also the ones that
you have: for example `1 2 5`. A number that you leave out, kingo takes out.

<details class="more">
<summary>Where does kingo write the short commands?</summary>

Into the file that every new terminal reads at its start: on a Mac `~/.zshrc`, in Ubuntu `~/.bashrc`. Its name starts
with a dot, so <span class="cmd-i cmd-i-t">`ls`</span> does not show it. kingo writes the short commands between two marked lines and changes nothing
else in the file. First, it keeps a copy of the file, next to it: for example `~/.bashrc.kingo-backup-20261118-130500`.
With <span class="cmd-i cmd-i-t">`kc`</span> and <span class="cmd-i cmd-i-t">`kingo`</span>, the lines look like this (here for Anna on Ubuntu):

```text
# >>> kingo shortcuts >>>
# Made by ./kingo shortcuts, which replaces these lines when it runs again. To take them out:  '/home/anna/kingo-pod/kingo' shortcuts remove
if [ -z "${KINGO_SHORTCUTS_SKIP:-}" ]; then
  unalias kc kingo 2>/dev/null
  function kc { '/home/anna/kingo-pod/kingo' kc "$@"; }
  function kingo { '/home/anna/kingo-pod/kingo' "$@"; }
fi
# <<< kingo shortcuts <<<
```

Each short command calls the file <span class="cmd-i cmd-i-t">`kingo`</span> in your kingo-pod folder. So when you update kingo-pod, the short commands
get the update too. To see your lines, paste on a Mac:

<div class="cmd cmd-terminal">

```
grep -A 10 ">>> kingo shortcuts" ~/.zshrc
```

</div>


In Ubuntu:

<div class="cmd cmd-terminal">

```
grep -A 10 ">>> kingo shortcuts" ~/.bashrc
```

</div>


To change them, run <span class="cmd-i cmd-i-t">`./kingo shortcuts`</span> again; do not edit the lines yourself. On Windows, Notepad would even break
the file: Ubuntu could not read it any more.

</details>

To take them out again: <span class="cmd-i cmd-i-t">`./kingo shortcuts remove`</span>, in your kingo-pod folder.

*From kingo-pod: <span class="cmd-i cmd-i-t">`./kingo shortcuts help`</span>.*

[Stuck? Help for step 11](#step-11)

## Your habits on one page

<div class="habits">

| Habit | What it gives you | Where it comes from |
|---|---|---|
| Know the model inside Claude Code | You know whose mistake it is, what it costs, and how to change it | [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop) |
| Write the facts of your setup into its start file (in kingo-pod, kingo does it for you) | Claude Code guesses less | [Tell Claude what it can't see](https://code.claude.com/docs/en/best-practices#tell-claude-what-it-cant-see) |
| Plan first when you are not sure what you want | You see a wrong idea in the plan, not in the work | [Brainstorm with Claude first](https://code.claude.com/docs/en/best-practices#brainstorm-with-claude-first) |
| Say what "done" looks like, and ask for proof | Claude Code can check its work against your goal | [Give Claude a check to run](https://code.claude.com/docs/en/best-practices#give-claude-a-check-to-run) |
| Tell Claude Code what it cannot see | Less guessing, less cost | [Write a specific prompt](https://code.claude.com/docs/en/best-practices#write-a-specific-prompt) |
| Watch, and press Esc when it goes in circles | You lose minutes, not an hour | [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session) |
| <span class="cmd-i cmd-i-c">`/clear`</span> after two failed tries and for a new task | Better answers, lower cost | [Steer the session](https://code.claude.com/docs/en/best-practices#steer-the-session) |
| Work on a copy where there is no undo | You try ideas without fear | [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#undo-changes-with-checkpoints); here: Langflow and n8n |
| Know where Claude Code may work, and give each project a folder of its own | The course stays clean, your project too | kingo-pod: the sandbox and its keys; [Permissions](https://code.claude.com/docs/en/permissions#permission-system) |

</div>

**Want more? [Optional · More room for Claude Code →](/abp/ws2/hw3-optional/)**

## If something goes wrong

Find your step.

#### Step 11

| What you see | What to do |
|---|---|
| New here: `No container engine found`, after <span class="cmd-i cmd-i-t">`kingo status`</span> or <span class="cmd-i cmd-i-t">`kingo update`</span> | These commands are for n8n and Langflow, which you do not need. <span class="cmd-i cmd-i-t">`kingo version`</span> shows which kingo-pod you have. To update kingo-pod, paste <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && git pull`</span>. |
| `command not found`, after <span class="cmd-i cmd-i-t">`kc`</span> | You are still in the old tab: open a new terminal tab. Still not? Paste <span class="cmd-i cmd-i-t">`cd ~/kingo-pod`</span>, then <span class="cmd-i cmd-i-t">`./kingo shortcuts`</span>, and type `1 5` again. |
| kingo says that <span class="cmd-i cmd-i-t">`kc`</span> already means something in your terminal | Another program uses that name. Type `yes` to take kingo's <span class="cmd-i cmd-i-t">`kc`</span> in its place, or press **Enter** to keep yours, and start with <span class="cmd-i cmd-i-t">`./kingo claude`</span> as before. |
