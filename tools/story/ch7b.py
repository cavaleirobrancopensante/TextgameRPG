from dsl import *
C = "Chapter VII — The Descent"
RD = [{"if": "clock.siege>=6", "goto": "end_siege"}, {"if": "clock.delve>=6", "goto": "end_starve"}]

def room(id, title, text, options, back):
    """options: (label, result, fx, req). Each result scene returns to `back`."""
    choices = []
    for n, (label, result, fx, req) in enumerate(options):
        rid = f"{id}_r{n}"
        sc(rid, title, result, [ch("Return to the stair.", back)], enter=fx, redirect=RD, chapter=C)
        choices.append(ch(label, rid, req=req))
    sc(id, title, text, choices, enter=["add:explored:1"], redirect=RD, chapter=C)

# ---------------- side-chamber pools ----------------
room("c7_r1a", "The Flooded Chapel", "A chapel of the dwarf-saints, knee-deep in black water. An altar of grey stone, a drowned bell, a faint smell of lilies.", [
    ("Pray at the altar.", "A cold peace. You rise lighter.", ["add:hp:4", "add:xp:1"], None),
    ("Search the altar's base.", "A reliquary, sealed. Inside, a thumb-bone of some dwarf-saint. Anselm reverently pockets it.", ["set:relic_shard", "add:xp:1", "add:clock.delve:1"], None),
], "c7_l1")
room("c7_r1b", "The Fungus Garden", "A cavern of pale mushrooms, tended once and never harvested. Some are edible. Some are not.", [
    ("Harvest carefully with Brom's lore.", "A basketful of good caps, enough for a week of stew.", ["add:clock.delve:-1", "add:xp:1"], "brom_ally"),
    ("Take what looks safe.", "You are mostly right. Roland spends a night being sick.", ["add:clock.delve:-1", "add:hp:-3"], None),
    ("Leave it. Fungus is not food.", "The caps nod gently in the draught as you walk away.", [], None),
], "c7_l1")
room("c7_r1c", "The Drowned Armoury", "Racks of dwarf-steel, half-submerged, rusting in the dark.", [
    ("Take what you can carry.", "A mail-shirt, two good axes, a helm. You are better armed.", ["add:max_hp:1", "add:hp:1", "add:clock.delve:1"], None),
    ("Leave it. The dead may need it more.", "A dwarf's ghost nods, from somewhere you cannot see.", ["add:renown:1"], None),
], "c7_l1")

room("c7_r2a", "The Counting-House", "A tiny office, desks and abacuses and a book of accounts the size of a door. Whoever kept the ledger kept it faithfully until the end.", [
    ("Read the ledger.", "Every coin in the hoard is recorded, and beside each entry, a name. The god tracks what it owns. Take the ledger and you could unmake the hoard.", ["set:knows_weakness", "set:hoard_ledger", "add:xp:2"], None),
    ("Burn it. The numbers should not exist.", "The ledger burns green. Somewhere above you, a coin rings.", ["add:xp:1", "add:renown:1"], None),
], "c7_l2")
room("c7_r2b", "The Mimic Vault", "A small chamber. A chest, open, gold glittering. Too obvious.", [
    ("Test it with a spear.", "The chest bites the spear in half. You step back, smiling, as it settles.", ["add:xp:1"], None),
    ("Open it anyway. (+100 coin.)", "It bites. The coin is real. You are missing a fingertip.", ["add:coin:100", "add:hp:-5", "add:corruption:1"], None),
    ("Leave.", "A wise decision.", [], None),
], "c7_l2")
room("c7_r2c", "The Idol Gallery", "A hundred golden idols in a hundred poses of reverence. Each wears the face of the thing below.", [
    ("Look away. Walk quickly.", "The idols watch you go.", ["add:xp:1"], None),
    ("Study one. Know your enemy.", "Its face is not a face. It is a hundred faces folded together. You see it in your dreams for weeks.", ["add:xp:2", "add:hp:-2", "set:knows_god_face"], None),
    ("Pry out a gem. A king's pocket is never full.", "A ruby the size of an egg. It is warm. It is humming.", ["add:coin:90", "add:corruption:1"], None),
], "c7_l2")

