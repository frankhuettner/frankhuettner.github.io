"""Test bench for a Langflow flow: runs every test case a few times, checks each answer, and shows the result on a
page with four tabs.

Two ways to use it, both with Python 3 alone (no packages to install):

  python3 test_bench.py                     a page on this laptop, http://localhost:8765: pick the flow (and, if you
                                            like, another model), click "Quick check" or "Full test", watch it
  python3 test_bench.py --run               a quick check without the page: the first 3 cases, once
  python3 test_bench.py --run --full        the full test without the page: every case, 3 runs (--runs); it writes
                                            report.html

A quick check shows in a minute that the bench reads your flow right; the full test gives the pass rate (Frank,
22 Nov 2026: "standardmäßig einen kurzen test fahren (den langen mit --full flag oder so ähnlich)"). Quick checks
appear in Results and Errors, not in All tests and Compare.
  python3 test_bench.py --report            only report.html again, from the tests stored in results/
  python3 test_bench.py --help              every option, with one sentence each

Above the tabs you pick the test, and the test to compare it with; with several flows or models, two filters narrow
both lists. Each tab shows what matters first; the rest opens with a click (a fold), and a click on a case opens its
window: the input, and every answer in every test.
  Run       the form: the flow, a model (optional), a name for the full test; Quick check or Full test (in
            report.html: how to start a test)
  Results   the test: the pass rate, one bar per run, how many cases were right in every run, every case as squares
            (one per run); all tests as bars, a click picks one. Folds: every case in a table; all tests in a table
  Compare   before and after: both numbers, what differs (the flow, the model, the prompt), better, worse, the same,
            the cases that changed. Folds: what changed in the prompt; both tests as squares; a confusion matrix each
  Errors    the cases to look at first, with "wrong every time: check the expected answer" and "runs disagree"; the
            most frequent mix-ups. Folds: all wrong cases; the cases whose runs disagree; the confusion matrix with
            the mix-ups; the share right by source. Across all tests: the cases wrong in every test
Click a column's title to sort a table, click again for the other order; type a word into Filter to see only the rows
with it (a case, a value, a word of the mail).

Each test case is one line of a CSV file (default: cases.csv next to this file):
  id            a number or a short name for the case
  input         what the flow gets, the text you would type into its Playground
  expected      with --field: the value the answer's field must have (Triage: --field action, expected reply);
                without --field: what must be in the answer, one or more short pieces of text separated by ";" (for
                example 6:15; works for me), big and small letters the same
  must_include  the older name of expected without --field (Frank, 22 Nov 2026: "fact ist komisch; expected scheint
                üblicher?!", then "ja"); still read
  subject       optional: a short title, shown in the report
  source        optional: who set the expected answer (a person, a real reply, a model)
  any other     goes to the flow's Text Input that feeds a field of that name (Draft Reply (Enron): as_of, the
                mail's date); every other Text Input gets input

An AI as judge (--judge, for free text, Frank, 22 Nov 2026: "mach noch eine optionale task mit dem judge"): every answer
goes to a judge flow, such as Judge Draft (Enron), with the input as mail, expected as reference and the answer as
draft. The judge gives a grade from 1 to 5 and says why; 4 or more counts as right. --judge-context replaces the
judge's setting (the Enron case) with your own. Each case then costs two calls. Use --field or --judge, not both.

A model (--model, or the field Model on the page) runs the same flow with another model for this test: the bench sends
it as a tweak to every model node of the flow (its field model_name), so the flow in Langflow stays as it is. Empty:
the model set in the flow.

Up to 8 calls run at the same time (--parallel; 1 for one after the other): a test mostly waits for the model, so
this makes it several times faster at the same cost. Seconds per call are measured with the others running.

Every call gets a new session_id, so no case sees another case's chat (Langflow 1.8 shares a session's memory, even
across flows: https://huettner.io/kingo-pod/upgrade/). Every answer is stored in results/, one JSON file per test,
with what was tested: the flow's name, when it was last changed, its model and temperature, and its prompt, with a
short prompt_id (so you know later which version of the flow a result belongs to), and the model the bench set.

The key: in your own terminal, the bench reads the Langflow key that ./kingo claude made (~/.config/kingo/langflow.key)
and talks to http://localhost:7860. Inside Claude Code's sandbox in kingo-pod, LANGFLOW_BASE_URL and LANGFLOW_API_KEY
are set instead, and the sandbox puts the real key into each request. The key never goes into the page.
"""
import argparse
import csv
import difflib
import gzip
import hashlib
import html
import json
import math
import os
import re
import statistics
import threading
import time
import urllib.error
import urllib.request
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

HERE = Path(__file__).resolve().parent
BASE = os.environ.get("LANGFLOW_BASE_URL", "http://localhost:7860").rstrip("/")


# ---------------------------------------------------------------- talking to Langflow

KEY_FILE = Path.home() / ".config" / "kingo" / "langflow.key"


def auth_headers():
    """x-api-key: inside Claude Code's sandbox the placeholder (the proxy puts in the real key); in your own terminal
    the key that ./kingo claude made for Claude Code. Since Langflow 1.5, /run needs an API key even with auto-login."""
    if os.environ.get("LANGFLOW_API_KEY"):
        return {"x-api-key": os.environ["LANGFLOW_API_KEY"]}
    if KEY_FILE.is_file():
        return {"x-api-key": KEY_FILE.read_text().strip()}
    raise SystemExit(f"No Langflow key: {KEY_FILE} is missing. Run ./kingo claude once in your kingo-pod folder; "
                     "it makes this key.")


def answer_text(reply):
    """The text of the flow's first output: outputs[0].outputs[0].results, as n8n reads it in WS2.1."""
    try:
        first = next(iter(reply["outputs"][0]["outputs"][0]["results"].values()))
        return first.get("text") if isinstance(first, dict) else str(first)
    except (KeyError, IndexError, StopIteration, TypeError, AttributeError):
        # the whole reply, but without its "inputs": they hold the test case's own input, where the check would find
        # the expected answer although the flow answered nothing (code review, 22 Nov 2026)
        def drop_inputs(x):
            if isinstance(x, dict):
                return {k: drop_inputs(v) for k, v in x.items() if k != "inputs"}
            return [drop_inputs(v) for v in x] if isinstance(x, list) else x
        return json.dumps(drop_inputs(reply))[:4000]


def call_flow(flow, text, headers, tweaks=None, timeout=300, input_type="any"):
    """One call; input_type "chat" when tweaks fill the Text Inputs ("any" would put the input into each of them)."""
    body = {"input_value": text, "input_type": input_type, "output_type": "any", "session_id": "test-" + uuid.uuid4().hex}
    if tweaks:   # for this call only, e.g. another model; the flow in Langflow stays as it is
        body["tweaks"] = tweaks
    body = json.dumps(body).encode()
    req = urllib.request.Request(f"{BASE}/api/v1/run/{flow}?stream=false", data=body, method="POST",
                                 headers={"Content-Type": "application/json", **headers})
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            reply = json.load(r)
        return answer_text(reply), None, time.monotonic() - t0
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read()[:300].decode(errors='replace')}", time.monotonic() - t0
    except Exception as e:  # timeouts, refused connections
        return None, f"{type(e).__name__}: {e}", time.monotonic() - t0


def get_json(path, headers, timeout=60):
    req = urllib.request.Request(BASE + path, headers={"Accept-Encoding": "identity", **headers})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def flow_snapshot(flow, headers):
    """What is tested: the flow as it is in Langflow when the test starts (read only). A test still runs without it."""
    try:
        heads = get_json("/api/v1/flows/?header_flows=true&get_all=true", headers)
        head = next(f for f in heads if flow in (f.get("endpoint_name"), f.get("id")))
        data = get_json(f"/api/v1/flows/{head['id']}", headers)
    except Exception as e:
        return {"flow": flow, "error": f"{type(e).__name__}: {e}"[:200]}
    models, prompts = {}, {}
    for n in data.get("data", {}).get("nodes", []):
        t = n.get("data", {}).get("node", {}).get("template", {}) or {}
        if isinstance(t.get("model_name"), dict) and t["model_name"].get("value"):
            models[n.get("id", "")] = {"model": t["model_name"]["value"], "temperature": (t.get("temperature") or {}).get("value")}
        for key in ("template", "system_prompt"):
            v = t.get(key)
            if isinstance(v, dict) and v.get("value") and (key == "system_prompt" or v.get("type") == "prompt"):
                prompts[n.get("id", "")] = v["value"]
    joined = "\n\n".join(f"[{k}]\n{v}" for k, v in sorted(prompts.items()))
    # the Text Inputs and the fields they feed (Draft Reply: one feeds mail, one as_of), from the flow's edges; ids
    # differ in each Langflow, so the bench reads them here
    texts = {n.get("id"): [] for n in data.get("data", {}).get("nodes", [])
             if (n.get("data", {}).get("type") or "") == "TextInput"}
    for e in data.get("data", {}).get("edges", []):
        f = ((e.get("data") or {}).get("targetHandle") or {}).get("fieldName")
        if e.get("source") in texts and f and f not in texts[e["source"]]:
            texts[e["source"]].append(f)
    return {"flow": data.get("name"), "id": data.get("id"), "endpoint": data.get("endpoint_name"),
            "updated_at": data.get("updated_at"), "models": models, "prompts": prompts,
            "prompt_id": hashlib.sha256(joined.encode()).hexdigest()[:6] if prompts else None, "text_inputs": texts}


KNOWN = {"id", "input", "expected", "must_include", "subject", "source"}


def input_tweaks(case, target):
    """A case's other columns (for example as_of) for the Text Inputs that feed a field of that name; every other Text
    Input gets the input. None when no column matches: then the input goes in as before."""
    ins = (target or {}).get("text_inputs") or {}
    extra = {k: v for k, v in case.items() if k and k not in KNOWN}
    mapped = {n: extra[f] for n, fields in ins.items() for f in fields if f in extra}
    if not mapped:
        return None
    return {n: {"input_value": mapped.get(n, case["input"])} for n in ins}


JUDGE_PASS = 4   # Judge Draft (Enron): a draft counts as right from grade 4
JUDGE_FIELDS = ("mail", "reference", "draft")


def judge_inputs(snap):
    """The judge's Text Inputs for mail, reference, draft (and context, if it has one); None if one is missing."""
    found = {f: n for n, fields in ((snap or {}).get("text_inputs") or {}).items() for f in fields
             if f in JUDGE_FIELDS + ("context",)}
    return found if all(f in found for f in JUDGE_FIELDS) else None


def judge_answer(judge, nodes, case, answer, headers, context=""):
    """(right?, grade, what it says, seconds): the judge flow compares the answer with expected."""
    tw = {nodes["mail"]: {"input_value": case["input"]}, nodes["reference"]: {"input_value": want_of(case, "")},
          nodes["draft"]: {"input_value": answer}}
    if context and "context" in nodes:
        tw[nodes["context"]] = {"input_value": context}
    text, error, seconds = call_flow(judge, "", headers, tw, input_type="chat")
    if error:
        return False, None, f"the judge failed: {error}"[:300], seconds
    try:
        g = json.loads(re.search(r"\{.*\}", text or "", re.S).group(0))
    except (AttributeError, ValueError):
        g = None
    grade = g.get("grade") if isinstance(g, dict) else None
    if not isinstance(grade, int) or isinstance(grade, bool):
        why = "; ".join(map(str, g.get("problems") or [])) if isinstance(g, dict) else str(text)[:200]
        return False, None, f"the judge gave no grade: {why}"[:300], seconds
    return grade >= JUDGE_PASS, grade, f"grade {grade}: {g.get('why') or ''}", seconds


# ---------------------------------------------------------------- checking an answer

def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def field_of(answer, field):
    """The field of a JSON answer; the answer may come inside ```json fences."""
    t = re.sub(r"^```(?:json)?|```$", "", str(answer or "").strip()).strip()
    try:
        v = json.loads(t)
    except ValueError:
        m = re.search(r"\{.*\}", t, re.S)
        v = json.loads(m.group(0)) if m else None
    return v.get(field) if isinstance(v, dict) else None


