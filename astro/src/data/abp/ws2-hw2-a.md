---
title: "Homework until 16 Nov, Part A: Claude Code"
---


### What is Claude Code?
Claude Code is a major innovation from Anthropic (OpenAI followed up with a clone called Codex; an open source alternative is called OpenCode). The idea is simple (which makes it even better).
1. Instead of copy/pasting code back and forth from Chat interfaces (like ChatGPT or Claude), Claude Code is a tool that simply writes directly onto your computer.
2. Instead of using complicated editors and heavy software, the tool is made to live directly in the terminal. This allowed Anthropic to quickly develop a robust tool, and to focus on the main ideas.
3. Instead of editing code or documents yourself, you describe to the AI what you want to be changed. By design, you use it as an agent.

It started as a simple idea but proved to be revolutionary in software development. Quickly, people also realized
its usefulness for working with other documents, like PowerPoint or Excel files.

### Better safe than sorry
Even though Claude Code usually has good intentions, it might accidentally do things on your computer that have seriously bad consequences. Hence, it’s always asking you for permission before doing something. Quickly, people said yes to everything instead of reading the fine print. Hence, developers decided to build sandboxes: within the sandbox, the AI can do what it wants, it might also reach out on well-defined paths, but that’s it.

![Claude Code as a robot in a sandbox called nono: inside, it may dig, play and build as it likes; nothing may leave the box.](/abp/ws2/img/sandbox.jpg)

We use the sandbox tool called **<a href="https://nono.sh/" target="_blank" rel="noopener">nono</a>**. We configure it so that Claude Code can
- only write in one folder: `~/kingo-pod/claude`,
- read the rest of kingo-pod to understand how it works,
- reach out to n8n, Langflow and your database,
- access the internet, and
- not do anything else on your laptop.

Typically, Claude Code uses the Claude models from Anthropic. Here, we use it with the model GLM 5.3 Flash, paid with the OpenRouter key you already have.

### 1. Update kingo-pod to get the new command `kingo claude`

Open a terminal (in Windows, start WSL/Ubuntu) and run this one line:

```
cd ~/kingo-pod && ./kingo update
```

When it is done, run 
```
./kingo help
```
You should see a line that starts with `kingo claude`.

