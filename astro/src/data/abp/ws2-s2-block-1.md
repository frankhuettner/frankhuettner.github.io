---
title: "Block 1 · Build and use a simple webhook"
---

You build a small workflow, *Hello*. Your browser calls n8n, and n8n answers. The node that waits for the call is a
**Webhook**.

### See what runs

1. In the terminal, run:

   ```
   cd ~/kingo-pod && ./kingo status
   ```

   You see one line for each service, with its status and its address. n8n is at `localhost:5678`, Langflow at
   `localhost:7860`.

### Build WS2.10 - Hello

1. In n8n, click **Create workflow**. Click its name at the top and give it this name:

   ```
   WS2.10 - Hello
   ```

2. Add the first node: a **Webhook** (type `Webhook` into the search). Rename it `webhook_hello`. Set it like this:

   **HTTP Method:** *GET* (as it comes). **Respond:** *Using 'Respond to Webhook' Node*. **Path:**

   ```
   hello
   ```

3. Click the dot on its right and add a **Respond to Webhook** node. Rename it `send_greeting`. Set it like this:

   **Respond With:** *JSON*. **Response Body:** switch it to *Expression* and paste:

   ```
   {{ { greeting: 'Hello, ' + ($json.query.name || 'you') } }}
   ```

4. Try it. Click **Execute workflow** at the bottom. n8n now waits for a call. Open a new browser tab and go to this
   address. Put your own name in place of Mina:

   ```
   http://localhost:5678/webhook-test/hello?name=Mina
   ```

   The tab shows the greeting. In n8n, you see the run on the canvas.

5. Publish the workflow: click **Publish** at the top. In the window that opens, click **Publish** again. Now the Production URL works too, without *Execute workflow*:

   ```
   http://localhost:5678/webhook/hello?name=Mina
   ```

<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6C0F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-3px;margin-right:.3em"><path d="M5.8 11.3 2 22l10.7-3.79"/><path d="M4 3h.01"/><path d="M22 8h.01"/><path d="M15 2h.01"/><path d="M22 20h.01"/><path d="m22 2-2.24.75a2.9 2.9 0 0 0-1.96 3.12c.1.86-.57 1.63-1.45 1.63h-.38c-.86 0-1.6.6-1.76 1.44L14 10"/><path d="m22 13-.82-.33c-.86-.34-1.82.2-1.98 1.11c-.11.7-.72 1.22-1.43 1.22H17"/><path d="m11 2 .33.82c.34.86-.2 1.82-1.11 1.98C9.52 4.9 9 5.52 9 6.23V7"/><path d="M11 13c1.93 1.93 2.83 4.17 2 5-.83.83-3.07-.07-5-2-1.93-1.93-2.83-4.17-2-5 .83-.83 3.07.07 5 2Z"/></svg> **Well done: your browser called n8n, and n8n answered "Hello, Mina".** You built your first Webhook: an address
where n8n waits for a call. This is how a page, a form or another app starts a workflow. Your own page uses exactly
this in block 2.

<div class="fine">

**Stuck?** Import `n8n/ws2_10_hello_solution.json`. It gives you the finished workflow `WS2.10 - Hello - SOLUTION`. Publish yours or the solution, not both: they use the same address.

</div>

**Next: [Block 2 · Let Claude Code build your page →](/abp/ws2/s2-block-2/)**
