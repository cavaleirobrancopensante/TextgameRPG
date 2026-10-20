class_name StoryEngine
extends RefCounted
## Pure game logic: state, conditions, effects, 2d6 checks. No UI.

const STATS := {"STR": 1, "DEX": -1, "CON": 0, "INT": 2, "WIS": 0, "CHA": 3}
const CLOCK_MAX := 6

var scenes: Dictionary = {}
var meta: Dictionary = {}
var state: Dictionary = {}
var rng := RandomNumberGenerator.new()

func load_story(path: String) -> bool:
	var f := FileAccess.open(path, FileAccess.READ)
	if f == null:
		push_error("Cannot open story: " + path)
		return false
	var data = JSON.parse_string(f.get_as_text())
	if typeof(data) != TYPE_DICTIONARY:
		push_error("Story JSON invalid")
		return false
	scenes = data["scenes"]
	meta = data.get("meta", {})
	rng.randomize()
	return true

func new_game() -> void:
	state = {
		"scene": meta.get("start", "c1_ford"),
		"hp": 18, "max_hp": 18, "xp": 1, "level": 4, "coin": 180,
		"pipe": 5, "gambit": 0, "renown": 0, "corruption": 0,
		"flags": {}, "court": ["Roland", "Aymer", "Bors", "Alcuin", "Anselm", "Sam", "Wat"],
		"clocks": {"siege": 0, "delve": 0},
		"log": [],
	}

# ---------- conditions ----------
func _key_value(key: String) -> int:
	if key.begins_with("clock."):
		return int(state["clocks"].get(key.substr(6), 0))
	return int(state.get(key, 0))

func check_req(req) -> bool:
	if req == null or req == "":
		return true
	for part in String(req).split("&"):
		if not _check_one(part.strip_edges()):
			return false
	return true

func _check_one(p: String) -> bool:
	if p.begins_with("!court:"):
		return not state["court"].has(p.substr(7))
	if p.begins_with("court:"):
		return state["court"].has(p.substr(6))
	if p.begins_with("!"):
		return not state["flags"].has(p.substr(1))
	for op in [">=", "<=", "=="]:
		var i := p.find(op)
		if i > 0:
			return _cmp(_key_value(p.substr(0, i)), op, int(p.substr(i + 2)))
	return state["flags"].has(p)

func _cmp(a: int, op: String, b: int) -> bool:
	match op:
		">=": return a >= b
		"<=": return a <= b
		_: return a == b

# ---------- effects ----------
func apply_effects(fx: Array) -> void:
	for e in fx:
		_apply(String(e))

func _apply(e: String) -> void:
	if e.begins_with("if:"):
		# conditional effect: "if:<req>?<effect>"
		var q := e.find("?")
		if q > 0 and check_req(e.substr(3, q - 3)):
			_apply(e.substr(q + 1))
		return
	if e.begins_with("set:"):
		state["flags"][e.substr(4)] = true
	elif e.begins_with("clear:"):
		state["flags"].erase(e.substr(6))
	elif e.begins_with("court:+"):
		var n := e.substr(7)
		if not state["court"].has(n):
			state["court"].append(n)
	elif e.begins_with("court:-"):
		state["court"].erase(e.substr(7))
	elif e.begins_with("add:"):
		var bits := e.split(":")
		var key := bits[1]
		var amt := int(bits[2])
		if key.begins_with("clock."):
			var c := key.substr(6)
			state["clocks"][c] = clampi(int(state["clocks"][c]) + amt, 0, CLOCK_MAX)
		elif key == "hp":
			state["hp"] = clampi(state["hp"] + amt, 0, state["max_hp"])
		elif key == "pipe" or key == "gambit" or key == "coin":
			state[key] = maxi(0, int(state[key]) + amt)
		else:
			state[key] = int(state.get(key, 0)) + amt
		if key == "xp" and state["xp"] >= state["level"] + 7:
			state["xp"] -= state["level"] + 7
			state["level"] += 1
			state["max_hp"] += 1
			state["flags"]["level_up"] = true
	elif e.begins_with("log:"):
		state["log"].append(e.substr(4))

# ---------- checks ----------
## Returns {dice:[a,b], mod:int, total:int, tier:"hit"|"mixed"|"miss", spent_gambit:bool}
func roll_check(stat: String) -> Dictionary:
	var a := rng.randi_range(1, 6)
	var b := rng.randi_range(1, 6)
	var mod: int = STATS.get(stat, 0)
	var total := a + b + mod
	var spent := false
	if state["gambit"] > 0 and (total == 6 or total == 9):
		state["gambit"] -= 1
		total += 1
		spent = true
	var tier := "miss"
	if total >= 10:
		tier = "hit"
	elif total >= 7:
		tier = "mixed"
	return {"dice": [a, b], "mod": mod, "total": total, "tier": tier, "spent_gambit": spent}

func pick_random(ids: Array) -> String:
	return String(ids[rng.randi_range(0, ids.size() - 1)])

# ---------- text templating ----------
## Inline conditionals in scene text: {{flag|shown if flag}} or {{!flag|shown if not}}.
func render_text(t: String) -> String:
	var out := ""
	var i := 0
	while true:
		var a := t.find("{{", i)
		if a < 0:
			out += t.substr(i)
			break
		out += t.substr(i, a - i)
		var b := t.find("}}", a)
		if b < 0:
			out += t.substr(a)
			break
		var inner := t.substr(a + 2, b - a - 2)
		var bar := inner.find("|")
		if bar > 0 and check_req(inner.substr(0, bar)):
			out += inner.substr(bar + 1)
		i = b + 2
	return out

# ---------- scene flow ----------
func current() -> Dictionary:
	return scenes[state["scene"]]

## Enter a scene: apply on_enter effects, handle redirects and death. Returns final scene id.
func enter(id: String) -> String:
	var guard := 0
	while guard < 8:
		guard += 1
		state["scene"] = id
		var sc: Dictionary = scenes[id]
		if not state["flags"].has("_entered_" + id):
			state["flags"]["_entered_" + id] = true
			apply_effects(sc.get("on_enter", []))
		else:
			apply_effects(sc.get("on_reenter", []))
		var nxt := ""
		if state["hp"] <= 0 and id != meta.get("death", "death"):
			nxt = meta.get("death", "death")
		else:
			for r in sc.get("redirect", []):
				if check_req(r.get("if", "")):
					nxt = r["goto"]
					break
		if nxt == "" or nxt == id:
			return id
		id = nxt
	return id

func visible_choices(sc: Dictionary) -> Array:
	var out := []
	for c in sc.get("choices", []):
		if check_req(c.get("req", "")):
			out.append(c)
	return out

# ---------- save/load ----------
const SAVE_PATH := "user://save.json"

func save_game() -> void:
	var f := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(state))

func has_save() -> bool:
	return FileAccess.file_exists(SAVE_PATH)

func load_game() -> bool:
	var f := FileAccess.open(SAVE_PATH, FileAccess.READ)
	if f == null:
		return false
	var d = JSON.parse_string(f.get_as_text())
	if typeof(d) != TYPE_DICTIONARY or not scenes.has(d.get("scene", "")):
		return false
	state = d
	for k in ["hp", "max_hp", "xp", "level", "coin", "pipe", "gambit", "renown", "corruption"]:
		state[k] = int(state.get(k, 0))
	for k in state["clocks"].keys():
		state["clocks"][k] = int(state["clocks"][k])
	return true
