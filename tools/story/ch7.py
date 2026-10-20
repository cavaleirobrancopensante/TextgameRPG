from dsl import *
C = "Chapter VII — The Descent"
RD = [{"if": "clock.siege>=6", "goto": "end_siege"}, {"if": "clock.delve>=6", "goto": "end_starve"}]

sc("c7_library", "The Concordance", """
Ambrose has not slept. He has the Concordance open across three tables, with notes in his own hand weighted down by a candlestick.

"I will tell you what I know," he says, "and then you will not like it."

The thing beneath the Deepholt is a necromancer of the First Era: a servant of the Enemy, one of seven, who calls itself a god and hoards what it takes. Everything the dwarves lost, it kept — gold, banners, bones. It has been feeding on the drowned dead of six sealed levels for a thousand years. Malgareth is its steward, not its master.

"Kill the god," says Ambrose, "and the horde above falls with it. That is what the Concordance says. I do not know if it is true."

He lowers his voice. "There is a name. I will write it, and seal it, and give it to you at the door. Not before."

{{ferrand_dead|In the crypt below the chapel, Brother Ferrand's body lies on its slab, where he died of the bite last winter. Anselm says the dead man's left eye has begun to open when the Skull passes. No one has found the courage to say what that means.}}
""", [ch("Gather the Court. Decide how to go down.", "c7_decide")], enter=["set:ferrand_dead", "set:name_pending"], chapter=C)

sc("c7_decide", "Above and Below", """
The scouts say fifteen thousand dead are on the road, led by Malgareth's second host. The Wall and the Bell can hold them for a time. But a time is all you have.

The descent will take days. Food below is finite. The walls above are finite. Two clocks, running at once.

And the Skull can only be in one place.
""", [
    ch("Take the Skull below. It makes the dead stop. The delve will go quicker, safer. The Bell rings plain above.", "c7_party", fx=["set:skull_below"]),
    ch("Leave the Skull in the Bell. Let it hold the wall, and go down without it.", "c7_party", fx=["set:skull_above"]),
], enter=["if:levy_big?add:clock.siege:1"], chapter=C)

sc("c7_party", "The Descent Party", """
Who goes?

Roland, to carry the standard. Durgan, who knows the stairs. Anselm, to hold the Skull. Theodore, who cannot be killed. Hetta, to scout.

Everyone else holds the mountain: Aldric on the wall, Isobel at the ledgers, Ambrose at the Bell. You look at them all, and the whole kingdom looks back at you.
""", [ch("Open the door to the Deepholt. Descend.", "c7_l1")], chapter=C)

sc("c7_l1", "Level One: The Wet Stair", """
The First Hall is quiet. The doors to the stair stand open, and below them a great flight of steps drops into black water.

Durgan lowers his lantern. "Flooded since the first time we sealed it. The water is the lich's, not ours."

Things move in it. They aren't breathing, but they are listening.
""", [
    rk("Wade through the flooded stair.", "CON", "c7_l1_ok", "c7_l1_cost", "c7_l1_bad"),
    ch("Have Durgan cut a dry path along the wall. It will take a day.", "c7_l1_ok", req="durgan_sworn", fx=["add:clock.delve:1"]),
    ch("Anselm lifts the Skull. The drowned stop.", "c7_l1_ok", req="skull_below"),
], redirect=RD, chapter=C)

sc("c7_l1_ok", "Down the Stair", """
You reach the landing wet and cold and whole. Behind you the water closes like a held breath.
""", [ch("Go on to Level Two.", "c7_l2")], enter=["add:xp:1"], redirect=RD, chapter=C)

