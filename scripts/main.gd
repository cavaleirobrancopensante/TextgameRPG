extends Control
## Mobile UI for The King in Flight. Everything is built in code (portrait layout).

const STORY_PATH := "res://data/story.json"
const GOLD := Color("#c9a24b")
const INK := Color("#14110f")
const PAPER := Color("#e9dfc8")
const DIM := Color("#8d8472")
const FONT_BODY := 30
const FONT_BTN := 28

var engine := StoryEngine.new()
var bg: ColorRect
var root_box: VBoxContainer
var stats_label: Label
var chapter_label: Label
var title_label: Label
var scroll: ScrollContainer
var body: RichTextLabel
var choices_box: VBoxContainer
var menu_layer: Control

func _ready() -> void:
	if not engine.load_story(STORY_PATH):
		return
	_build_ui()
	_show_title()

# ---------- UI construction ----------
func _build_ui() -> void:
	bg = ColorRect.new()
	bg.color = INK
	bg.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(bg)

	var margin := MarginContainer.new()
	margin.set_anchors_preset(Control.PRESET_FULL_RECT)
	for side in ["left", "right", "top", "bottom"]:
		margin.add_theme_constant_override("margin_" + side, 24)
	# keep clear of notches / gesture bars
	var safe := DisplayServer.get_display_safe_area()
	if safe.size.x > 0:
		margin.add_theme_constant_override("margin_top", 24 + int(max(0, safe.position.y) * 0.5))
	add_child(margin)

	root_box = VBoxContainer.new()
	root_box.add_theme_constant_override("separation", 14)
	margin.add_child(root_box)

	var top := HBoxContainer.new()
	root_box.add_child(top)
	chapter_label = _label("", 22, DIM)
	chapter_label.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(chapter_label)
	var menu_btn := Button.new()
	menu_btn.text = "☰"
	menu_btn.custom_minimum_size = Vector2(80, 64)
	menu_btn.add_theme_font_size_override("font_size", 32)
	menu_btn.pressed.connect(_show_pause_menu)
	top.add_child(menu_btn)

	stats_label = _label("", 24, GOLD)
	stats_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	root_box.add_child(stats_label)

	title_label = _label("", 40, GOLD)
	title_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	root_box.add_child(title_label)

	scroll = ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	root_box.add_child(scroll)

	var inner := VBoxContainer.new()
	inner.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	inner.add_theme_constant_override("separation", 20)
	scroll.add_child(inner)

	body = RichTextLabel.new()
	body.bbcode_enabled = true
	body.fit_content = true
	body.scroll_active = false
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_font_size_override("normal_font_size", FONT_BODY)
	body.add_theme_font_size_override("bold_font_size", FONT_BODY)
	body.add_theme_font_size_override("italics_font_size", FONT_BODY)
	body.add_theme_color_override("default_color", PAPER)
	inner.add_child(body)

	choices_box = VBoxContainer.new()
	choices_box.add_theme_constant_override("separation", 14)
	choices_box.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	inner.add_child(choices_box)

func _label(t: String, size: int, col: Color) -> Label:
	var l := Label.new()
	l.text = t
	l.add_theme_font_size_override("font_size", size)
	l.add_theme_color_override("font_color", col)
	return l

func _make_button(text: String, cb: Callable, accent := false) -> Button:
	var b := Button.new()
	b.text = text
	b.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	b.custom_minimum_size = Vector2(0, 96)
	b.add_theme_font_size_override("font_size", FONT_BTN)
	b.alignment = HORIZONTAL_ALIGNMENT_LEFT
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color("#2a231c") if not accent else Color("#4a3a17")
	sb.border_color = GOLD
	sb.set_border_width_all(2)
	sb.set_corner_radius_all(10)
	sb.set_content_margin_all(16)
	b.add_theme_stylebox_override("normal", sb)
	var hov := sb.duplicate()
	hov.bg_color = Color("#3a3024")
	b.add_theme_stylebox_override("hover", hov)
	b.add_theme_stylebox_override("pressed", hov)
	b.add_theme_color_override("font_color", PAPER)
	b.pressed.connect(cb)
	return b

func _clear_choices() -> void:
	for c in choices_box.get_children():
		c.queue_free()

# ---------- screens ----------
func _show_title() -> void:
	_close_menu()
	chapter_label.text = ""
	stats_label.text = ""
	title_label.text = "THE KING IN FLIGHT"
	body.text = "[center][i]Gregory VII, the Exiled[/i]\n\nThe realm is ash. The dead march behind you.\nYou carry nothing but a crown, a court, and a saint's name.[/center]"
	_clear_choices()
	if engine.has_save():
		choices_box.add_child(_make_button("Continue", _on_continue, true))
	choices_box.add_child(_make_button("New Game", _on_new_game, not engine.has_save()))
	choices_box.add_child(_make_button("Quit", func(): get_tree().quit()))

func _on_new_game() -> void:
	engine.new_game()
	_go(engine.state["scene"])

func _on_continue() -> void:
	if engine.load_game():
		_render(engine.state["scene"])
	else:
		_on_new_game()

