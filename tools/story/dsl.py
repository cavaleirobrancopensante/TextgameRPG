SCENES = []

def sc(id, title, text, choices=None, enter=None, reenter=None, redirect=None, ending=None, chapter=""):
    d = {"id": id, "title": title, "text": text.strip(), "chapter": chapter}
    if choices: d["choices"] = choices
    if enter: d["on_enter"] = enter
    if reenter: d["on_reenter"] = reenter
    if redirect: d["redirect"] = redirect
    if ending: d["ending"] = ending
    SCENES.append(d)

def ch(text, goto, req=None, fx=None):
    d = {"text": text, "goto": goto}
    if req: d["req"] = req
    if fx: d["fx"] = fx
    return d

def rnd(text, ids, req=None, fx=None):
    d = {"text": text, "random": ids}
    if req: d["req"] = req
    if fx: d["fx"] = fx
    return d

def rk(text, stat, hit, mixed, miss, req=None, fx=None, hit_fx=None, mixed_fx=None, miss_fx=None):
    chk = {"stat": stat, "hit": hit, "mixed": mixed, "miss": miss}
    if hit_fx: chk["hit_fx"] = hit_fx
    if mixed_fx: chk["mixed_fx"] = mixed_fx
    if miss_fx: chk["miss_fx"] = miss_fx
    d = {"text": text, "check": chk}
    if req: d["req"] = req
    if fx: d["fx"] = fx
    return d
