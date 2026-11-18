---
title: "Homework until 23 Nov, Part A: The model and the facts"
---


### 1. Know the model inside Claude Code (here: GLM 5.3 Flash)

Claude Code has two parts:

- **The tool** is the program in your terminal, on your laptop. It carries out the steps: it reads files, runs
  commands and shows you what happens. It also keeps the whole conversation since you started Claude Code, and at
  every step, it sends the conversation to the model.
- **The model** runs on a server of the company that offers it, not on your laptop. It reads the conversation and
  decides the next step: which file to read, which command to run, what to tell you.

In the course, the model is GLM 5.3 Flash, by the company Z.ai. The same tool also works with other models, for
example with Claude, by Anthropic, the company that makes Claude Code. In this homework, "Claude Code" means both parts together, as you see
them in your terminal. Where it matters which part does something, we say "the tool" or "the model".

<figure class="hx hx-model" aria-label="You, Claude Code and the model behind it"><div class="hx-model__row"><div class="hx-card person"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c.8-4 4-6.5 8-6.5s7.2 2.5 8 6.5"/></svg></span><b>You</b><span>write the prompt, and steer</span></div><div class="hx-wire" aria-hidden="true"><i></i></div><div class="hx-card tool"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="4" width="19" height="16" rx="2"/><path d="m7 9 3 3-3 3"/><path d="M13 15h4"/></svg></span><b>The tool</b><span>on your laptop: carries out the steps, keeps the conversation</span></div><div class="hx-wire hx-wire--late" aria-hidden="true"><i></i></div><div class="hx-card brain"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/><path d="M12 5v13"/></svg></span><b>The model</b><span>on a server: decides the next step</span><div class="hx-switch" role="group" aria-label="Which model"><button type="button" data-pick="course" aria-pressed="true"><code>./kingo claude</code></button><button type="button" data-pick="login" aria-pressed="false"><code>./kingo claude --login</code></button></div><p class="hx-pick" data-for="course"><strong>GLM 5.3 Flash</strong> by Z.ai, through OpenRouter, paid with your OpenRouter key</p><p class="hx-pick" data-for="login"><strong>Claude</strong> (Sonnet, Opus …) by Anthropic, paid by your Claude subscription</p></div></div><figcaption>Claude Code: the tool and the model. Each dot is one step: the tool sends the conversation to the model, and the model answers with the next step. The two buttons swap the model; the tool stays the same.</figcaption></figure>

**Your turn: see which model works for you.** Start Claude Code. Paste this line into your terminal. The dollar
sign before it stands for the terminal: it is not part of the command.

<div class="cmd cmd-terminal">

```
cd ~/kingo-pod && ./kingo claude
```

</div>


<details class="more">
<summary>New here? Start Claude Code in your practice folder</summary>

Start it as in your first start: paste this line in place of the one above.

<div class="cmd cmd-terminal">

```
cd ~/kingo-pod && ./kingo claude --in ~/projects/practice
```

</div>


</details>

Look at its first lines. In our tests, they looked like this:

<figure class="hx hx-banner" aria-label="The first lines of Claude Code in our tests"><div class="hx-term hx-term--still"><div class="hx-banner__lines"> <span class="logo">▐▛███▛█</span>   <b>Claude Code</b> v2.1.322
<span class="logo">▝▜██████▀</span>  <mark>z-ai/glm-5.3-flash</mark> · <mark>API Usage Billing</mark>
 <span class="logo">▝▝   ▝▝</span>   ~/kingo-pod/claude</div></div><figcaption>The first lines of Claude Code in our tests, with your folder in the third line. Marked: the model, and how it is paid.</figcaption></figure>

The second line names the model, `z-ai/glm-5.3-flash`, and how it is paid: `API Usage Billing` means per use, here
with your OpenRouter key. Find the two in your own first lines.

**Commands with a slash.** In Claude Code, where you write your prompts, you can also type commands that start
with <span class="cmd-i cmd-i-c">`/`</span> (do not type the sparkles: we use them here only to tell these commands apart from terminal commands). They
control the tool itself, for example:

- <span class="cmd-i cmd-i-c">`/exit`</span> ends Claude Code.
- <span class="cmd-i cmd-i-c">`/clear`</span> empties the conversation, for a fresh start. Your files stay as they are.

