#!/usr/bin/env python3
"""Random-walk playtester mirroring scripts/story_engine.gd. Finds soft-locks (no visible choices)."""
import json, random, re, collections, os
S = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "story.json")))["scenes"]
MODS = {"STR": 1, "DEX": -1, "CON": 0, "INT": 2, "WIS": 0, "CHA": 3}

def new():
    return dict(scene="c1_ford", hp=18, max_hp=18, xp=1, level=4, coin=180, pipe=5, gambit=0, flags={},
                court=["Roland", "Aymer", "Bors", "Alcuin", "Anselm", "Sam", "Wat"], clocks={"siege": 0, "delve": 0})
def val(st, k): return st["clocks"].get(k[6:], 0) if k.startswith("clock.") else st.get(k, 0)
def req(st, r):
    for p in (r or "").split("&"):
        p = p.strip()
        if not p: continue
        if p.startswith("!court:"):
            if p[7:] in st["court"]: return False
        elif p.startswith("court:"):
            if p[6:] not in st["court"]: return False
        elif p.startswith("!"):
            if p[1:] in st["flags"]: return False
        else:
            m = re.match(r"(.+?)(>=|<=|==)(-?\d+)$", p)
            if m:
                a, o, b = val(st, m[1]), m[2], int(m[3])
                if not {">=": a >= b, "<=": a <= b, "==": a == b}[o]: return False
            elif p not in st["flags"]: return False
    return True
def fx(st, es):
    for e in es:
        if e.startswith("if:"):
            q = e.index("?")
            if req(st, e[3:q]): fx(st, [e[q+1:]])
        elif e.startswith("set:"): st["flags"][e[4:]] = 1
        elif e.startswith("clear:"): st["flags"].pop(e[6:], None)
        elif e.startswith("court:+"):
            if e[7:] not in st["court"]: st["court"].append(e[7:])
        elif e.startswith("court:-"):
            if e[7:] in st["court"]: st["court"].remove(e[7:])
        elif e.startswith("add:"):
            _, k, n = e.split(":"); n = int(n)
            if k.startswith("clock."): st["clocks"][k[6:]] = max(0, min(6, st["clocks"][k[6:]] + n))
            elif k == "hp": st["hp"] = max(0, min(st["max_hp"], st["hp"] + n))
            else: st[k] = max(0, st.get(k, 0) + n) if k in ("pipe", "gambit", "coin") else st.get(k, 0) + n
def enter(st, i):
    for _ in range(8):
        st["scene"] = i; sc = S[i]; key = "_e_" + i
        if key not in st["flags"]: st["flags"][key] = 1; fx(st, sc.get("on_enter", []))
        else: fx(st, sc.get("on_reenter", []))
        nxt = ""
        if st["hp"] <= 0 and i != "death": nxt = "death"
        else:
            for r in sc.get("redirect", []):
                if req(st, r["if"]): nxt = r["goto"]; break
        if not nxt or nxt == i: return i
        i = nxt
    return i
def roll(st, stat):
    t = random.randint(1, 6) + random.randint(1, 6) + MODS[stat]
    if st["gambit"] > 0 and t in (6, 9): st["gambit"] -= 1; t += 1
    return "hit" if t >= 10 else "mixed" if t >= 7 else "miss"

ends, locks, visits = collections.Counter(), collections.Counter(), collections.Counter()
N = 20000
for _ in range(N):
    st = new(); cur = enter(st, "c1_ford"); steps = 0
    while steps < 600:
        steps += 1; visits[cur] += 1; sc = S[cur]
        if "ending" in sc: ends[sc["ending"]] += 1; break
        ch = [c for c in sc.get("choices", []) if req(st, c.get("req"))]
        if not ch: locks[cur] += 1; break
        c = random.choice(ch); fx(st, c.get("fx", []))
        if "check" in c:
            k = roll(st, c["check"]["stat"]); fx(st, c["check"].get(k + "_fx", [])); cur = enter(st, c["check"][k])
        elif "random" in c: cur = enter(st, random.choice(c["random"]))
        else: cur = enter(st, c["goto"])
    else: locks["LOOP>600:" + cur] += 1
print("endings:"); [print(f"  {v/N:6.1%}  {k}") for k, v in ends.most_common()]
print("softlocks:", dict(locks) or "none")
print("never visited:", sorted(set(S) - set(visits)) or "none")
