from dsl import *
C = "Chapter II — Aldermont"

sc("c2_gate", "A Shut Gate", """
Aldermont sits on a bluff above the river Vellin, grey-walled and very quiet. The gates are shut. On the wall stands a knight in the white tabard of the Order of the Red Hand, and beside him a boy of fourteen in a lord's cloak that doesn't fit.

"No one enters," calls Brother-Captain Ulric Vance. "The plague is in the town. Six days ago it took the lord. Go around, or go back."

Four hundred people stand behind you in the cold. Some of them are coughing.
""", [
    rk("Persuade Vance. Appeal to the honour of his Order.", "CHA", "c2_vance_hit", "c2_vance_mixed", "c2_vance_miss"),
    ch("Show the standard. Tell them who stands at their gate.", "c2_vance_royal"),
    ch("Ask what the plague actually is. Perhaps it is not what he fears.", "c2_ask_plague"),
], chapter=C)

sc("c2_ask_plague", "What Is the Sickness?", """
"A bite," Vance admits at last. "The dead came through here a week ago — a patrol, a few. The bitten sicken and die. Then rise. We burned the lord on the sixth night. The boy kept his secret until the wall began to talk."

A bite. Not a miasma. That changes everything.
""", [
    rk("Offer terms: inspection by a chirurgeon at the gate, no one bitten enters.", "INT", "c2_vance_hit", "c2_vance_mixed", "c2_vance_miss"),
], enter=["set:knows_bite"], chapter=C)

sc("c2_vance_royal", "By Right", """
The standard is old, and even Vance knows it. But a king in flight is only a man with a banner.

"I was bound to the Lord of Aldermont," he says slowly. "He is dead. I am bound to this boy. Not to you."
""", [
    rk("Remind him that the boy will die too, if the town falls.", "CHA", "c2_vance_hit", "c2_vance_mixed", "c2_vance_miss"),
], chapter=C)

sc("c2_vance_hit", "The Gate Opens", """
Something goes out of Vance's shoulders. He lowers his hand. "I've waited a week for a man who would tell me the truth about what is coming. You're him." He turns. "Open the gate!"

The iron groans. The boy Aldric looks at you with enormous eyes, and Vance kneels on the wall, in armour, awkwardly.

"My sword is yours, sire. The Red Hand is yours."
""", [ch("Enter Aldermont.", "c2_town")], enter=["set:vance_sworn", "add:xp:1", "add:gambit:1"], chapter=C)

sc("c2_vance_mixed", "Conditions", """
"Inspection," Vance says. "Every soul. Any bite stays outside the wall. Any bite."

It is a harsh rule. It is also the correct one. You nod.
""", [ch("Enter Aldermont under inspection.", "c2_town")], enter=["set:vance_sworn", "set:bitten_outside"], chapter=C)

sc("c2_vance_miss", "A Shut Door", """
"No." Vance's voice does not move. "Go around. Take the river road. I can't gamble four hundred lives on a stranger's word."

You are already turning to leave when a shout rings from the column — a woman has collapsed, her sleeve soaked in black. Everyone sees. Vance sees.

It is Maud, the mother of a boy called Tom. The bitten one is her son.
""", [ch("Show Vance the wound. Beg him to look.", "c2_vance_late")], chapter=C)

sc("c2_vance_late", "A Look At the Leg", """
Vance comes down from the wall himself and kneels beside the boy Tom. The calf is a ruin: black veins running up past the knee.

"Above the rot," he says very quietly. "It might be taken. It would have to be done now. I have a chirurgeon, Brother Ferrand. If you're willing to try, I will open the gate for you."
""", [ch("\"Open the gate.\"", "c2_town", fx=["set:vance_sworn", "set:tom_bitten_at_gate", "add:xp:1"])], chapter=C)

