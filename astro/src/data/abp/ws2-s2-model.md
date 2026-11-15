---
title: "Change the model that Claude Code uses"
---

In the course, Claude Code uses the model **GLM 5.3 Flash**. It reaches the model through **OpenRouter**, and it pays
with **your OpenRouter key**. You can change all three. This page shows how.

You need this page only if you want another model. The course works with the settings as they are.

There are three ways. Take the one that fits you:

- **Another model at OpenRouter.** You keep your key and change one name.
- **Your Claude subscription.** You have Claude Pro or Max: Claude Code uses it, with Anthropic's models.
- **Anthropic's API, or another provider.** For example Claude Sonnet 5.5 with an Anthropic API key, or a server
  of your company.

<div class="warn" markdown="1">

The second and the third way need a new kingo-pod. Check it:

```
cd ~/kingo-pod && ./kingo claude help
```

Is there a line with `--login`? Then you have it. If not, run `./kingo update` first.

</div>

## Where each thing is set

Three files decide how Claude Code runs in kingo-pod. Each has one job.

| What | Where it is set | Whose file |
|---|---|---|
| **The model** Claude Code asks for | `kingo-pod/claude/.claude/settings.json` | yours: kingo writes it once and never again |
| **The provider** the request goes to, and **the key** it is paid with | the sandbox profile: `kingo-pod/setup/claude/nono-profile-base.json` | kingo's: every `./kingo update` brings a new copy |
| **Your additions** to the sandbox profile | `kingo-pod/my-nono-profile.json` | yours: kingo reads it and never changes it |

Claude Code itself never sees a key. The sandbox (nono) keeps your key in a file outside everything Claude Code can
read, and puts it into each request on the way out. Inside the sandbox, the key is a stand-in.

## Use another model at OpenRouter

Your key stays the same. Only the name of the model changes.

### 1. Pick a model