room("c7_r3a", "The Sergeant's Room", "A small room with a bunk, a table, a dead dwarf slumped in a chair. A journal open before him.", [
    ("Read the journal.", "He recorded the lich's coming, and the six levels, and a back-way around the Market: a ladder behind the third pillar.", ["set:deep_map", "add:xp:1"], None),
    ("Bury him.", "A small kindness. A small dignity. Hetta sings something under her breath.", ["add:renown:1", "add:clock.delve:1"], None),
], "c7_l3")
room("c7_r3b", "The Chained Pit", "A pit where the lich kept the living. Seven men, shackled, filthy, barely alive.", [
    ("Free them. Bring them up.", "They are weak, but they are alive. Seven more mouths for the road, and seven more reasons to win.", ["add:renown:2", "add:clock.delve:1", "add:xp:1"], None),
    ("Free them, and send them up with Hetta.", "They stumble toward the light. You hope.", ["add:renown:1", "add:xp:1"], "court:Hetta"),
    ("Leave them. There is not time.", "Their eyes follow you out. You do not look back.", ["add:renown:-1"], None),
], "c7_l3")
room("c7_r3c", "The Bunk Cellar", "A cellar of crates and sacks beneath the barracks. Dry. Dry! Whole sacks of hard bread.", [
    ("Take the bread.", "You have not eaten this well since Aldermont.", ["add:clock.delve:-1", "add:hp:3"], None),
], "c7_l3")

room("c7_r4a", "The Bone Library", "Shelves of books bound in grey skin. A scholar's reading room, lit by green fire.", [
    ("Read the first book on the first shelf.", "It is a grammar of the god's language. You can read it, somehow. It reads you back.", ["set:knows_god_name", "add:xp:2", "add:corruption:1"], None),
    ("Look for a book on binding.", "A slim volume on the binding of spirits: how to weaken a thing held by its own hoard.", ["set:knows_weakness", "add:xp:1"], None),
    ("Burn the library.", "The books scream as they burn. It is the worst sound you have heard.", ["add:xp:1", "add:renown:1", "add:hp:-2"], None),
], "c7_l4")
room("c7_r4b", "The Puppet Theatre", "A stage. A velvet curtain. Behind it, the skeleton of a child with strings attached.", [
    ("Cut the strings.", "The little bones fall in a heap. Roland says a quiet prayer.", ["add:xp:1", "add:renown:1"], None),
    ("Watch the play.", "The skeleton acts out the Ford. It is accurate. It is horrible.", ["add:xp:1", "set:knows_upstream"], None),
], "c7_l4")
room("c7_r4c", "The Pawn-Shop", "A shop with a dozen grey stalls. A pale clerk behind the counter does not look at you, but speaks.", [
    ("Sell a pipe-leaf for a charm of warding. (1 pipe)", "A small tin charm, warm as a bird. It will turn aside one blow.", ["add:pipe:-1", "add:max_hp:2", "add:hp:2"], "pipe>=1"),
    ("Buy a vial of stillwater. (50 coin)", "Drink it and the dead's stare cannot freeze you.", ["add:coin:-50", "set:stillwater"], "coin>=50"),
    ("Walk out.", "The clerk's smile follows you.", [], None),
], "c7_l4")

