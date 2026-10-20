from dsl import *
C = "Chapter III — The Weald"

sc("c3_ashgrove", "Ashgrove", """
Ashgrove is a village of thatch and apple-orchards at the Weald's edge, and it has had a bad week. A bard-voice — Alcuin's — sings the column in. The villagers hide, then peer, then, slowly, come out.

An old wise-woman beckons you to a low cottage. In the bed lies a girl, perhaps twelve, whose arm is black to the shoulder.

"Nan," says the grandmother. "Four days. I've kept her breathing. But I cannot make it stop."
""", [
    ch("\"Sleep is all that holds the rot. Can you put her into a death-sleep?\"", "c3_nan_sleep", req="knows_bite"),
    ch("\"The arm must come off — at once.\"", "c3_nan_arm"),
    ch("Offer the grandmother a place in the column. Bring Nan along, sleeping or not.", "c3_nan_carry"),
], chapter=C)

sc("c3_nan_sleep", "A Death-Mimicking Sleep", """
The wise-woman pales, then nods. "Poppy. Henbane. A pinch of deathherb. It will slow her heart to a whisper. She will look dead, and she will not die. Not for a long time."

It is a gamble, and the only one on the table. The old woman measures out the draught with hands that have done this before.
""", [ch("Take Nan with the column.", "c3_weald")], enter=["set:nan_sleeping", "add:xp:1"], chapter=C)

sc("c3_nan_arm", "Too Late", """
Ferrand shakes his head even before the wise-woman does. "Four days, sire. It's in the blood."

Nan dies that night, quietly. Her grandmother refuses to let you burn her until the sun has risen. When you do, the old woman stands very straight and says nothing at all.
""", [ch("Move on, heavier than before.", "c3_weald")], enter=["set:nan_dead"], chapter=C)

sc("c3_nan_carry", "A Cart for the Girl", """
You lay Nan in the back of a wain with the old woman beside her. No one speaks. There is nothing else to try.

The old woman will not look at you, and does not need to. She will keep her granddaughter alive by will alone, as long as she can.
""", [ch("Move on.", "c3_weald")], enter=["set:nan_cart"], chapter=C)

sc("c3_weald", "The Weald Road", """
The Weald is ancient oak and old hunting lanes. The column strings out along the track, a mile long and as quiet as four hundred frightened people can be.

Rumour says dwarven path-wardens still watch the hill roads north. Rumour says the Skull's bearer went that way. The road forks: a lane through the deep wood, a track along the ridge, and an old cart-road through a ruined hamlet.
""", [
    rnd("Take the deep wood.", ["c3_dng_patrol", "c3_dng_wolves", "c3_dng_hamlet"]),
    rnd("Take the ridge.", ["c3_dng_patrol", "c3_dng_hamlet", "c3_dng_rest"]),
    ch("Take the ruined hamlet road.", "c3_dng_hamlet"),
], chapter=C)

sc("c3_dng_patrol", "Grey Riders", """
Three riders in grey cloaks, on horses with the wrong eyes. They do not speak. They are not alive, and they are looking for something very particular.

They are looking for the box.
""", [
    ch("Ambush them from the trees with the Court.", "c3_patrol_fight"),
    rk("Hide the column. Let them pass.", "INT", "c3_patrol_hit", "c3_patrol_mixed", "c3_patrol_miss"),
], chapter=C)

sc("c3_patrol_fight", "Ambush", """
Roland, Hartmann and the others burst from cover. It is brief and ugly. Grey cloaks fall; the horses scream; and in the end one rider pins a knight, and Roland takes its head clean off.
""", [ch("Go on toward the hills.", "c3_hills")], enter=["add:hp:-3", "add:xp:1"], chapter=C)

sc("c3_patrol_hit", "A Silent Column", """
You pass four hundred people in the shadow of the beeches without a single cough. The riders ride by, fifty feet away, and the horses do not even turn their heads.

It is the best order you have ever given.
""", [ch("Go on toward the hills.", "c3_hills")], enter=["add:xp:1", "add:gambit:1"], chapter=C)