Open [openrouter.ai/models](https://openrouter.ai/models) and pick a model. Copy its ID: the short name under the
title, for example `z-ai/glm-5.3-flash`.

<div class="warn" markdown="1">

Check two things on the model's page before you take it. **Tools:** Claude Code works by calling tools; a model
without tool use cannot run a command or write a file. **Images:** `look` shows Claude Code a picture of a page it
wrote; a model that takes only text cannot see it.

</div>

A bigger model costs more for each request. The price is on the same page.

### 2. Put the ID into the settings

Open the settings file.

On a Mac:

```
open -e ~/kingo-pod/claude/.claude/settings.json
```

On Windows, in the Ubuntu window:

```bash
cd ~/kingo-pod/claude/.claude && notepad.exe settings.json
```

Six lines name the model. Replace `z-ai/glm-5.3-flash` in **all six** with the ID you copied:

```json
"ANTHROPIC_MODEL": "z-ai/glm-5.3-flash",
"ANTHROPIC_DEFAULT_OPUS_MODEL": "z-ai/glm-5.3-flash",
"ANTHROPIC_DEFAULT_SONNET_MODEL": "z-ai/glm-5.3-flash",
"ANTHROPIC_DEFAULT_HAIKU_MODEL": "z-ai/glm-5.3-flash",
"ANTHROPIC_DEFAULT_FABLE_MODEL": "z-ai/glm-5.3-flash",
"CLAUDE_CODE_SUBAGENT_MODEL": "z-ai/glm-5.3-flash",
```

Claude Code uses different models for different jobs: a big one to plan, a small one for short tasks, one for its
helpers. The six lines give the same model to every job. Leave one line out, and Claude Code asks for one of Anthropic's
models for that job.

Save the file.

### 3. Start Claude Code again

```
cd ~/kingo-pod && ./kingo claude
```

The first lines of Claude Code show the model it uses. Your ID is there: it worked.

### Go back

Put `z-ai/glm-5.3-flash` back into the six lines. Or delete the file `settings.json`: the next `./kingo claude`
writes the course's settings again.

## Use your Claude subscription

Do you have a Claude subscription (Pro or Max)? Then Claude Code in kingo-pod can use it. You get Anthropic's models,
your subscription pays, and Claude Code needs no OpenRouter key.

### 1. Start with `--login`

```
cd ~/kingo-pod && ./kingo claude --login
```

### 2. Log in, once

**On a Mac:** your browser opens. Log in to Claude and agree.

**On Windows:** Claude Code shows a long address in the Ubuntu window. Copy it into your browser, log in to Claude
and agree. The page shows a code. Copy the code, paste it into the Ubuntu window and press Enter.

kingo says `Logged in.` and Claude Code starts. The next time, `./kingo claude --login` starts at once.

**Where is my login?** Not in the sandbox. nono, the sandbox, keeps your login for itself and gives Claude Code a
stand-in. The stand-in works only inside this sandbox. So a mistake of Claude Code cannot give your login away.
The file `kingo-pod/setup/claude/nono-profile-login.json` shows how this is set up.

### 3. Check the model

The first lines of Claude Code show the model. It is one of Anthropic's now, for example Sonnet. Type `/model` in
Claude Code to pick another one.

<div class="warn" markdown="1">

Run one session with `--login` at a time. Two at once can break the login. If Claude Code says that you are not
logged in, type `./kingo claude logout` and start again.

</div>

### Go back

Start without `--login`: `./kingo claude` is the course's again, with GLM 5.3 Flash and your OpenRouter key. The two
do not disturb each other. To end the login on this laptop:

```
cd ~/kingo-pod && ./kingo claude logout
```

## Use Anthropic's API, or another provider

A provider is the service that runs the model: OpenRouter, Anthropic, or a server of your company. Claude Code speaks
to it in one format, the Messages API of Anthropic. Every provider that offers this format works.

You change three things: the key, the route, and the settings. The example is Anthropic's own API, with Claude
Sonnet 5.5.

### 1. Save the key where the sandbox finds it

In your terminal, not in Claude Code:

```bash
read -rs KEY && printf '%s' "$KEY" > ~/.config/kingo/anthropic.key && chmod 600 ~/.config/kingo/anthropic.key; unset KEY
```

The line waits. Paste your key and press Enter. You do not see the key as you paste it.

### 2. Tell the sandbox about the provider

Make your own profile from the example, in the kingo-pod folder:

```bash
cd ~/kingo-pod && cp setup/claude/my-nono-profile.example.json my-nono-profile.json
```

Open it. On a Mac:

```
open -e ~/kingo-pod/my-nono-profile.json
```

On Windows, in the Ubuntu window:

```bash
cd ~/kingo-pod && notepad.exe my-nono-profile.json
```

Put this block after the block `"meta": { ... },`:

```json
"network": {
  "custom_credentials": {
    "anthropic": {
      "upstream": "https://api.anthropic.com",
      "credential_key": "file://__KEYS_DIR__/anthropic.key",
      "env_var": "ANTHROPIC_API_KEY",
      "inject_header": "x-api-key",
      "credential_format": "{}"
    }
  }
},
```

What the five lines say:

| Line | Meaning |
|---|---|
| `upstream` | the address of the provider |
| `credential_key` | the file with your key. kingo fills in `__KEYS_DIR__`: it is `~/.config/kingo` |
| `env_var` | the variable in which Claude Code finds the stand-in for the key |
| `inject_header` | the header in which the provider expects the key |
| `credential_format` | how the key is written there. `{}` is the key itself |

The name `anthropic` must stay. The course profile has a route with this name, to OpenRouter. Your block takes its
place.

The example also lets Claude Code read and write in `kingo-pod/shared`: it can change or delete every file there. If
you do not want that, delete the block `"filesystem": { ... }` from your file.

### 3. Change the settings

Open `kingo-pod/claude/.claude/settings.json`, as above.

1. Delete this line. It keeps Claude Code from using a key, and now it has one:

    ```json
    "ANTHROPIC_API_KEY": "",
    ```

2. Put Anthropic's model IDs into the six lines that name the model:

    ```json
    "ANTHROPIC_MODEL": "claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-5-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-5-5",
    "ANTHROPIC_DEFAULT_FABLE_MODEL": "claude-fable-5-2",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-5-5",
    ```

   Claude Code starts with Sonnet 5.5. In Claude Code, `/model` switches to Opus, Haiku or Fable. Another provider
   has its own IDs: look them up in its documentation.

### 4. Start Claude Code again

```
cd ~/kingo-pod && ./kingo claude
```

kingo says `The sandbox follows your own profile too`. The first lines of Claude Code show your model.

<div class="warn" markdown="1">

`./kingo claude` still asks for an OpenRouter key and checks it at every start, also when your requests go to
another provider. Keep your OpenRouter key.

</div>

### Go back

Delete `my-nono-profile.json`, and delete `settings.json`. The next `./kingo claude` is the course's again.

## What does not change

- **The sandbox.** Claude Code writes only in `kingo-pod/claude` (and in `kingo-pod/shared`, if you keep the example's
  block `filesystem`), with every model and every provider.
- **Your key stays outside.** With another provider too, Claude Code gets a stand-in.
- **n8n, Langflow and the database.** Claude Code reaches them as before.