sc("c2_town", "Inside the Walls", """
Aldermont is a small town with big stone. A ring of granaries. A river-quay. A stew-pond that was once a moat. On the wall, Vance's Red Hand brothers keep a grim, careful watch.

The steward you will come to know as Lady Isobel — widow of the dead lord, a Vance by birth — meets you at the Guild Hall with a ledger already in hand.

"I will hate you for the whole of this," she says by way of welcome, "and I will do it well. What do you want first?"
""", [
    ch("Meet with Brother Ferrand and learn the sickness.", "c2_ferrand"),
    ch("Meet with the Guild Master, Corvin Bael — owner of the grain.", "c2_bael"),
    ch("Walk the wall with young Aldric.", "c2_aldric"),
    ch("Call the council. The dead are close.", "c2_hub", req="bael_keys"),
], chapter=C)

sc("c2_ferrand", "The Chirurgeon of the Red Hand", """
Brother Ferrand keeps records of the dead in a crabbed hand, with the same care other men give holy books. He is thin, calm, and dreadful to look at.

He sets out the rules he has learned in one week of horror: the bitten sicken in a day and die in three; the dead rise in a night; fire is the only certain answer; and — "this I only half believe" — the Skull, they say, makes them stop.

"If you have such a thing, sire, I would like very much to be wrong about it."
""", [
    ch("\"There is a boy named Tom. His leg is bitten. Can it be saved?\"", "c2_tom", req="!tom_done"),
    ch("Ask Ferrand to teach you the signs of infection.", "c2_ferrand_signs", req="!ferrand_taught"),
    ch("Return to the Guild Hall.", "c2_town"),
], chapter=C)

sc("c2_ferrand_signs", "The Rules of the Bite", """
Ferrand counts them on his fingers.

*One:* a bite is a death-sentence unless the limb is taken above the rot within a day.
*Two:* the dead are slow in cold and fast in warmth.
*Three:* they will not cross running water willingly.
*Four:* they want the living — but they want the Skull more.

You commit it to memory. It is the first real knowledge you've had of the enemy.
""", [ch("Back to the question of the boy.", "c2_ferrand")], enter=["set:ferrand_taught", "set:knows_bite", "add:gambit:1"], chapter=C)

sc("c2_tom", "The Amputation", """
Tom is fourteen, white as milk, and trying hard not to cry. His mother Maud holds his hand. The black veins have reached the knee.

"Above the rot," Ferrand says. "A hand-span above the knee. The saw is clean. The brandy is poor. And someone must hold the boy."

He looks at you. Not at your crown. At your hands.
""", [
    ch("Hold the boy yourself. A king who sends others to a bedside is no king.", "c2_tom_hold"),
    ch("Order Ferrand to proceed. You will wait outside with Maud.", "c2_tom_outside"),
    rk("Take the saw. Your hands are steadier than the chirurgeon's, after the Ford.", "DEX", "c2_tom_ok", "c2_tom_scarred", "c2_tom_bad", req="steady"),
], chapter=C)

sc("c2_tom_hold", "A King Holds a Boy", """
It takes twelve minutes. You do not look away. Tom screams once, and then does not, and then looks at you with a child's complete trust.

"Is it done?"

"It is done, Tom."

He lives. Maud will not say thank you; she simply puts her forehead on your sleeve and shakes. You will carry that sleeve for a long time.
""", [ch("Leave the infirmary.", "c2_town")], enter=["set:tom_done", "set:tom_saved", "add:xp:1", "add:hp:-1"], chapter=C)

sc("c2_tom_outside", "The Waiting Room", """
Maud grips your hand through the whole of it. The boy's screams go up through the stone ceiling. Ferrand emerges at last, apron red, and nods.

"He will live, sire. He will not walk the way he did."
""", [ch("Leave the infirmary.", "c2_town")], enter=["set:tom_done", "set:tom_saved"], chapter=C)

sc("c2_tom_ok", "Steady Hands", """
The fen-reed in your veins does what it was grown to do. The saw does not hesitate. Ferrand says nothing at all, but when you return the saw he looks at you the way a craftsman looks at a peer.

Tom lives, and the leg is clean.
""", [ch("Leave the infirmary.", "c2_town")], enter=["set:tom_done", "set:tom_saved", "add:xp:1"], chapter=C)

