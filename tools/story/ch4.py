from dsl import *
C = "Chapter IV — The Deepholt"

sc("c4_deepholt_road", "The Road Up", """
The land climbs into raw stone. Cold streams. Ancient steps hewn into the mountain, wide as a street and worn smooth by a thousand years of dwarvish boots. At the head of the stair, a gate of grey stone the height of a cathedral, half-closed.

Hetta whistles. A horn answers from inside. Slowly, the gate opens.

The Deepholt: the last great hall of the dwarves.
""", [ch("Enter.", "c4_gate")], chapter=C)

sc("c4_gate", "Durgan, Stone-Warden", """
The first dwarf you see is old even by dwarf measure — two hundred years, perhaps more — with a beard in nine braids and a hammer as long as a halberd. He stands beside a throne he does not sit on.

"Durgan, Stone-Warden of the Deepholt. The last of it, near enough." He looks at the column, and at you. "You are the exiled king. I see why you fled. I do not see how you lived."

Behind him the hall is half-empty. A few hundred dwarves. A great many empty benches.
""", [
    ch("\"I'm told the dead came up from below your halls.\"", "c4_deep_warning"),
    ch("\"I need walls. In exchange, I'll offer you something: the oath of a king.\"", "c4_oath"),
    ch("Show him the Skull.", "c4_skull_show", req="skull_recovered"),
], chapter=C)

sc("c4_deep_warning", "What the Dwarves Woke", """
Durgan is silent for a long time.

"My forefathers dug too deep," he says at last. "Six levels below the Great Hall we found something that was not stone. We sealed it. We said we would never speak of it. And then, one winter, the dead came up through the floor."

He raps the flagstone with his hammer, once. It rings hollow.

"The lich is a hand, king. Not the head."
""", [
    ch("\"Then we strike at the head.\"", "c4_oath", fx=["set:knows_deep"]),
    ch("\"Then we leave this place before it wakes again.\"", "c4_oath", fx=["set:knows_deep"]),
], chapter=C)

sc("c4_skull_show", "The Skull in the Hall", """
Anselm sets the box on the long stone table. Dwarves crowd round in silence. When the lid lifts, the whole hall holds its breath.

Nothing happens. And then everything stops: the torches steady, the drafts die, and from far below, in the stone, you feel a thing you had not noticed — a faint, constant, grinding hum — *cease*.

Durgan sits down on the steps of his throne, finally. "That," he says. "That is what I have been listening to for thirty years."
""", [ch("\"Then we can end it.\"", "c4_oath")], enter=["set:skull_shown_durgan", "add:xp:1"], chapter=C)

sc("c4_oath", "The Oath of Stone and Crown", """
Durgan lays his hammer across his knees.

"I'll tell you my price, king. Not gold. I want a name, so my grandchildren remember who I served. I want my folk, the ones who remain, kept alive. And I want the deep ended."

You have a sword at your hip, a crown in your pack, and a title you don't hold any more.
""", [
    ch("Knight him. \"Rise, Durgan of the Deepholt — Warden of the Realm.\"", "c4_knight", fx=["set:durgan_knight"]),
    rk("Offer it as an alliance of equals. He will respect it more.", "CHA", "c4_equal_hit", "c4_knight", "c4_equal_miss"),
], chapter=C)

sc("c4_knight", "Nobledwarfship", """
Durgan has never been knighted in two hundred years. He is, you discover, delighted by the idea, and horrified at being delighted. He kneels with a grunt like a collapsing wall.

"I'll be damned," he says as you touch his shoulder. "A dwarf with a title."

The hall roars. For the first time since the Ford, someone is cheering you for a reason.
""", [ch("Meet the dwarf-folk. Learn what they can do.", "c4_brom")], enter=["set:durgan_sworn", "add:xp:1", "add:coin:-20"], chapter=C)

sc("c4_equal_hit", "A Handshake of Stone", """
He takes your hand in a grip that could split rock. "Equal, then. Until you prove otherwise."

It is the finest alliance you have ever made. He will keep it longer than any oath.
""", [ch("Meet the dwarf-folk.", "c4_brom")], enter=["set:durgan_sworn", "set:durgan_equal", "add:xp:1", "add:gambit:1"], chapter=C)