room("c7_r5a", "The Weeping Vault", "A vault where the stone itself weeps. The drops, if you catch them, burn like acid.", [
    ("Walk through quickly.", "Your sleeves are ruined. Your skin, mostly, is not.", ["add:hp:-2"], None),
    ("Collect the weeping in a flask.", "A vial of acid, perhaps useful against the god's hoard.", ["set:acid_flask", "add:xp:1"], None),
], "c7_l5")
room("c7_r5b", "The Echo Chamber", "A circular room that returns every sound three times. Your footsteps. Your breath. A fourth voice, quieter, speaking your name.", [
    ("Answer it.", "\"Gregory,\" it says. \"Come down. Come down and rest.\" You step back, shaking, with the voice still in your ear.", ["add:corruption:1", "add:xp:1"], None),
    ("Shout the saint's prayer.", "The echoes fall silent. The fourth voice does not return.", ["add:xp:1", "add:hp:2"], None),
], "c7_l5")
room("c7_r5c", "The Drowned Reliquary", "In a pool of black water, a casket of silver. A relic, half-submerged. You know the sign on the lid: Saint Gregory's own.", [
    ("Retrieve it, whatever the water does.", "A finger-bone of the saint. Anselm weeps. The Skull stirs in its box, as if greeted by a brother.", ["set:relic_shard", "set:skull_renewed", "add:xp:3", "add:hp:-3"], None),
    ("Pray over the casket and leave it.", "Some things are not for the taking.", ["add:xp:1", "add:renown:1"], None),
], "c7_l5")

# ---------------- camps ----------------
CONVOS = [
    ("roland", "Roland", "court:Roland", "Sir Roland has carried the standard since the defile. He sits with his back to a wall, sword across his knees.\n\n\"You never asked why I took the standard,\" he says. \"Nobody asked me to. I saw it fall. I couldn't bear to watch it lie there.\"\n\n{{bond_roland|You hold his shoulder. It's the closest thing to a prayer either of you has.}}",
        ["add:xp:1", "if:bond_roland?add:hp:6", "if:bond_roland?add:gambit:1"]),
    ("anselm", "Anselm", "court:Anselm", "Anselm has not slept since the Ford. He tells you, softly, that the Skull is lighter some days than others, and that on the heavy days he can feel it watching.\n\n\"I have wondered whether I am keeping it,\" he says, \"or whether it is keeping me.\"",
        ["add:xp:1", "set:anselm_confided", "add:gambit:1"]),
    ("durgan", "Durgan", "durgan_sworn", "Durgan sharpens his hammer by the fire, stone on iron, a hypnotic sound.\n\n\"Three hundred years I lived here,\" he says, \"and I never once walked past the Hoard. I heard it. I always heard it. Now I will see what it is.\"\n\n{{durgan_crown|He touches the crown at his belt and says nothing.}}",
        ["add:xp:1", "add:renown:1"]),
    ("theodore", "Theodore", "court:Theodore", "Sir Theodore does not sleep. He sits upright in the dark, and speaks only when addressed.\n\n\"I remember dying,\" he says. \"I remember the Ford, and then a very long quiet, and then your voice. I do not remember being afraid. Is that wrong?\"",
        ["add:xp:1", "set:theodore_confided"]),
    ("hetta", "Hetta", "court:Hetta", "Hetta spreads her cloak and tells you she has never trusted a king. Her father was a smith who refused to kneel to one. She says it with a grin.\n\n\"But you are a funny sort of king,\" she says. \"You listen.\"",
        ["add:xp:1", "add:renown:1"]),
]

def make_camp(n, back):
    camp = f"c7_camp{n}"
    choices = []
    for key, name, req, text, fx in CONVOS:
        rid = f"{camp}_{key}"
        reqs = "!talked_%s" % key
        if req and "|" not in req: reqs += " & " + req
        sc(rid, f"By the Fire: {name}", text, [ch("The fire dies low. Sleep.", camp)], enter=fx + ["set:talked_" + key], redirect=RD, chapter=C)
        choices.append(ch(f"Sit with {name}.", rid, req=reqs))
    choices.append(ch("Eat, sleep, and rise. (Recover 6 HP.)", back, fx=["add:hp:6", "set:camped_" + str(n)]))
    sc(camp, "A Camp in the Dark", """
You find a niche in the stone that is dry enough, and a corner that is quiet enough, and you make a small fire of dwarf-coal.

The mountain presses on all sides. Somewhere above, the world is burning. But for an hour, here, there is a fire and a few people who trust you.
""", choices, enter=["add:clock.delve:1"], reenter=[], redirect=RD, chapter=C)