sc("c3_patrol_mixed", "A Near Thing", """
They pass — but one child sneezes. A rider halts, head turning. Alcuin covers the noise with a loud, off-key lay about a drunk friar.

It works. Barely.
""", [ch("Go on toward the hills.", "c3_hills")], chapter=C)

sc("c3_patrol_miss", "Spotted", """
The riders wheel. The column scatters. Before the Court can form, they are on the baggage — and two are dead before Roland drives them off.
""", [ch("Gather the survivors and go on.", "c3_hills")], enter=["add:hp:-3", "add:coin:-20"], chapter=C)

sc("c3_dng_wolves", "Wolves", """
They are not undead wolves. They are only hungry ones, driven out of the hills by something worse. A dozen of them, thin as sticks, circling the cart-line.
""", [
    ch("Throw rations to them. Feed what you can.", "c3_wolves_fed", fx=["add:coin:-10"]),
    ch("Draw steel. Kill them quickly.", "c3_wolves_fight", fx=["add:hp:-2"]),
], chapter=C)

sc("c3_wolves_fed", "Mercy", """
Wolves are simple creatures. They eat, they leave, and in the morning there are tracks all around the camp that are not a threat but a courtesy.

Hunger recedes along the hills.
""", [ch("Go on toward the hills.", "c3_hills")], chapter=C)

sc("c3_wolves_fight", "Steel and Teeth", """
Three wolves die. A fourth takes a bite out of your calf before Aymer's blade finds it. The pack scatters.
""", [ch("Go on toward the hills.", "c3_hills")], chapter=C)

sc("c3_dng_hamlet", "The Silent Hamlet", """
Eleven cottages. A well. Not a single living soul, and not a single corpse. The doors are open. The hearths are cold.

On the green, someone has laid a long line of folded clothes, one set for every villager.
""", [
    ch("Search the cottages for supplies.", "c3_hamlet_search"),
    ch("Burn the hamlet. Whatever lives here must not follow.", "c3_hamlet_burn"),
    ch("Pass through in silence and move on.", "c3_hills"),
], chapter=C)

sc("c3_hamlet_search", "What the Hamlet Kept", """
Under the floorboards of the smith's cottage you find a cache: dried meat, a wineskin, a scatter of old coin. Someone prepared for a long siege and then — walked out. Calmly. In their sleep, maybe.
""", [ch("Take it and go.", "c3_hills")], enter=["add:coin:40", "add:hp:2", "set:hamlet_unease"], chapter=C)

sc("c3_hamlet_burn", "Ashes", """
You burn it all, and watch the smoke climb. It feels like a dedication, or an apology.
""", [ch("Go on.", "c3_hills")], enter=["add:xp:1"], chapter=C)

sc("c3_dng_rest", "A Quiet Night", """
No dead. No wolves. Just the stars through the leaves and the weight of the Skull's absence. You sleep, which you didn't think you could.
""", [ch("Go on toward the hills.", "c3_hills")], enter=["add:hp:4"], chapter=C)

sc("c3_hills", "The Hill Road", """
At the end of the Weald the land climbs. Pines. Scree. A cold wind with iron in it.

On a boulder above the trail, a small, hawk-eyed figure in a leather jerkin lifts a hand, and a crossbow does not quite lower.

"Dwarf," she says, unnecessarily. "Hetta, path-warden of the Deepholt. You're far from your throne, king."
""", [
    ch("\"I'm looking for a priest with a box.\"", "c3_hetta_priest", req="skull_in_hills"),
    ch("\"I'm looking for the Deepholt. I need walls.\"", "c3_hetta_walls"),
], chapter=C)