Type <span class="cmd-i cmd-i-c">`/`</span> now, where you write your prompts: a list of all commands opens, and there are many more. You meet some of
them in this homework. Leave with <span class="cmd-i cmd-i-c">`/exit`</span>.

<div class="quiz sort">

**Quiz.** Which part is it, the tool or the model? Sort each card into its box.

| What is true | Which part |
|---|---|
| Runs on your laptop | The tool |
| Runs on a server of the company that offers it | The model |
| Keeps the whole conversation and sends it to the model at every step | The tool |
| Decides which command to run next | The model |
| Empties the conversation when you type <span class="cmd-i cmd-i-c">`/clear`</span> | The tool |
| Writes Chinese all of a sudden, in the middle of an English task | The model |

<details class="more">
<summary>Why</summary>

The tool is the part on your laptop: it keeps the conversation and carries out what the model decides. The model is
the part on a server: it decides the next step and writes the words. So when Claude Code suddenly writes Chinese,
that comes from the model, and one line steers it back: "Please write in English."

</details>

</div>

**Why this matters.** Each model makes its own kind of mistakes. In our tests, GLM 5.3 Flash went in circles and
switched to Chinese (as we'll discuss in step 6); another model may make other mistakes. This homework develops your habits, things that
you do: how you ask, how you watch, how you check. So they help with any model.

**Four settings decide which model works, and how.** They are the first four rows of this table. **Note: An API is the
way that programs talk to each other**, here the tool and the server of the model. A token is a short piece of text, often
part of a word.

| | <span class="cmd-i cmd-i-t">`./kingo claude`</span> | <span class="cmd-i cmd-i-t">`./kingo claude --login`</span> |
|---|---|---|
| **The model name:** which model answers | `z-ai/glm-5.3-flash`, that is GLM 5.3 Flash, by Z.ai | Claude (Sonnet, Opus …), by Anthropic |
| **The API URL:** where the tool sends the conversation | to OpenRouter, which passes it on to a server that runs the model | to Anthropic |
| **The API key:** who pays | you, with your OpenRouter key: about 0.15 US dollars per million tokens in, 0.50 US dollars per million tokens out | your Claude subscription, up to its limits: your login takes the place of a key |
| **The context window:** how long the conversation can get | 200,000 tokens: kingo sets this | 1,000,000 tokens on the current Claude models |
| <span class="cmd-i cmd-i-c">`/effort`</span>: how much the model thinks before it answers | not for this model | <span class="cmd-i cmd-i-c">`/effort low`</span> to <span class="cmd-i cmd-i-c">`/effort max`</span> |

200,000 tokens is a lot: the text of several books. When the conversation gets near the end of its context window,
the tool shortens it: it replaces the older part with a summary.

<figure class="hx hx-set" data-mode="name" aria-label="The four settings"><div class="hx-switch" role="group" aria-label="Pick a setting"><button type="button" data-mode="name" aria-pressed="true">Model name</button><button type="button" data-mode="url" aria-pressed="false">API URL</button><button type="button" data-mode="key" aria-pressed="false">API key</button><button type="button" data-mode="ctx" aria-pressed="false">Context window</button></div><div class="hx-set__path"><div class="hx-set__node tool"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="4" width="19" height="16" rx="2"/><path d="m7 9 3 3-3 3"/><path d="M13 15h4"/></svg></span><b>The tool</b><span>on your laptop</span></div><div class="hx-set__wire"><i class="pkt"><svg class="hx-i key" viewBox="0 0 24 24" aria-hidden="true"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5"/></svg></i></div><div class="hx-set__node router"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/></svg></span><b>OpenRouter</b><span><code>openrouter.ai/api</code></span></div><div class="hx-set__wire two"><i class="pkt"><svg class="hx-i key" viewBox="0 0 24 24" aria-hidden="true"><path d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"/><circle cx="16.5" cy="7.5" r=".5"/></svg></i></div><div class="hx-set__node brain"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/><path d="M12 5v13"/></svg></span><b>The model</b><span><code>z-ai/glm-5.3-flash</code></span></div></div><div class="hx-set__ctx" aria-hidden="true"><span>The conversation</span><i></i><em>200,000 tokens</em></div><p class="hx-pick" data-for="name"><strong>The model name</strong> says which model answers: <code>z-ai/glm-5.3-flash</code>. OpenRouter passes the conversation on to a server that runs this model.</p><p class="hx-pick" data-for="url"><strong>The API URL</strong> says where the tool sends the conversation, at every step: to <code>https://openrouter.ai/api</code>.</p><p class="hx-pick" data-for="key"><strong>The API key</strong> goes with every request. OpenRouter charges the owner of the key: you.</p><p class="hx-pick" data-for="ctx"><strong>The context window</strong> says how long the conversation can get: 200,000 tokens. Near that limit, the tool replaces the older part with a summary.</p><figcaption>Click the four settings: each one lights up what it decides.</figcaption></figure>

**What leaves your laptop.** At every step, the tool sends the conversation to the model: your prompts, and
everything that Claude Code read, for example files and mails from your database. With your OpenRouter key, it goes
to OpenRouter and on to a server that runs the model; with `--login`, it goes to Anthropic. OpenRouter keeps your prompts
only if you switch that on, and the company that runs the model has its own rules.

- **In your team's project:** its data goes out to the data centers in the same way when Claude Code reads it as when
  your Langflow flows send it to a model. This is okay: the data is synthetic, made up for the course.
- **At work:** let Claude Code read company or customer data only when you may send that data to every company that
  gets it: the company that runs the model, and any service in between, such as OpenRouter.

**The model is set for you.** kingo set the four settings for you. In all six places where Claude Code names a
model, one for each of its jobs, kingo put GLM 5.3 Flash. In the course, your OpenRouter key works only for the course's
models: after <span class="cmd-i cmd-i-c">`/model`</span> and another name, Claude Code shows an error. To go back, type <span class="cmd-i cmd-i-c">`/model z-ai/glm-5.3-flash`</span> in
Claude Code, or start <span class="cmd-i cmd-i-t">`./kingo claude`</span> again in your terminal.

**If you have a Claude Pro or Max subscription, you can use it with <span class="cmd-i cmd-i-t">`./kingo claude --login`</span>:** then Claude Code uses
Anthropic's models, and your Claude subscription pays. Type <span class="cmd-i cmd-i-c">`/model`</span> in Claude Code and pick one.

<details class="more">
<summary>Beyond OpenRouter and Anthropic subscription: using other APIs</summary>

**With a key that may use other models,** for example your own key or one at work, type <span class="cmd-i cmd-i-c">`/model`</span> and the model's
name in Claude Code. You find the name, its ID, on the model's page at [openrouter.ai/models](https://openrouter.ai/models), under
its title. Before you take a model, check four things on its page:

- **Tools:** the model must support them. Here, tools are the actions that the model can ask the tool to do, such
  as read a file or run a command. Without them, the model can only write text.
- **Images:** the model must read images, too. Once the conversation holds a picture, for example a page that Claude
  Code looked at, a model for text only stops with an error.
- **Context:** 200,000 tokens or more: kingo lets the conversation grow that long.
- **Price:** per million tokens, in and out. A bigger model often costs more. Give your key a credit limit on
  openrouter.ai (Settings, Keys): the key then stops at that amount.

**In the course folder, you can also change which API Claude Code uses,** for example to use a local model or
Anthropic's API instead of OpenRouter. [Change the model](/abp/ws2/s2-model/#use-anthropics-api-or-another-provider) shows how to do this.

</details>

<details class="more">
<summary>If you use Claude Code without kingo: the names of the four settings</summary>

Outside kingo, you set the four settings yourself. Claude Code reads them from environment variables. You can also
write them into a file `settings.json`, under `"env"`: kingo did that for the model names, for the course in
`~/kingo-pod/claude/.claude/settings.json`, and for a folder of your own in `~/kingo-pod/setup/claude/settings-in.json`.

| Setting | Its name in Claude Code |
|---|---|
| The model name | `ANTHROPIC_MODEL`, and five more, for Claude Code's other jobs, as in kingo's `settings.json` |
| The API URL | `ANTHROPIC_BASE_URL`, for OpenRouter: `https://openrouter.ai/api` |
| The API key | for OpenRouter: `ANTHROPIC_AUTH_TOKEN`, with `ANTHROPIC_API_KEY` set to `""`; for Anthropic's own API: `ANTHROPIC_API_KEY` |
| The context window | `CLAUDE_CODE_MAX_CONTEXT_TOKENS`, for a model that Claude Code does not know |

- **A key is a password.** Never write it into a file that you share or upload, for example to GitHub. In kingo,
  Claude Code never sees your key: the sandbox keeps it and adds it to each request on the way out.
- **Claude Code knows the context window of Claude models only.** For any other model, it assumes one, and that may
  be wrong. So give it the size from the model's page, or a smaller one. kingo gives 200,000 tokens, though GLM 5.3
  Flash takes more than 1,000,000: so the tool shortens a long conversation earlier, and each step after that costs
  less.

*From Anthropic's pages on [environment variables](https://code.claude.com/docs/en/env-vars) and on
[the context window of a model it does not know](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id),
and OpenRouter's guide [Claude Code integration](https://openrouter.ai/docs/guides/coding-agents/claude-code-integration).*

</details>

Done: you know who answers you, where your words go, and who pays.

**Next time.** When you start Claude Code somewhere new, read its first lines: which model works there, and who
pays?

*From Anthropic's [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop):
"models that reason and tools that act", and its pages on [model configuration](https://code.claude.com/docs/en/model-config)
and [commands](https://code.claude.com/docs/en/commands). The price and the context window of GLM 5.3 Flash are from
[OpenRouter](https://openrouter.ai/z-ai/glm-5.3-flash), 18 Nov 2026. What OpenRouter keeps: its pages on
[data collection](https://openrouter.ai/docs/guides/privacy/data-collection) and
[provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging); the credit limit:
[Limits](https://openrouter.ai/docs/api/reference/limits).*

[Stuck? Help for step 1](#step-1)

### 2. Give Claude Code the facts of your setup (here: kingo does it for you)

<div class="quiz">

**Quiz.** Langflow and n8n come in many versions, and what works in one version may fail in another. How does Claude
Code know which versions run in your kingo-pod?

<ul>
<li>From what the model learned: it knows every version of Langflow and n8n</li>
<li data-right>From the files it reads at the start, and from what it finds out while it works</li>
<li>From the newest documentation on the internet</li>
</ul>

<details class="more">
<summary>Show the answer</summary>

**From its files and from what it finds out.** The model learned a lot about Langflow and n8n, but not which
versions run on your laptop. The newest documentation is for the newest version, and your setup may run an older one.
When its files say nothing, Claude Code has to guess and try, and that takes time. A few lines in its files save it
that search.

Here, three short files tell Claude Code the facts of your kingo-pod: how to find the versions, where Langflow and n8n
describe their API (the way other programs talk to them), how long they may take to answer, and what you can do that
Claude Code cannot.

</details>

</div>

In kingo-pod, kingo gives Claude Code these facts: at every start of <span class="cmd-i cmd-i-t">`./kingo claude`</span>, it writes them into your
course folder. **Your turn:** see them.

<details class="more">
<summary>New here? Look at what kingo writes for the course</summary>

With `--in`, kingo writes no file into your folder: these facts are about n8n and Langflow, which you do not have.
But kingo-pod holds the files that kingo writes for the course, in the folder `~/kingo-pod/setup/claude`. On a Mac,
paste this line into your terminal:

<div class="cmd cmd-terminal">

```
open -e ~/kingo-pod/setup/claude/AGENTS.md
```

</div>


On Windows, paste this line into the Ubuntu app:

<div class="cmd cmd-terminal">

```
cd ~/kingo-pod/setup/claude && notepad.exe AGENTS.md
```

</div>


Find the section "Facts about this setup", right above the heading `# Your team's rules`. Its three lines with `@`
load the three files in the folder `info-for-ai`, next to `AGENTS.md`. Close the file without a change. Then skip
the four steps below, and read on at **For any project**.

</details>

1. Start Claude Code. Is it running already? Type <span class="cmd-i cmd-i-c">`/exit`</span> first. Then paste this line into your terminal: it updates
   kingo-pod and starts Claude Code.
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod && ./kingo update && ./kingo claude
   ```

   </div>

   Before Claude Code starts, kingo says which files of your course folder it wrote: the first time, `AGENTS.md` and
   three files in the folder `info-for-ai`. Do you start Claude Code with `--login`? Then kingo asks for your
   OpenRouter key if it does not have it yet: paste the key that your flows in Langflow use. With it, Claude Code can
   try the models of your flows.
2. Open your course folder, `~/kingo-pod/claude`: there Claude Code works for the course. Open a second terminal tab
   ([how](/abp/ws2/hw3/#your-terminal-in-short)). On a Mac, paste this line:
   <div class="cmd cmd-terminal">

   ```
   open ~/kingo-pod/claude
   ```

   </div>

   On Windows, paste this line into the Ubuntu app:
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod/claude && explorer.exe .
   ```

   </div>

   Tip for Windows: pin the folder, so that you find it again without the command. Click the arrow **↑** next to the
   address bar: now you see the folder `claude`. Right-click it and choose **Pin to Quick access**. From then on, it is
   in the left column of every File Explorer window.

   <details class="more">
   <summary>Windows: how can Ubuntu open a window of Windows?</summary>

   Ubuntu runs inside Windows, and the two can reach each other:

   - From Ubuntu, you can start programs of Windows: <span class="cmd-i cmd-i-t">`explorer.exe`</span> is the File Explorer, <span class="cmd-i cmd-i-t">`notepad.exe`</span> is Notepad.
     The dot in <span class="cmd-i cmd-i-t">`explorer.exe .`</span> means: the folder you are in.
   - So the File Explorer shows your folder in Ubuntu, and you can drag files from Windows into it.
   - Ubuntu also sees your files in Windows: the drive `C:` is the folder `/mnt/c`. Still, keep your work in Ubuntu,
     under `~`, as this homework does: Microsoft advises it.

   *From Microsoft's [Working across file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems).*

   </details>

3. In the course folder, open the folder `info-for-ai`: it holds three short files, `kingo-pod.md`, `langflow.md`
   and `n8n.md`. In the terminal, this line lists them:
   <div class="cmd cmd-terminal">

   ```
   ls ~/kingo-pod/claude/info-for-ai
   ```

   </div>

4. Open `AGENTS.md` in a text editor, as in
   [step 6 of the last homework](/abp/ws2/hw2-a/#6-see-the-instructions-claude-code-reads-at-every-start). On a Mac,
   paste this line into your terminal:
   <div class="cmd cmd-terminal">

   ```
   open -e ~/kingo-pod/claude/AGENTS.md
   ```

   </div>

   On Windows, paste this line into the Ubuntu app:
   <div class="cmd cmd-terminal">

   ```
   cd ~/kingo-pod/claude && notepad.exe AGENTS.md
   ```

   </div>

   Find the section "Facts about this setup", right above the heading `# Your team's rules`. Its three lines with
   `@` load the three files.

**What stays, and what kingo writes.** kingo writes everything above `# Your team's rules` anew at every start, and
the files in `info-for-ai` too. So your team's rules go below the heading: there they stay. Did a line of your own
land above the heading? kingo moves it below the heading and says so. The file as it was, kingo keeps in
`~/kingo-pod/backups/course-files/`.

Done. At every start, the tool now loads these five files, its start files, and gives them to the model, before your
first prompt:

<figure class="hx hx-start" aria-label="What Claude Code reads at the start"><ol class="hx-files"><li style="--i:0"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><code>CLAUDE.md</code><span>Claude Code opens it first. It points to AGENTS.md: <code>@AGENTS.md</code></span></li><li style="--i:1"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><code>AGENTS.md</code><span>how to reach the services, your team's rules, and three lines with <code>@info-for-ai/…</code></span></li><li style="--i:2"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><code>info-for-ai/kingo-pod.md</code><span>you, the student, and this kingo-pod</span></li><li style="--i:3"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><code>info-for-ai/langflow.md</code><span>this Langflow: how to find its version, where its API is described</span></li><li style="--i:4"><span class="hx-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg></span><code>info-for-ai/n8n.md</code><span>this n8n: how to find its version, where its API is described</span></li></ol><div class="hx-start__view" aria-hidden="true"><b>The model gets all five</b><span>before your first prompt</span><i style="--i:0"></i><i style="--i:1"></i><i style="--i:2"></i><i style="--i:3"></i><i style="--i:4"></i></div><figcaption>Each <code>@</code> in a file makes the tool load one more file. The model gets all five, at every start.</figcaption></figure>

**For any project.** Here, kingo wrote the facts for you; in a project of your own, you write them yourself. Claude
Code loads the file `CLAUDE.md` at every start. Many other coding agents (tools like [OpenCode](https://opencode.ai))
read a file `AGENTS.md` instead, and Claude Code reads that file too when a folder has no `CLAUDE.md`. Here,
`CLAUDE.md` only points to `AGENTS.md`, so both work.

Four tips for such a file:

- **Keep it short.** The model reads every line, for every task.
- **Write down what Claude Code cannot find out by itself**, or only after a long search: for example, which versions
  you run, a decision that is only in your head, and anything you had to correct twice.
- **Say how to check the work**, for example with the command that runs the tests.
- **Name the limits.** Does Claude Code work in a sandbox? Write down what it may do there, what it may not, and what
  you can do for it. Then it does not lose time finding the limits by trial and error.

**Next time.** When you correct Claude Code twice on the same thing, ask it: "Write this into AGENTS.md, below
`# Your team's rules`." From then on, it reads it at every start.

*From Anthropic's [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#tell-claude-what-it-cant-see):
tell Claude what it can't see (the limits of a sandbox are such a thing), and
[keep CLAUDE.md short](https://code.claude.com/docs/en/best-practices#keep-claude-md-short); on `AGENTS.md`:
[How Claude remembers your project](https://code.claude.com/docs/en/memory#agents-md) and OpenCode's page on
[instructions](https://opencode.ai/docs/instructions/). Pin to Quick access: Microsoft's
[File Explorer in Windows](https://support.microsoft.com/en-us/help/4028316).*

[Stuck? Help for step 2](#step-2)

**Next: [Part B · Ask well →](/abp/ws2/hw3-b/)**

## If something goes wrong

Find your step.

#### Step 1

| What you see | What to do |
|---|---|
| New here: kingo says `n8n and Langflow must be running first` | That is the start for the course. Start Claude Code in your folder: <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo claude --in ~/projects/practice`</span>. |
| New here: kingo says `Claude Code is not installed`, or `python3 is missing` | Paste the line that kingo names after it, then start again. |
| After <span class="cmd-i cmd-i-c">`/exit`</span>, nono writes `Sandbox denial: … paths blocked` and `Fix flags` | That is the fence at work: Claude Code looked at places outside it, for example your own `~/.claude` and the keychain of your Mac, and nono said no. Claude Code works without them. Add none of these flags: they would open the fence. |
| After <span class="cmd-i cmd-i-c">`/model`</span> and a name, Claude Code shows an error | In the course, your key works only for the course's models. Type <span class="cmd-i cmd-i-c">`/model z-ai/glm-5.3-flash`</span> to go back. With a key that may use other models, check the name on the model's page, and that the model supports tools and images: `No endpoints found …` means that OpenRouter found no server for this model that takes your request, for example because the model reads only text and the conversation holds a picture. |

#### Step 2

| What you see | What to do |
|---|---|
| `No such file or directory` for `~/kingo-pod/claude` | Claude Code never started in the course folder. Do [step 4 of the last homework](/abp/ws2/hw2-a/#4-start-claude-code-and-give-it-its-keys) first. |
| You see no `AGENTS.md` in the course folder | Same as above: start Claude Code once with <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo claude`</span>, then <span class="cmd-i cmd-i-c">`/exit`</span>. |
| There is no folder `info-for-ai` in your course folder | kingo-pod is not up to date yet. Paste this line into your terminal again: <span class="cmd-i cmd-i-t">`cd ~/kingo-pod && ./kingo update && ./kingo claude`</span>. |
| kingo says that your `AGENTS.md` has no heading "# Your team's rules" | Open `AGENTS.md`, and write the line `# Your team's rules` above your team's rules, or at the end of the file. Then start <span class="cmd-i cmd-i-t">`./kingo claude`</span> again. |
| kingo says that it moved lines below `# Your team's rules` | They were above the heading, where kingo writes its own part. Now they are right below the heading: check them there. The file as it was is in `~/kingo-pod/backups/course-files/`. |
| <span class="cmd-i cmd-i-t">`./kingo claude`</span> (or <span class="cmd-i cmd-i-t">`./kingo claude --login`</span>) asks for your OpenRouter key, and you do not have it any more | Make a new key on openrouter.ai (Settings, Keys) and paste it. |