for n, scene in [(1, "c7_l2"), (2, "c7_l3"), (3, "c7_l4"), (4, "c7_l5")]:
    make_camp(n, scene)

# ---------------- throne variants ----------------
sc("c7_final_skull_try", "A Dimmed Relic", """
Anselm lifts the Skull. It is not what it was. The light is smaller. The silence is shorter.

The god's four hundred eyes turn toward it, and it laughs, and the laugh is the sound of coins pouring.

"Smaller," it says. "Fainter. You spent some of it on a child."
""", [
    rk("Add your will to Anselm's. Bear the weight with him.", "WIS", "c7_final_skull", "c7_final_skull_cost", "c7_final_fight"),
    ch("Hold. The relic shard in your pocket may be enough.", "c7_final_skull", req="relic_shard"),
], redirect=RD, chapter=C)
sc("c7_final_skull_cost", "The Cost", """
The Skull holds. Anselm does not. He sinks to his knees, blood from his nose, hands white around the relic, and still holds it up.

The god comes apart, slowly, and Anselm does not rise again for a month.
""", [ch("Stand over what remains.", "c8_victory_hub")], enter=["add:xp:2", "set:god_dead", "set:anselm_hurt"], redirect=RD, chapter=C)

sc("c7_final_blade", "The Rune-Blade", """
You see it now: the seam in the throne where coin met bone. Durgan's rune on the blade begins to glow, a low red like banked coals.

"The heart," Malgareth said. The ledger said the heart. You step inside the god's reach, and drive the blade in.
""", [ch("Watch it come apart.", "c8_victory_hub")], enter=["add:xp:3", "set:god_dead", "add:hp:-4"], redirect=RD, chapter=C)

sc("c7_final_bell", "Far Above, A Bell", """
You hold. Roland holds. Theodore holds the door. The god's hundred arms beat on you like a storm.

And then, from very far above — a hundred feet of stone and six sealed levels — a sound. A single note, rolling down through the mountain like a thrown cloth. The Bell of Saint Gregory, with the Skull in its heart, ringing for the king.

The god *stops*. Coin by coin, bone by bone, it comes apart.
""", [ch("Stand over what remains.", "c8_victory_hub")], enter=["add:xp:3", "set:god_dead", "set:bell_finale"], redirect=RD, chapter=C)

sc("c7_final_horn", "The Horn of Durgan", """
Durgan lifts the great horn and blows a note that rattles the gold on the walls. From the stair behind you comes an answering roar, hundreds of voices, hammers on shields.

Bruni's dwarves pour into the throne-room like a flood of iron. The god turns to face them. It is the moment you have been waiting for.
""", [
    rk("Strike while it is distracted.", "STR", "c7_final_horn_hit", "c7_final_horn_hit", "c7_final_fight"),
], enter=["add:clock.siege:1"], redirect=RD, chapter=C)
sc("c7_final_horn_hit", "A Coalition of Stone", """
Dwarf and man and the undying knight strike together. The god cannot hold both fronts. Coin falls like rain.
""", [ch("Stand over what remains.", "c8_victory_hub")], enter=["add:xp:3", "set:god_dead", "add:renown:2"], redirect=RD, chapter=C)

sc("c7_final_malgareth", "The Steward Turns", """
A step on the stair. Another. A cloaked figure in grey stops at the doorway of the throne-room, and lifts his hood.

"I am tired of following," says Malgareth, and for the first time in three hundred years, he sounds young.

He raises his hand. The green light flares. The god turns to look at its steward, and for a moment, it is afraid.
""", [ch("Strike now!", "c8_victory_hub")], enter=["add:xp:3", "set:god_dead", "set:malgareth_helped", "set:malgareth_ok"], redirect=RD, chapter=C)