sc("c2_tom_scarred", "A Hard Cut", """
Your hand wavers once, but Ferrand is there to correct it. It is done, and it is ugly, and Tom will live.
""", [ch("Leave the infirmary.", "c2_town")], enter=["set:tom_done", "set:tom_saved"], chapter=C)

sc("c2_tom_bad", "The Saw Slips", """
The cut is wrong. Ferrand takes the saw from you without a word and finishes it, but the boy has lost blood he couldn't spare.

By morning he is alive, barely, and grey. Maud does not look at you.
""", [ch("Leave the infirmary.", "c2_town")], enter=["set:tom_done", "add:hp:-1"], chapter=C)

sc("c2_bael", "The Guild Master", """
Corvin Bael owns Aldermont's grain: eight great stone granaries and the chain of river-barges that feed them. He is round, shrewd, and visibly counting what a king in flight might cost him.

He hands you a ring of iron keys.

"I give you the keys because the alternative is that the dead take them. But I want an answer, sire. Four hundred refugees, six hundred townsfolk. Winter. My granaries last thirty days. On the thirty-second day — *where do we eat?*"
""", [
    ch("\"Carp. Stew-ponds, a fish for every mouth. And mushroom-caves in the dry cellars.\"", "c2_bael_carp", fx=["set:carp_plan"]),
    ch("\"We leave before day thirty. We take the grain, the barges and the walls with us.\"", "c2_bael_evac", fx=["set:evac_plan"]),
    rk("\"I will make the dwarves open their own larders to you.\" (A promise.)", "CHA", "c2_bael_dwarves", "c2_bael_evac", "c2_bael_doubt"),
], chapter=C)

sc("c2_bael_carp", "The Stew-Pond Plan", """
Bael's eyebrows climb. Lady Isobel, listening from the door, says dryly, "That might actually work. I resent it."

The old moat is stocked by dawn.
""", [ch("Back to the Hall.", "c2_town", fx=["set:bael_keys", "add:xp:1"])], chapter=C)

sc("c2_bael_evac", "Moving the Town", """
It is a mad scheme. It might be the only sane one. Bael writes it in his ledger with a face like a man signing his own death warrant.
""", [ch("Back to the Hall.", "c2_town", fx=["set:bael_keys"])], chapter=C)

sc("c2_bael_dwarves", "A Promise of the Deep", """
Bael blinks. "The Deepholt? Nobody has seen a dwarf in a hundred years."

"Then I will be the first."

He laughs, and then does not. "Then I'll tell the barge-men to load for the north."
""", [ch("Back to the Hall.", "c2_town", fx=["set:bael_keys", "set:evac_plan", "set:promised_dwarves", "add:xp:1"])], chapter=C)

