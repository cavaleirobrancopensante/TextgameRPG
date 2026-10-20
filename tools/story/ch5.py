from dsl import *
C = "Chapter V — The Bell"

sc("c5_abbey", "Saint Gregory-in-the-Hills", """
The abbey sits on a shelf of rock above the treeline: a grey chapel, a cloister, a belfry, and three hundred monks in undyed wool who have spent a decade praying for the end of the world and have, to their credit, kept very good records of its approach.

The abbot, Ambrose, is a lean man with burn-scarred hands and a laugh that arrives unexpectedly. He kneels the moment he sees the standard — not to you, you realise, but to the *saint's* arms stitched on it.

"You are late, sire," he says. "But you have not come empty-handed."
""", [
    ch("Present the Skull to the abbot.", "c5_ambrose", req="skull_recovered"),
    ch("Tell him the column's need: food, shelter, the dead on the road.", "c5_ambrose"),
], chapter=C)

sc("c5_ambrose", "Abbot Ambrose", """
Ambrose leads you through the cloister to the library: a long vaulted room, shelves bowed with scrolls. One of them lies open, a vast pre-Fall volume in a script you do not know.

"The Concordance," he says. "A record of the First Era, when the saints were men and the Enemy walked in daylight. There is a necromancer in it. A servant of the Enemy, one of seven. It calls itself a god. It sleeps below a mountain."

He taps the page. "I think your dwarves woke it."

He looks at you. "I will tell you the rest, sire. But not tonight. First: the Bell."
""", [ch("Follow him to the belfry.", "c5_bell")], enter=["set:concordance_seen"], chapter=C)

sc("c5_bell", "The Bell of Saint Gregory", """
The Bell is old and green with weathering, and as large as a hay-wain. It hangs in an open belfry, its clapper wrapped in leather.

"When the great bell rings," Ambrose says, "the dead lie down. It has not rung in sixty years. It rings *better* with a relic in its heart."

He looks pointedly at the Skull's box.
""", [
    ch("Mount the Skull inside the Bell. Let it ring the dead down.", "c5_bell_arm", req="skull_recovered"),
    ch("Keep the Skull on your person. The Bell can ring without it.", "c5_bell_plain"),
], chapter=C)

sc("c5_bell_arm", "Armed", """
Anselm weeps as he sets the Skull into a cradle of silver wire within the bell's belly. Ambrose strikes it once, softly, with a padded hammer.

The note goes out across the valley. Somewhere distant, you hear something drop. It is a *sound of falling*, as if a legion had lain down in the night.

The Bell is armed.
""", [ch("Go down to the river. Hollowmill awaits.", "c5_hollowmill")], enter=["set:bell_armed", "add:xp:1"], chapter=C)

sc("c5_bell_plain", "Unarmed", """
The Bell rings: a good, deep note, but a plain one. It will lull the weaker dead. It will not stop an army.

Ambrose does not argue. He folds his hands. "Then we will pray it is enough."
""", [ch("Go down to the river. Hollowmill awaits.", "c5_hollowmill")], chapter=C)

sc("c5_hollowmill", "Hollowmill Lock", """
Down the mountain, at the join of two rivers, a stone lock-house guards the only boat-route out of the hills: Hollowmill. A cluster of mill-wheels. A moat. A single stone bridge.

Sir Roland takes the lock-house without a fight. Alcuin the envoy takes the miller's wife's tea.

"If the dead come," Roland says, "they come across this bridge, or they don't come."
""", [
    ch("Fortify the bridge and the lock. Build for a siege.", "c5_fortify"),
    ch("Send riders to the Fenmarch. The fen-folk may know something.", "c5_fenmarch"),
], chapter=C)

sc("c5_fortify", "Holding the Lock", """
You work with Roland, Hartmann and the miller. Beams across the bridge. Barrels of pitch at the mill-race. A chain across the river. It is the kind of work you were born to.
""", [
    rk("Plant the standard. Make this ground yours.", "CHA", "c5_fortify_hit", "c5_fortify_mixed", "c5_fortify_miss"),
], chapter=C)

sc("c5_fortify_hit", "Ground Won", """
The standard goes in. The soldiers around it stand straighter. For a moment Hollowmill is not a mill-lock; it is a place with a king. The people feel it. They begin to build faster.
""", [ch("Meet with the fen-folk.", "c5_fenmarch")], enter=["set:hollowmill_held", "add:xp:1", "add:gambit:1"], chapter=C)