sc("c7_final_name", "The God Calls You By Name", """
\"Gregory,\" it says, in the voice you heard in the Echo Chamber, in the ledger, in the coin. \"You have carried a small hoard of your own. A crown, a Court, a kingdom's worth of guilt. I see it. I know its weight.\"

You are not sure whether it is lying.

\"Take mine. All of it. The Deepholt's treasure. The six levels. A thousand years of servants who never tire. And in return — only that you *keep* it.\"
""", [
    ch("Refuse. You are a king, not a hoarder.", "c7_throne"),
    ch("Take the hoard.", "end_goldking"),
], redirect=RD, chapter=C)

# ---------------- victory hub & endings ----------------
sc("c8_victory_hub", "The Quiet", """
The hum is gone. For the first time in a thousand years, the mountain is silent.

Above, a long way up, a bell rings. It sounds like the end of something.

{{god_dead|The coin of the god's hoard lies in drifts, dull and lifeless. It is only gold now.}}
""", [
    ch("Carry the Skull back up. The war is over.", "c8_peace"),
    ch("Install the Skull in a shrine at the Bell. Found the new Order of Saint Gregory.", "end_vigil"),
    ch("Free Malgareth. He has earned an end.", "end_malgareth", req="malgareth_ok"),
    ch("Bind yourself with the Skull, as Theodore was bound. Be the mountain's undying king.", "end_undying", req="court:Theodore"),
    ch("Stay below. Keep the Skull here, with the thing that cannot be allowed to rise again.", "end_sacrifice"),
], chapter=C)

sc("c8_peace", "The Peace", """
You climb for two days. At the top of the stair the sun is a white wound in the sky, and the dead lie on the slope like fallen wheat. Aldric is on the wall, and he sees the standard, and begins to weep.

The horde does not rise.

A kingdom has to decide what it is for. The war is done. What now?
""", [
    ch("March on the Ford with the levy. Reclaim the realm.", "end_return", req="drive_reclaim & renown>=3"),
    ch("Raise your heir to a throne that will outlast you.", "end_dynasty", req="drive_heir"),
    ch("Throw the greatest feast the mountain has ever seen.", "end_feast", req="drive_pleasure"),
    ch("Sit by the fire in the Great Hall and let the world be small.", "end_triumph"),
], chapter=C)

def ending(id, title, text, label):
    sc(id, title, text, ending=label, chapter=C)

ending("end_return", "The Return to the Ford", """
The levy marches in the spring: two thousand on foot, five hundred on mule, and the standard of the House of Gregory raised at the head. At the Ford, the river is clean and the dead are gone. The Ford is just water.

You plant the standard on the south bank. Halbrecht, who still does not call you Majesty, drives the post.

{{renown>=6|The first villages come to you before you have asked for them. By midsummer you have a thousand more people in the column, and you do not turn any of them away.}}
{{bors_saved|Bors rides at your right hand, spare and silent.}}{{alcuin_double|Alcuin writes the proclamation, and it is the best thing he ever wrote.}}{{theodore_back|Theodore holds the south bank. He does not sleep.}}

You are not the king you were. You are the king the Ford made. It will do.
""", "RECLAMATION — The Return to the Ford")

ending("end_dynasty", "The Dynasty", """
{{heir_healed|Your son grows into a tall, thin, watchful boy, with his mother's green eyes and your stubborn chin.}}{{heir_slow|Your son, the quiet one, grows with the patience of an oak.}}{{heir_emmet|Emmet grows into a king's heir with a wooden horse still tucked in his saddlebag.}}{{heir_tom|Tom takes the standard when you cannot carry it, one-legged and straight-backed.}}{{heir_aldric|Aldric takes the throne at twenty-one, and holds the mountain for fifty years.}}

You live to see his coronation. You live to see the crown on his head, in the Great Hall, among the dwarves and the monks and the fen-folk, and you whisper to Roland, who is very old now, that you were right to run.

Roland grunts. \"You were right to stop running.\"

The House of Gregory outlasts the Fall.
""", "DYNASTY — A Line That Outlasts the Fall")

