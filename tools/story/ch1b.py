from dsl import *
C = "Chapter I — The Ford"

sc("c1_hub", "A Night in Tollmere", """
The column has a few hours before it must move. Tollmere is half-abandoned, but a half-abandoned town still has lamps, a smithy, and sick people. A king has hours, not days, and a hundred ways to spend them.
""", [
    ch("Help the sick and the lost in the refugee tents.", "c1_triage", req="!did_triage"),
    ch("Visit the smithy. Halbrecht may be able to arm the column.", "c1_forge", req="!did_forge"),
    ch("The Boar and Lantern still has its lamps lit. One drink. One song.", "c1_tavern", req="!did_tavern"),
    ch("Interview the people who saw the Ford. Piece together how it fell.", "c1_witness", req="!did_witness"),
    ch("Enough. Decide the fate of the Skull and move.", "c1_skull_split"),
], chapter=C)

sc("c1_triage", "The Tents", """
Mostly it is coughs and blisters and a very old woman who wants to know if the king has eaten. A child asks if the dead are really coming. You tell her the truth and she nods with tremendous seriousness.

You are not a physician. You can only do what a king can: sit, listen, and be seen.
""", [
    ch("Give your own ration to the old woman.", "c1_hub", fx=["set:did_triage", "add:renown:1", "add:hp:-1"]),
    ch("Organise the tents: water here, sick there, fires every ten paces.", "c1_hub", fx=["set:did_triage", "add:renown:1", "add:xp:1"]),
], chapter=C)

sc("c1_forge", "Halbrecht's Forge", """
Halbrecht keeps the forge going by himself. He takes in refugees' pots and pans and turns them into spearheads with unlovely efficiency.

"Pay me or don't," he says. "I'll arm whoever stands."
""", [
    ch("Commission mail for the knights. (40 coin)", "c1_hub", req="coin>=40", fx=["add:coin:-40", "set:did_forge", "set:knights_mailed", "add:max_hp:2", "add:hp:2"]),
    ch("Commission 200 spearheads for the column. (30 coin)", "c1_hub", req="coin>=30", fx=["add:coin:-30", "set:did_forge", "set:column_armed", "add:renown:1"]),
    ch("Ask him to teach your squires to forge. It's free.", "c1_hub", fx=["set:did_forge", "set:halbrecht_taught", "add:xp:1"]),
], chapter=C)

sc("c1_tavern", "The Boar and Lantern", """
The innkeeper refuses payment for the first cup and takes it for the second. A fiddler plays something rude. For ten minutes you are a man in a tavern, and the Ford is a story other people tell.
""", [
    ch("Drink deeply and let the evening carry you. (10 coin)", "c1_tavern_drink", req="coin>=10", fx=["add:coin:-10"]),
    ch("One cup, and listen to the room.", "c1_tavern_listen"),
    ch("Leave. This is not the night for it.", "c1_hub", fx=["set:did_tavern"]),
], chapter=C)

