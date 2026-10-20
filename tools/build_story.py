#!/usr/bin/env python3
"""Compile tools/story/*.py into data/story.json and validate the branch graph."""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "story"))
import dsl
for m in ["ch0", "ch1", "ch1b", "ch2", "ch2b", "ch3", "ch3b", "ch4", "ch4b", "ch5", "ch5b", "ch6", "ch6b", "ch7", "ch7b"]:
    __import__(m)

sys.path.insert(0, HERE)
import patches  # noqa: applies post-import edits
START, DEATH = "c0_prologue", "death"
scenes = {}
errors, warns = [], []
for s in dsl.SCENES:
    if s["id"] in scenes:
        errors.append(f"duplicate scene id {s['id']}")
    scenes[s["id"]] = s

def targets(sc):
    for c in sc.get("choices", []):
        if "goto" in c: yield c["goto"], "choice"
        for t in c.get("random", []): yield t, "random"
        if "check" in c:
            for k in ("hit", "mixed", "miss"): yield c["check"][k], "check"
    for r in sc.get("redirect", []): yield r["goto"], "redirect"

def req_tokens(req):
    for part in str(req).split("&"):
        part = part.strip()
        if not part: continue
        if "|" in part: errors.append(f"unsupported '|' in req: {req}")
        if re.search(r"(>=|<=|==)", part): continue
        yield part.lstrip("!").removeprefix("court:")

set_flags, used_flags = set(), set()
def fx_flags(fx):
    for e in fx:
        while e.startswith("if:"):
            q = e.index("?")
            for t in req_tokens(e[3:q]): used_flags.add(t)
            e = e[q+1:]
        if e.startswith("set:"): set_flags.add(e[4:])
        m = re.match(r"add:([\w.]+):(-?\d+)$", e)
        if e.startswith("add:") and not m: errors.append(f"bad effect {e}")

for sid, sc in scenes.items():
    fx_flags(sc.get("on_enter", [])); fx_flags(sc.get("on_reenter", []))
    for r in sc.get("redirect", []):
        for t in req_tokens(r["if"]): used_flags.add(t)
    for c in sc.get("choices", []):
        fx_flags(c.get("fx", []))
        if "req" in c: [used_flags.add(t) for t in req_tokens(c["req"])]
        if "check" in c:
            for k in ("hit", "mixed", "miss"): fx_flags(c["check"].get(k + "_fx", []))
    for t in re.findall(r"\{\{(.*?)\|", sc["text"]):
        for tok in req_tokens(t): used_flags.add(tok)
    for t, kind in targets(sc):
        if t not in scenes: errors.append(f"{sid}: {kind} -> missing scene '{t}'")
    if "ending" not in sc and not sc.get("choices"):
        errors.append(f"{sid}: dead end (no choices, not an ending)")
    if "ending" in sc and sc.get("choices"):
        warns.append(f"{sid}: ending has choices")
    if sc["text"].count("{{") != sc["text"].count("}}"):
        errors.append(f"{sid}: unbalanced {{{{ }}}}")

for need in (START, DEATH):
    if need not in scenes: errors.append(f"missing {need}")

# reachability (ignores requirements: optimistic)
seen, stack = set(), [START]
while stack:
    x = stack.pop()
    if x in seen or x not in scenes: continue
    seen.add(x)
    stack += [t for t, _ in targets(scenes[x])]
seen.add(DEATH)  # reached via hp<=0
for sid in scenes:
    if sid not in seen: warns.append(f"unreachable: {sid}")
# every reachable scene must be able to reach an ending
can_end = {sid for sid, s in scenes.items() if "ending" in s}
changed = True
while changed:
    changed = False
    for sid, s in scenes.items():
        if sid not in can_end and any(t in can_end for t, _ in targets(s)):
            can_end.add(sid); changed = True
for sid in seen:
    if sid in scenes and sid not in can_end: errors.append(f"{sid}: cannot reach any ending")
for f in sorted(used_flags - set_flags):
    if f not in ("tom_done",) and not f.startswith(("hp", "coin", "xp", "built", "pipe", "gambit")):
        warns.append(f"flag used but never set: {f}")

endings = sorted(s["ending"] for s in scenes.values() if "ending" in s)
print(f"{len(scenes)} scenes, {len(endings)} endings")
for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
if errors: sys.exit(1)
out = {"meta": {"title": "The King in Flight", "start": START, "death": DEATH}, "scenes": scenes}
dest = os.path.join(HERE, "..", "data", "story.json")
with open(dest, "w") as f: json.dump(out, f, indent=1, ensure_ascii=False)
print("wrote", os.path.normpath(dest))
