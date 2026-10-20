from dsl import *
C = "Chapter I — The Ford"

sc("c1_ford", "The Ford", """
The Ford is behind you, and the Ford is lost.

You saw the line break. You saw the dead rise out of the river as if the water had only been holding them. Your army, your nobles, half your name — gone into the black current while the lich Malgareth walked the far bank and did not even hurry.

Now it is night on the south road. Sir Roland carries the standard, torn but still lifted. Your Court straggles behind you: knights, envoys, two frightened squires. And in a wooden box strapped to Father Anselm's back, wrapped in a grey cloth, rides the one thing that made the dead *stop* at the Ford.

The Skull of Saint Gregory II the Undying.

Sir Roland waits for your order.
""", [
    ch("Rally the Court. They must see a king, not a refugee.", "c1_rally"),
    ch("Study the road. Where will the dead come from, and when?", "c1_study"),
    ch("Take a moment alone. Fill the pipe.", "c1_pipe"),
], chapter=C)

sc("c1_rally", "A King Before Them", """
You stand where the firelight finds you and say what a king must say: that the Ford was a battle, not an ending; that every man who walked out of it is a man the lich did not take.

Roland kneels first. Then Aymer. Then — slowly, like men remembering a habit — the rest.
""", [
    rk("Make them believe it.", "CHA", "c1_rally_hit", "c1_rally_mixed", "c1_rally_miss"),
], chapter=C)

sc("c1_rally_hit", "They Believe", """
Something returns to their faces. Not hope — discipline, which is better. The squires stop shaking. Alcuin the envoy murmurs that he has heard worse speeches from kings who won.

You have made a Court again.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], enter=["add:xp:1", "add:gambit:1", "set:rallied"], chapter=C)

sc("c1_rally_mixed", "Hollow Cheer", """
They stand. They cheer, a little. But you hear in it the sound of men who need you to be right and are afraid you are not.

It will do. It must.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], enter=["add:xp:1"], chapter=C)

sc("c1_rally_miss", "Silence", """
The words come out sounding like a will being read. Nobody cheers. A squire starts to weep and tries to hide it.

Roland, loyal Roland, simply says, "Lead on, sire." It is the kindest thing anyone has said all day.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], chapter=C)

sc("c1_study", "The Chessmaster's Eye", """
You close your eyes and lay the board out in your head: the river, the Ford, the road, the hills north-east where the dwarves are said to dig. The lich does not tire. The dead do not sleep. But armies — even dead ones — move on roads, and roads are lines, and lines can be read.
""", [
    rk("Read the lines.", "INT", "c1_study_hit", "c1_study_mixed", "c1_study_miss"),
], chapter=C)

sc("c1_study_hit", "Lines on the Map", """
Three days. The legion will take Tollmere in three days, and Aldermont in perhaps eight. North of the Weald the roads thin, and thin roads are slow roads. The old dwarf-halls — the Deepholt — would be the nearest place with walls worth the name.

You have *seen* the war, and you hold two moves of it in your hand.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], enter=["add:gambit:2", "set:knows_roads"], chapter=C)