sc("c2_bael_doubt", "A Promise Unkept", """
"A king who promises dwarves he has never met," Bael murmurs. "You must forgive me if I don't unload the barges just yet."

He keeps the keys. For now.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_aldric", "The Boy Lord", """
Aldric, Lord of Aldermont, is fourteen and has buried his father in secret. He walks the wall every night. He does not eat much.

"Vance says I should leave with you. Lady Isobel says I should stay and die as a lord. My father said," his voice cracks, "that a lord's first duty is to the people on his wall."

He looks at you, hoping for an answer he can stand on.
""", [
    ch("\"A lord's first duty is to live long enough to rule. Leave when the wall tells you.\"", "c2_aldric_live", fx=["set:aldric_trusts"]),
    ch("\"Your father was right. You'll be the last off the wall. I'll see to it that it's a long, long line.\"", "c2_aldric_last", fx=["set:aldric_last", "add:xp:1"]),
], chapter=C)

sc("c2_aldric_live", "Practical Wisdom", """
Aldric nods slowly. It is not the answer he wanted, but it is one he can survive. "I'll tell Vance."
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_aldric_last", "The Last Off the Wall", """
Aldric straightens. For a moment you see the man he will be, if he lives. "Then I'll hold it," he says. "As long as it takes."

You hope you have not just killed him.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_hub", "The Council of Aldermont", """
Night falls over Aldermont. Lady Isobel lays out the ledger on the long table. Vance, Ferrand, Bael and young Aldric stand around it. Roland stands at your shoulder.

"The dead are three days off," Isobel says. "Not a hundred miles. The wall will hold if the Red Hand can keep it. But there is a choice that has to be made tonight."
""", [
    ch("Strip the town and send everything north by the river. Abandon Aldermont.", "c2_strip", fx=["set:town_stripped"]),
    ch("Hold the wall. Buy time for the evacuation to be done properly.", "c2_hold"),
], chapter=C)

sc("c2_strip", "Stripping Aldermont", """
Every barge on the Vellin is loaded by dawn. Grain, tools, iron, the bells of the lesser churches, the lead from the roofs. Bael walks the quay with his ledger and weeps quietly at the arithmetic.

Lady Isobel supervises the evacuation of the sick. Ferrand burns the dead. Roland, at your side, mutters that it is the most efficient looting he has ever seen, and he is not joking.
""", [
    ch("Stay until the last barge. Show them a king does not flee first.", "c2_departure", fx=["add:hp:-2", "add:xp:1"]),
    ch("Leave with the first barges and trust Vance to bring the rearguard.", "c2_departure"),
], chapter=C)

sc("c2_hold", "Holding the Wall", """
The dead come at midnight, as slow as winter, and as many. They climb the bluff in a grey tide.

You stand on the wall beside Vance and Aldric and Sir Hartmann, who has been a serjeant of Aldermont's town-watch and who kneels, before the whole garrison, in the mud of the parapet, and gives you his sword.

"I will serve a king who stands where I stand."
""", [
    rk("Direct the defence. Read the dead like a board.", "INT", "c2_hold_hit", "c2_hold_mixed", "c2_hold_miss"),
], enter=["court:+Hartmann", "set:hartmann_knelt"], chapter=C)

sc("c2_hold_hit", "The Wall Holds", """
Fire, pitch, and a single well-placed ballista bolt through the leading file break the wave before it finds the walls. By dawn, the slope is ash and the town is breathing.

The Red Hand cheers you by name.
""", [ch("Prepare the departure.", "c2_departure")], enter=["add:xp:1", "add:gambit:1"], chapter=C)

sc("c2_hold_mixed", "A Costly Night", """
The wall holds, but not before a section of the east parapet gives way. Four brothers of the Red Hand fall, and two of the dead get into the grain-lofts before Vance personally burns them out.

You have won. It has cost.
""", [ch("Prepare the departure.", "c2_departure")], enter=["add:hp:-2"], chapter=C)

sc("c2_hold_miss", "The Wall Breaks", """
The east parapet falls inward. You are on the wall when it happens. Hartmann drags you out of the rubble by the collar, bleeding, shouting something you cannot hear.

By dawn, a third of the garrison is dead, and the town is burning.
""", [ch("Flee while you can.", "c2_departure")], enter=["add:hp:-6", "set:aldermont_burned"], chapter=C)

sc("c2_departure", "The River North", """
You leave Aldermont as the sun rises: a long line of barges and carts, a column of the living, and behind it, a black plume where the town burns by Vance's order, so that nothing shall rise there.

Isobel stands in the stern of the lead barge and does not look back. "I'll hate you the whole way," she says. It is not entirely a promise.

Ahead lies the Weald, the village of Ashgrove, and somewhere beyond, in the hills, the dwarves' mountain.
""", [
    ch("Take the Weald road toward Ashgrove.", "c3_ashgrove"),
], enter=["court:+Hartmann", "set:isobel_steward"], chapter=C)
