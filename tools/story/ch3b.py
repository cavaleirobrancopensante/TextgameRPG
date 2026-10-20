from dsl import *
C = "Chapter III — The Weald"

POOL = ["c3_dng_patrol", "c3_dng_wolves", "c3_dng_hamlet", "c3_dng_rest", "c3_dng_shrine", "c3_dng_hermit",
        "c3_dng_deserters", "c3_dng_ghost", "c3_dng_orchard", "c3_dng_bridge", "c3_dng_herald", "c3_dng_wisp", "c3_dng_child"]

sc("c3_leg", "The Road Winds On", """
Another day of oak and leaf-mould. The column is thinner than it was. The children have stopped asking how far.

The road forks again, as roads do.
""", [
    rnd("Take the high road, along the ridge.", POOL),
    rnd("Take the low road, along the stream.", POOL),
    rnd("Take the game-trail through the beech wood.", POOL),
], enter=["add:leg:1"], reenter=["add:leg:1"], redirect=[{"if": "leg>=3", "goto": "c3_hills"}], chapter=C)

sc("c3_dng_shrine", "A Roadside Shrine", """
A weathered stone shrine under an oak, carved with a skull-and-halo you know very well: Saint Gregory, patron of your house. Someone has been here recently; a candle stub burns in the niche.

Whoever it was is gone. The candle is still warm.
""", [
    rk("Pray, and listen. Perhaps the saint will answer.", "WIS", "c3_shrine_hit", "c3_shrine_mixed", "c3_shrine_miss"),
    ch("Relight the candle and move on.", "c3_leg", fx=["add:renown:1"]),
], chapter=C)
sc("c3_shrine_hit", "A Small Miracle", """
There is no voice. There is only a feeling, like warm hands on your shoulders, and the sudden knowledge that you were not abandoned at the Ford. When you open your eyes your wounds have closed.
""", [ch("Go on.", "c3_leg")], enter=["add:hp:8", "add:xp:1", "set:saint_favour"], chapter=C)
sc("c3_shrine_mixed", "A Quiet Hour", """
The silence is restful, at least. You rise stiff and calm.
""", [ch("Go on.", "c3_leg")], enter=["add:hp:3"], chapter=C)
sc("c3_shrine_miss", "Unanswered", """
Nothing. A crow laughs. You suppose even saints have their silences, and yours is longer than most.
""", [ch("Go on.", "c3_leg")], chapter=C)

sc("c3_dng_hermit", "The Hermit of the Ash Tree", """
A wizened man in a coat of sewn rabbit-skins sits cross-legged on the track, refusing to move. He claims to be four hundred years old, and does not look it, and does not look much younger.

"I have news," he says. "I will trade it for tobacco."
""", [
    ch("Give him a pipe-leaf. (Costs 1 pipe.)", "c3_hermit_news", req="pipe>=1", fx=["add:pipe:-1"]),
    ch("Give him coin. (20)", "c3_hermit_news", req="coin>=20", fx=["add:coin:-20"]),
    ch("Walk around him.", "c3_leg"),
], chapter=C)
sc("c3_hermit_news", "The Hermit's News", """
"The lich walks behind his host, never in it. He cannot stand the sound of running water. The Skull's bearer is alive, I think; I smelled smoke from a shepherd's hut. And there's a thing *beneath* the dwarves' mountain that sings in my sleep."

He smiles. "That is all. That will be enough, if you are lucky."
""", [ch("Thank him.", "c3_leg")], enter=["add:xp:1", "set:knows_deep", "set:knows_river_weakness"], chapter=C)