def check(case, answer, field):
    """(right?, what it got): with a field, the field must equal expected; else every part of expected (separated by
    ";") must be in the answer."""
    if answer is None:
        return False, "no answer"
    if field:
        if not str(case.get("expected") or "").strip():   # "" == "" would pass (code review, 23 Nov 2026)
            return False, "no expected answer in this case"
        try:
            got = field_of(answer, field)
        except ValueError:
            got = None
        return (got is not None and norm(got) == norm(case.get("expected"))), ("no " + field if got is None else str(got))
    parts = [f.strip() for f in str(want_of(case, "")).split(";") if f.strip()]
    if not parts:   # an empty expected would find "everything" (code review, 22 Nov 2026)
        return False, "no expected answer in this case"
    missing = [f for f in parts if norm(f) not in norm(answer)]
    return (not missing), ("all found" if not missing else "missing: " + "; ".join(missing))


# ---------------------------------------------------------------- one test: all cases, a few runs

STATE = {"running": False, "done": 0, "total": 0, "name": "", "error": ""}


QUICK = 3   # a quick check: the first 3 cases, once
PARALLEL = 8   # calls at the same time (Frank, 23 Nov 2026: "mach die parallelisierung; 8 als default"): a test waits
               # mostly for the model, so 8 at once take about as long as one; the cost is the same


def run_test(flow, cases, runs, field, name, cases_file, out_dir, model="", quick=False, judge="", judge_context="",
             parallel=PARALLEL):
    if quick:
        cases, runs = cases[:QUICK], 1
    if judge and field:
        STATE["error"] = "Use --field or --judge, not both."
        raise SystemExit(STATE["error"])
    try:
        headers = auth_headers()
    except SystemExit as e:
        STATE["error"] = str(e)
        raise
    target, tweaks = flow_snapshot(flow, headers), None
    if model:   # the same flow with another model: a tweak for each node that has a model
        nodes = list(target.get("models") or {})
        if not nodes:
            STATE["error"] = (f"The bench cannot set the model: it found no model in the flow {flow}"
                              + (f" ({target['error']})" if target.get("error") else "") + ". Leave Model empty.")
            raise SystemExit(STATE["error"])
        tweaks = {n: {"model_name": model} for n in nodes}
    nodes = None
    if judge:
        jt = flow_snapshot(judge, headers)
        nodes = judge_inputs(jt)
        if not nodes:
            STATE["error"] = (f"The bench cannot use the judge {judge}: it found no Text Inputs for mail, reference and "
                              "draft in it" + (f" ({jt['error']})" if jt.get("error") else "") + ".")
            raise SystemExit(STATE["error"])
    test = {"name": name, "flow": flow, "field": field, "cases_file": cases_file, "runs": runs,
            "started": datetime.now().isoformat(timespec="seconds"), "target": target, "results": []}
    if judge:
        test["judge"] = {"flow": judge, "pass": JUDGE_PASS, "target": jt, **({"context": judge_context} if judge_context else {})}
    extra = input_tweaks(cases[0], target) if cases else None
    if extra:   # which columns went to which Text Input
        test["inputs"] = sorted({k for c in cases[:1] for k in c if k and k not in KNOWN})
    if model:
        test.update(model=model, tweaks=tweaks)
    if quick:
        test["quick"] = True
    test["parallel"] = parallel = max(1, int(parallel or 1))
    STATE.update(running=True, done=0, total=runs * len(cases), name=name, error="")
    rows, lock = {}, threading.Lock()

    def one(run, i, case):   # one case in one run: the call, then the check or the judge
        ins = input_tweaks(case, target)
        answer, error, seconds = call_flow(flow, case["input"], headers, {**(tweaks or {}), **(ins or {})} or None,
                                           input_type="chat" if ins else "any")
        row = {"case": case["id"], "run": run, "answer": answer, "seconds": round(seconds, 1)}
        if nodes and answer is not None and want_of(case, "").strip():
            ok, grade, got, jsec = judge_answer(judge, nodes, case, answer, headers, judge_context)
            row.update(grade=grade, judge_seconds=round(jsec, 1))
            if grade is None:   # the judge failed or gave no grade: not the flow's fault (code review, 23 Nov 2026)
                row["judge_failed"] = True
        else:
            ok, got = check(case, answer, field)
        row.update(ok=ok, got=error or got)
        with lock:
            rows[(run, i)] = row
            STATE["done"] += 1

    pool = ThreadPoolExecutor(max_workers=parallel)
    try:   # run 1 first, then run 2 ...; up to `parallel` calls at once
        jobs = [pool.submit(one, run, i, case) for run in range(1, runs + 1) for i, case in enumerate(cases)]
        for job in jobs:
            job.result()   # an error in one call stops the test here
    finally:
        pool.shutdown(wait=False, cancel_futures=True)   # after Ctrl+C or an error: no new calls
        with lock:
            test["results"] = [rows[k] for k in sorted(rows)]   # in the order of the runs and the cases
        if len(test["results"]) < runs * len(cases):   # stopped (Ctrl+C or an error): not a whole test
            test["stopped"] = f'after {len(test["results"])} of {runs * len(cases)} answers'
        test["finished"] = datetime.now().isoformat(timespec="seconds")
        out_dir.mkdir(exist_ok=True)
        path = out_dir / f"{test['started'].replace(':', '-')}-{re.sub(r'[^A-Za-z0-9_-]+', '-', name)}.json"
        path.write_text(json.dumps(test, indent=1, ensure_ascii=False))
        STATE["running"] = False
    return test