ending("end_feast", "The Last Feast", """
It is the greatest feast the mountain has ever seen. Three hundred monks drunk on dwarf ale. Dwarves dancing with widows. A bard from the Fenmarch with a drum and an eel.

At midnight you climb onto a table and make a speech nobody remembers. You wake at noon on the floor of the Chapel with Roland's cloak over you and Ambrose, laughing, holding a cup of water.

\"A king should not drink so much,\" says the Abbot.

\"A king,\" you say, \"should have lived to need to.\"

{{isobel_durgan|Durgan and Isobel dance a slow, ridiculous waltz.}}{{queen_saoirse|Saoirse sits at your side and refuses to let you stand.}}
""", "PLEASURE — The Last Feast")

ending("end_vigil", "The Vigil of Saint Gregory", """
The Skull is set in the Bell, and the Bell is housed in a great round tower on the mountain's shoulder. Anselm and Ambrose found a new Order: the Vigil of Saint Gregory, whose sole purpose is to keep the dead lying down.

You do not rule them. You are their first pilgrim.

For a hundred years the Bell rings at dawn, and every dawn the dead lie still, and every dawn a monk in grey wool climbs the tower stair and says the saint's name aloud.

{{saint_favour|It is said that the saint himself smiled, the first morning, and that his smile was warm.}}
""", "VIGIL — The Order of Saint Gregory")

ending("end_malgareth", "A Lich Released", """
You speak the name Ambrose wrote. Malgareth hears it, and for the first time in three hundred years he looks like a man. His hands tremble. The green light drains from his eyes.

\"Thank you,\" he says. \"I have been tired for so long.\"

He turns to dust on the stair. He leaves behind a small, plain stool, and a ring of keys. The ring opens the sealed archive of the Deepholt, and in it, a great deal of knowledge the dwarves had lost.

{{bors_taken|You find in the archive the last letter Bors wrote, in his own hand. It is a very good letter.}}

Some things, you think, are not victories. They are mercies.
""", "MERCY — A Lich Released")

ending("end_undying", "The Undying King", """
Anselm raises the Skull and speaks the rite. It is like Theodore's, but not the same; you feel the breath leave your body, and then return, strange.

You do not age. You do not sleep. You do not tire. You sit on a plain stool in the Great Hall of the Deepholt with a pipe in your mouth, and over the years you watch your friends grow old and die: Roland, Durgan, Isobel, Saoirse, the boy Tom with his one leg.

At last, you are the only one who remembers the Ford.

It is not what you wanted. It is, you suppose, what you asked for.
""", "THE UNDYING KING")

ending("end_goldking", "The Gold King", """
The god takes you gently. There is no violence. Its hundred arms fold around you like a father's, and its voice is every comfort you have ever craved.

When you wake, you are on the throne. The god is not dead; it is *you*. You wear its form as easily as a coat. The hoard is yours, and the six levels, and a legion of drowned servants, patient as stone.

Roland kneels first. It is the worst thing you have ever seen.

You rule for a thousand years. They are a very long time.
""", "THE GOLD KING — The Hoarder Reborn")

ending("end_regency", "The Regency of Saoirse", """
You stay in the door while the others carry the Skull out. The god strikes you down in the third blow. The last thing you hear is Roland weeping, and the last thing you see is the standard, going up the stair.

Saoirse takes the regency. She holds it for eighteen years, with the fen-folk and the dwarves and the monks and an iron will. When your son is old enough, she hands him the crown with a small, secret smile, and says:

\"Your father ran, once. And then, once, he did not.\"
""", "REGENCY — The Fen-Queen's Crown")