sc("c3_dng_deserters", "Deserters", """
Eleven men in the muddy remains of your own army's colours sit around a fire. They stand when they see the column, weapons half-drawn. They look ashamed, and starving, and dangerous.

Their sergeant is a broad woman named Corbin with a scar through one eyebrow.

"We ran at the Ford," she says flatly. "I'll not lie about it. Now do you hang us, or do you feed us?"
""", [
    ch("Feed them. Take their oaths. A soldier who has run once will not run twice.", "c3_deserters_recruit", fx=["set:deserters_recruited", "add:renown:1"]),
    rk("Shame them into service. Remind them whose banner they wear.", "CHA", "c3_deserters_recruit", "c3_deserters_half", "c3_deserters_fight"),
    ch("Hang the sergeant. The rest may follow or starve.", "c3_deserters_hang", fx=["add:renown:-1"]),
    ch("Leave them be. You have no food to spare.", "c3_leg"),
], chapter=C)
sc("c3_deserters_recruit", "Corbin's Eleven", """
They kneel one at a time, awkwardly. Corbin keeps her eyes down until the last, then meets yours.

"I'll hold your bridge, sire," she says. "I'll hold it until I'm dead. It'd be a better end than the last."
""", [ch("Move on, a little stronger.", "c3_leg")], enter=["set:deserters_recruited", "court:+Corbin", "add:xp:1"], chapter=C)
sc("c3_deserters_half", "Grudging Service", """
They follow, but they do not forgive. Corbin marches at the back of the column, watching your back with a look that could be loyalty or the opposite.
""", [ch("Move on.", "c3_leg")], enter=["set:deserters_recruited", "set:corbin_sour", "court:+Corbin"], chapter=C)
sc("c3_deserters_fight", "Steel Drawn", """
They don't want to fight, but fear makes fools of everyone. A short, ugly scuffle later, three of them are dead and you have a gash across the thigh.
""", [ch("Move on.", "c3_leg")], enter=["add:hp:-3", "add:renown:-1"], chapter=C)
sc("c3_deserters_hang", "The Sergeant on the Branch", """
Corbin dies in silence. The remaining ten eat your rations and follow, because they have nowhere else to go. They will never look at you again.
""", [ch("Move on.", "c3_leg")], enter=["set:deserters_cowed", "add:xp:1"], chapter=C)

sc("c3_dng_ghost", "The Soldier at the Ford of the Stream", """
A pale figure stands in the water of a shallow ford: a young soldier in your colours, knee-deep, staring up the stream. He does not move. He does not blink. He is not undead; undead do not weep.

"I am waiting for my captain," he says to no one. "He said to hold the ford."
""", [
    rk("Speak to him gently. Release him from his post.", "WIS", "c3_ghost_hit", "c3_ghost_mixed", "c3_ghost_miss"),
    ch("Salute him. Let him keep his post.", "c3_leg", fx=["add:renown:1"]),
], chapter=C)
sc("c3_ghost_hit", "Relieved of Duty", """
"Stand down, soldier," you say, and he does, smiling, grateful, and fades into the water like a held breath. Something warm settles in your chest.
""", [ch("Go on.", "c3_leg")], enter=["add:xp:1", "add:hp:3"], chapter=C)
sc("c3_ghost_mixed", "An Answering Nod", """
He looks at you. He nods. He does not leave, but he turns to face the water, and for the first time stops weeping.
""", [ch("Go on.", "c3_leg")], chapter=C)
sc("c3_ghost_miss", "A Cold Hand", """
He turns, and the weeping stops, and for a moment you see the thing the Ford made of him. Cold fingers brush your face. You flinch, run, and are quiet for the rest of the day.
""", [ch("Go on.", "c3_leg")], enter=["add:hp:-2"], chapter=C)

sc("c3_dng_orchard", "The Abandoned Orchard", """
Apple trees in a half-wild orchard, fruit heavy on the branch. Bees in the blossom. The air smells like the end of summer.

It is the loveliest place you have seen in a year, and for a moment you forget the dead.
""", [
    ch("Camp here a night. Eat. Rest. Let the children climb the trees.", "c3_orchard_rest"),
    ch("Pick what you can carry and move on.", "c3_leg", fx=["add:hp:2", "add:coin:10"]),
], chapter=C)
sc("c3_orchard_rest", "A Night Among Apples", """
{{drive_pleasure|You dance with a miller's daughter and lose three hours to cider. In the morning you feel ten years younger.}}{{!drive_pleasure|Alcuin plays the lute under the stars. The children sleep in a heap. You sit with your pipe and let the world be small.}}
""", [ch("In the morning, go on.", "c3_leg")], enter=["add:hp:6", "add:renown:1", "if:drive_pleasure?add:xp:2"], chapter=C)

sc("c3_dng_bridge", "The Broken Bridge", """
A stone bridge over a fast, cold river. The middle arch has fallen in; the supports stand like broken teeth. Beyond lies the road. The dead cannot swim, but neither can the column.
""", [
    rk("Engineer a crossing: fell trees, build a raft-bridge.", "INT", "c3_bridge_hit", "c3_bridge_mixed", "c3_bridge_miss"),
    ch("Send scouts to find another ford. It will take a day.", "c3_leg", fx=["add:coin:-10"]),
], chapter=C)
sc("c3_bridge_hit", "A Good Bridge", """
In four hours you have a crossing that will take wagons. Halbrecht, if he is with you, looks at it with grudging admiration.
""", [ch("Cross.", "c3_leg")], enter=["add:xp:1", "add:renown:1"], chapter=C)
sc("c3_bridge_mixed", "It Holds", """
It holds, mostly. A cart goes into the river, with a sack of seed in it.
""", [ch("Cross.", "c3_leg")], enter=["add:coin:-10"], chapter=C)
sc("c3_bridge_miss", "The Raft Turns", """
The first raft capsizes. A man drowns in the shallows. The second works. The column crosses in grim silence.
""", [ch("Cross.", "c3_leg")], enter=["add:hp:-2", "add:renown:-1"], chapter=C)