sc("c1_tavern_drink", "A King With a Cup", """
{{drive_pleasure|It is what you wanted. A warm room, a rough song, a stranger's laugh. You sleep two hours on a bench and wake restored.}}{{!drive_pleasure|It is pleasant, and a little shaming. You sleep badly on a bench and wake with the song stuck in your head.}}
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_tavern", "if:drive_pleasure?add:xp:2", "if:drive_pleasure?add:hp:6", "if:!drive_pleasure?add:hp:2"], chapter=C)

sc("c1_tavern_listen", "What the Room Knows", """
Three versions of the Ford, none the same. A drunk river-man swears the dead rose *from upstream*, before the line even broke. A tanner says the Duke's banner was already in the water. A girl says the lich walked across the water as if it were a road.

You pocket all three.
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_tavern", "set:knows_upstream", "add:xp:1"], chapter=C)

sc("c1_witness", "The Survivors", """
You find nine survivors and a ledger-clerk who counted them. Their accounts disagree on everything but one: Malgareth did not seem to be *winning* the battle. He seemed to be *searching* in it.
""", [
    ch("Ask about the Skull: who knew where it was kept?", "c1_witness_skull"),
    rk("Press them on the betrayal. Someone opened the gate.", "CHA", "c1_witness_hit", "c1_witness_mixed", "c1_witness_miss", req="fall_betrayed"),
    ch("Thank them and go.", "c1_hub", fx=["set:did_witness", "add:xp:1"]),
], chapter=C)

sc("c1_witness_skull", "Who Knew", """
Only three people knew where the relic was kept: the chaplain, who is dead; Anselm, who is here; and the Duke's steward, who is missing.

You write the missing steward's name in your head. It is a short list and now you know who is on it.
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_witness", "set:knows_steward_missing", "add:xp:1"], chapter=C)

sc("c1_witness_hit", "The Name", """
A boy of sixteen, shaking, remembers: it was Lord Varric of the Western March, who left his post at the river-gate half an hour before the dead rose. Not fled. *Left*, on foot, alone, with a bundle.

You have a name, now, to hate. It is a luxury.
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_witness", "set:knows_varric", "add:xp:1", "add:gambit:1"], chapter=C)

sc("c1_witness_mixed", "A Rumour of a Name", """
They give you a half-name — "Lord V-something, from the west" — and a direction. It is enough to start a nightmare.
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_witness", "set:knows_varric_half"], chapter=C)

sc("c1_witness_miss", "Frightened Silence", """
They close like clams. Nobody wants to be the man who named a lord on the road. You leave with nothing and a bad taste.
""", [ch("Back to the night.", "c1_hub")], enter=["set:did_witness"], chapter=C)

# --- Night raid, between Tollmere and Aldermont ---
sc("c1_night", "Fire in the Night", """
On the second night out of Tollmere, the first fire-arrow arrives. It hits a wain loaded with straw and tinder, and the wain becomes a torch.

*Wood burns,* Aymer said. The riders in grey have come, and they are shooting at the wagons, not at the people.

{{skull_kept|The Skull's box is in Anselm's wagon. It is the third from the front.}}{{skull_in_hills|The Skull is far from here, but the lich's riders do not know that. They are burning wagons to find it.}}
""", [
    rk("Organise a bucket line and a fire-break. Save the column.", "CHA", "c1_night_hit", "c1_night_mixed", "c1_night_miss"),
    rk("Hunt the archers in the dark with the knights.", "DEX", "c1_night_hunt_hit", "c1_night_hunt_mixed", "c1_night_miss"),
    ch("Use the Chessmaster's eye: where would *you* shoot from? (Spend a Gambit.)", "c1_night_hunt_hit", req="gambit>=1", fx=["add:gambit:-1"]),
], chapter=C)

sc("c1_night_hit", "The Column Holds", """
The line of buckets runs from the stream to the first wagon in under two minutes. The fire-break is a ditch dug by a hundred hands. The grey riders see a column that does not panic and turn their horses away.
""", [ch("Press on to Aldermont.", "c2_gate")], enter=["add:renown:1", "add:xp:1"], chapter=C)

sc("c1_night_mixed", "A Wagon Lost", """
You save the column but lose the lead wagon: grain, tools and blankets. The grey riders are gone by dawn, leaving only arrows in the earth and a smell of wet ash.
""", [ch("Press on to Aldermont.", "c2_gate")], enter=["add:coin:-20"], chapter=C)

sc("c1_night_miss", "Panic", """
A woman screams "the dead!" though there are no dead, and half the column stampedes into the dark. It takes until dawn to gather them. Eleven are missing. The wagons burned.
""", [ch("Press on to Aldermont.", "c2_gate")], enter=["add:coin:-40", "add:renown:-1", "add:hp:-2"], chapter=C)

sc("c1_night_hunt_hit", "A Rider Taken", """
You and the knights circle behind them in the dark. Two riders fall; the third is pulled from the saddle by Roland and pinned, still moving, still smiling.

"I can ask it questions," says Anselm quietly. "If you can stand the answers."
""", [
    ch("Question the grey rider.", "c1_prisoner"),
    ch("Burn it. Some questions have bad answers.", "c2_gate", fx=["add:xp:1"]),
], chapter=C)

sc("c1_night_hunt_mixed", "Two Archers Escape", """
You kill one rider and drive off another. The third is gone before you reach the tree-line. The wagon is lost, but the rest is saved.
""", [ch("Press on to Aldermont.", "c2_gate")], enter=["add:coin:-10", "add:xp:1"], chapter=C)

sc("c1_prisoner", "What the Dead Say", """
The grey rider speaks in a flat voice, answering what is asked and no more.

"The Master walks behind the host and will not come near the river. The Master serves one who sleeps below. The Master wants the sleeping thing, for the one who sleeps will not wake without it, but a thing in the Master's hands is a thing the one below cannot take."

It stops. Its jaw works. "That is all. That is all I know."

Anselm crosses himself. "He is afraid of what is below him."
""", [ch("Burn the rider. Press on.", "c2_gate")], enter=["set:knows_steward", "set:knows_deep", "add:xp:2", "add:gambit:1"], chapter=C)