sc("c1_study_mixed", "A Partial Map", """
You can see the shape of it, though not the timing. Tollmere will fall. Aldermont might hold. The north is a question mark.

One Gambit, then — one move you can bend the board with.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], enter=["add:gambit:1"], chapter=C)

sc("c1_study_miss", "Too Many Pieces", """
Every line crosses another. You cannot tell which of them is the enemy's and which is your own fear. You open your eyes feeling older.
""", [ch("Move on toward Tollmere.", "c1_tollmere")], chapter=C)

sc("c1_pipe", "The Pipe", """
You sit apart, on a fallen cart, and open the little leather case that was the one personal thing you carried out of the capital. Three leaves in it, dried in three different ways. A king's small vices.
""", [
    ch("Fen-Reed — steadies the hands.", "c1_pipe_done", req="pipe>=1", fx=["add:pipe:-1", "add:hp:3", "set:steady"]),
    ch("Skyleaf — sharpens the mind.", "c1_pipe_done", req="pipe>=1", fx=["add:pipe:-1", "add:gambit:1"]),
    ch("Deepcure — endures.", "c1_pipe_done", req="pipe>=1", fx=["add:pipe:-1", "add:hp:6"]),
    ch("Put it away. There'll be worse nights to save it for.", "c1_pipe_done"),
], chapter=C)

sc("c1_pipe_done", "The Smoke Clears", """
For a few breaths the world is only a king, a cart, and a thread of smoke. Then Roland coughs politely, and the world returns.

"The road, sire?"
""", [ch("Take the road to Tollmere.", "c1_tollmere")], chapter=C)

sc("c1_tollmere", "The Gate of Tollmere", """
Tollmere is a river town of smiths and tanners, and it is already dying. Smoke from the east quarter. Refugees clogging the gate. And standing in the middle of the road with a drawn sword and open, milky eyes, Sir Aymer of the Ford.

Your knight. One of the men you thought lost. He is not blinking, and his lips are moving with words that are not his.

"The Master sends greeting to the Gregorian," he says in a voice like a cellar door. "The Master asks only for the sleeping thing. The skull sleeps in a wooden box. And wood burns."

Behind you, Anselm's hand tightens on the box.
""", [
    rk("Speak to the man inside him. Break the lich's grip with your voice.", "CHA", "c1_aymer_hit", "c1_aymer_mixed", "c1_aymer_miss"),
    ch("Order Roland to put Aymer down before he strikes.", "c1_aymer_fight"),
    ch("Have Anselm lift the Skull. Make the dead thing stop.", "c1_aymer_skull", req="court:Anselm"),
], chapter=C)

sc("c1_aymer_hit", "Aymer Returns", """
"Aymer. Aymer of the Ford. You held my left flank at Brightwater when the others ran. Come back."

Something flickers behind the milk. The sword shakes. And then the knight collapses to his knees and vomits black water, and weeps, and says your name — your *real* name — over and over.

The lich's hand is out of him. For now.
""", [ch("Raise him up and bring him with the column.", "c1_halbrecht")],
   enter=["add:xp:1", "set:aymer_free", "set:aymer_loyal"], chapter=C)

sc("c1_aymer_mixed", "Half a Man", """
Aymer breaks — but not cleanly. He drops the sword, clutching his head, and speaks in two voices at once: his own, begging, and the cellar-door voice laughing.

"It *wants* the skull," he gasps. "It told me where to find you. It has other servants on the road. Hurry."

Then he's yours again, shaking, and you are warned.
""", [ch("Bring him with the column. Quickly.", "c1_halbrecht")],
   enter=["set:aymer_free", "set:malgareth_warned", "add:coin:-10"], chapter=C)

sc("c1_aymer_miss", "The Sword Comes Down", """
The words die between you. Aymer lunges. Roland barely gets the standard-pole in the way, and the blade opens your arm to the bone before the knights drag Aymer off you.
""", [ch("Hold him down. This will take another way.", "c1_aymer_skull", req="court:Anselm"),
      ch("Hold him down. This will take another way.", "c1_aymer_fight", req="!court:Anselm")],
   enter=["add:hp:-4"], chapter=C)

sc("c1_aymer_skull", "The Saint Speaks", """
Anselm opens the box. Only a crack. Only for the length of a breath.

The Skull does not glow. It does not speak. It simply *is*, in the way a stone in a river is, and the lich's voice goes out of Aymer like a candle in a draught.

He sags into Roland's arms. Anselm shuts the box with trembling fingers and says, to no one, "It costs me, every time."

You have shown the Skull to a crowd. Hundreds saw. That cannot be unseen.
""", [ch("Bring Aymer with the column.", "c1_halbrecht")],
   enter=["set:aymer_free", "set:skull_seen", "add:xp:1"], chapter=C)

sc("c1_aymer_fight", "Blood on the Road", """
Roland and Bors take him between them. It is not a duel; it is a sad, brutal wrestle in the mud, and when it ends Aymer is bleeding from the scalp, unconscious but alive, and the milk has drained from his eyes.

The lich's hold is broken, but a man does not return from that without scars.
""", [ch("Carry him with the column.", "c1_halbrecht")],
   enter=["set:aymer_free", "add:hp:-2"], chapter=C)

sc("c1_halbrecht", "The Smith Who Won't Kneel", """
Tollmere's smith, a barrel-chested man named Halbrecht, has taken it upon himself to lead the refugees out. He eyes you without bowing.

"I hear you're the king. I hear you lost the Ford. I don't care. I have four hundred people who need a road, and I'll follow whoever has one."

Around you, the knights stiffen.
""", [
    ch("\"I have a road. Follow me, Halbrecht, and call me what you like.\"", "c1_halbrecht_ok", fx=["set:halbrecht_ally", "add:xp:1"]),
    ch("\"You will address your king properly.\"", "c1_halbrecht_proud", fx=["set:halbrecht_cold"]),
    ch("Offer coin for his people's obedience. (30 coin)", "c1_halbrecht_coin", req="coin>=30", fx=["add:coin:-30"]),
], chapter=C)

sc("c1_halbrecht_ok", "Respect Without Titles", """
He studies you a long moment, then nods once. "Halbrecht. Smith. Remember it."

You will. It's the first honest conversation you've had in a year.
""", [ch("Decide the fate of the Skull. It cannot stay with the column.", "c1_skull_split")], chapter=C)

sc("c1_halbrecht_proud", "Pride", """
Halbrecht's mouth twists. "Majesty," he says, flat as a plank. But he stays, because he has no better road. You've bought obedience; you've not bought him.
""", [ch("Decide the fate of the Skull.", "c1_skull_split")], chapter=C)

sc("c1_halbrecht_coin", "Bought Loyalty", """
He weighs the coins in his palm. "That'll feed the children for a week." He tucks them away. It's not warmth. It's a contract.
""", [ch("Decide the fate of the Skull.", "c1_skull_split")], enter=["set:halbrecht_ally"], chapter=C)

sc("c1_skull_split", "Where Should the Skull Sleep?", """
Aymer's warning plays on you: *wood burns.* The lich wants the Skull, and a column of four hundred refugees and a dying king is the worst place for it to be.

Anselm has not slept since the Ford. He can carry it into the hills, away from the army, toward whatever safe place the dwarves may still hold. But he cannot go alone.
""", [
    ch("Send Anselm with Sir Bors and the squire Wat into the hills — a small, quiet party.", "c1_skull_hills",
       fx=["set:skull_in_hills", "set:sent_bors", "court:-Anselm", "court:-Bors", "court:-Wat"]),
    ch("Send Anselm with Sir Aymer — who knows what the lich wants — and the squire Sam.", "c1_skull_hills",
       fx=["set:skull_in_hills", "set:sent_aymer", "court:-Anselm", "court:-Aymer", "court:-Sam"]),
    ch("Keep the Skull. If the lich wants it, let him come through you.", "c1_skull_kept", fx=["set:skull_kept"]),
], chapter=C)

sc("c1_skull_hills", "Into the Hills", """
Anselm touches your hand in blessing and the little party vanishes into the grey dawn, a priest, a knight, a youth, and a box. You watch until they are specks.

"They will be found or they will not," Roland says quietly. "And so will we."

You turn the column north, toward Aldermont.
""", [ch("North, to Aldermont.", "c2_gate")], chapter=C)

sc("c1_skull_kept", "The King Keeps His Own", """
You will not give a relic of your house to the wilderness. The Skull stays with the column.

Anselm bows, grateful and afraid. Every nightfall from now will be a vigil.
""", [ch("North, to Aldermont.", "c2_gate")], chapter=C)