func _go(id: String) -> void:
	var final_id := engine.enter(id)
	engine.save_game()
	_render(final_id)

func _update_stats() -> void:
	var s := engine.state
	var t := "HP %d/%d   Lv %d   XP %d   Coin %d   Pipe %d" % [s["hp"], s["max_hp"], s["level"], s["xp"], s["coin"], s["pipe"]]
	if s["gambit"] > 0:
		t += "   Gambit %d" % s["gambit"]
	if s.get("renown", 0) != 0:
		t += "   Renown %d" % s["renown"]
	if s.get("corruption", 0) > 0:
		t += "   Taint %d" % s["corruption"]
	var cl: Dictionary = s["clocks"]
	if cl.get("siege", 0) > 0:
		t += "\nSiege above " + _pips(cl["siege"])
	if cl.get("delve", 0) > 0:
		t += "   Supplies below " + _pips(cl["delve"])
	stats_label.text = t

func _pips(n: int) -> String:
	return "●".repeat(n) + "○".repeat(StoryEngine.CLOCK_MAX - n)

func _render(id: String, prefix := "") -> void:
	var sc: Dictionary = engine.scenes[id]
	engine.state["scene"] = id
	chapter_label.text = sc.get("chapter", "")
	title_label.text = sc.get("title", "")
	_update_stats()
	var txt: String = prefix + engine.render_text(sc.get("text", ""))
	if engine.state["flags"].has("level_up"):
		engine.state["flags"].erase("level_up")
		txt = "[color=#c9a24b][b]You reach level %d.[/b][/color]\n\n" % engine.state["level"] + txt
	body.text = txt
	scroll.scroll_vertical = 0
	_clear_choices()
	if sc.has("ending"):
		_render_ending(sc)
		return
	for c in engine.visible_choices(sc):
		var label: String = c["text"]
		if c.has("check"):
			label += "  [%s]" % c["check"]["stat"]
		choices_box.add_child(_make_button(label, _on_choice.bind(c)))

func _render_ending(sc: Dictionary) -> void:
	body.text += "\n\n[center][color=#c9a24b][b]— %s —[/b][/color][/center]" % sc["ending"]
	choices_box.add_child(_make_button("Return to title", _on_finish, true))

func _on_finish() -> void:
	DirAccess.remove_absolute(ProjectSettings.globalize_path(StoryEngine.SAVE_PATH))
	_show_title()

func _on_save_quit() -> void:
	engine.save_game()
	_show_title()

func _on_choice(c: Dictionary) -> void:
	engine.apply_effects(c.get("fx", []))
	if c.has("check"):
		_resolve_check(c)
	elif c.has("random"):
		_go(engine.pick_random(c["random"]))
	else:
		_go(c["goto"])

func _resolve_check(c: Dictionary) -> void:
	var chk: Dictionary = c["check"]
	var r := engine.roll_check(chk["stat"])
	var tier: String = r["tier"]
	engine.apply_effects(chk.get(tier + "_fx", []))
	var sign_ := "+" if r["mod"] >= 0 else "−"
	var line := "[color=#8d8472]%s  %d + %d %s %d%s = %d  →  %s[/color]\n\n" % [
		chk["stat"], r["dice"][0], r["dice"][1], sign_, absi(r["mod"]),
		" +1 Gambit" if r["spent_gambit"] else "", r["total"],
		{"hit": "Full success", "mixed": "Success, at a cost", "miss": "Failure"}[tier]]
	var target: String = chk[tier]
	var final_id := engine.enter(target)
	engine.save_game()
	_render(final_id, line)

# ---------- pause menu ----------
func _show_pause_menu() -> void:
	if menu_layer:
		return
	menu_layer = Control.new()
	menu_layer.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(menu_layer)
	var dim := ColorRect.new()
	dim.color = Color(0, 0, 0, 0.85)
	dim.set_anchors_preset(Control.PRESET_FULL_RECT)
	menu_layer.add_child(dim)
	var m := MarginContainer.new()
	m.set_anchors_preset(Control.PRESET_FULL_RECT)
	for side in ["left", "right", "top", "bottom"]:
		m.add_theme_constant_override("margin_" + side, 40)
	menu_layer.add_child(m)
	var v := VBoxContainer.new()
	v.add_theme_constant_override("separation", 16)
	m.add_child(v)
	v.add_child(_label("The King's Court", 36, GOLD))
	var court := RichTextLabel.new()
	court.fit_content = true
	court.bbcode_enabled = true
	court.add_theme_font_size_override("normal_font_size", 28)
	var names: Array = engine.state["court"]
	court.text = "[color=#e9dfc8]" + (", ".join(names) if names.size() > 0 else "No one remains.") + "[/color]"
	v.add_child(court)
	var spacer := Control.new()
	spacer.size_flags_vertical = Control.SIZE_EXPAND_FILL
	v.add_child(spacer)
	v.add_child(_make_button("Resume", _close_menu, true))
	v.add_child(_make_button("Save and go to title", _on_save_quit))

func _close_menu() -> void:
	if menu_layer:
		menu_layer.queue_free()
		menu_layer = null