sc("c5_fortify_mixed", "A Good Wall", """
The bridge is blocked, the mill-race trapped. Not perfect, but enough.
""", [ch("Meet with the fen-folk.", "c5_fenmarch")], enter=["set:hollowmill_held"], chapter=C)

sc("c5_fortify_miss", "A Crack in the Plan", """
The pitch-barrels leak. The chain is the wrong length. A day of work undone, and the miller's apprentice drowned in the mill-race.
""", [ch("Meet with the fen-folk.", "c5_fenmarch")], enter=["add:hp:-2"], chapter=C)

sc("c5_fenmarch", "Fenmarch", """
Beyond the lock the river spreads into a flat, silver marsh: the Fenmarch. Reed-towns on stilts. Boats like leaves. The fen-folk are small, brown, and extremely good at not being found.

Their ruler is a princess named Saoirse. She is twenty-six, has red-brown hair and green eyes like the marsh in autumn, and has already decided that she doesn't like you.

"They tell me you're a king," she says. "I have a hundred reed-boats and a very small treasury. Tell me what's in it for the fen."
""", [
    ch("\"Safe harbour. A wall on the river. A place for your people when the dead come.\"", "c5_saoirse_deal"),
    rk("\"A union. My crown and yours, my Court and your boats.\"", "CHA", "c5_saoirse_marry", "c5_saoirse_deal", "c5_saoirse_cold"),
], chapter=C)

sc("c5_saoirse_deal", "An Alliance", """
Saoirse weighs it, her chin on her fist. "Safe harbour I can sell to my elders. A wall on the river, perhaps. But I want it in writing."

You sign. She signs. Her signature is neater than yours.
""", [ch("Return to Hollowmill. The scouts report movement.", "c5_siege")], enter=["set:fen_allied", "add:xp:1"], chapter=C)

sc("c5_saoirse_marry", "A Union", """
The council of reed-elders confers for three hours in a language you don't speak. When they emerge, Saoirse is already smiling.

"You are not what I expected," she says. "I find that I do not mind."

You are married by the end of the week, in a flat-bottomed boat, under a roof of woven reeds, with Roland as the only witness who can swim.
""", [ch("Return to Hollowmill. The scouts report movement.", "c5_siege")], enter=["set:fen_allied", "set:queen_saoirse", "add:xp:2", "add:gambit:1"], chapter=C)

sc("c5_saoirse_cold", "Cold Courtesy", """
"A union? With a king whose kingdom is a column of beggars?" She doesn't smile. "No. But I'll sell you my boats."

It costs you forty coins. The boats are good.
""", [ch("Return to Hollowmill. The scouts report movement.", "c5_siege")], enter=["set:fen_boats", "add:coin:-40"], chapter=C)

sc("c5_siege", "The Host Arrives", """
They come at dusk: first as a smudge on the horizon, then as a tide.

Ten thousand dead. Fifteen. Marching in ranks, as if drilled. In their midst, borne on a litter of bone, a grey-robed figure in a hood, hands clasped.

The lich Malgareth reaches the far bank and lifts his hand. The host halts. A silence falls over the river.

Then comes the voice, not shouted but *placed* into every ear at once, patient as a physician:

"King Gregory. Give me the skull, and your people may walk free. I will keep my word."
""", [
    ch("\"Take it, and my people live.\" (Consider the offer.)", "c5_offer"),
    ch("Refuse. Raise the standard.", "c5_refuse"),
], chapter=C)

sc("c5_offer", "The Offer of Malgareth", """
You hold your breath. It is a good offer. It may even be true.

But Anselm, standing beside you, has gone the color of tallow. "My lord," he whispers. "If you give it up, the world ends. Not just ours. All of it."

You stand at the edge of the bridge with the Skull in a wooden box at your side and the lich's patient voice in your ears.
""", [
    ch("Refuse. Raise the standard.", "c5_refuse", fx=["set:malgareth_offer_refused"]),
    ch("Stall him. Ask for three days to consider.", "c5_stall", fx=["set:malgareth_offer_pending"]),
], chapter=C)