[Stuck? Help for step 1](#step-1)

### 2. Install Claude Code and its sandbox

One line installs three programs: **nono** (the sandbox), **psql** (so that Claude Code can talk to your Postgres database) and
**Claude Code**. Run the command in the terminal:

On a Mac:

```
brew install nono libpq && curl -fsSL https://claude.ai/install.sh | bash
```

On WSL (Ubuntu in Windows):

```
curl -fsSL https://nono.sh/install.sh | sh && sudo apt install -y postgresql-client && curl -fsSL https://claude.ai/install.sh | bash
```

<details class="more">
<summary>Already using Claude Code?</summary>

Run the command anyway: it installs Claude Code the way Anthropic recommends, or brings it up to date. Your own settings
and your login stay as they are.

Did you install Claude Code with Homebrew or npm instead? Then you now have two installations. `./kingo claude` always takes the new one.
To keep only the new one, remove the old one:

- Homebrew: `brew uninstall --cask claude-code`
- npm: `npm uninstall -g @anthropic-ai/claude-code`

</details>

[Stuck? Help for step 2](#step-2)

### 3. Make a key in n8n

Claude Code works on your workflows through n8n's API. For that, it needs a key from n8n.

1. **Open n8n** at <http://localhost:5678> and sign in.
2. Click **Settings** at the bottom of the left sidebar, then **n8n API**.
3. Click **Create API key**. In the window *Create API Key*:
   - Label: `claude`
   - Expiration: **Never**. Then the key works for the whole course.
4. Click **Save**. Copy the key and keep it for step 4: n8n shows it only once.

[Stuck? Help for step 3](#step-3)

### 4. Start Claude Code and give it its keys

In the terminal, run:

```
cd ~/kingo-pod && ./kingo claude
```

Always start Claude Code for the course this way. A plain `claude` starts a standard Claude Code, without the sandbox
and without the course settings ([what is different](#what-is-different-from-a-standard-claude-code-and-where-it-is-configured)).

The first time, `kingo claude` asks for two keys. You do not see a key as you paste it: that is on purpose.

1. Paste your OpenRouter key (or your group’s key) and press Enter.
2. Paste the n8n key from step 3, and press Enter.

<details class="more">
<summary>Don’t I need to give it a key to Langflow?</summary>

`kingo-pod` can make this and hand it to Claude Code. To be honest, if you have superuser access to the database used by Langflow (and by n8n), and to the file system, then you can get a lot of credentials. Feel free to ask Claude Code more about this later. And while you’re at it, you can ask how an admin can extract credentials saved to n8n.

</details>

Then Claude Code starts and asks a few questions of its own:

3. Pick a theme for Claude Code that you like, and press Enter.
4. *Do you trust the files in this folder?* Choose **Yes**.

You see Claude Code waiting for your first words. Well done: your coding agent is set up.

[Stuck? Help for step 4](#step-4)

### 5. Let’s try it out

Type this and press Enter:

```
List my n8n workflows and tell me in one sentence each what they do.
```

Before Claude Code runs a command, it asks you. Read what it wants to do, then agree. You should see WS2.0,
WS2.1, WS2.3 and WS2.4, each with a sentence. That is Claude Code reading your n8n.

To leave Claude Code (and to get back to the terminal), run
```
/exit
```
Sometimes when exiting Claude Code, you get a question from nono sandbox, if it should give Claude Code further permissions. Only add something if you know what you’re doing.

Now you can continue using this terminal as usual (you can also just open another one like you can open another tab in your browser).

[Stuck? Help for step 5](#step-5)

### 6. See the instructions Claude Code reads at every start

Claude Code reads the file `AGENTS.md` in its folder at every start (actually, it reads `CLAUDE.md` which here just has a link to `AGENTS.md`). You can have a look inside (the `cat` command just prints the content of the file into the terminal and you can continue using the terminal as usual):

```
cat ~/kingo-pod/claude/CLAUDE.md
```
And
```
cat ~/kingo-pod/claude/AGENTS.md
```

With your team's rules in `AGENTS.md`, Claude Code builds the way your team decides: the same names, the same contracts between flows and between tools.

Start Claude Code again with 
```
cd ~/kingo-pod && ./kingo claude
```
and ask:

```
What are our team's rules?
```

Claude Code should say that your team has not added its rules yet. That is right, and it shows that Claude Code has read `AGENTS.md`.

<details class="more">
<summary>How do I change AGENTS.md myself?</summary>

Open it in a text editor, like any text file:

- On a Mac, this line opens it in TextEdit:
  ```
  open -e ~/kingo-pod/claude/AGENTS.md
  ```
- On Windows, in the Ubuntu app, this line opens it in Notepad:
  ```
  cd ~/kingo-pod/claude && notepad.exe AGENTS.md
  ```

Change it, then save with **Cmd+S** (Mac) or **Ctrl+S** (Windows).

Or do it in **nano**, an editor inside the terminal. It works the same on a Mac and in the Ubuntu app. Do not confuse
nano with nono:

- **nano** is the opposite of a huge tool like MS Word for a simple task.
- **nono** is the opposite of saying "yes, yes, …" to Claude Code.

```
nano -w ~/kingo-pod/claude/AGENTS.md
```

(`-w` keeps long lines as they are.)

- Move with the arrow keys, and type as usual. A mouse click does not move the cursor.
- Paste: on a Mac **Cmd+V**, in the Ubuntu app a right click.
- Save: **Ctrl+O** (on a Mac the key *control*, not *command*), then **Enter**.
- Leave nano: **Ctrl+X**.

The two lines at the bottom of nano show these keys: `^O` means **Ctrl+O**.

Claude Code reads `AGENTS.md` only when it starts. After a change, leave Claude Code with `/exit` and start it again.

**Try it:** add this line at the very end of `AGENTS.md`, with your own language if it is not Korean:

```
Always answer me in Korean.
```

Save, `/exit` and start Claude Code again with
```
./kingo claude
```
and ask it something: it answers in Korean. Keep the line, or delete it again. 

It’s a good idea to add your team’s design rules to `AGENTS.md`.
</details>

[Stuck? Help for step 6](#step-6)

### What Claude Code can do, and what it cannot

Careful, if you just type `claude`, then Claude Code runs in the standard way as Anthropic had it set up. Please always use
```
./kingo claude
```
This way, it’s in the nono sandbox.

| Claude Code can | Claude Code cannot |
|---|---|
| read and write in `~/kingo-pod/claude` | write anywhere else on your laptop |
| read kingo-pod: `compose.yml`, the guides | change kingo-pod, or run `./kingo` |
| change your n8n workflows, Langflow flows and database | see your keys: it gets stand-ins |
| look things up on the web | see your own Claude Code settings, if you use Claude Code already |

Sometimes, Claude Code wants to execute a command (which we don’t allow), and then it’ll tell you to run a command on its behalf in the terminal.

**Only run a command in your own terminal if you understand it.**

Claude Code cannot leave its sandbox, but a command you type does. When Claude Code says that the sandbox blocks it, that is the sandbox doing its job. When the sandbox asks you to give additional permissions after leaving Claude Code, then only add something if you know what you’re doing.

### You decide: should Claude Code ask before every command?

So far Claude Code asks you before it runs a command or changes something. You can also let it work without asking. To this end,
you start it with this line:

```
./kingo yolo
```

The first time, Claude Code asks whether you accept this mode. Choose **Yes, I accept**.

| | ./kingo claude | ./kingo yolo | claude (without kingo) |
|---|---|---|---|
| Your laptop is | protected by the nono sandbox and by Claude Code’s hesitations | protected by the nono sandbox | protected only by Claude Code’s hesitations: no sandbox |
| Your workflows, flows and database | you see every change before it happens | Claude Code changes them at once, mistakes too | out of reach at first, as Claude Code has no keys for them; but it can read every file you can, your keys too |
| Your user experience | many requests for permissions, often the same ones | Claude Code works on by itself | Anthropic's standard Claude Code: your own Anthropic login and bill, and the usual requests for permissions |

Inside the sandbox, Claude Code’s requests for permission do not protect your laptop: the sandbox does that, with or
without them. They protect your project from Claude Code's mistakes. If you let Claude Code work without asking, save your work first. This line saves your
n8n workflows and your Langflow flows into `~/kingo-pod/backups/` (not your own tables in the database):

```
cd ~/kingo-pod && ./kingo backup
```

Many people start with the requests for permission and switch once they trust what Claude Code does in their project. It is your choice,
and you can change it at every start.

### What is different from a standard Claude Code, and where it is configured

The Claude Code you started with `./kingo claude` is set up for the course.

<div class="warn">

**And if I just type `claude`?**

Then you get a standard Claude Code with Anthropic's settings: no sandbox, your own `~/.claude`, your own Anthropic
login. Even in `~/kingo-pod/claude`, a plain `claude` runs without the sandbox and without the keys. **Here, you're on
your own, kid.**

The course setup holds only when you start Claude Code with `./kingo claude` or `./kingo yolo`.

</div>

<details class="more">
<summary>In detail: what <code>./kingo claude</code> changes, and where</summary>

What is different from a Claude Code you install and start with `claude`, and the file where each
part is configured:

| | A standard Claude Code | Here, started with `./kingo claude` | Configured for the course in |
|---|---|---|---|
| Start | `claude`, in any folder | `./kingo claude` in the kingo-pod folder; `./kingo yolo` is the same without requests for permission. Claude Code works in `kingo-pod/claude` | `kingo-pod/kingo`, the script behind every `./kingo` command. Before Claude Code starts, it checks that n8n and Langflow run, asks for your keys the first time, copies `AGENTS.md`, `CLAUDE.md` and `.claude/settings.json` into `kingo-pod/claude/` the first time, and writes the nono profile. Then it starts Claude Code inside nono. |
| Model and bill | Claude models, with an Anthropic account or key | GLM 5.3 Flash through OpenRouter, paid with your OpenRouter key | `kingo-pod/claude/.claude/settings.json` names the model, for every role (`ANTHROPIC_MODEL` and the lines `ANTHROPIC_DEFAULT_…_MODEL`). The nono profile sends Claude Code's requests to OpenRouter instead of Anthropic, and puts your OpenRouter key into them. |
| Keys | kept by Claude Code itself | kept in `~/.config/kingo/`; Claude Code sees only stand-ins | `kingo-pod/kingo` asks for your OpenRouter and n8n keys, makes the Langflow key itself, and keeps them in `~/.config/kingo/`, readable only by you. When it starts Claude Code, it hands them to nono, not to Claude Code. The nono profile says, for OpenRouter, n8n and Langflow, where nono's proxy puts the real key into a request. |
| Files | Claude Code reads and writes wherever you may, after asking | Claude Code writes only in `kingo-pod/claude` and `~/.kingo-claude`, reads `kingo-pod`, and nothing else; the operating system enforces it | The nono profile `~/.config/nono/profiles/kingo-claude.json` lists the folders Claude Code may read and write, and the few environment variables that reach Claude Code: other keys on your laptop do not. `kingo` writes it anew at every start from `kingo-pod/setup/claude/nono-profile.json`, so a change to it does not last. On top, `kingo-pod/claude/.claude/settings.json` forbids Claude Code to read `.env` files, `~/.ssh` and `~/.aws`. |
| Sandbox | Claude Code's own sandbox, for commands only, if you turn it on | nono, around all of Claude Code: its commands, and its own tools for files too | the nono profile. `kingo-pod/claude/.claude/settings.json` turns Claude Code's own sandbox off (`sandbox.enabled`): nono covers more. |
| Settings and history | `~/.claude` | `~/.kingo-claude`; your own `~/.claude` stays untouched | `kingo-pod/kingo` starts Claude Code with `CLAUDE_CONFIG_DIR=~/.kingo-claude`: Claude Code keeps its settings, sessions and history there. An Anthropic login stored there, `kingo` removes at every start: the course does not use it, and Claude Code could read it. |
| Instructions | a `CLAUDE.md` that you write | `AGENTS.md`: the part about kingo-pod and your team's rules; `CLAUDE.md` only points to it | `kingo-pod/claude/AGENTS.md`, yours to change, and `kingo-pod/claude/CLAUDE.md`, which holds only `@AGENTS.md`. `settings.json` makes Claude Code skip the `CLAUDE.md` of kingo-pod itself, which is for kingo-pod's developers (`claudeMdExcludes`). |
| Memory | hidden in `~/.claude/projects/` | in `kingo-pod/claude/memory/`, where you can read it | `kingo-pod/claude/.claude/settings.json` (`autoMemoryDirectory`) |
| What leaves the laptop | the model's requests and the web pages Claude Code looks up, plus usage data, error reports and feedback to Anthropic; pages on claude.ai (artifacts) and Remote Control, if you use them | the model's requests, to OpenRouter only, and the web pages Claude Code looks up; usage data, error reports, feedback, pages on claude.ai and Remote Control are off | `kingo-pod/kingo` turns off pages on claude.ai, usage data, error reports and all traffic that is not needed, when it starts Claude Code. `kingo-pod/claude/.claude/settings.json` turns off the same, and also feedback (`DISABLE_FEEDBACK_COMMAND`), Remote Control (`disableRemoteControl`), pages on claude.ai (`enableArtifact`) and the check of each web address at Anthropic before Claude Code reads a page (`skipWebFetchPreflight`). |
| Requests for permission | Claude Code asks before a command | the same; `./kingo yolo` turns them off | `kingo-pod/kingo`: `./kingo yolo` starts Claude Code with `--dangerously-skip-permissions`. The sandbox stays the same. |
| Updates | Claude Code updates itself | no self-update: run the install line again | `kingo-pod/claude/.claude/settings.json`: `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also turns off the self-update. |

</details>

**Claude Code's memory.** Claude Code writes down for itself what it learns about your project, so that it still knows it
in the next session: for example a name your team chose, or a mistake it should not make again. Usually this memory
is hidden in Claude Code's own folder. Here it lies in `~/kingo-pod/claude/memory/`, so you can read what Claude Code remembers,
and correct or delete it. The file `MEMORY.md` there lists everything it keeps.

Claude Code can explain all of this itself. Ask it:

```
How are you set up here, and what is different from a standard Claude Code?
```

**Next: [Part B · Find out why your mail AI assistant missed the kimchi →](/abp/ws2/hw2-b/)**

## If something goes wrong

Find your step. Still stuck? Write to Frank: then we fix it together.

#### Step 1

| What you see | What to do |
|---|---|
| `./kingo help` shows no `kingo claude` | Run `./kingo update` again and look for errors near the end. Send Frank what `./kingo version` shows. |

#### Step 2

| What you see | What to do |
|---|---|
| `brew: command not found` (Mac) | The line needs Homebrew. It is missing, or your Terminal does not find it. Do [Step 1 — Install Homebrew](https://huettner.io/kingo-pod/mac/#step-1--install-homebrew) of the kingo-pod Mac guide, with its "Next steps" lines. Open a new Terminal window and run the line again. |
| `Unable to locate package` (Windows) | Run `sudo apt update`, then the line again. |
| A download error | Check that you are online, then run the line again. |
| The line says that a folder is not on your PATH | Nothing to do: `./kingo claude` finds the programs anyway. |

#### Step 3

| What you see | What to do |
|---|---|
| You closed the window before you copied the key | Make a new key the same way. In the list on the page *n8n API*, delete the old one. |

#### Step 4

| What you see | What to do |
|---|---|
| `nono is not installed` or `Claude Code is not installed` | Run the line of step 2 again. |
| `Sandbox initialization failed: WSL2: proxy-only network mode cannot be kernel-enforced` (Windows) | Your kingo-pod is too old for Windows. Run `./kingo update`, then step 4 again. After the update, `./kingo version` shows 1.4.6 or newer (on Kingo 1.5: 1.5.5 or newer). |
| `WARNING: WSL2 insecure proxy mode` (Windows) | Nothing to do: on Windows, this line comes at every start. There, the sandbox cannot lock the network, and in this course Claude Code may use the internet anyway. Your files stay protected, and Claude Code still does not see your keys. |
| `n8n and Langflow must be running first` | Run `./kingo up`, then step 4 again. |
| `n8n did not accept the key` | Make a new key as in step 3. Then run `./kingo claude` again: it asks for the key. |
| `openrouter did not accept the key` | Check the key Yanbo gave you. Then run `./kingo claude` again: it asks for the key. |
| Claude Code asks you to log in to Anthropic | Do not log in. Type `/exit` and write to Frank. |
| `removed an Anthropic login` | You logged in to Anthropic inside `./kingo claude`. `kingo` removed that login again: the course does not use it, and Claude Code could read it there. Your own Claude Code login is not affected. |

#### Step 5

| What you see | What to do |
|---|---|
| Claude Code says it cannot reach n8n | Check that n8n opens at <http://localhost:5678>. If not, run `./kingo up` in your own terminal, then ask again. |

#### Step 6

| What you see | What to do |
|---|---|
| `No such file or directory` | `./kingo claude` makes these files at its first start. Do step 4 first. |
