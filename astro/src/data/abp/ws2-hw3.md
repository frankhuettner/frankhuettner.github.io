---
title: "Homework until 23 Nov: get more out of Claude Code"
---

## Your goal of this HW

- **You know which LLM works inside Claude Code, what that changes for you, and how you can change it.** An LLM
  (large language model) is an AI that reads and writes text; ChatGPT runs on one, too. From here on, we call it "the
  model".

- **Claude Code knows the facts of your setup (here: your kingo-pod, the course software on your laptop), so it does
  not have to guess.**

- **You know nine habits that get you good results from Claude Code, in any project.**

- **You planned and built a small website with Claude Code, in a folder of its own, outside the course.**

- **You start Claude Code with one short command, from any folder.**

- **Optional: you give Claude Code one more folder, and you work in two sessions at once.**

In the course, there is nothing new to install: you only update kingo-pod.

**Your turn** means: do it now. **Next time** means: a habit for your next work with Claude Code; nothing to do now.

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

    Near the end, it says `Stack updated — kingo-pod` and the version: 1.4.24 or higher, or 1.5.23 or higher with
    Kingo 1.5.
  - Claude Code, as you set it up in the last homework (<span class="cmd-i cmd-i-t">`./kingo claude`</span>);
  - your team's project: the Langflow flow and the n8n workflow you work on.
- **New here, without the course?** You can do this homework too, and you need less: open the two boxes below.

<details class="more">
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

4. **A way to pay for the model.** Either an OpenRouter key of your own: OpenRouter passes what Claude Code sends on
   to the model, and bills it to your key. On [openrouter.ai](https://openrouter.ai), make an account and add
   credits. Then open Settings, then Keys, make a key, and give it a credit limit: the key stops at that amount. Or a
   Claude Pro or Max subscription: then you need no key.

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

With a Claude subscription, start with `--login`, and kingo asks for no key:
<span class="cmd-i cmd-i-t">`./kingo claude --login --in ~/projects/practice`</span>. Then you log in to Claude, once:
[Use your Claude subscription](/abp/ws2/s2-model/#use-your-claude-subscription) shows how.

Claude Code then asks you to pick a theme, and whether you trust the files in this folder: choose **Yes**, it is your
own folder. Type <span class="cmd-i cmd-i-c">`/exit`</span> to leave.

**How you read this homework.** It speaks to the students of the course: of their team's project, and of their last
homework. Where you do something else, a box or a line **New here?** says what. In every **Your turn**, unless it
says otherwise:

- where you start Claude Code with <span class="cmd-i cmd-i-t">`./kingo claude`</span>, start it with <span class="cmd-i cmd-i-t">`./kingo claude --in ~/projects/practice`</span>;
- where it says your course folder, `~/kingo-pod/claude`, take your folder `~/projects/practice`.

*From Anthropic's [Advanced setup](https://code.claude.com/docs/en/setup#install-claude-code), OpenRouter's
[FAQ](https://openrouter.ai/docs/faq#how-do-i-get-started-with-openrouter) and its page on
[limits](https://openrouter.ai/docs/api/reference/limits), and kingo-pod's guides for
[Mac](https://huettner.io/kingo-pod/mac/) and [Windows](https://huettner.io/kingo-pod/windows/).*

[Stuck? Help for new readers](/abp/ws2/hw3-a/#step-1)

</details>

<details class="more">
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

*From Apple's [Open new Terminal windows and tabs](https://support.apple.com/guide/terminal/trmlb20c7888/mac) and
Microsoft's [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/).*

**Ready? [Start with Part A · The model and the facts →](/abp/ws2/hw3-a/)**