def load_cases(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    # "Expected" or "expected " count as expected (code review, 22 Nov 2026)
    rows = [{(k or "").strip().lower(): v for k, v in r.items()} for r in rows]
    cols = set(rows[0]) if rows else set()
    if "input" not in cols or not cols & {"expected", "must_include"}:
        raise SystemExit(f"{path}: the test bench needs the columns id, input and expected. This file has: "
                         + (", ".join(sorted(c for c in cols if c)) or "no columns") + ".")
    cases = [r for r in rows if (r.get("input") or "").strip()]
    seen, empty = {}, []
    for i, c in enumerate(cases, 1):
        cid = (c.get("id") or "").strip() or str(i)
        if cid in seen:   # two cases with one id would merge into one (code review, 22 Nov 2026)
            old = cid
            while cid in seen:   # the new id must be free too (code review, 23 Nov 2026)
                seen[old] += 1
                cid = f"{old}-{seen[old]}"
            print(f"Note: two test cases have the id {old}. The second one is now {cid}.")
        seen.setdefault(cid, 1)
        c["id"] = cid
        if not str(want_of(c, "")).strip():
            empty.append(cid)
    if empty:
        print(f"Note: {len(empty)} test case(s) have no expected answer, so they count as wrong: " + ", ".join(empty))
    return cases


def load_tests(out_dir):
    """Every result file of this bench in out_dir. Other JSON files there (from another script) are left out."""
    tests = []
    for p in sorted(out_dir.glob("*.json")):
        try:
            t = json.loads(p.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(t, dict) and t.get("results") and isinstance(t["results"], list) and "name" in t and "runs" in t:
            tests.append(t)
    return tests


# ---------------------------------------------------------------- the page

CSS = """
body{font:15px/1.45 Pretendard,system-ui,sans-serif;color:#24303f;margin:0;background:#f6f8fa}
main{max-width:1020px;margin:0 auto;padding:22px 26px 60px}
h1{font-size:24px;color:#1F3864;margin:0 0 2px} h2{font-size:17px;color:#1F3864;margin:24px 0 8px}
h3{font-size:15px;color:#1F3864;margin:16px 0 6px}
.sub{color:#4b5563;margin:0 0 6px} .card{background:#fff;border:1px solid #e3e7ec;border-radius:14px;padding:16px 18px}
form{display:flex;gap:12px;align-items:end;flex-wrap:wrap} label{font-size:12px;font-weight:700;color:#4b5563;display:grid;gap:4px}
input,select{font:inherit;padding:7px 9px;border:1px solid #cfd6de;border-radius:8px;width:170px;background:#fff}
button{font:inherit;font-weight:800;background:#FF6C0F;color:#fff;border:0;border-radius:10px;padding:9px 18px;cursor:pointer}
button.second{background:#fff;color:#1F3864;box-shadow:inset 0 0 0 1.6px #1F3864}
.prog{height:12px;background:#e3e7ec;border-radius:99px;overflow:hidden;margin:8px 0} .prog i{display:block;height:100%;background:#2563eb}
.big{display:flex;gap:28px;align-items:center;flex-wrap:wrap} .rate{font-size:46px;font-weight:800;color:#124633;line-height:1}
.rate small{font-size:16px;color:#4b5563;font-weight:600;display:block;margin-top:6px}
.rate small.ci{color:#124633;font-weight:800}
.verdict{border-radius:12px;padding:10px 14px;font-size:14.5px;margin:10px 0} .verdict b{font-size:16px}
.verdict.up{background:#e3f1e8;color:#124633} .verdict.down{background:#fde8e1;color:#8f1d12}
.verdict.none{background:#eef1f4;color:#24303f} ul.how{margin:6px 0;padding-left:1.1em;font-size:13.5px}
.bars{display:grid;gap:6px;min-width:300px} .bar{display:grid;grid-template-columns:56px 1fr 52px;gap:8px;align-items:center;font-size:13px}
.bar span{height:16px;background:#e3e7ec;border-radius:5px;overflow:hidden} .bar span i{display:block;height:100%;background:#124633}
table{border-collapse:collapse;width:100%;background:#fff;border-radius:12px;overflow:hidden}
th,td{padding:7px 9px;border-bottom:1px solid #eef1f4;text-align:left;vertical-align:top;font-size:13.5px} th{background:#f2f5fa;color:#1F3864}
td.c{text-align:center;width:118px} .ok,.no{display:inline-block;min-width:96px;border-radius:7px;padding:3px 6px;font-weight:700;font-size:12.5px}
.ok{background:#e3f1e8;color:#124633} .no{background:#fde8e1;color:#b42318}
details summary{cursor:pointer;list-style:none} details summary::-webkit-details-marker{display:none}
pre{white-space:pre-wrap;font-size:12px;background:#f6f8fa;border-radius:8px;padding:8px;text-align:left;margin:4px 0}
.muted{color:#4b5563;font-size:13px}
.chips{display:flex;gap:3px;flex-wrap:wrap} .chips span{min-width:0;padding:2px 5px} td.c .chips{justify-content:center}
.mix td{text-align:center} .mix td:first-child{text-align:left}
.flag{display:inline-block;margin:3px 4px 0 0;font-size:12px;font-weight:700;color:#7a5400;background:#fff4d6;border-radius:6px;padding:1px 6px}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:10px 0}
.four div{border-radius:12px;padding:10px 12px;font-size:13.5px} .four b{display:block;font-size:26px;line-height:1.1}
.g{background:#e3f1e8;color:#124633} .r{background:#fde8e1;color:#b42318} .x{background:#eef1f4;color:#24303f}
.y{background:#fff4d6;color:#7a5400}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px} .two .card h3{margin:0 0 4px;color:#1F3864;font-size:15px}
pre.diff{font-size:12px;background:#0f1b2d;color:#e6edf6;border-radius:10px;padding:10px 12px}
pre.diff .add{color:#86efac} pre.diff .del{color:#fca5a5} pre.diff .sep{color:#94a3b8}
pre.cmd{background:#0f1b2d;color:#e6edf6;border-radius:10px;padding:10px 12px;font-size:13px}
nav.tabs{display:flex;gap:6px;margin:12px 0 0;border-bottom:2px solid #dfe5ec}
nav.tabs a{padding:9px 18px;font-weight:800;color:#4b5563;text-decoration:none;border-radius:10px 10px 0 0}
nav.tabs a:hover{background:#eef2f7}
.tab{display:none;scroll-margin-top:12px} .tab:target{display:block}
main:not(:has(.tab:target)) .tab.default{display:block}
main:not(:has(.tab:target)) nav.tabs a.default,main:has(#run:target) a[href="#run"],
main:has(#results:target) a[href="#results"],main:has(#compare:target) a[href="#compare"],
main:has(#errors:target) a[href="#errors"],main:has(#tests:target) a[href="#tests"]{background:#1F3864;color:#fff}
nav.tabs .grp{align-self:center;margin-left:14px;padding-left:12px;border-left:1px solid #cfd6de;font-size:11px;font-weight:800;
letter-spacing:.06em;text-transform:uppercase;color:#4b5563}
.tl{background:#fff;border:1px solid #e3e7ec;border-radius:14px;padding:8px}
.tl .lg{display:flex;gap:18px;font-size:12px;color:#4b5563;padding:4px 8px 8px}
.tl .lg i{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-2px;margin-right:5px}
.tl .tr{display:grid;grid-template-columns:290px 1fr;gap:14px;align-items:center;padding:6px 8px;border-radius:8px;cursor:pointer}
.tl .tr:hover{background:#f2f5fa} .tl .nm b{display:block;font-size:13.5px} .tl .nm span{font-size:12px;color:#4b5563}
.tl .bb{display:flex;align-items:center;gap:8px;margin:2px 0}
.tl .trk{flex:1;max-width:520px;height:12px;border-right:1px solid #e3e7ec;background:linear-gradient(to right,#e3e7ec 1px,transparent 1px) 0 0/50% 100%}
.tl .trk span{display:block;height:12px;border-radius:0 4px 4px 0} .tl .b1{background:#3b5bdb} .tl .b2{background:#0f9f8f}
.tl .trk{position:relative} .tl .trk .ci{position:absolute;top:1px;height:10px;box-sizing:border-box;border-left:2px solid #111827;
border-right:2px solid #111827;background:linear-gradient(#111827,#111827) center/100% 2px no-repeat}
.tl .lg i.cil{width:18px;height:10px;box-sizing:border-box;border-left:2px solid #111827;border-right:2px solid #111827;border-radius:0;
background:linear-gradient(#111827,#111827) center/100% 2px no-repeat}
.tl .bb em{font-style:normal;font-weight:700;font-size:12px;width:44px}
.q{display:inline-block;width:18px;height:18px;line-height:18px;border-radius:4px;vertical-align:middle;text-align:center;
font-size:12px;font-weight:800;color:#fff}
.q3{background:#15803d} .q2{background:#7cc49a} .q1{background:#f8c3b3;box-shadow:inset 0 0 0 1.5px #d03b3b}
.q0{background:#d03b3b} .qn{background:#fff;box-shadow:inset 0 0 0 1.5px #cfd6de}
table.grid td.qc{text-align:center;width:64px} [data-go]{cursor:pointer} tr[data-go]:hover td{background:#f7f9fc}
.pick{display:flex;gap:14px;align-items:end;flex-wrap:wrap;background:#eef2f7;border-radius:12px;padding:10px 12px;margin:10px 0 4px}
.pick select{width:auto;max-width:440px} .pick .only{display:flex;gap:10px;padding-right:14px;border-right:1px solid #cfd6de}
.view:not(.on){display:none}
details.fold{border:1px solid #e3e7ec;border-radius:12px;background:#fff;margin:10px 0}
details.fold>summary{padding:10px 14px;font-weight:800;color:#1F3864}
details.fold>summary::before{content:"\\25B8  "} details.fold[open]>summary::before{content:"\\25BE  "}
details.fold>summary span{font-weight:400;color:#4b5563} details.fold>div{padding:0 14px 14px}
tr[data-case]{cursor:pointer} tr[data-case]:hover td{background:#f7f9fc}
table.lines td{vertical-align:middle}
.chart{display:block;max-width:100%;height:auto;margin:8px 0 6px} .chart .lab{font-size:12px;fill:#4b5563}
.chart .name{font-size:13px;font-weight:700;fill:#24303f} .chart .val{font-size:12px;font-weight:700;fill:#24303f}
.chart [data-case]{cursor:pointer} .chart [data-case]:hover{opacity:.7}
.chart .k{fill:#15803d} .chart .w{fill:#fde8e1;stroke:#d03b3b;stroke-width:1.5} .chart .m{fill:#fff;stroke:#cfd6de;stroke-width:1.5}
.chart g[data-t]{cursor:pointer} .chart g[data-t] .bg{fill:transparent} .chart g[data-t]:hover .bg{fill:#f2f5fa}
.chart g[data-t].sel .bg{fill:#fff4d6}
th.sorter{cursor:pointer;user-select:none} th.sorter:hover{background:#e6ecf5}
th[data-dir="asc"]::after{content:" \\25B2";font-size:10px} th[data-dir="desc"]::after{content:" \\25BC";font-size:10px}
.tools{display:flex;gap:10px;align-items:center;margin:0 0 8px} input.find{width:360px}
.mxs{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start} .mxs .card{padding:12px 14px} .mxs h3{margin:0;font-size:15px;color:#1F3864}
table.matrix{width:auto;margin-top:8px;border-radius:0} table.matrix th,table.matrix td{text-align:center;padding:6px 10px;font-size:13px;border:2px solid #fff}
table.matrix td{font-weight:700;min-width:34px} table.matrix td.z{color:#6b7480;font-weight:400} table.matrix th.e{text-align:right}
table.matrix td.rt{background:#fff;color:#24303f;font-weight:400}
.overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(15,27,45,.45);z-index:10;overflow:auto;padding:36px 16px}
.overlay.on{display:block}
.sheet{max-width:880px;margin:0 auto;background:#fff;border-radius:16px;padding:18px 22px 22px;box-shadow:0 10px 40px rgba(0,0,0,.25)}
.sheet .close{float:right;background:#1F3864;padding:6px 14px}
.case{display:none} .case.on{display:block} .case h2{margin-top:0}
pre.mail{max-height:280px;overflow:auto} pre.exp{border-left:4px solid #1e7a4a}
h3 .muted{font-weight:400;font-size:13px;margin-left:6px}
.ct{display:grid;grid-template-columns:200px 1fr;gap:10px;padding:8px 0;border-bottom:1px solid #eef1f4}
.ct details>summary{color:#1F3864;font-weight:700;font-size:13px;margin-top:4px}
"""

# Sorting and filtering the tables, the choice of the tests, and the window of a case: a few lines of JavaScript in
# the page, no internet. Texts from the tests are only read and set as text (textContent), never as HTML.
JS = """
(function () {
  var $ = function (id) { return document.getElementById(id); };
  var each = function (sel, f) { [].forEach.call(document.querySelectorAll(sel), f); };
  each('table.sort', function (tb) {
    var head = tb.rows[0], body = head.parentNode, data = function () { return [].slice.call(tb.rows, 1); };
    if (tb.classList.contains('filter')) {
      var box = document.createElement('input'), info = document.createElement('span'), bar = document.createElement('div');
      box.type = 'search'; box.className = 'find'; box.placeholder = 'Filter: type a word, for example a case or a value';
      info.className = 'muted'; bar.className = 'tools'; bar.appendChild(box); bar.appendChild(info);
      tb.parentNode.insertBefore(bar, tb);
      box.addEventListener('input', function () {
        var q = box.value.trim().toLowerCase(), shown = 0, rows = data();
        rows.forEach(function (r) {
          var hit = !q || r.textContent.toLowerCase().indexOf(q) >= 0;
          r.style.display = hit ? '' : 'none'; if (hit) shown++;
        });
        info.textContent = q ? shown + ' of ' + rows.length + ' rows' : '';
      });
    }
    [].forEach.call(head.cells, function (th, i) {
      th.classList.add('sorter'); th.title = 'Click to sort; click again for the other order';
      th.addEventListener('click', function () {
        var dir = th.getAttribute('data-dir') === 'asc' ? 'desc' : 'asc';
        [].forEach.call(head.cells, function (h) { h.removeAttribute('data-dir'); });
        th.setAttribute('data-dir', dir);
        var key = function (r) {
          var c = r.cells[i]; if (!c) return '';
          var v = c.hasAttribute('data-v') ? c.getAttribute('data-v') : c.textContent.trim();
          return /^-?[0-9]/.test(v) ? parseFloat(v) : v.toLowerCase();
        };
        data().sort(function (a, b) {
          var x = key(a), y = key(b);
          var d = (typeof x === 'number' && typeof y === 'number') ? x - y : String(x).localeCompare(String(y), undefined, {numeric: true});
          return dir === 'asc' ? d : -d;
        }).forEach(function (r) { body.appendChild(r); });
      });
    });
  });

  function setTest(k) {
    each('select.p-test', function (x) { x.value = k; });
    each('.view[data-t]', function (v) { v.classList.toggle('on', v.getAttribute('data-t') === k); });
  }
  function showPair() {
    var b = $('p-before'), a = $('p-after'), hit = false; if (!b || !a) return;
    each('.view[data-pair]', function (v) {
      var on = v.getAttribute('data-pair') === b.value + '|' + a.value; v.classList.toggle('on', on); if (on) hit = true;
    });
    each('.view[data-none]', function (v) { v.classList.toggle('on', !hit); });
  }
  function showTests() {
    var f = $('f-flow'), m = $('f-model'), k = (f ? f.value : '') + '|' + (m ? m.value : '');
    each('.view[data-f]', function (v) { v.classList.toggle('on', v.getAttribute('data-f') === k); });
  }
  each('select.p-test', function (x) { x.addEventListener('change', function () { setTest(x.value); }); });
  ['p-before', 'p-after'].forEach(function (id) { if ($(id)) $(id).addEventListener('change', showPair); });
  ['f-flow', 'f-model'].forEach(function (id) { if ($(id)) $(id).addEventListener('change', showTests); });
  var first = document.querySelector('select.p-test');   // a browser may keep a choice over a reload
  if (first) setTest(first.value);
  showPair(); showTests();

  var ov = $('case');
  function openCase(id) {
    var hit = false;
    each('#case .case', function (c) { var on = c.getAttribute('data-c') === id; c.classList.toggle('on', on); if (on) hit = true; });
    if (hit) { ov.classList.add('on'); ov.scrollTop = 0; }
  }
  document.addEventListener('click', function (e) {
    var el = e.target; if (!el || !el.closest) return;
    if (ov && (el === ov || el.closest('.close'))) { ov.classList.remove('on'); return; }
    if (el.closest('#case')) return;
    var c = el.closest('[data-case]'); if (c && ov) { openCase(c.getAttribute('data-case')); return; }
    var g = el.closest('[data-go]'); if (g) { setTest(g.getAttribute('data-go')); location.hash = '#results'; }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && ov) ov.classList.remove('on'); });
})();
"""

# ---------------------------------------------------------------- pictures: inline SVG, no packages

GOOD, BAD, WRONG_FILL = "#15803d", "#d03b3b", "#fde8e1"  # right: a filled green square; wrong: light red with a red
#                                                         edge, so the two differ in lightness too, not only in colour
SERIES = ("#3b5bdb", "#0f9f8f")   # the bars of all tests: the pass rate, right in all runs (two colours that people
#                                   with colour blindness can tell apart, checked with a palette validator)
GREENS = ("#e3f1e8", "#b9dfc6", "#7cc49a", "#1e7a4a")   # the matrix, right answers: few (light) to many (dark)
REDS = ("#fde8e1", "#f8c3b3", "#f0957c", "#b42318")     # the matrix, wrong answers
COMPARE_LAST = 12   # Compare has a view for every pair of the last 12 tests on these test cases, and of the two named
#                    with --compare (22 Nov 2026: with 12 tests, Compare offered tests it had no view for and showed nothing)


def pct(a, b):
    return f"{round(100 * a / b)} %" if b else "–"


# The 95 % confidence interval (Frank, 22 Nov 2026: "1. ja", to the question whether the bench should show it; the
# word: "confidence instead of certainty? also, 95% confidence interval?"). As in Anthropic,
# "A statistical approach to model evaluations" (19 Nov 2024): each case counts once (its runs are not independent, so
# they are averaged), and two tests are compared case by case (paired differences).
Z95 = 1.96
T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
       12: 2.179, 15: 2.131, 20: 2.086, 25: 2.060, 30: 2.042, 40: 2.021, 60: 2.000, 120: 1.980}   # t, 97.5 %


def shares(t):
    """Each case's share of right answers over its runs."""
    return {cid: sum(r["ok"] for r in rs) / len(rs) for cid, rs in by_case(t).items()}


def rate_range(t):
    """(low, high): the 95 % confidence interval of the pass rate, the Wilson interval over the cases (it also works at 0 and 100 %,
    where 5 of 5 still leaves room below); None without cases."""
    s = list(shares(t).values())
    n = len(s)
    if not n:
        return None
    p, z2 = sum(s) / n, Z95 * Z95
    centre = (p + z2 / (2 * n)) / (1 + z2 / n)
    half = Z95 * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / (1 + z2 / n)
    return max(0.0, centre - half), min(1.0, centre + half)


def change_range(a, b):
    """(change, low, high) from a to b, as shares: the mean of the differences case by case over the cases of both,
    with the t distribution; None with fewer than 2 such cases."""
    sa, sb = shares(a), shares(b)
    d = [sb[cid] - sa[cid] for cid in sa if cid in sb]
    if len(d) < 2:
        return None
    m = sum(d) / len(d)
    half = T95[max(k for k in T95 if k <= len(d) - 1)] * statistics.stdev(d) / math.sqrt(len(d))
    return m, max(-1.0, m - half), min(1.0, m + half)


def points(x):
    return f"{100 * x:+.1f}".replace("-", "−") + " points"


def range_txt(r):
    return f"{round(100 * r[0])}–{round(100 * r[1])} %"


RANGE_HOW = (
    '<ul class="how"><li>Each test case counts once: its runs are averaged, because the runs of one case are not '
    'independent of each other.</li>'
    '<li>The pass rate: the Wilson interval over the test cases.</li>'
    '<li>The change between two tests: the difference case by case, with the t distribution.</li>'
    '<li>It holds for mails like your test cases. More test cases make the interval narrower; more runs help less.</li></ul>'
    '<p class="muted">Source: Anthropic, <a href="https://www.anthropic.com/research/statistical-approach-to-model-evals" '
    'target="_blank" rel="noopener">A statistical approach to model evaluations</a> ↗ (19 Nov 2024).</p>')


def esc(s):
    return html.escape(str(s))


def by_case(t):
    """Each case's answers in a test, in the order of the runs."""
    out = {}
    for r in sorted(t["results"], key=lambda r: r["run"]):
        out.setdefault(r["case"], []).append(r)
    return out


def right_in_all(t):
    """(cases right in every run, cases)."""
    cases = by_case(t)
    return sum(all(r["ok"] for r in rs) for rs in cases.values()), len(cases)


def flow_label(t):
    """The flow a test ran on: its name in Langflow and the name in its address, Triage (Enron) - SOLUTION
    (enron-triage-solution); tests from before 22 Nov 2026 only know the address."""
    name = (t.get("target") or {}).get("flow")
    return f'{name} ({t["flow"]})' if name and name != t["flow"] else t["flow"]


def flow_models(t):
    return sorted({m["model"] for m in ((t.get("target") or {}).get("models") or {}).values() if m.get("model")})


def model_of(t):
    """The model a test ran with: the one the bench set (--model), else the flow's own, else what the test says."""
    return t.get("model") or ", ".join(flow_models(t)) or t.get("label") or "model not recorded"


def when(t):
    try:
        return datetime.fromisoformat(t["started"]).strftime("%d %b %H:%M")
    except ValueError:
        return t["started"]


def test_label(t):
    return f'{t["name"]} · {when(t)} · {model_of(t)}'


def prompt_of(t):
    """A short id of the prompt: from the flow's snapshot, or from how a simulated test was made (models/run_triage.py)."""
    tg, m = t.get("target") or {}, t.get("method") or {}
    return tg.get("prompt_id") or (m.get("prompt_sha256") or "")[:6] or None


def version_of(t):
    """What was tested, in one line: the flow, the model and its temperature, prompt_id, the flow's last change."""
    tg = t.get("target") or {}
    parts = [flow_label(t)]
    if t.get("model"):
        own = ", ".join(flow_models(t))
        parts.append(f'{t["model"]}, set by the bench' + (f' (the flow’s own: {own})' if own else ""))
    if not tg:
        parts.append(f'{t["label"]}' if t.get("label") else "flow not recorded (a test from before 22 Nov 2026)")
        m = t.get("method") or {}
        if m.get("prompt"):
            parts.append(f'prompt {Path(m["prompt"]).stem} {prompt_of(t)}')
        return " · ".join(parts)
    if tg.get("error"):
        return " · ".join(parts + ["not read from Langflow"])
    if not t.get("model"):
        parts += sorted({m["model"] + (f', temperature {m["temperature"]}' if m.get("temperature") is not None else "")
                         for m in (tg.get("models") or {}).values()})
    if tg.get("prompt_id"):
        parts.append(f'prompt {tg["prompt_id"]}')
    if tg.get("updated_at"):
        parts.append(f'flow changed {str(tg["updated_at"])[:16].replace("T", " ")}')
    j = t.get("judge")
    if j:
        jm = sorted({m["model"] for m in ((j.get("target") or {}).get("models") or {}).values()})
        parts.append(f'judged by {j["flow"]}' + (f' ({", ".join(jm)})' if jm else ""))
    return " · ".join(parts)


def chip(r):
    label = f'grade {r["grade"]}' if r.get("grade") is not None else str(r["got"])[:14]
    return f'<span class="{"ok" if r["ok"] else "no"}">{esc(label)}</span>'


def chips(rs):
    return f'<span class="chips">{"".join(chip(r) for r in rs) or "–"}</span>'


def fold(title, note, body, open_=False):
    """Level 2: a section that opens with a click; its title says what is in it."""
    n = f' <span>· {esc(note)}</span>' if note else ""
    return f'<details class="fold"{" open" if open_ else ""}><summary>{esc(title)}{n}</summary><div>{body}</div></details>'


def view(attr, key, on, body):
    return f'<div class="view{" on" if on else ""}" {attr}="{esc(key)}">{body}</div>'


def squares_svg(ids, bands, title_of, changed=None):
    """Every case, every run: one column per case, one square per run, right filled green, wrong light red.
    bands: [(name, answers by case, runs)], one above the other in each column (Compare: the first test above the
    second). changed: {case id: "better" or "worse"}, marked under the column. A click opens the case."""
    changed = changed or {}
    n = len(ids)
    s, colgap = (22, 16) if n <= 12 else (14, 6) if n <= 40 else (9, 3)
    g = 3 if s > 9 else 2
    pitch, two = s + colgap, len(bands) > 1
    left = 124 if two else 50
    cols = max(1, (900 - left) // pitch)
    labels = n <= 40 and all(len(str(c)) <= 4 for c in ids)
    heights = [k * s + (k - 1) * g for _, _, k in bands]
    body_h = sum(heights) + 10 * (len(bands) - 1)
    line_h = body_h + (17 if labels else 0) + (14 if changed else 0) + 14
    top = 32
    out = [f'<rect x="0" y="4" width="12" height="12" rx="2.5" fill="{GOOD}"/><text x="18" y="15" class="lab">right</text>'
           f'<rect x="70.75" y="4.75" width="10.5" height="10.5" rx="2" fill="{WRONG_FILL}" stroke="{BAD}" stroke-width="1.5"/>'
           f'<text x="88" y="15" class="lab">wrong</text>']
    x = 145
    if changed:
        out.append(f'<path d="M{x},16 l6,-11 l6,11 z" fill="{GOOD}"/><text x="{x + 18}" y="15" class="lab">better</text>'
                   f'<path d="M{x + 78},5 l6,11 l6,-11 z" fill="{BAD}"/><text x="{x + 96}" y="15" class="lab">worse</text>')
        x += 160
    out.append(f'<text x="{x}" y="15" class="lab">· one column per case, one square per run · click a square to open the case</text>')
    lines = (n + cols - 1) // cols
    for line in range(lines):
        y0, off = top + line * line_h, 0
        for (name, _, runs), h in zip(bands, heights):
            if two:
                out.append(f'<text x="{left - 10}" y="{y0 + off + h / 2 + 4:.1f}" text-anchor="end" class="name">'
                           f'{esc(name[:16])}</text>')
            else:
                for k in range(1, runs + 1):
                    out.append(f'<text x="{left - 8}" y="{y0 + off + (k - 1) * (s + g) + s / 2 + 4:.1f}" '
                               f'text-anchor="end" class="lab">run {k}</text>')
            off += h + 10
    for i, cid in enumerate(ids):
        line, col = divmod(i, cols)
        x, y = left + col * pitch, top + line * line_h
        for (name, bc, runs), h in zip(bands, heights):
            rs = {r["run"]: r for r in bc.get(cid, [])}
            for k in range(1, runs + 1):
                r, yy = rs.get(k), y + (k - 1) * (s + g)
                if r is None:
                    out.append(f'<rect x="{x + .75}" y="{yy + .75}" width="{s - 1.5}" height="{s - 1.5}" rx="2" class="m"/>')
                    continue
                what = ("right" if r["ok"] else "wrong") + f': {str(r["got"])[:30]}'
                tip = (f'ID {cid} · {name[:20]} · run {k} · {what}' if two else
                       f'ID {cid} · {title_of(cid)[:50]} · run {k} · {what}')
                look = (f'x="{x}" y="{yy}" width="{s}" height="{s}" rx="2.5" class="k"' if r["ok"] else
                        f'x="{x + .75}" y="{yy + .75}" width="{s - 1.5}" height="{s - 1.5}" rx="2" class="w"')
                out.append(f'<rect {look} data-case="{esc(cid)}"><title>{esc(tip)}</title></rect>')
            y += h + 10
        y = top + line * line_h + body_h
        if labels:
            out.append(f'<text x="{x + s / 2}" y="{y + 14}" text-anchor="middle" class="lab">{esc(cid)}</text>')
            y += 17
        if cid in changed:
            mx = x + s / 2
            out.append(f'<path d="M{mx - 6},{y + 12} l6,-11 l6,11 z" fill="{GOOD}"><title>ID {esc(cid)}: better</title></path>'
                       if changed[cid] == "better" else
                       f'<path d="M{mx - 6},{y + 1} l6,11 l6,-11 z" fill="{BAD}"><title>ID {esc(cid)}: worse</title></path>')
    w = max(left + min(n, cols) * pitch, 640 if changed else 520)
    h = top + lines * line_h
    return (f'<svg class="chart" width="{w}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="Every case, every run: green right, red wrong">{"".join(out)}</svg>')


def answered(r):
    """What the flow answered, for the confusion matrix: the field's value, or no answer (an error, a timeout)."""
    return "no answer" if r.get("answer") is None else (norm(r.get("got")) or "empty")


def matrix_axes(tests, cases):
    """The same rows and columns for every matrix: the rows are the expected answers, most frequent first; the
    columns are those, then the other answers (more than 9 columns: the rarest fold into other)."""
    exp = {c["id"]: norm(c.get("expected")) for c in cases}
    rows = [k for k, _ in Counter(exp[r["case"]] for t in tests for r in t["results"] if r["case"] in exp).most_common()]
    extra = [k for k, _ in Counter(answered(r) for t in tests for r in t["results"]).most_common() if k not in rows]
    if len(rows) + len(extra) > 9:
        extra = extra[:max(0, 8 - len(rows))] + ["other"]
    return rows, rows + extra


def matrix_html(t, cases, axes):
    """A confusion matrix: one row per expected answer, one column per answer of the flow, the number of answers in
    each cell; right on the diagonal (green), wrong elsewhere (red); darker means more often."""
    rows, cols = axes
    exp = {c["id"]: norm(c.get("expected")) for c in cases}
    count = Counter()
    for r in t["results"]:
        a = answered(r)
        count[(exp.get(r["case"], ""), a if a in cols else "other")] += 1
    top = max(count.values(), default=1)

    def cell(e, a):
        k = count.get((e, a), 0)
        if not k:
            return '<td class="z">·</td>'
        ramp = GREENS if e == a else REDS
        step = min(3, max(0, -(-4 * k // top) - 1))
        ink = "#fff" if step == 3 else "#24303f"
        tip = f'expected {e}, the flow answered {a}: {k} answers' + (" (right)" if e == a else " (wrong)")
        return f'<td style="background:{ramp[step]};color:{ink}" title="{esc(tip)}">{k}</td>'

    body = "".join(
        f'<tr><th class="e">{esc(e)}</th>{"".join(cell(e, a) for a in cols)}'
        f'<td class="rt">{pct(count.get((e, e), 0), sum(count.get((e, a), 0) for a in cols))}</td></tr>' for e in rows)
    return (f'<div class="card"><h3>{esc(t["name"])}</h3><div class="muted">{esc(model_of(t))} · {esc(when(t))}</div>'
            f'<table class="matrix"><tr><th></th><th colspan="{len(cols)}">the flow answered</th><th></th></tr>'
            '<tr><th class="e">expected</th>' + "".join(f'<th>{esc(a)}</th>' for a in cols) +
            f'<th>right</th></tr>{body}</table></div>')


def matrices(tests, cases, axes, beside=""):
    """The confusion matrices of these tests side by side, with one explanation, and beside them what is given
    (Errors: the most frequent mix-ups); only for tests with --field."""
    tests = [t for t in tests if t.get("field")]
    if not tests:
        return ""
    return ('<p class="muted">One row per expected answer, one column per answer of the flow; each cell counts the '
            'answers. Green, on the diagonal: right. Red: wrong. Darker: more often. Last column: the share right.</p>'
            '<div class="mxs">' + "".join(matrix_html(t, cases, axes) for t in tests) + beside + '</div>')


# ---------------------------------------------------------------- the tabs: level 1 first, level 2 in folds

def want_of(c, field):
    return str(c.get("expected") if field else (c.get("expected") or c.get("must_include")) or "")


def short(s, n=90):
    """A long expected answer (with a judge: a whole reply) in one table cell."""
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n - 1] + "…"


def failed_note(res):
    """A warning when calls failed: Langflow gave no answer (an HTTP error, a timeout). They count as wrong, so the pass
    rate is too low (code review, 22 Nov 2026)."""
    failed = [r for r in res if r.get("answer") is None]
    judged = [r for r in res if r.get("judge_failed")]
    out = ""
    if judged:
        out += (f'<div class="card" style="border-color:#f3b8a8;margin-top:12px"><b>{len(judged)} of {len(res)} answers '
                f'got no grade from the judge,</b> for example: {esc(str(judged[0].get("got", ""))[:120])}. They count as '
                'wrong, so this pass rate is too low. Check that the judge flow runs, then run the test again.</div>')
    if not failed:
        return out
    return (f'<div class="card" style="border-color:#f3b8a8;margin-top:12px"><b>{len(failed)} of {len(res)} calls failed:'
            f'</b> Langflow gave no answer, for example {esc(str(failed[0].get("got", ""))[:120])}. They count as wrong, so '
            'this pass rate is too low. Check that Langflow runs and that your laptop stays awake, then run the test '
            'again.</div>') + out


def render_results(t, cases):
    """Results, one test. Level 1: the numbers and every case as squares. Level 2: the table of every case."""
    res, runs = t["results"], t["runs"]
    right = sum(r["ok"] for r in res)
    secs = [r["seconds"] for r in res]
    bars = "".join(
        f'<div class="bar"><b>run {k}</b><span><i style="width:{100 * sum(r["ok"] for r in rr) / max(len(rr), 1):.0f}%"></i></span>'
        f'{sum(r["ok"] for r in rr)} of {len(rr)}</div>'
        for k, rr in enumerate([[r for r in res if r["run"] == k] for k in range(1, runs + 1)], 1))
    info = {c["id"]: c for c in cases}
    title = lambda cid: str(info.get(cid, {}).get("subject") or info.get(cid, {}).get("input", "")[:60])
    bc = by_case(t)
    every, n = right_in_all(t)
    every_txt = f'<b>{every} of {n}</b> cases right in all {runs} runs<br/>' if runs > 1 else ""
    rng = rate_range(t) or (0.0, 0.0)
    rows = "".join(
        f'<tr data-case="{esc(cid)}"><td><b>{esc(cid)}</b> {esc(title(cid))}</td><td>{esc(short(want_of(info.get(cid, {}), t.get("field"))))}</td>'
        + "".join((f'<td class="c" data-v="{int(r["ok"])}">{chip(r)}</td>' if r else '<td class="c muted" data-v="-1">–</td>')
                  for r in [next((x for x in rs if x["run"] == k), None) for k in range(1, runs + 1)]) + '</tr>'
        for cid, rs in bc.items())
    j = t.get("judge") or {}
    check_txt = (f'the judge flow {j["flow"]} gives a grade of {j.get("pass", JUDGE_PASS)} or more (from 1 to 5) when it '
                 'compares the answer with expected' if j else
                 f'the field {t["field"]} equals expected' if t.get("field") else "the answer contains every piece of expected")
    table = (f'<p class="muted">Right when {esc(check_txt)}. Click a case to open it: its input and every answer.</p>'
             f'<table class="sort filter"><tr><th>Case</th><th>Expected</th>'
             + "".join(f"<th>run {k}</th>" for k in range(1, runs + 1)) + f'</tr>{rows}</table>')
    return (f'<h2>{esc(t["name"])} · {esc(model_of(t))} · {esc(when(t))}</h2><p class="muted">Tested: {esc(version_of(t))}</p>'
            f'<div class="card"><div class="big">'
            f'<div class="rate">{pct(right, len(res))}<small>{right} of {len(res)} answers right · {n} cases × {runs} runs</small>'
            + (f'<small class="ci">A quick check: {n} cases, once. Your pass rate comes from the full test.</small></div>'
               if t.get("quick") else f'<small class="ci">Stopped {esc(t["stopped"])}: not in All tests and Compare.</small></div>'
            if t.get("stopped") else f'<small class="ci">95 % confidence interval: {range_txt(rng)}</small></div>')
            + f'<div class="bars">{bars}</div>'
            f'<div class="muted">{every_txt}median {statistics.median(secs) if secs else 0:.1f} s per call<br/>'
            f'slowest {max(secs) if secs else 0:.1f} s</div></div></div>'
            + failed_note(res)
            + '<h2>Every case, every run</h2>'
            + squares_svg(list(bc), [("", bc, runs)], title)
            + fold("Every case in a table", f"{n} cases", table)
            + ("" if t.get("quick") else fold(
                "What the 95 % confidence interval means", f"{range_txt(rng)} on {n} cases",
                f'<p>With 95 % confidence, the pass rate of this flow on mails like your {n} test cases lies between '
                f'{round(100 * rng[0])} and {round(100 * rng[1])} %.</p>' + RANGE_HOW)))


def pick_pair(tests, names=None):
    """The two tests to compare: the newest test of each name given, else the last two tests with different names."""
    newest = {}
    for t in tests:
        newest[t["name"]] = t   # tests come sorted by time
    if names and all(n in newest for n in names) and names[0] != names[1]:
        return newest[names[0]], newest[names[1]]
    order = sorted(newest.values(), key=lambda t: t["started"])
    return (order[-2], order[-1]) if len(order) >= 2 else None


def prompt_changes(a, b):
    """(places, HTML): where the prompts of the two tests' flows differ; (0, "") if the same or not recorded."""
    pa = (a.get("target") or {}).get("prompts") or {}
    pb = (b.get("target") or {}).get("prompts") or {}
    if not pa or not pb or pa == pb:
        return 0, ""
    lines, places = [], 0
    for node in sorted(set(pa) | set(pb)):
        for line in difflib.unified_diff(str(pa.get(node, "")).splitlines(), str(pb.get(node, "")).splitlines(),
                                         lineterm="", n=1):
            if line.startswith(("---", "+++")):
                continue
            if line.startswith("@@"):
                places += 1
                if places > 1:
                    lines.append('<span class="sep">…</span>')
                continue
            cls = "add" if line.startswith("+") else "del" if line.startswith("-") else ""
            lines.append(f'<span class="{cls}">{esc(line)}</span>' if cls else esc(line))
    return places, ('<p class="muted">Red: only in the first test\'s flow; green: only in the second. The rest is the '
                    f'same.</p><pre class="diff">{chr(10).join(lines)}</pre>')


def render_compare(a, b, cases, axes):
    """Compare, before (a) and after (b). Level 1: both numbers, what differs, the four boxes, the cases that changed.
    Level 2: the prompt's changes, both tests as squares, the confusion matrices."""
    ca, cb = by_case(a), by_case(b)
    both = [cid for cid in ca if cid in cb]
    share = lambda rs: sum(r["ok"] for r in rs) / max(len(rs), 1)
    better = [cid for cid in both if share(cb[cid]) > share(ca[cid])]
    worse = [cid for cid in both if share(cb[cid]) < share(ca[cid])]
    same_right = [cid for cid in both if share(ca[cid]) == share(cb[cid]) == 1]
    same_rest = [cid for cid in both if cid not in better and cid not in worse and cid not in same_right]
    info = {c["id"]: c for c in cases}
    title = lambda cid: str(info.get(cid, {}).get("subject") or "")

    def card(t, role):
        res = t["results"]
        every, n = right_in_all(t)
        all_txt = f" · {every} of {n} cases right in all {t['runs']} runs" if t["runs"] > 1 else ""
        return (f'<div class="card"><h3>{esc(t["name"])} <span class="muted">({role})</span></h3>'
                f'<div class="muted">{esc(flow_label(t))} · {esc(model_of(t))} · {esc(when(t))}</div>'
                f'<div class="rate" style="font-size:34px;margin-top:8px">{pct(sum(r["ok"] for r in res), len(res))}'
                f'<small>{sum(r["ok"] for r in res)} of {len(res)} answers right{all_txt}</small></div></div>')

    ch = change_range(a, b)
    if ch:
        m, lo, hi = ch
        word, cls = (("measurably better", "up") if lo > 0 else ("measurably worse", "down") if hi < 0 else
                     ("no measurable difference", "none"))
        why = (f"The interval includes 0: {word} on these {len(both)} test cases." if cls == "none" else
               f"The whole interval is {'above' if cls == 'up' else 'below'} 0: {word}.")
        verdict = (f'<p class="verdict {cls}"><b>Change: {points(m)}</b> · 95 % confidence interval {points(lo)[:-7]} to '
                   f'{points(hi)}. {why}</p>')
    else:
        verdict = ""
    places, diff = prompt_changes(a, b)
    differs = []
    if flow_label(a) != flow_label(b):
        differs.append(f"the flow: {flow_label(a)}, then {flow_label(b)}")
    if model_of(a) != model_of(b):
        differs.append(f"the model: {model_of(a)}, then {model_of(b)}")
    check_of = lambda t: (f'the judge {t["judge"]["flow"]}' + (" with its own setting" if t["judge"].get("context") else "")
                          if t.get("judge") else f'the field {t["field"]}' if t.get("field") else "the text check")
    if check_of(a) != check_of(b):   # another check is another measure (code review, 23 Nov 2026)
        differs.append(f"the check: {check_of(a)}, then {check_of(b)}")
    if places:
        differs.append(f"the prompt, in {places} place" + ("s" if places > 1 else ""))
    elif prompt_of(a) and prompt_of(b) and prompt_of(a) != prompt_of(b):
        differs.append(f"the prompt: {prompt_of(a)}, then {prompt_of(b)}")
    known = (a.get("target") or a.get("method")) and (b.get("target") or b.get("method"))
    differs_txt = ("What differs: " + "; ".join(differs) + "." if differs else
                   "The same flow, model, prompt and check: the difference comes from the runs." if known else "")
    rows = "".join(
        f'<tr data-case="{esc(cid)}"><td><b>{esc(cid)}</b> {esc(title(cid))}</td><td>{esc(short(want_of(info.get(cid, {}), b.get("field"))))}</td>'
        f'<td class="c" data-v="{1 if cid in better else 0}">{"<span class=" + chr(34) + "ok" + chr(34) + ">better</span>" if cid in better else "<span class=" + chr(34) + "no" + chr(34) + ">worse</span>"}</td>'
        f'<td class="c" data-v="{share(ca[cid]):.3f}">{chips(ca[cid])}</td><td class="c" data-v="{share(cb[cid]):.3f}">{chips(cb[cid])}</td></tr>'
        for cid in better + worse)
    changed_table = (f'<table class="sort filter lines"><tr><th>Case</th><th>Expected</th><th>Change</th>'
                     f'<th>{esc(a["name"])}</th><th>{esc(b["name"])}</th></tr>{rows}</table>'
                     if rows else '<p class="muted">No case changed between the two tests.</p>')
    missing = len(set(ca) ^ set(cb))
    note = (f'<p class="muted">{missing} cases are in only one of the two tests and are left out: compare tests on the '
            'same test cases.</p>' if missing else "")
    changed = {cid: "better" for cid in better}
    changed.update({cid: "worse" for cid in worse})
    level2 = ""
    if places:
        level2 += fold("What changed in the prompt", f"{places} place" + ("s" if places > 1 else ""), diff)
    if len(both) <= 60:   # more cases: the grid of All tests shows every case in every test, in a smaller file
        level2 += fold("Every case, both tests", "squares",
                       f'<p class="muted">Each column is one case: the squares of <b>{esc(a["name"])}</b> above, of '
                       f'<b>{esc(b["name"])}</b> below.</p>' +
                       squares_svg(both, [(a["name"], ca, a["runs"]), (b["name"], cb, b["runs"])], title, changed))
    mx = matrices([a, b], cases, axes)
    if mx:
        level2 += fold("What each flow answered", "two confusion matrices", mx)
    if ch:
        level2 += fold("What the 95 % confidence interval means", "the change",
                       '<p>The change is the difference in pass rate, case by case, over the test cases of both tests. '
                       'With 95 % confidence, the true change on mails like these lies in the interval. If the interval '
                       'includes 0, the two tests may differ only by chance.</p>' + RANGE_HOW)
    return (f'<div class="two" style="margin-top:14px">{card(a, "before")}{card(b, "after")}</div>'
            + (f'<p class="muted">{esc(differs_txt)}</p>' if differs_txt else "") + verdict
            + f'<div class="four"><div class="g"><b>{len(better)}</b>better</div><div class="r"><b>{len(worse)}</b>worse</div>'
            f'<div class="x"><b>{len(same_right)}</b>right in both, every run</div>'
            f'<div class="y"><b>{len(same_rest)}</b>the same, not always right</div></div>'
            + note + '<h2>The cases that changed</h2><p class="muted">Better: right in more runs than before; worse: in '
            'fewer. Click a case to open it.</p>' + changed_table + level2)


def flags_of(rs):
    wrong = sum(not r["ok"] for r in rs)
    out = []
    if rs and wrong == len(rs) and len(rs) >= 2:
        out.append('<span class="flag">wrong every time: check the expected answer</span>')
    if 0 < wrong < len(rs):
        out.append('<span class="flag">runs disagree</span>')
    return "".join(out)


def render_errors(t, cases, axes):
    """Errors, one test. Level 1: the cases to look at first, the most frequent mix-ups in one line. Level 2: all
    wrong cases, the cases whose runs disagree, the confusion matrix with the mix-ups, the share right by source."""
    info = {c["id"]: c for c in cases}
    bc = by_case(t)
    field = t.get("field")
    wrong_of = lambda cid: sum(not r["ok"] for r in bc[cid])
    bad = sorted([cid for cid in bc if wrong_of(cid)], key=lambda c: (-wrong_of(c) / len(bc[c]), -wrong_of(c)))
    wrong_total = sum(wrong_of(c) for c in bc)
    mix = Counter((norm(info.get(r["case"], {}).get("expected")), answered(r)) for r in t["results"] if not r["ok"]) if field else Counter()

    def row(cid):
        c, rs = info.get(cid, {}), bc[cid]
        src = f'<div class="muted">set by: {esc(c["source"])}</div>' if c.get("source") else ""
        return (f'<tr data-case="{esc(cid)}"><td><b>{esc(cid)}</b> {esc(c.get("subject") or "")}{src}</td>'
                f'<td>{esc(short(want_of(c, field)))}</td><td class="c" data-v="{wrong_of(cid) / len(rs):.4f}"><b>{wrong_of(cid)}</b> of {len(rs)}</td>'
                f'<td>{chips(rs)}{flags_of(rs)}</td></tr>')
    head = f'<tr><th>Case</th><th>Expected</th><th>Wrong</th><th>The runs</th></tr>'
    if not bad:
        return f'<h2>{esc(t["name"])} · {esc(model_of(t))} · {esc(when(t))}</h2><p class="muted">Nowhere: every answer of this test was right.</p>'
    out = [f'<h2>{esc(t["name"])} · {esc(model_of(t))} · {esc(when(t))}</h2><p class="muted">{wrong_total} wrong answer{"s" if wrong_total != 1 else ""} in {len(bad)} of '
           f'{len(bc)} cases. Click a case to open it: its input and every answer, in every test.</p>',
           '<h3>Look at these first</h3>', f'<table class="lines">{head}{"".join(row(c) for c in bad[:5])}</table>']
    if mix:
        top = "; ".join(f"{e} given as {g} ({n}×)" for (e, g), n in mix.most_common(3))
        out.append(f'<p class="muted"><b>The most frequent mix-ups:</b> {esc(top)}</p>')
    if len(bad) > 5:
        out.append(fold("All wrong cases", f"{len(bad)}", f'<table class="sort filter">{head}{"".join(row(c) for c in bad)}</table>'))
    unstable = [cid for cid in bc if 0 < wrong_of(cid) < len(bc[cid])]
    if unstable:
        out.append(fold("Cases whose runs disagree", f"{len(unstable)}",
                        '<p class="muted">The same flow and the same input, a different result from run to run: the '
                        'prompt leaves room here, or the case lies on a border.</p>'
                        f'<table class="sort filter">{head}{"".join(row(c) for c in unstable)}</table>'))
    if field:
        beside = ('<div class="card"><h3>The most frequent mix-ups</h3><table class="mix sort" style="margin-top:8px">'
                  '<tr><th>Expected</th><th>Given instead</th><th>How often</th></tr>' +
                  "".join(f'<tr><td>{esc(e)}</td><td>{esc(g)}</td><td>{n}</td></tr>' for (e, g), n in mix.most_common(10)) +
                  '</table></div>') if mix else ""
        out.append(fold("Confusion matrix and mix-ups", "", matrices([t], cases, axes, beside)))
    sources = list(dict.fromkeys(c["source"] for c in cases if c.get("source")))
    if sources:
        src_of = {c["id"]: c.get("source") for c in cases}
        cells = lambda s: [r for r in t["results"] if src_of.get(r["case"]) == s]
        out.append(fold("Right, by who set the expected answer", f"{len(sources)} sources",
                        '<table class="mix sort"><tr><th>Set by</th><th>Cases</th><th>Right</th></tr>' + "".join(
                            f'<tr><td>{esc(s)}</td><td>{sum(1 for c in cases if c.get("source") == s)}</td>'
                            f'<td>{pct(sum(r["ok"] for r in cells(s)), len(cells(s)))}</td></tr>' for s in sources) + '</table>'))
    return "".join(out)


def case_panels(same, cases):
    """Level 3: one window per case, its input and every answer in every test, newest test first."""
    out = []
    per = [(t, by_case(t)) for t in reversed(same)]
    for c in cases:
        cid = c["id"]
        if not any(cid in bc for _, bc in per):
            continue
        src = f' <span class="muted">set by: {esc(c["source"])}</span>' if c.get("source") else ""
        rows = []
        for t, bc in per:
            rs = bc.get(cid)
            if not rs:
                continue
            answers = "".join(f'<div class="muted">run {r["run"]} · {"right" if r["ok"] else "wrong"}: {esc(r["got"])} · '
                              f'{r["seconds"]} s</div><pre>{esc(r["answer"] or r["got"])}</pre>' for r in rs)
            rows.append(f'<div class="ct"><div><b>{esc(t["name"])}</b><div class="muted">{esc(when(t))} · {esc(model_of(t))}</div></div>'
                        f'<div>{chips(rs)}{flags_of(rs)}<details><summary>Read the answers</summary>{answers}</details></div></div>')
        # the expected answer in a box of its own, between the input and the answers (Frank, 22 Nov 2026, on the window
        # of a case judged against a whole reply: "where can i see what is the expected answer?")
        out.append(f'<div class="case" data-c="{esc(cid)}"><h2>Case {esc(cid)} · {esc(c.get("subject") or "")}</h2>'
                   f'<h3>The input</h3><pre class="mail">{esc(c.get("input", ""))}</pre>'
                   f'<h3>The expected answer{src}</h3><pre class="mail exp">{esc(want_of(c, ""))}</pre>'
                   f'<h3>Every test, newest first</h3>{"".join(rows)}</div>')
    return ('<div id="case" class="overlay"><div class="sheet"><button class="close" type="button">Close</button>'
            + "".join(out) + '</div></div>')


def run_cmd(s, last, model=True):
    """The command of the last test (or of the bench's start), to copy."""
    flow = last["flow"] if last and " " not in str(last["flow"]) else s.get("flow", "enron-triage")
    field = last.get("field") if last else s.get("field")
    judge = ((last or {}).get("judge") or {}).get("flow") if last else s.get("judge")
    m = (last or {}).get("model") if last else s.get("model")
    return (f'python3 test_bench.py --flow {flow}' + (f' --field {field}' if field else "") +
            (f' --judge {judge}' if judge else "") +
            (f' --model {m}' if m and model else "") + f' --cases {s.get("cases_name", "cases.csv")}')


def run_more(s, last):
    """Run, level 2: let Claude Code run the bench or fit it to your flow; where the key comes from."""
    base = run_cmd(s, last, model=False)
    asks = [
        ("Run the test", f"Run the test bench in test/ without its page: {base} --run --full --name today. Then tell me the "
                         "pass rate, and which cases failed in which runs."),
        ("Find out why cases failed", "Read the newest file in test/results/. For every case that failed, tell me in one "
                                      "line what my flow answered and why that may be wrong. Do not change my flow."),
        ("Fit the bench to your flow", "The test bench in test/test_bench.py does not read my Langflow flow right. Find out "
                                       "why from my flow and from the newest file in test/results/. Make a copy of the "
                                       "bench, test/test_bench_ours.py, that works with my flow, and tell me the command "
                                       "to start it. Do not change my flow, and do not change test/cases.csv. What I see:"),
        ("Compare models", f"Run the test bench in test/ three times without its page: {base} --run --full, each time with another "
                           "--model: anthropic/claude-haiku-5.5, z-ai/glm-5.3-flash and qwen/qwen3.6-35b-a3b, with the names "
                           "haiku, glm and qwen. Then write the report with --report, and tell me which model was right "
                           "most often, whether the difference is measurable (the 95 % confidence interval in its tab Compare), and "
                           "how many seconds per call each took."),
    ]
    claude = ('<p>Claude Code can run the bench for you, without the page: with <b>--run --full</b> (only <b>--run</b>: '
              'a quick check). It is the same test, and the answers go into the same folder results/. The page itself '
              'you start in your own terminal: Claude Code cannot open it for you.</p><p>Copy one of these requests into '
              'Claude Code, in your kingo-pod folder; test/ is the folder of the bench there:</p>' +
              "".join(f'<h3>{esc(t)}</h3><pre class="cmd">{esc(a)}</pre>' for t, a in asks) +
              '<p class="muted">Each run sends every case to your flow, once per run; your flow pays its model with its '
              'own OpenRouter key.</p>')
    # in plain words (Frank, 22 Nov: "bitte verständlich schreiben", on the first version of this fold)
    key = ('<p>To use your Langflow, the bench needs your Langflow key, like a password. Usually you do nothing: the '
           'bench finds the key by itself.</p>'
           '<ul><li><b>You start the bench in your terminal:</b> it uses the key that <b>./kingo claude</b> saved on your '
           'laptop, in the file ~/.config/kingo/langflow.key.</li>'
           '<li><b>Claude Code runs the bench for you:</b> Claude Code never gets your key. It works in a protected area, '
           'the sandbox; the sandbox adds your key to each message just before the message reaches Langflow.</li>'
           '<li><b>You test another model:</b> you need no other key. The bench only tells your flow which model to '
           'use, and your flow calls that model with the OpenRouter key it already has.</li>'
           '<li><b>You do not use kingo,</b> for example with another Langflow: make a key in that Langflow (Settings, '
           'Langflow API Keys). In your terminal, before you start the bench, put the key into LANGFLOW_API_KEY and the '
           'address of that Langflow into LANGFLOW_BASE_URL.</li></ul>'
           '<p class="muted">The bench never writes your key into the page, the report or the folder results/.</p>')
    return (fold("Let Claude Code run the bench, or fit it to your flow", "four requests to copy", claude)
            + fold("Your Langflow key: where the bench finds it", "usually nothing to do", key))


def run_help(s, last):
    """The tab Run of report.html: a saved file cannot run a test, so it says how to start one."""
    cmd = run_cmd(s, last)
    return (f'<div class="card" style="margin-top:14px"><b>This is the saved report: it shows the tests, but it cannot '
            f'run one.</b><p>To run a test yourself:</p><ol><li>Open your own terminal, not Claude Code, and go to the '
            f'folder with test_bench.py (in the course: <b>cd ~/kingo-pod/claude/test</b>).</li>'
            f'<li>Start the bench, here with the settings of the last test:<pre class="cmd">{esc(cmd)}</pre>'
            f'Leave the terminal open while the page works; Ctrl+C stops it.</li>'
            f'<li>Open <b>http://localhost:8765</b> in your browser. Its tab Run has the form: Flow, Model (optional), '
            f'a name, and two buttons: Quick check (the first {QUICK} cases, once) and Full test.</li></ol>'
            f'<p class="muted">Without the page: add <b>--run</b> to the command for a quick check, or <b>--run --full '
            f'--name today</b> for the full test. The bench runs it in the terminal and writes this report again.</p></div>' + run_more(s, last))


def run_form(s):
    out = []
    judge_txt = (f'Judge: every answer goes to the flow <b>{esc(s["judge"])}</b>, which gives a grade from 1 to 5; '
                 f'{JUDGE_PASS} or more counts as right. Each case costs two calls.<br/>' if s.get("judge") else "")
    if STATE["running"]:
        out.append(f'<div class="card" style="margin-top:14px"><b>Running: {esc(STATE["name"])}</b> · {STATE["done"]} of {STATE["total"]} answers'
                   f'<div class="prog"><i style="width:{100 * STATE["done"] / max(STATE["total"], 1):.0f}%"></i></div>'
                   f'<span class="muted">This page reloads by itself. You can close it; the test runs on.</span></div>')
        return "".join(out)
    if STATE["error"]:
        out.append(f'<div class="card" style="border-color:#f3b8a8;margin:14px 0 12px"><b>The test did not start.</b> '
                   f'{esc(STATE["error"])}</div>')
    out.append(f'''<form class="card" method="post" action="/run" style="margin-top:14px">
  <label>Flow (name in its address)<input name="flow" value="{esc(s.get("flow", ""))}"/></label>
  <label>Model (optional)<input name="model" value="{esc(s.get("model") or "")}" placeholder="the flow's own" style="width:230px"/></label>
  <label>A name for the full test<input name="name" placeholder="today" onkeydown="if (event.key === 'Enter') {{ event.preventDefault(); this.form.requestSubmit(this.form.querySelector('button[value=full]')); }}"/></label>
  <button name="mode" value="quick" class="second">Quick check</button>
  <button name="mode" value="full">Full test</button></form>
<p class="muted"><b>Quick check:</b> the first {QUICK} cases, once, to see in a minute that the bench reads your flow
right. <b>Full test:</b> all {s.get("n_cases", "your")} cases, {s.get("runs", 3)} times: your pass rate.<br/>
Model: empty runs the flow with the model set in it. An OpenRouter model, for example
anthropic/claude-haiku-5.5, runs the same flow with that model for this test; the flow in Langflow stays as it is.<br/>
{judge_txt}When the test is done, see <a href="#results">Results</a>. A second test with another name, for example of your Demo Day
flow or with another model, lets you <a href="#compare">compare</a> the two.</p>''')
    out.append(run_more(s, None))
    return "".join(out)


def pick_select(same, key, sel, attr):
    """A list of the tests, grouped by model, newest first; with several flows, each test names its flow."""
    groups = {}
    for t in reversed(same):
        groups.setdefault(model_of(t), []).append(t)
    flows = len({flow_label(t) for t in same}) > 1
    label = lambda t: f'{t["name"]} · {when(t)}' + (f' · {flow_label(t)}' if flows else "")
    return (f'<select {attr}>' + "".join(
        f'<optgroup label="{esc(m)}">' + "".join(
            f'<option value="{key(t)}"{" selected" if t is sel else ""}>{esc(label(t))}</option>' for t in ts) + '</optgroup>'
        for m, ts in groups.items()) + '</select>')


def tests_table(sub, key):
    """All tests in a table: one row per test; a click opens its Results."""
    def every(x):
        e, n = right_in_all(x)
        return f'<td data-v="{e / max(n, 1):.4f}">{e} of {n}</td>' if x["runs"] > 1 else '<td data-v="-1">–</td>'
    rows = "".join(
        f'<tr data-go="{key(x)}"><td>{esc(x["name"])}</td><td>{esc(flow_label(x))}<div class="muted">{esc(model_of(x))}</div></td>'
        f'<td>{x["started"].replace("T", " ")}</td>'
        f'<td data-v="{sum(r["ok"] for r in x["results"])}">'
        f'{" · ".join(str(sum(r["ok"] for r in x["results"] if r["run"] == k)) for k in range(1, x["runs"] + 1))}'
        f' of {len(x["results"]) // max(x["runs"], 1)}</td>'
        f'<td data-v="{sum(r["ok"] for r in x["results"]) / max(len(x["results"]), 1):.4f}"><b>{pct(sum(r["ok"] for r in x["results"]), len(x["results"]))}</b></td>'
        f'<td data-v="{(rate_range(x) or (0, 0))[0]:.4f}">{range_txt(rate_range(x)) if rate_range(x) else "–"}</td>'
        f'{every(x)}<td>{statistics.median([r["seconds"] for r in x["results"]]) if x["results"] else 0:.1f} s</td></tr>'
        for x in reversed(sub))
    return ('<p class="muted">Click a test to open its Results.</p><table class="sort filter"><tr><th>Name</th>'
            '<th>Flow · model</th><th>When</th><th>Right per run</th><th>Pass rate</th><th>95 % confidence interval</th><th>Right in all runs</th>'
            f'<th>Median</th></tr>{rows}</table>')


def render_tests_view(sub, cases, key, show_flow):
    """All tests, for one choice of the filters. Level 1: a row of bars per test (a click opens its Results).
    Level 2: every case in every test (a grid), all tests in a table, the cases wrong in every test."""
    if not sub:
        return '<p class="muted" style="margin-top:14px">No test with this flow and this model.</p>'
    info = {c["id"]: c for c in cases}
    rows = []
    bar = lambda v, cls, ci="": (f'<div class="bb"><div class="trk"><span class="{cls}" style="width:{100 * v:.1f}%"></span>'
                                 f'{ci}</div><em>{round(100 * v)} %</em></div>')
    # the 95 % confidence interval of the pass rate as a line with ends (Frank, 22 Nov: "1. ja", the range in All tests too)
    whisker = lambda r: (f'<i class="ci" style="left:{100 * r[0]:.1f}%;width:{100 * (r[1] - r[0]):.1f}%"></i>' if r else "")
    for t in sub:
        res = t["results"]
        right = sum(r["ok"] for r in res)
        every, n = right_in_all(t)
        sub_txt = f'{when(t)} · {model_of(t)}' + (f' · {flow_label(t)}' if show_flow else "")
        rng = rate_range(t)
        tip = (f'{t["name"]}: {right} of {len(res)} answers right' + (f', 95 % confidence interval {range_txt(rng)}' if rng else "") +
               (f'; {every} of {n} cases right in all {t["runs"]} runs' if t["runs"] > 1 else "") + '. Click to open its Results.')
        rows.append(f'<div class="tr" data-go="{key(t)}" title="{esc(tip)}"><div class="nm"><b>{esc(t["name"])}</b>'
                    f'<span>{esc(sub_txt)}</span></div><div>{bar(right / max(len(res), 1), "b1", whisker(rng))}'
                    f'{bar(every / max(n, 1), "b2") if t["runs"] > 1 else ""}</div></div>')
    lead = ('<h2>The tests</h2><p class="muted">Oldest at the top. Click a test to open its Results; point at it for '
            f'its numbers.</p><div class="tl"><div class="lg"><span><i style="background:{SERIES[0]}"></i>pass rate: share '
            f'of the answers right</span><span><i class="cil"></i>its 95 % confidence interval</span><span><i style="background:{SERIES[1]}"></i>'
            f'share of the cases right in all runs</span></div>{"".join(rows)}</div>'
            '<p class="muted">Intervals that overlap do not prove that two tests are equal: for two tests, the tab Compare '
            'checks the change case by case.</p>')
    per = [(t, by_case(t)) for t in sub]
    ids = list(dict.fromkeys(cid for _, bc in per for cid in bc))
    share = lambda rs: sum(r["ok"] for r in rs) / len(rs)

    def q(s):
        if s is None:
            return '<span class="q qn"></span>'
        cls, mark = ("q3", "✓") if s == 1 else ("q2", "") if s >= .5 else ("q1", "") if s > 0 else ("q0", "✗")
        return f'<span class="q {cls}">{mark}</span>'

    def order(cid):
        v = [share(bc[cid]) for _, bc in per if bc.get(cid)]
        return (-(max(v) - min(v)), sum(v) / len(v))

    grid_rows, always = [], []
    for cid in sorted(ids, key=order):
        c = info.get(cid, {})
        vals = [(t, bc.get(cid)) for t, bc in per]
        present = [share(rs) for _, rs in vals if rs]
        allright = sum(1 for x in present if x == 1)
        wrong_all = len(present) >= 2 and all(x == 0 for x in present)
        if wrong_all:
            always.append(cid)
        flag = '<div class="flag">wrong in every test: check the expected answer</div>' if wrong_all else ""
        cells = "".join(
            (f'<td class="qc" data-v="{share(rs):.3f}" title="{esc(t["name"])} · ID {esc(cid)}: '
             f'{sum(r["ok"] for r in rs)} of {len(rs)} right">{q(share(rs))}</td>') if rs else
            ('<td class="qc" data-v="-1">' + q(None) + '</td>') for t, rs in vals)
        grid_rows.append(f'<tr data-case="{esc(cid)}"><td><b>{esc(cid)}</b> {esc(c.get("subject") or "")}{flag}</td>'
                         f'<td>{esc(short(want_of(c, sub[-1].get("field"))))}</td>{cells}'
                         f'<td data-v="{allright / max(len(present), 1):.3f}">{allright} of {len(present)}</td></tr>')
    heads = "".join(f'<th title="{esc(test_label(t))}">{esc(t["name"][:16])}<div class="muted">'
                    f'{esc(model_of(t).split("/")[-1][:18])}</div></th>' for t, _ in per)
    grid = ('<p class="muted"><span class="q q3">✓</span> right in all runs · <span class="q q2"></span> in most · '
            '<span class="q q1"></span> in some · <span class="q q0">✗</span> in none. The cases where the tests differ '
            'most come first. Click a case to open it.</p>'
            f'<table class="sort filter grid"><tr><th>Case</th><th>Expected</th>{heads}<th>Right in all runs</th></tr>'
            f'{"".join(grid_rows)}</table>')
    out = lead + fold("Every case in every test", f"{len(ids)} cases × {len(sub)} tests", grid)
    out += fold("All tests in a table", f"{len(sub)} tests", tests_table(sub, key))
    if len(sub) >= 2:
        names = "".join(f'<th>{esc(t["name"])}<div class="muted">{esc(when(t))}</div></th>' for t, _ in per)
        body = ('<p class="muted">Wrong in every run of every test: the flows may be right and the expected answer '
                'wrong. Check it.</p>' + (
                    f'<table class="sort filter"><tr><th>Case</th><th>Expected</th>{names}</tr>' + "".join(
                        f'<tr data-case="{esc(cid)}"><td><b>{esc(cid)}</b> {esc(info.get(cid, {}).get("subject") or "")}</td>'
                        f'<td>{esc(info.get(cid, {}).get("expected") or "")}</td>'
                        + "".join(f'<td>{chips(bc.get(cid, []))}</td>' for _, bc in per) + '</tr>' for cid in always)
                    + '</table>' if always else '<p class="muted">None: every case was right at least once.</p>'))
        out += fold("Cases wrong in every test", f"{len(always)}", body)
    return out


def render_page(tests, cases, form=True, settings=None, names=None):
    s = settings or {}
    ids = {c["id"] for c in cases}   # a test belongs to these cases if all its cases are among them
    same = [t for t in tests if t["results"] and {r["case"] for r in t["results"]} <= ids]
    keys = {id(t): f"t{i}" for i, t in enumerate(same)}
    key = lambda t: keys[id(t)]
    full = [t for t in same if not t.get("quick") and not t.get("stopped")]   # All tests and Compare: whole tests only
    pair = pick_pair(full, names)
    sel_t = (pair[1] if names and pair else same[-1]) if same else None   # Results and Errors
    sel_b = pair[0] if pair else (full[-2] if len(full) >= 2 else (full[-1] if full else None))   # Compare: before
    sel_a = pair[1] if pair else (full[-1] if full else None)                                     # Compare: after
    default = "run" if (form and (STATE["running"] or not same)) else ("compare" if names else "results")
    cname = esc(s.get("cases_name", ""))
    title = f'How often your Langflow flow is right, on the {len(cases)} test cases of {cname}'
    sub = "Test bench · " + (f'{len(same)} test{"s" if len(same) != 1 else ""} so far · the last: <b>{esc(same[-1]["name"])}</b>, '
                             f'{esc(when(same[-1]))}' if same else "no test yet")
    parts = [f'<main><h1>{title}</h1><p class="sub">{sub}</p>']
    tabs = [("run", "Run", ""), ("results", "Results", "One test"), ("errors", "Errors", ""),
            ("tests", "All tests", "Several tests"), ("compare", "Compare", "")]
    mark = ' class="default"'
    parts.append('<nav class="tabs">' + "".join(
        (f'<span class="grp">{g}</span>' if g else "") + f'<a href="#{k}"{mark if k == default else ""}>{v}</a>'
        for k, v, g in tabs) + '</nav>')
    sec = lambda k, body: f'<section id="{k}" class="tab{" default" if k == default else ""}">{body}</section>'
    parts.append(sec("run", run_form(s) if form else run_help(s, same[-1] if same else None)))
    if same:
        axes = matrix_axes(same, cases)
        test_pick = ('<div class="pick"><label>Test' + pick_select(same, key, sel_t, 'class="p-test"') +
                     '</label><span class="muted">grouped by model</span></div>')
        parts.append(sec("results", test_pick + "".join(
            view("data-t", key(t), t is sel_t, render_results(t, cases)) for t in same)))
        parts.append(sec("errors", test_pick + "".join(
            view("data-t", key(t), t is sel_t, render_errors(t, cases, axes)) for t in same)))
        flows = list(dict.fromkeys(t["flow"] for t in full))   # by its address: older tests do not know the name
        named = {t["flow"]: flow_label(t) for t in full if t.get("target")}
        models = list(dict.fromkeys(model_of(t) for t in full))
        fopts = [""] + ([str(i) for i in range(len(flows))] if len(flows) > 1 else [])
        mopts = [""] + ([str(i) for i in range(len(models))] if len(models) > 1 else [])
        filt = ""
        for id_, label, vals in (("f-flow", "Flow", [named.get(f, f) for f in flows]), ("f-model", "Model", models)):
            if len(vals) > 1:
                filt += (f'<label>{label}<select id="{id_}"><option value="">all</option>' +
                         "".join(f'<option value="{i}">{esc(v)}</option>' for i, v in enumerate(vals)) + '</select></label>')
        fit = lambda t, fi, mi: (fi == "" or t["flow"] == flows[int(fi)]) and (mi == "" or model_of(t) == models[int(mi)])
        alltests = (f'<div class="pick">{filt}<span class="muted">show only the tests of one flow or one model</span></div>'
                    if filt else "") + "".join(
            view("data-f", f"{fi}|{mi}", fi == "" and mi == "",
                 render_tests_view([t for t in full if fit(t, fi, mi)], cases, key, len(flows) > 1))
            for fi in fopts for mi in mopts) if full else (
            '<p class="muted" style="margin-top:18px">No full test yet: a quick check shows only in Results and Errors. '
            'Click <b>Full test</b> in the tab Run.</p>')
        others = len(tests) - len(same)
        if others:
            alltests += (f'<p class="muted">{others} more tests in results/ ran on other test cases; start the bench with '
                         'their --cases to see them.</p>')
        parts.append(sec("tests", alltests))
        last = {id(t) for t in full[-COMPARE_LAST:]} | {id(sel_b), id(sel_a)}
        recent = [t for t in full if id(t) in last]
        pairs = "".join(view("data-pair", f"{key(a)}|{key(b)}", a is sel_b and b is sel_a, render_compare(a, b, cases, axes))
                        for a in recent for b in recent if a is not b)
        hit = sel_b is not sel_a and any(x is sel_b for x in recent) and any(x is sel_a for x in recent)
        none = view("data-none", "1", not hit,
                    '<p class="muted" style="margin-top:18px">' +
                    ("Compare needs two tests on the same test cases, for example <b>demo-day</b> for your Demo Day flow "
                     "and <b>today</b> for today's flow." if len(full) < 2 else
                     "Pick two different tests.") + '</p>')
        older = (f' · the last {COMPARE_LAST} tests; for an older one, write the report with --compare and its name'
                 if len(recent) < len(full) else "")
        pick2 = ('<div class="pick"><label>Before' + pick_select(recent, key, sel_b, 'id="p-before"') + '</label><label>After' +
                 pick_select(recent, key, sel_a, 'id="p-after"') + f'</label><span class="muted">grouped by model{older}</span></div>')
        parts.append(sec("compare", pick2 + pairs + none))
        parts.append(case_panels(same, cases))
    else:
        empty = ('<p class="muted" style="margin-top:18px">No test on these test cases yet. ' +
                 ('Click the tab <b>Run</b>, then <b>Quick check</b> or <b>Full test</b>.</p>' if form else 'Run a test, then write this report again.</p>'))
        for k in ("results", "errors", "tests", "compare"):
            parts.append(sec(k, empty))
    refresh = '<meta http-equiv="refresh" content="3;url=/"/>' if form and STATE["running"] else ""
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"/>{refresh}<title>Test bench: {cname}</title>'
            f'<style>{CSS}</style></head><body>{"".join(parts)}</main><script>{JS}</script></body></html>')


# ---------------------------------------------------------------- the server

def serve(args, cases):
    settings = {"flow": args.flow, "model": args.model, "field": args.field, "judge": args.judge, "runs": args.runs,
                "cases_name": Path(args.cases).name, "n_cases": len(cases)}
    start = threading.Lock()
    own = {f"http://{h}:{args.port}" for h in ("localhost", "127.0.0.1")}

    def run_in_background(*a):
        try:
            run_test(*a)
        except SystemExit:   # a missing key, a model or judge the bench cannot use: STATE["error"] says it
            pass
        except Exception as e:   # anything else: say it on the page (code review, 23 Nov 2026)
            STATE["error"] = f"The test stopped: {type(e).__name__}: {e}"[:300]
        finally:
            STATE["running"] = False

    class Page(BaseHTTPRequestHandler):
        def _send(self, code, body, ctype="text/html; charset=utf-8", extra=None):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body.encode())

        def do_GET(self):
            q = parse_qs(urlparse(self.path).query)
            names = (q["a"][0], q["b"][0]) if q.get("a") and q.get("b") else None
            self._send(200, render_page(load_tests(args.out), cases, True, settings, names))

        def do_POST(self):
            origin = self.headers.get("Origin")
            if origin and origin not in own:   # another website open in the same browser must not start tests
                return self._send(403, "Only the test bench's own page can start a test.", "text/plain; charset=utf-8")
            if self.path != "/run":
                return self._send(303, "", extra={"Location": "/"})
            form = parse_qs(self.rfile.read(int(self.headers.get("Content-Length", 0))).decode())
            flow = (form.get("flow", [args.flow])[0] or args.flow).strip()
            model = (form.get("model", [""])[0] or "").strip()
            quick = form.get("mode", ["full"])[0] == "quick"
            name = "quick check" if quick else ((form.get("name", [""])[0] or "").strip() or "today")   # the grey "today" is a placeholder
            with start:   # running from this click on, so the next page shows the progress and a second click waits
                if STATE["running"]:
                    return self._send(303, "", extra={"Location": "/"})
                settings.update(flow=flow, model=model)
                STATE.update(running=True, done=0, total=0, name=name, error="")
            threading.Thread(target=run_in_background, args=(flow, cases, args.runs, args.field, name, args.cases,
                                                             args.out, model, quick, args.judge, args.judge_context,
                                                             args.parallel),
                             daemon=True).start()
            self._send(303, "", extra={"Location": "/"})

        def log_message(self, *a):
            pass

    print(f"Test bench: open http://localhost:{args.port} in your browser. Stop it with Ctrl+C.")
    try:
        ThreadingHTTPServer(("127.0.0.1", args.port), Page).serve_forever()
    except KeyboardInterrupt:   # Ctrl+C: a line, not a Python traceback; and at once, also during a test (its
        print("\nTest bench stopped.", flush=True)   # parallel calls would otherwise keep the bench running to the end)
        os._exit(0)


def main():
    # every option with a sentence (Frank, 23 Nov 2026: "sind die flags (was heißt --field?) dokumentiert?")
    ap = argparse.ArgumentParser(description=" ".join(__doc__.split("\n\n")[0].split()) + " Without --run or --report, it "
                                 "opens its page. More at the top of this file.")
    ap.add_argument("--flow", default="enron-triage", help="the flow to test: the endpoint name, the last part of its "
                                                           "address (.../api/v1/run/NAME), or its id")
    ap.add_argument("--model", default="", help="run the flow with this model instead of its own, for this test "
                                                "(an OpenRouter model, for example anthropic/claude-haiku-5.5)")
    ap.add_argument("--cases", default=str(HERE / "cases.csv"), help="the CSV file with the test cases, with the "
                                                                      "columns id, input and expected (default: cases.csv)")
    ap.add_argument("--field", default="", help="read only this field of the JSON in each answer: a case is right when "
                                                "the field equals expected (big and small letters the same). Without "
                                                "--field, every piece of expected must be in the answer. Triage: "
                                                "--field action")
    ap.add_argument("--judge", default="", help="let this judge flow grade every answer against expected, 1 to 5, "
                                                "right from 4 (for free text; for example enron-judge); not with --field")
    ap.add_argument("--judge-context", default="", help="with --judge: your own setting for the judge, instead of its own")
    ap.add_argument("--runs", type=int, default=3, help="how often each case runs in the full test (default 3)")
    ap.add_argument("--parallel", type=int, default=PARALLEL, help=f"calls at the same time (default {PARALLEL}; 1: one "
                                                                     "after the other)")
    ap.add_argument("--name", default="today", help="with --run --full: a name for the test, for example today or v2 "
                                                     "(default: today)")
    ap.add_argument("--out", type=Path, default=HERE / "results", help="the folder for the results, one JSON file per "
                                                                       "test (default: results); report.html goes next to it")
    ap.add_argument("--port", type=int, default=8765, help="the port of the page (default 8765)")
    ap.add_argument("--run", action="store_true", help="a quick check without the page (the first 3 cases, once); "
                                                       "with --full the full test; then write report.html")
    ap.add_argument("--full", action="store_true", help="with --run: every case, --runs times")
    ap.add_argument("--report", action="store_true", help="only write report.html again, from the tests in --out")
    ap.add_argument("--compare", nargs=2, metavar=("FIRST", "SECOND"),
                    help="the names of the two tests that report.html opens Compare with (default: the last two names)")
    args = ap.parse_args()
    cases = load_cases(args.cases)
    if not (args.run or args.report):
        return serve(args, cases)
    if args.run:
        name = args.name if args.full else "quick check"
        try:
            t = run_test(args.flow, cases, args.runs, args.field, name, args.cases, args.out, args.model, not args.full,
                         args.judge, args.judge_context, args.parallel)
        except KeyboardInterrupt:   # the stopped test is stored; do not wait for the calls still running
            print("\nTest stopped. What was done is stored in", args.out, flush=True)
            os._exit(1)
        right = sum(r["ok"] for r in t["results"])
        print(f"{name}: {right} of {len(t['results'])} right, per run: " +
              ", ".join(str(sum(r["ok"] for r in t["results"] if r["run"] == k)) for k in range(1, t["runs"] + 1))
              + ("" if args.full else ". A quick check: the full test with --run --full."))
    report = args.out.parent / "report.html"   # next to its results: a test elsewhere leaves this one alone
    report.write_text(render_page(load_tests(args.out), cases, False,
                                  {"flow": args.flow, "field": args.field, "judge": args.judge,
                                   "cases_name": Path(args.cases).name},
                                  tuple(args.compare) if args.compare else None))
    print("Report:", report)


if __name__ == "__main__":
    main()
