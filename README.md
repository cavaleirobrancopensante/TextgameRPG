# The King in Flight — a branching mobile text RPG (Godot 4.7)

You are **Gregory VII, the Exiled**. The lich Malgareth's legion has broken your realm at the Ford;
you carry the Skull of Saint Gregory II the Undying, a Court of loyal retainers, and nothing else.
Seven chapters, ~180 scenes, 2d6 "Dungeon World"-style checks (10+ success, 7–9 at a cost, 6− failure),
Gambits, two nested clocks (the siege above, the supplies below) and **8 endings**.

## Run
Open the folder in Godot 4.7 and press play (portrait, 720×1280, Mobile renderer).
For Android add an export preset (Project → Export → Android). Progress autosaves to `user://save.json`.

## Layout
- `scripts/story_engine.gd` — game logic (state, conditions, effects, checks, save/load)
- `scripts/main.gd` — touch UI built in code
- `data/story.json` — compiled story (generated)
- `tools/story/ch1..ch7.py` — **story source** (edit these), `tools/dsl.py` helpers
- `tools/build_story.py` — compiles + validates every link, dead end and reachability
- `tools/simulate.py` — random playtester (finds soft-locks, shows ending distribution)

## Editing the story
```
python3 tools/build_story.py   # rebuild data/story.json and validate
python3 tools/simulate.py      # playtest 20,000 random runs
```
Conditions (`req`): `flag`, `!flag`, `court:Name`, `hp>=5`, `clock.siege>=3`, combine with `&`.
Effects: `set:flag`, `clear:flag`, `add:hp:-3`, `add:clock.delve:1`, `court:+Name`, `if:<req>?<effect>`.
Text may contain `{{flag|shown if flag}}` / `{{!flag|shown if not}}`.
