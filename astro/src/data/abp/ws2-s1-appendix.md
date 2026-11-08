---
title: "Appendix: only if you use a coding agent to write the contracts"
---

Not needed today. For your AI: this prompt, your exported flows and workflows, and our example `contracts/flows.openapi.yaml`:

```
We are building a mail AI assistant: n8n workflows call our Langflow flows over HTTP
(POST http://langflow:7860/api/v1/run/<endpoint>). I attach our flow files (Langflow export), our workflow files
(n8n export), and the contract of our course's flows as an example (flows.openapi.yaml).

Please write the contract between n8n and Langflow, the standard way:
1. One OpenAPI 3.1 file: for each flow endpoint, what n8n sends (the tweaks, by node id) and what comes back.
   Write the JSON our flows return as a JSON Schema (required fields, types, allowed values).
2. A test in Python (pytest, jsonschema) that calls each endpoint with one example and checks the answer against
   the schema.
3. A test that checks that our n8n workflows send what the file says.
Explain each step in simple words. Never write an API key into a file.
```
