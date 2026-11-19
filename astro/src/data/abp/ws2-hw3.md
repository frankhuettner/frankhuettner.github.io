---
title: "Homework until 23 Nov: get more out of Claude Code"
---

**Why this homework?** Working with AI feels fast. But feeling fast is not the same as being fast. In 2025, the
research group METR measured it: 16 experienced developers worked on 246 real tasks, some with AI tools and some
without. With AI, the developers believed that they were 20% faster. The clock said: they were 19% slower
([METR, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).

The tools are better today, and METR itself says that this number is out of date
([METR, 2026](https://metr.org/blog/2026-02-24-uplift-update/)). But one lesson stays: you cannot feel whether the
AI makes you faster. So do not trust the feeling: learn how to work with the tool. This homework shows you how,
introducing nine habits that you'll try out yourself.

<p class="newhere-note"><strong>You do not have everything from the course on your laptop?</strong> Maybe you are
not in the course. Maybe you have n8n and Langflow, but you did not do the last homework. Or you just want to work on
a project of your own. You can do this homework too: wherever you see a box or a line <strong>New here?</strong>,
always open it, and do what it says.</p>

## Your goals for this homework

- **You know which LLM works inside Claude Code, what that changes for you, and how you can change it.** An LLM
  (large language model) is an AI that reads and writes text; ChatGPT runs on one, too. From here on, we call it "the
  model".

- **Claude Code knows the facts of your setup (here: your kingo-pod, the course software on your laptop), so it does
  not have to guess.**

- **You know nine habits that get you good results from Claude Code, in any project.**

- **You planned and built a small website with Claude Code, in a folder of its own, outside the course.**

- **You start Claude Code with one short command, from any folder.**

- **Optional: you give Claude Code one more folder, you work in two sessions at once, and you know how to give a
  project a key of its own.**

In the course, there is nothing new to install: you only update kingo-pod.

**Where to type it.** A sign before a command tells you where it goes:

- a dollar sign: into your terminal (on Windows: the Ubuntu app), as in <span class="cmd-i cmd-i-t">`./kingo status`</span>;
- sparkles: into Claude Code, where you write to the model, as in <span class="cmd-i cmd-i-c">`/clear`</span>.

**The sign is not part of the command:** do not type it. In a box, the Copy button leaves it out.

## Before you start

- **Deadline:** **Monday, 23 November**, before the lecture at 10:50.
- **You need, in the course:**
  - your kingo-pod, updated and running. Paste this line into your terminal: it updates kingo-pod and starts it.
    <div class="cmd cmd-terminal">

    ```
    cd ~/kingo-pod && ./kingo update
    ```

    </div>

    Near the end, it says `Stack updated — kingo-pod` and the version: 1.4.28 or higher, or 1.5.27 or higher with
    Kingo 1.5.
  - Claude Code, set up as in the last homework: installed with its sandbox
    ([step 2](/abp/ws2/hw2-a/#2-install-claude-code-and-its-sandbox)), with a key in n8n
    ([step 3](/abp/ws2/hw2-a/#3-make-a-key-in-n8n)), and started once with <span class="cmd-i cmd-i-t">`./kingo claude`</span>, where it took your
    OpenRouter key and your n8n key ([step 4](/abp/ws2/hw2-a/#4-start-claude-code-and-give-it-its-keys));
  - your team's project: the Langflow flow and the n8n workflow you work on.
- **New here: without the course, without the last homework, or for a project of your own?** You can do this
  homework too, and you need less: open the two boxes below.

<details class="more newhere">
<summary>New here? What you need, and your first start</summary>

You need no n8n, no Langflow and no Podman: Claude Code works in a folder of your own. You need four things:

1. **A terminal.** On a Mac: the app Terminal. On Windows: the Ubuntu app, a Linux that runs inside Windows. To
   install it, follow steps 1 and 2 of [kingo-pod's guide for Windows](https://huettner.io/kingo-pod/windows/). The
   steps after them install n8n and Langflow, which you do not need.
2. **kingo-pod.** This line copies kingo-pod into your home folder. On a Mac, paste it into Terminal:
   <div class="cmd cmd-terminal">

   ```
   git clone https://github.com/frankhuettner/kingo-pod.git ~/kingo-pod
   ```

   </div>

   A window asks to install the "Command Line Developer Tools"? Click **Install**, wait until it is done, and paste
   the line again. On Windows, paste this line into the Ubuntu app. It asks for your Linux password, which you do not
   see as you type:
   <div class="cmd cmd-terminal">

   ```
   sudo apt update && sudo apt install -y git python3 && git clone https://github.com/frankhuettner/kingo-pod.git ~/kingo-pod
   ```

   </div>

3. **Claude Code.** Paste this line, on a Mac and in Ubuntu:
   <div class="cmd cmd-terminal">

   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   </div>

4. **An OpenRouter key of your own.** OpenRouter passes what Claude Code sends on to the model, and bills it to
   your key. On [openrouter.ai](https://openrouter.ai), make an account and add credits. Then open Settings, then
   Keys, make a key, and give it a credit limit: the key stops at that amount.

**Your first start.** Make a folder to practise in, and start Claude Code there. Paste:

<div class="cmd cmd-terminal">

```
mkdir -p ~/projects/practice && cd ~/kingo-pod && ./kingo claude --in ~/projects/practice
```

</div>


The first time, kingo gets nono, the sandbox that Claude Code works in. Then it asks for your OpenRouter key: paste
it, and press **Enter**. You do not see the key as you paste it: that is on purpose. Then kingo gets a browser, with
which Claude Code looks at the pages that it writes. In Ubuntu, kingo may ask to install a few packages for the
browser: press **Enter**, and type your Linux password.

kingo asks for nothing else here: no key of n8n, and no mailbox. Both belong to the setup of the course, and you can
skip them for this homework:

- **A key of n8n.** Only the start for the course asks for it: <span class="cmd-i cmd-i-t">`./kingo claude`</span> without `--in`. That start also
  needs n8n and Langflow running.
- **A mailbox.** No start of Claude Code asks for it. It is for the mail AI assistant of the course, and only the
  command <span class="cmd-i cmd-i-t">`./kingo mail`</span> sets it up.

You can do both later, whenever you like: your practice folder and your OpenRouter key stay as they are. The pages
of the course show how. [kingo-pod's guide](https://huettner.io/kingo-pod/) installs n8n and Langflow,
[the preparatory homework](/abp/ws2/hw/) sets up the mailbox, and
[steps 3 and 4 of the last homework](/abp/ws2/hw2-a/#3-make-a-key-in-n8n) show the first start for the course.

You also have a Claude Pro or Max subscription? Then you can let it pay for the model. Start with `--login`:

<div class="cmd cmd-terminal">

```
cd ~/kingo-pod && ./kingo claude --login --in ~/projects/practice
```

</div>


Then you log in to Claude, once:
[Use your Claude subscription](/abp/ws2/s2-model/#use-your-claude-subscription) shows how.

Claude Code then asks you to pick a theme, and whether you trust the files in this folder: choose **Yes**, it is your
own folder. Type <span class="cmd-i cmd-i-c">`/exit`</span> to leave.

**How you read this homework.** It speaks to the students of the course: of their team's project, and of their last
homework. Where you do something else, a box or a line **New here?** says what. In every **Your turn**, unless it
says otherwise:

- where you start Claude Code with <span class="cmd-i cmd-i-t">`./kingo claude`</span>, start it with <span class="cmd-i cmd-i-t">`./kingo claude --in ~/projects/practice`</span>;
- where it says your course folder, `~/kingo-pod/claude`, take your folder `~/projects/practice`.

<span class="src">From Anthropic's [Advanced setup](https://code.claude.com/docs/en/setup#install-claude-code), OpenRouter's
[FAQ](https://openrouter.ai/docs/faq#how-do-i-get-started-with-openrouter) and its page on
[limits](https://openrouter.ai/docs/api/reference/limits), and kingo-pod's guides for
[Mac](https://huettner.io/kingo-pod/mac/) and [Windows](https://huettner.io/kingo-pod/windows/).</span>

[Stuck? Help for new readers](/abp/ws2/hw3-a/#step-1)

</details>

<details class="more newhere">
<summary>New here? The words of the course</summary>

- **kingo-pod:** the course software on your laptop. In the course, n8n and Langflow run in it. Its command, <span class="cmd-i cmd-i-t">`kingo`</span>,
  also starts Claude Code in a sandbox: <span class="cmd-i cmd-i-t">`./kingo claude`</span>, when you are in the folder `~/kingo-pod`.
- **The sandbox:** a fence around Claude Code, here nono. Inside the fence, Claude Code works as it likes. Outside, it
  can read nothing and change nothing.
- **The mail AI assistant:** what the teams build in the course. It reads new mail, sorts it, and drafts answers,
  with the help of older mails in a database. It sends nothing without your OK.
- **Langflow and n8n:** the two tools in which the teams build it. Langflow holds the flows, the brain of the
  assistant: for example the flow that drafts an answer. n8n holds the workflows, its muscle: they fetch the mail,
  call the flows, and send the answers that you approve.

</details>

## Your terminal, in short

**More than one terminal.** As in a browser, you can open more than one tab: one for Claude Code, one for your own
commands.

- On a Mac, in Terminal: press **Cmd+T** for a new tab.
- On Windows, in the Ubuntu window: click the small arrow **˅** next to the **+** at the top, and choose **Ubuntu**.
  The **+** alone may open PowerShell, which runs commands in Windows, not in Ubuntu. No **+** at the top? Start the Ubuntu app
  a second time: that gives you a second window.

**Where am I?** `~` is your home folder: `~/kingo-pod` is the folder kingo-pod in it. These commands help you find
your way:

- <span class="cmd-i cmd-i-t">`pwd`</span> shows the folder that the terminal is in.
- <span class="cmd-i cmd-i-t">`ls`</span> lists what is in that folder. With a folder after it, it lists that folder: <span class="cmd-i cmd-i-t">`ls ~/kingo-pod`</span> shows what is in
  your kingo-pod.
- <span class="cmd-i cmd-i-t">`cd`</span> with a folder goes into that folder. <span class="cmd-i cmd-i-t">`cd`</span> alone goes back to your home folder.
- <span class="cmd-i cmd-i-t">`clear`</span> empties the window of the terminal.

<figure class="hx hx-try" data-out="{&quot;~&quot;: {&quot;pwd&quot;: &quot;/home/anna&quot;, &quot;ls&quot;: &quot;kingo-pod&quot;}, &quot;~/kingo-pod&quot;: {&quot;pwd&quot;: &quot;/home/anna/kingo-pod&quot;, &quot;ls&quot;: &quot;backups  bundles.sha256  claude  CLAUDE.md  cloudbeaver  compose.yml  docs  jupyterhub  kingo  langflow  LICENSE  mail  PLAN-NATIVE-STACK.md  postgres-init  README.md  setup  shared  site  VERSION&quot;}}" aria-label="A terminal for practice"><div class="hx-term"><div class="hx-term__bar"><span class="dots"><i></i><i></i><i></i></span><em>Terminal for practice: nothing runs on your laptop</em></div><ol class="hx-try__log" aria-live="polite"><li class="you"><span class="pr">anna@laptop:~&#36;</span>pwd</li><li>/home/anna</li><li class="you"><span class="pr">anna@laptop:~&#36;</span>ls</li><li>kingo-pod</li></ol><div class="hx-term__keys hx-try__keys" role="group" aria-label="Commands to try"><button type="button" data-cmd="pwd"><code>pwd</code></button><button type="button" data-cmd="ls"><code>ls</code></button><button type="button" data-cmd="cd ~/kingo-pod"><code>cd ~/kingo-pod</code></button><button type="button" data-cmd="cd"><code>cd</code></button><button type="button" data-cmd="clear"><code>clear</code></button></div></div><figcaption>Click a command. Before the dollar sign, the terminal shows the folder that it is in: <code>~</code> is your home folder.</figcaption></figure>

<span class="src">From Apple's [Open new Terminal windows and tabs](https://support.apple.com/guide/terminal/trmlb20c7888/mac) and
Microsoft's [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/).</span>

**Ready? [Start with Part A · The model and the facts →](/abp/ws2/hw3-a/)**