sc("c4_equal_miss", "A Cold Look", """
"You offer me an alliance because you cannot afford to knight me," Durgan observes. "That is a lie, but a polite one."

He agrees anyway. It will take work to earn his warmth.
""", [ch("Meet the dwarf-folk.", "c4_brom")], enter=["set:durgan_sworn"], chapter=C)

sc("c4_brom", "Brom's Draught", """
Brom is a squat brewer with a belly like a keg and the soft hands of a man who has been wrong about many things and kind about all of them.

"Infection, aye?" He taps a stoppered clay jar. "Deep-cap draught. Mushroom from the lower caves. Slows the heart and breath to a trickle. Holds the rot but doesn't heal it. One dose fits any body. It needs cold, and a drop each dawn."

He looks at you. "I assume you have somebody."
""", [
    ch("\"Seven of the bitten are in the column, kept alive only by luck.\"", "c4_brom_save", req="!nan_dead"),
    ch("\"Nan is sleeping. I want her dose.\"", "c4_brom_nan", req="nan_sleeping"),
    ch("\"The girl in the cart — Nan — I want her dose.\"", "c4_brom_nan", req="nan_cart"),
    ch("\"Not now. What else do you have?\"", "c4_theodore"),
], chapter=C)

sc("c4_brom_save", "Seven Lives", """
Brom takes the jar to the infirmary himself. By dawn, seven bitten villagers sleep in cold stone cots, their veins fading from black to dull grey.

"It won't cure them," he warns. "But it will give you time to find someone who can."
""", [ch("Thank him and move on.", "c4_theodore")], enter=["set:infected_held", "set:brom_ally", "add:xp:1"], chapter=C)

sc("c4_brom_nan", "A Child's Dose", """
He mixes a thimble. "Small body, small dose." The girl's chest rises, once, twice, slow as a clock in a cold room.

"She'll keep. Find me a cure and I'll wake her."
""", [ch("Thank him and move on.", "c4_theodore")], enter=["set:nan_held", "set:brom_ally", "add:xp:1"], chapter=C)

sc("c4_theodore", "The Hall of the Fallen", """
Durgan leads you down into the First Hall — a vault of pillars and vast silence. Along its walls stand the dead of the Deepholt's last war: dwarves and men in rows, motionless, eyes open, bound by the lich's will.

And in the centre, a human knight in your kingdom's old colours. He is perfectly still. Tabard torn, helm gone, face pale as candle-wax.

"Sir Theodore," Roland whispers. "He fell at the Ford."
""", [
    ch("Bring the Skull forward. Let Anselm raise it.", "c4_theodore_skull", req="skull_recovered"),
    ch("Leave them in peace. The dead should not be disturbed.", "c4_leave"),
], chapter=C)

sc("c4_theodore_skull", "The Undying Knight", """
Anselm lifts the Skull. The dead of the First Hall do not move — but the knight in the centre blinks. Once. Twice. A breath, drawn in like a drowning man's.

"My king," says Sir Theodore. "I do not know why I am not dead. But I am glad to see you."

He cannot be killed, you will learn; the Skull has bound him to the living world. It is a gift. It is a very dangerous one.
""", [ch("Embrace him. Another knight returns.", "c4_leave")],
   enter=["court:+Theodore", "set:theodore_back", "add:xp:1", "add:hp:-2"], chapter=C)

sc("c4_leave", "A Hall of Stone", """
The Deepholt is not safe, you realise — only quiet. Below the First Hall, six sealed levels. Beneath those, a patient listening.

You cannot stay. You cannot hold this place against both the legion from above and the deep from below. Durgan agrees, grimly.

"There's a place," he says, "in the hills. An abbey. Monks of Saint Gregory — your saint. They keep a bell. They say the Bell rings the dead down."
""", [ch("Take the column to the Abbey of Saint Gregory-in-the-Hills.", "c5_abbey")],
   enter=["set:left_deepholt"], chapter=C)
