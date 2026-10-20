"""Post-import patches: add choices / reroute existing scenes without hand-editing earlier chapter files."""
import dsl
def S(i):
    for s in dsl.SCENES:
        if s["id"] == i: return s
    raise KeyError(i)
def add_choice(scene, choice, index=None):
    s = S(scene); s.setdefault("choices", [])
    if index is None: s["choices"].append(choice)
    else: s["choices"].insert(index, choice)
def add_enter(scene, fx): S(scene).setdefault("on_enter", []).extend(fx)
def set_redirect(scene, rd): S(scene).setdefault("redirect", []).extend(rd)
def reroute(scene, old, new):
    for c in S(scene).get("choices", []):
        if c.get("goto") == old: c["goto"] = new
        for k in ("hit", "mixed", "miss"):
            if "check" in c and c["check"][k] == old: c["check"][k] = new
from dsl import ch, rk, rnd

# --- Aldermont hub additions ---
add_choice("c2_town", ch("Something is wrong in the column. A thread, a bird, a whisper.", "c2_spy", req="!spy_started & bael_keys"), 3)
add_choice("c2_town", ch("Sit with Lady Isobel and her ledger.", "c2_isobel", req="!did_isobel"), 3)
add_choice("c2_town", ch("The dead lord's cellar is still full.", "c2_cellar", req="!did_cellar"), 3)
add_choice("c2_town", ch("Raise the standard on Aldermont's keep.", "c2_standard", req="drive_reclaim & !did_standard"), 3)

# --- betrayal at the bridge if an active spy was never dealt with ---
set_redirect("c5_siege", [{"if": "spy_active & !spy_done", "goto": "c5_betrayal"}])

# --- Deepholt hub ---
for sid in ("c4_brom_save", "c4_brom_nan"):
    reroute(sid, "c4_theodore", "c4_hub")
reroute("c4_brom", "c4_theodore", "c4_hub")
# durgan recruit Hetta
add_enter("c4_gate", ["court:+Hetta"])

# --- Fenmarch / siege ---
add_choice("c5_fenmarch", ch("\"First, the marsh-wraiths. Let me earn your ear.\"", "c5_wraith", req="!wraiths_cleared"), 0)
reroute("c5_stall", "c5_prep", "c5_three_days")
add_choice("c5_three_days", ch("Use Pell's letters: the lich has been reading what we wrote.", "c5_feint_hit", req="pell_double"), 2)
add_choice("c5_prep", ch("Challenge the host's champion to single combat on the bridge.", "c5_champion", req="!champion_done"), 1)
add_choice("c5_prep", ch("No Bell, no rafts: hold the bridge with pikes.", "c5_bridge_hold"), 3)

# --- Mountain ---
reroute("c6_found", "c6_year", "c6_season")
S("c6_found")["redirect"] = [{"if": "built>=3", "goto": "c6_season"}]
S("c6_year")["choices"] = [
    ch("Hold the child. Name him.", "c6_heir", req="queen_saoirse"),
    ch("Continue.", "c6_adopt", req="!queen_saoirse & drive_heir"),
    ch("Continue.", "c6_feast", req="!queen_saoirse & !drive_heir"),
]
reroute("c6_heir", "c6_feast", "c6_heir_choice")

# --- six-year text fix ---
S("c6_year")["text"] = S("c6_year")["text"].replace(
"By the next autumn there are children playing in the courtyard. By the autumn after that, a baby is born in the royal chambers: a frail, red-haired, green-eyed boy who does not cry as loud as he should.",
"By the next autumn there are children playing in the courtyard.\n\n{{queen_saoirse|By the autumn after that, a baby is born in the royal chambers: a frail, red-haired, green-eyed boy who does not cry as loud as he should.}}{{!queen_saoirse|You sit at the high table, and look at the empty chair beside you, and think about lines that end.}}")

# --- Descent additions ---
def side(level_scene, n, pool):
    add_choice(level_scene, rnd("Explore a side-chamber.", pool, req=f"!explored_L{n}", fx=[f"set:explored_L{n}"]))
side("c7_l1", 1, ["c7_r1a", "c7_r1b", "c7_r1c"])
side("c7_l2", 2, ["c7_r2a", "c7_r2b", "c7_r2c"])
side("c7_l3", 3, ["c7_r3a", "c7_r3b", "c7_r3c"])
side("c7_l4", 4, ["c7_r4a", "c7_r4b", "c7_r4c"])
side("c7_l5", 5, ["c7_r5a", "c7_r5b", "c7_r5c"])
for n, lvl in [(1, "c7_l2"), (2, "c7_l3"), (3, "c7_l4"), (4, "c7_l5")]:
    add_choice(lvl, ch("Make camp before going on.", f"c7_camp{n}", req=f"!camped_{n}"), 0)
add_choice("c7_l1", ch("Hold up the delvers' lantern: the water-things shrink from its light.", "c7_l1_ok", req="delver_lantern", fx=["add:xp:1"]))
add_choice("c7_l1", ch("Descend by rope-shaft, bypassing the stair.", "c7_l2", req="delver_rope", fx=["add:clock.delve:1"]))
add_choice("c7_l3", ch("Hetta scouts a safe path among the bunks.", "c7_l3_ok", req="court:Hetta"))
add_choice("c7_l4", ch("The old map shows a ladder behind the third pillar. Skip the Market.", "c7_l5", req="deep_map"))
add_enter("c7_l2_purse", ["add:corruption:1"])
add_enter("c7_l2_loot", ["add:corruption:1"])

# throne
t = S("c7_throne")["choices"]
t[0]["req"] = "skull_below & !skull_dimmed"
add_choice("c7_throne", ch("Anselm lifts the Skull. It is dimmer than it was.", "c7_final_skull_try", req="skull_below & skull_dimmed"))
add_choice("c7_throne", ch("Drive Durgan's rune-blade into the seam: the heart of the throne.", "c7_final_blade", req="rune_blade & knows_weakness"))
add_choice("c7_throne", rk("Hold out until the Bell above is rung. Roland knows the hour.", "CON", "c7_final_bell", "c7_final_bell", "c7_final_fight", req="skull_above", mixed_fx=["add:hp:-4"]))
add_choice("c7_throne", ch("Sound Durgan's great horn. The dwarf-host will come.", "c7_final_horn", req="bruni_ally & durgan_sworn"))
add_choice("c7_throne", ch("You are not alone. Look to the stair.", "c7_final_malgareth", req="malgareth_ok"))
add_choice("c7_throne", ch("The god's voice sounds, very faintly, like your own.", "c7_final_name", req="corruption>=2"))
add_choice("c7_final_fight", ch("Hold the doorway while Roland carries the Skull out.", "end_regency", req="queen_saoirse"))
add_choice("c7_final_fight", ch("Hold the doorway while Roland carries the Skull out.", "end_sacrifice", req="!queen_saoirse"))
add_enter("c6_season", ["set:ferrand_dead"])