sc("c7_l1_cost", "A Soaked Pack", """
The supplies are spoiled by the water. You reach the landing but the packs are heavy and sour.
""", [ch("Go on to Level Two.", "c7_l2")], enter=["add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_l1_bad", "Hands in the Water", """
Something takes your ankle and pulls. By the time Roland hauls you free, you've swallowed half the stair, and the packs have gone under.
""", [ch("Go on to Level Two.", "c7_l2")], enter=["add:hp:-4", "add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_l2", "Level Two: The Hoard", """
A vault the size of a cathedral, filled to the rafters with treasure: heaped coin, gem-studded armour, ranks of gold idols, dwarven banners worked in silver thread. Everything the Deepholt lost, kept in mounds.

Durgan stops walking. His hand is on his hammer, and the knuckles are white.

"My grandfather's crown," he says quietly. "There. On the pile."

The coin murmurs. It is not a sound. It is the *impression* of a sound, as of something that wants.
""", [
    ch("Touch nothing. Walk the path through the middle.", "c7_l3", fx=["add:clock.delve:1", "add:xp:1"]),
    ch("Take a purse. (+60 coin.)", "c7_l2_purse", fx=["add:coin:60", "set:took_hoard"]),
    ch("Take the crown for Durgan. A king gives gifts.", "c7_l2_crown", req="durgan_sworn"),
    rk("Scoop the treasure. The realm needs gold. (+200 coin.)", "DEX", "c7_l2_loot", "c7_l2_wights", "c7_l2_wights", fx=["set:took_hoard"], hit_fx=["add:coin:200"]),
], redirect=RD, chapter=C)

sc("c7_l2_purse", "A Little Weight", """
You take only what fits in a pocket. The coins are cold. For a moment you could swear one of them *whispered*.

Roland says nothing. Durgan says nothing. The silence is very loud.
""", [ch("Go on to Level Three.", "c7_l3")], enter=["add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_l2_crown", "The Crown of Durgan's Grandfather", """
You lift it down. The hoard sighs. The stone floor trembles, then settles. Durgan takes the crown with both hands and weeps openly.

"I have waited three hundred years to hold this."

It will matter later. Durgan does not forget a gift.
""", [ch("Go on to Level Three.", "c7_l3")], enter=["set:durgan_crown", "add:xp:1", "add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_l2_loot", "A King's Ransom", """
You load a canvas sack with a stranger's life's work. It is the most you have held since the Ford. The hoard does not seem to mind.

Yet.
""", [ch("Go on to Level Three.", "c7_l3")], enter=["add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_l2_wights", "Hoard-Wights", """
The coins stand up. Not literally, though they might as well: the pile coughs up a dozen things in dead-gold armour, hollow-eyed, bearing the shapes of dwarves long buried.

They come for you.
""", [
    ch("Fight them with Roland and Theodore.", "c7_l3", fx=["add:hp:-4", "add:clock.delve:1"]),
    ch("Anselm lifts the Skull. They stop.", "c7_l3", req="skull_below", fx=["add:clock.delve:1"]),
], redirect=RD, chapter=C)

sc("c7_l3", "Level Three: The Drowned Barracks", """
Rows of stone bunks. A long, low hall. In every bunk, a body: wet, grey, motionless. Six hundred of them, or more. They sleep with their eyes open.

At the far end of the hall, a man in rusted mail is chained to a pillar. He is alive. He lifts his head as you approach.

{{bors_taken|It is Sir Bors.}}{{!bors_taken|He is a stranger — a prisoner of the lich, human, half-starved.}}
""", [
    rk("Cross the hall in silence. Do not wake them.", "DEX", "c7_l3_ok", "c7_l3_wake", "c7_l3_wake"),
    ch("Anselm lifts the Skull. Walk through them.", "c7_l3_ok", req="skull_below"),
    ch("Theodore walks ahead. The undying knight cannot be harmed by them.", "c7_l3_theo", req="theodore_back"),
], enter=["add:clock.siege:1"], redirect=RD, chapter=C)

sc("c7_l3_ok", "Past the Sleepers", """
You cross the hall. The dead do not stir. At the pillar the chained man raises his head, and the lamp reveals his face.

{{bors_taken|It is Bors.}}
""", [
    ch("Free the prisoner.", "c7_l3_free"),
], redirect=RD, chapter=C)

sc("c7_l3_theo", "The Undying Walks First", """
Theodore walks down the aisle between the bunks, hand on his sword. The sleepers turn their heads to follow him and do not rise. The undying knight reaches the pillar first and cuts the chain.

"I know this face," he says. "He rode with me."
""", [ch("Take the prisoner.", "c7_l3_free")], redirect=RD, chapter=C)

sc("c7_l3_wake", "They Wake", """
A bunk creaks. Then another. Then six hundred wet hands push against stone, and the whole hall sits up together.
""", [
    ch("Run for the pillar. Cut the prisoner free and go.", "c7_l3_free", fx=["add:hp:-5", "add:clock.delve:1"]),
    ch("Anselm lifts the Skull.", "c7_l3_ok", req="skull_below", fx=["add:clock.delve:1"]),
], redirect=RD, chapter=C)

sc("c7_l3_free", "The Prisoner", """
{{bors_taken|"Sire," says Bors, with a voice like a rusted hinge. "I held out as long as I could. Not very long."}}{{!bors_taken|The man is Sir Garrick of the old garrison — one of the Deepholt's human wardens. "Six years," he says. "I thought it was six years."}}

He is thin, bearded, and alive. That is more than you expected.
""", [
    ch("Share your rations. Bring him with you.", "c7_l4", fx=["add:clock.delve:1", "if:bors_taken?court:+Bors", "if:bors_taken?set:bors_saved", "add:xp:1"]),
    ch("Send him up with Hetta. He is too weak to follow.", "c7_l4", fx=["if:bors_taken?court:+Bors", "if:bors_taken?set:bors_saved", "add:xp:1"]),
], redirect=RD, chapter=C)

sc("c7_l4", "Level Four: The Sunless Market", """
A great square of stone shopfronts, long vacated, lit by a cold, steady green glow. Stalls hold bone-carved wares, books of grey skin, dolls with too many joints.

In the centre of the square, seated on a plain stool, the grey-robed lich Malgareth is waiting.

"King Gregory," he says gently. "Sit. We have so little time, and so much to say."
""", [
    ch("Sit. Hear him out.", "c7_malgareth"),
    ch("Draw steel. End this now.", "c7_malg_fight"),
    ch("Refuse to sit. Stand and speak.", "c7_malg_stand"),
], enter=["add:clock.siege:1"], redirect=RD, chapter=C)

sc("c7_malgareth", "A Lich's Offer", """
He has a quiet, scholarly manner. "The god below is not my master. It is my jailer. It took me at the Ford of an older river, three hundred years ago, and I have served ever since. I do not enjoy it."

He lifts one gloved hand. "Give me the Skull. I will use it to put it down. I have studied the Skull for three centuries. You have carried it for three weeks. Which of us is better qualified?"

It is the most reasonable offer you have heard in two years.
""", [
    ch("\"No. I will not hand the Skull to you.\"", "c7_malg_no"),
    rk("\"Tell me how to kill it. Tell me the weakness.\"", "CHA", "c7_malg_weakness", "c7_malg_half", "c7_malg_lie"),
    ch("Consider it. (Hand over the Skull.)", "c7_malg_deal", req="skull_below"),
], redirect=RD, chapter=C)

sc("c7_malg_no", "A Disappointed Scholar", """
"A pity," says Malgareth. He gets to his feet, brushing dust from his robes. "I do not have the strength to take it from you. I had hoped you would be persuadable."

He steps aside. "The stair is that way. I shall wait here. Perhaps we will speak again."
""", [ch("Go on to Level Five.", "c7_l5")], redirect=RD, chapter=C)

sc("c7_malg_weakness", "The Truth, For Once", """
Malgareth hesitates for a long moment. The green light flickers.

"It is bound to its hoard. Every coin is a nail in its coffin. If the hoard is scattered, it weakens. If the Skull is raised in its throne-room, it *stops*."

He looks almost relieved. "I have never told anyone that. It took me three centuries to find the courage."
""", [ch("Go on to Level Five.", "c7_l5")], enter=["set:knows_weakness", "add:xp:1", "add:gambit:2"], redirect=RD, chapter=C)

sc("c7_malg_half", "A Half-Truth", """
"The Skull is a part of it," he says carefully. "And the hoard is a part. But I do not know all the parts."

It is not nothing.
""", [ch("Go on to Level Five.", "c7_l5")], enter=["set:knows_weakness", "add:gambit:1"], redirect=RD, chapter=C)

sc("c7_malg_lie", "A Lie", """
He smiles his small, old smile. "Strike it in the heart," says Malgareth, and says nothing more. You are not certain he told you the truth.
""", [ch("Go on to Level Five.", "c7_l5")], redirect=RD, chapter=C)

sc("c7_malg_deal", "The Skull Changes Hands", """
You hold out the box. Malgareth takes it with both hands, as one takes a newborn. He lifts the lid.

The Skull lies in its cloth. Malgareth looks at it for a very long time.

Then he closes the lid and hands it back.

"You would have given it to me," he says wonderingly. "I did not think anyone would."

He steps aside. "Go down. I will not follow. I am tired of following."
""", [ch("Go on to Level Five.", "c7_l5")], enter=["set:malgareth_trusted", "set:malgareth_ok", "add:xp:2"], redirect=RD, chapter=C)

sc("c7_malg_stand", "Words Standing Up", """
You do not sit. Malgareth lifts one eyebrow, amused, and lets the silence drag.

"As you wish," he says. "The question stands."
""", [
    ch("\"No.\"", "c7_malg_no"),
    ch("Draw steel.", "c7_malg_fight"),
], redirect=RD, chapter=C)

sc("c7_malg_fight", "Steel on Bone", """
Roland and Theodore charge. Malgareth is no swordsman, but he does not need to be: the green light flares, and the stalls of the Market begin to stand up, shelf by shelf, and come for you.
""", [
    rk("Hold the line.", "STR", "c7_malg_win", "c7_malg_drive", "c7_malg_drive"),
    ch("Anselm lifts the Skull.", "c7_malg_skull", req="skull_below"),
], redirect=RD, chapter=C)

sc("c7_malg_win", "The Steward Falls Back", """
The lich staggers, gutted by Roland's blade, and vanishes into the green dark with a hiss.

He will not die. But he is wounded, and the road to the fifth level is open.
""", [ch("Go on to Level Five.", "c7_l5")], enter=["add:xp:2", "add:hp:-2"], redirect=RD, chapter=C)

sc("c7_malg_drive", "Overrun", """
The Market overwhelms you. Theodore holds the stair so the rest of you can retreat. It is an expensive retreat.
""", [ch("Go on to Level Five.", "c7_l5")], enter=["add:hp:-6", "add:clock.delve:1"], redirect=RD, chapter=C)

sc("c7_malg_skull", "Stopped", """
Anselm lifts the Skull. The stalls fall back into silence. Malgareth stares at it from across the square, and something in his face breaks.

"Take it away," he says in a very small voice. "*Please.*"

He retreats into the dark.
""", [ch("Go on to Level Five.", "c7_l5")], enter=["add:xp:1", "set:malgareth_broken", "set:malgareth_ok"], redirect=RD, chapter=C)

sc("c7_l5", "Level Five: The Cistern of Names", """
A round hall, a great black cistern in the centre, lined with the names of the dead. Thousands. Each carved in a different hand.

Anselm kneels at the edge of the water and reads, his lips moving.

"They're all here," he says. "Every soul it took. It keeps them."

The water begins to ripple, as though something very large has noticed you.
""", [
    ch("Read the names aloud. Give them back their dead.", "c7_l5_read"),
    ch("Cross quickly. There is no time for grief.", "c7_l6", fx=["add:clock.delve:1"]),
    ch("Break the cistern. Let the names go.", "c7_l5_break", req="durgan_sworn"),
], enter=["if:skull_below?add:clock.siege:1"], redirect=RD, chapter=C)

sc("c7_l5_read", "The Reading of the Names", """
It takes an hour. Anselm reads. Alcuin, who is not even here — you realise it is Roland reading, in a voice you have never heard from him.

When you are finished the water is still. Something in the black has turned, and let go.
""", [ch("Go on to the last stair.", "c7_l6")], enter=["add:clock.delve:1", "add:xp:2", "set:names_read", "add:hp:4"], redirect=RD, chapter=C)

sc("c7_l5_break", "Durgan's Hammer", """
Durgan brings his hammer down once, twice, three times on the lip of the cistern. The stone cracks. The water drains away into the rock with a sound like a long exhale.

"There," he says. "Let them rest."
""", [ch("Go on to the last stair.", "c7_l6")], enter=["add:xp:1", "add:clock.delve:1", "set:cistern_broken"], redirect=RD, chapter=C)

sc("c7_l6", "Level Six: The Door", """
The last stair ends at a door of black iron, the height of three men. Hinges the size of a bull. A single keyhole, no bigger than your thumb.

Ambrose's sealed letter is in your pocket, as he promised. You break the wax and read the name. You do not speak it. You do not need to.

From behind the door comes the grinding hum you first heard in the Great Hall: the sound of something enormous, thinking.
""", [
    ch("Open the door.", "c7_throne"),
    ch("Turn back. Seal the door again. You have done enough.", "end_flight"),
], redirect=RD, chapter=C)

sc("c7_throne", "The Throne of the Hoarder", """
It is not a throne-room. It is the heart of a mountain, hollowed and lined with gold. A single seat of fused coin and bone. And upon it, the thing that calls itself a god.

It is not shaped like a man. It is not shaped like anything. It is a column of the dead, standing, bound by sinew and coin into a form that watches you with four hundred eyes.

"King Gregory," it says, in every voice it has ever eaten. "You have brought my bones back to me."

It means the Skull.
""", [
    ch("Anselm lifts the Skull. End it.", "c7_final_skull", req="skull_below"),
    ch("Charge it with your sword. Roland and Theodore at your side.", "c7_final_fight"),
    rk("Use the scattered hoard: break the coin-throne and unbind it.", "INT", "c7_final_hoard", "c7_final_fight", "c7_final_fight", req="knows_weakness"),
    ch("Listen. Hear what the god has to offer a king.", "c7_final_bargain"),
], redirect=RD, chapter=C)

sc("c7_final_skull", "The Skull Raised", """
Anselm lifts the Skull and the whole chamber goes still.

The god sees it. It knows what it is. It opens its four hundred mouths and screams, and the scream is the sound of every soul it ever kept, rising at once.

Then the god *stops*. Coin by coin, bone by bone, the thing on the throne comes apart, and what is left is a dry, grey drift, like ash.
""", [
    ch("Stand over what remains.", "c8_victory_hub"),
], enter=["add:xp:3", "set:god_dead"], redirect=RD, chapter=C)

sc("c7_final_hoard", "The Throne Broken", """
You see it all at once: the coin and bone and gold lashed into a body. You see where the seams are, and which nail holds the rest.

"Durgan," you say. "The third rank from the left. The great banner-pole."

The dwarf's hammer comes down like a falling star.
""", [ch("Watch it come apart.", "c8_victory_hub")], enter=["add:xp:3", "set:god_dead", "set:hoard_scattered"], redirect=RD, chapter=C)

sc("c7_final_fight", "The Last Battle", """
The god fights as a dozen men would: a hundred arms, a hundred swords. Roland takes a blow meant for you. Theodore, the undying, simply stands in the doorway and refuses to move.

You hack at the throne with a king's sword and a king's courage. It is not enough. It is never enough.
""", [
    ch("Press on. (Spend a Gambit.)", "c8_victory_hub", req="gambit>=1", fx=["add:gambit:-1", "add:hp:-6", "set:god_dead", "add:xp:2"]),
    ch("Anselm lifts the Skull at the last moment.", "c7_final_skull", req="skull_below"),
    rk("Throw everything into one last charge.", "STR", "c8_victory_hub", "c8_victory_hub", "end_death",
       hit_fx=["set:god_dead", "add:xp:2"], mixed_fx=["set:god_dead", "add:hp:-8", "add:xp:1"]),
    ch("Fall back. This was a mistake.", "end_death"),
], redirect=RD, chapter=C)

sc("c7_final_bargain", "The Hollow Crown", """
The god leans forward. "A king without a kingdom. A man with a skull he cannot use. I offer you what you wanted at the Ford: a crown that cannot be taken. A realm that will not die. A people who will never leave you."

Its voice is very gentle.

"Kneel."
""", [
    ch("Refuse. Stand and fight.", "c7_final_fight"),
    ch("Kneel.", "end_bargain"),
], redirect=RD, chapter=C)

# ------- endings -------
sc("end_triumph", "The Kingdom Under the Mountain", """
You climb for two days. At the top of the stair the sun is a white wound in the sky, and the dead are lying on the slope of the mountain like fallen wheat. Aldric is on the wall. He sees the standard and begins to weep.

The horde does not rise. Malgareth's host lies still across a hundred miles of road.

{{bors_saved|Bors rides at your side in the procession, thin and quiet, and keeps his sword drawn for a month.}}{{theodore_back|Theodore, the undying, takes the Wall. He does not sleep. He does not need to.}}{{isobel_durgan|Isobel and Durgan hold the Great Hall together, and the dwarves rebuild it in her name.}}{{heir_frail|Your son sees the sun for the first time on the day you return. He cries, loud for once, and Saoirse laughs until she weeps.}}{{durgan_crown|Durgan wears his grandfather's crown at the coronation, and swears a second time.}}

You do not sit on a throne. You sit on a stool by the fire in the Great Hall of the Deepholt, with a pipe in your mouth, and watch your people eat.

It is enough.
""", ending="TRIUMPH — The Kingdom Under the Mountain", chapter=C)

sc("end_sacrifice", "The King Under the Mountain", """
You send Roland up with the standard, and Anselm with the box. You stay, with Durgan, who refuses to leave, and Theodore, who cannot.

The door seals behind you. The three of you sit on the stone steps of a ruined throne-room and wait, as the god's ashes settle, in the dark.

Years later, the scholars say, a light is seen burning in the deepest window of the Deepholt. A king keeps watch.
""", ending="SACRIFICE — The King Under the Mountain", chapter=C)

sc("end_bargain", "The Hollow Crown", """
You kneel. The god puts its crown on your head: a ring of gold and bone and screaming faces.

For a thousand years you rule. Your Court never leaves you. Your people never die. They do not sleep, or eat, or leave. They simply stand in rows in the Great Hall of the Deepholt, eyes open, and obey.

Roland is the last to look at you with recognition. He kneels, too, and weeps, and does not rise.
""", ending="BARGAIN — The Hollow Crown", chapter=C)

sc("end_flight", "The Long Road", """
You seal the door behind you. Durgan sets the stone. Anselm says the old prayer. You climb.

The god below does not wake. Not that year. Not that decade. You and your people live in the mountain for a generation, and then, when you are old and the walls are strong, you wander back down to the lowlands and teach your grandchildren to listen at night for a sound beneath the floor.

You have not won. But you have not lost.
""", ending="FLIGHT — The Long Road", chapter=C)

sc("end_siege", "The Walls Fall", """
You hear it first as a bell, ringing wild: Ambrose, shouting down the stair. Then the sound stops.

By the time you climb out, the mountain is burning. Isobel's ledger lies in the courtyard, pages scattered. Aldric's sword is in the stone beside the gate.

The dead have taken everything. You have the Skull. You have no one left to protect with it.
""", ending="THE WALLS FALL", chapter=C)

sc("end_starve", "The Dark Below", """
The food runs out on the fifth day. The lamps run out on the sixth. On the seventh, you sit in the dark with Roland, who says he is not hungry, and Theodore, who does not need to be.

Years later, someone finds your standard on the stair of the sixth level, folded neatly on a rock.
""", ending="THE DARK BELOW", chapter=C)

sc("death", "Gregory VII Falls", """
You fall.

The last thing you see is Roland's face, white and furious, and the standard going down behind you like a flag in a storm.

There is no one to carry the Skull now. There is only the dark, and the voice of the god, patient, pleased.
""", ending="DEATH — Here Lies Gregory the Exiled", chapter=C)

sc("end_death", "A Fatal Error", """
You fall back too late. The god's reach is long.
""", ending="DEATH — A Fatal Error", chapter=C)