sc("c3_hetta_priest", "A Trail of Chalk", """
"A priest with a box? Aye." Hetta jerks a thumb. "My lads picked up a squire two days ago, half-dead, half-mad, asking for a king. Chalk marks on the rocks all the way back to a shepherd's hut."

She leads you there at a run.
""", [ch("Follow Hetta.", "c3_find_anselm")], chapter=C)

sc("c3_hetta_walls", "The Warden's Terms", """
Hetta studies the column. "Walls we have. Food we have, for a while. Trust takes longer. My lord Durgan will want to see the thing you carry before he lets a thousand strangers through his gate."

She doesn't say "the Skull." But she knows.
""", [
    ch("\"First, I must find the priest who carries it.\"", "c3_find_anselm", req="skull_in_hills"),
    ch("\"The Skull is with me.\"", "c3_skull_ambush", req="skull_kept"),
], chapter=C)

sc("c3_find_anselm", "The Shepherd's Hut", """
The hut is a ruin of stone and turf. Anselm is sitting against the wall, grey with exhaustion, the box across his knees. Wat sits next to him, whittling. Beside them, bandaged, sits whoever you sent: Sir Bors or Sir Aymer.

Anselm looks up. "I have not slept since the Ford," he says with something like pride. "But I have not put it down."
""", [
    ch("Embrace him and take the news.", "c3_anselm_news", req="sent_bors"),
    ch("Embrace him and take the news.", "c3_anselm_news_aymer", req="sent_aymer"),
], enter=["court:+Anselm", "court:+Wat"], chapter=C)

sc("c3_anselm_news", "Bors Is Taken", """
Sir Bors is not here.

"Grey riders," Anselm says. "Five nights ago. They came for the box. Sir Bors rode out to draw them off — we saw him fall from the horse. We did not see him rise."

Wat's knife stops moving. "He was taken, sire. Not killed. They *took* him."

An open wound that cannot be treated: your knight, a prisoner of the lich.
""", [ch("Gather yourselves. The column is two days' march from the dwarf-gate.", "c4_deepholt_road")],
   enter=["set:bors_taken", "court:-Bors", "set:skull_recovered"], chapter=C)

sc("c3_anselm_news_aymer", "Aymer Held", """
Aymer sits against the wall with a rag around his ribs and a grim half-smile. "Five riders, sire. I took three. Anselm took the fourth with a candlestick."

Anselm blushes. "It was a very heavy candlestick."

You laugh for the first time in a month.
""", [ch("Gather yourselves. The column is two days' march from the dwarf-gate.", "c4_deepholt_road")],
   enter=["court:+Aymer", "set:skull_recovered", "add:xp:1"], chapter=C)

sc("c3_skull_ambush", "Grey Riders, Again", """
That night they come for the box: six riders, silent, very fast. Bors sees them first and shouts the alarm.

"Anselm, the Skull! Give me the decoy!"

He has had a wooden box made, an empty twin. He seizes it, mounts, and gallops hard into the dark, with six riders following.
""", [
    ch("Let him go. It is the only way.", "c3_bors_gone"),
    ch("Charge after him with Roland and Hartmann.", "c3_bors_charge"),
], chapter=C)

sc("c3_bors_gone", "A Brave Knight", """
You hear the hoofbeats fade. Then, much later, a single scream, cut off.

At dawn Hetta and her wardens find nothing but churned earth and a single broken stirrup.
""", [ch("Press on toward the dwarf-gate.", "c4_deepholt_road")],
   enter=["set:bors_taken", "court:-Bors", "set:skull_recovered"], chapter=C)

sc("c3_bors_charge", "The Chase", """
You do not catch him. But you break two of the riders on the stones of a dry stream, and one of them speaks before it falls apart.

"The Master takes what is brought to him. The Master is patient."

Bors is gone. But you know where he went.
""", [ch("Press on toward the dwarf-gate.", "c4_deepholt_road")],
   enter=["set:bors_taken", "court:-Bors", "set:skull_recovered", "add:hp:-3", "add:xp:1"], chapter=C)