sc("c3_dng_herald", "A Herald Under a White Flag", """
A single rider in grey with a white flag trots down the road toward you, stops, and bows. He is not dead, you realise; he is a man, thin and sallow, wearing the livery of the Western March.

"Lord Varric sends his compliments to the Gregorian," he says, "and begs to know whether the king will treat."
""", [
    ch("Hear the herald out.", "c3_herald_hear"),
    ch("Hang the herald from the nearest oak.", "c3_herald_hang", fx=["add:renown:-1"]),
    ch("Send the herald back with a message: \"Come yourself.\"", "c3_leg", fx=["add:xp:1"], req="knows_varric"),
    ch("Send the herald back with a message: \"Come yourself.\"", "c3_leg", fx=["add:xp:1"]),
], chapter=C)
sc("c3_herald_hear", "Varric's Offer", """
"My lord says there is a way for the realm to live, and for you to live in it. He asks only the Skull, for the master he serves does not wish you harm. He asks you to consider that the Ford was not a defeat. It was an *invitation*."

The herald smiles weakly. "I am only paid to say it."
""", [
    ch("\"Tell your lord I will see him in the dust.\"", "c3_leg", fx=["set:varric_hostile", "add:xp:1"]),
    ch("Keep the herald as a hostage. He may know things.", "c3_herald_hostage"),
], chapter=C)
sc("c3_herald_hostage", "A Reluctant Guest", """
The herald is no hero. In an hour he has told you what he knows: Varric commands a small host in the west, serves a "grey lord" who is a steward of something older, and is very, very afraid of being replaced.
""", [ch("Go on.", "c3_leg")], enter=["set:knows_steward", "set:knows_varric", "add:xp:1"], chapter=C)
sc("c3_herald_hang", "A Short Rope", """
The herald dies without a word. Roland looks at the oak, and then at you, and then at the oak again.
""", [ch("Go on.", "c3_leg")], chapter=C)

sc("c3_dng_wisp", "Lights in the Marsh", """
Pale blue lights hover above a stretch of bog. They bob and flicker. Alcuin whispers that they say a treasure is buried in the middle.

Hetta, if she were here, would tell you wisps are not honest. But Hetta is not here.
""", [
    rk("Follow the lights. (A king can't resist gold.)", "WIS", "c3_wisp_hit", "c3_wisp_mixed", "c3_wisp_miss"),
    ch("Burn them off with torches.", "c3_leg"),
    ch("Lead the column around the bog.", "c3_leg", fx=["add:coin:-5"]),
], chapter=C)
sc("c3_wisp_hit", "A Cache in the Marsh", """
The wisps lead to a drowned shrine, and in the shrine, a dwarf-made chest of coin and a ring of green stone. You take the coin, not the ring.
""", [ch("Go on.", "c3_leg")], enter=["add:coin:80", "add:xp:1"], chapter=C)
sc("c3_wisp_mixed", "Mud and Coin", """
You find a few coins in the muck and lose your boots in the bog.
""", [ch("Go on.", "c3_leg")], enter=["add:coin:20"], chapter=C)
sc("c3_wisp_miss", "Drowning Lights", """
The lights lead in. You go in. Roland drags you out by the hair. You will not be going into bogs for some time.
""", [ch("Go on.", "c3_leg")], enter=["add:hp:-5"], chapter=C)

sc("c3_dng_child", "A Lost Child", """
A boy of six sits in the middle of the road, clutching a wooden horse. He says his name is Emmet. He says the dead took his mother "gently". He doesn't cry; he's past it.

The column parts around him and does not know what to do.
""", [
    ch("Take Emmet in. He rides with you.", "c3_child_adopt", fx=["set:emmet_adopted", "add:renown:1"]),
    ch("Send him to the abbey with a guide.", "c3_leg"),
    ch("Leave coin and food with him and go. You have no room.", "c3_leg", fx=["add:coin:-5", "add:renown:-1"]),
], chapter=C)
sc("c3_child_adopt", "A Boy on a Wagon", """
Emmet rides on Maud's wagon next to Tom. By nightfall he has stopped speaking about the dead and started speaking about the horse.

{{drive_heir|You find yourself thinking of the heir you do not have, and of the odd arithmetic of love.}}
""", [ch("Go on.", "c3_leg")], enter=["add:xp:1", "if:drive_heir?add:xp:1"], chapter=C)