sc("c5_stall", "Three Days", """
"Three days," Malgareth says, and for the first time he sounds almost amused. "I have waited three centuries. Three days is a courtesy. You may have them."

It is a gift you did not earn. You intend to spend it.
""", [ch("Make your preparations.", "c5_prep")], enter=["add:xp:1"], chapter=C)

sc("c5_refuse", "The King's Answer", """
"No," you say.

It is not shouted. It does not need to be. Roland raises the standard behind you. Alcuin begins, unprompted, a marching song. Soldiers on the walls take up the chorus.

Malgareth lowers his hand. The host surges across the water.
""", [ch("Make your preparations.", "c5_prep")], enter=["add:xp:1"], chapter=C)

sc("c5_prep", "Three Plans", """
The river is the only thing standing between you and fifteen thousand dead. You have whatever you've built: a bridge, a chain, a lock, a Bell on the mountain — if you armed it — and a fleet of fen-boats if you made friends.

What do you do?
""", [
    ch("Ring the Bell. Let the Skull call the dead down.", "c5_bell_ring", req="bell_armed"),
    ch("Fire-rafts. Load every barge with pitch and send them down the river into the host.", "c5_fire_raft"),
    ch("Evacuate. Take everyone upriver by night.", "c5_evac_first"),
], chapter=C)

sc("c5_bell_ring", "The Bell Rings", """
Ambrose strikes the Bell with both arms. The note rolls down the mountain and across the river like a thrown cloth.

The first rank of the dead sags. The second pitches forward. By the tenth rank, the whole host is going down like wheat before a scythe — tens of thousands of them, lying down on the riverbank in the grey dusk.

On the far bank Malgareth lifts his hood and, for the first time, you see him surprised.

He steps back and vanishes into the mist.
""", [ch("Press the advantage. Burn the fallen.", "c5_victory")], enter=["add:xp:2", "set:bell_rang"], chapter=C)

sc("c5_fire_raft", "The Fire-Rafts", """
Every barge on the river is tied together, soaked in pitch, loaded with straw and oil. The fen-boatmen pole them out into the current. Brom stands on the quay holding a lit torch with an expression of pure joy.

The dead do not fear fire. But they cannot cross it.
""", [
    rk("Time the release. Send them down at the exact moment the host crosses.", "INT", "c5_raft_hit", "c5_raft_mixed", "c5_raft_miss"),
], chapter=C)

sc("c5_raft_hit", "The River Burns", """
The Vellin becomes a ribbon of fire for half a mile. Ten thousand dead go into it and do not come out. A tower of black smoke climbs to the clouds.

Malgareth stands on the far bank, hood back, watching it burn. He looks at you across the water and gives a small, appreciative bow.
""", [ch("Press the advantage.", "c5_victory")], enter=["add:xp:2", "add:gambit:1"], chapter=C)

sc("c5_raft_mixed", "A Breach", """
The rafts burn half the host. The other half wades through the shallows and reaches the bridge. Roland holds it for an hour, until the Bell on the mountain — struck at last — rings the rest down.
""", [ch("Count the cost.", "c5_victory")], enter=["add:xp:1", "add:hp:-3"], chapter=C)

sc("c5_raft_miss", "The Wind Turns", """
The wind shifts. The fire-rafts drift into your own quay. The storehouse goes up. Half the grain is lost.

The host crosses unhindered.
""", [ch("Evacuate while there is time.", "c5_evac_first")], enter=["add:hp:-4", "add:coin:-40"], chapter=C)

sc("c5_victory", "The Bank at Dawn", """
In the morning the far bank is quiet. The dead lie where they fell, and the fen-folk, who are not squeamish, begin burning them in long, patient rows.

Malgareth is gone. The river runs black and the fen-folk hum as they work.

The war is not won. But the Hollowmill is yours. And on the mountain, the Bell still rings.
""", [ch("Gather the column. You need a home.", "c6_found")], enter=["set:hollowmill_victory"], chapter=C)

sc("c5_evac_first", "The Night March", """
You do not fight what you cannot beat. Under a moon the colour of tin, the column loads onto fen-boats and slips upriver in silence, four hundred people and a thousand animals, carts dismantled, lamps shuttered.

Behind you the dead reach an empty bridge. A mile on, you hear the first of them fall into the river, uncomprehending.

It is not a victory. It is survival.
""", [ch("Find a home in the hills.", "c6_found")], enter=["set:evacuated"], chapter=C)
