from dsl import *
C = "Chapter VI — Stone Upon Stone"

sc("c6_found", "Founding", """
The mountain above the abbey has a long shelf of rock, a spring, and a view down three valleys. It is the best place you have seen in a year, and it is nothing yet. A kingdom needs more than a standard, and you have the people to build it.

Durgan paces the ground with a measuring-cord, grumbling about foundations. Isobel stands with the ledger.

"We have the labour for three works before winter," she says. "Choose well."
""", [
    ch("The Mill — a water-wheel on the spring, to grind grain and drive saws.", "c6_found", req="!b_mill", fx=["set:b_mill", "add:built:1"]),
    ch("The Granary — stone-vaulted, rat-proof, big enough for a winter.", "c6_found", req="!b_granary", fx=["set:b_granary", "add:built:1"]),
    ch("The Chapel — a place for Anselm and Ambrose to hold the dead's rites.", "c6_found", req="!b_chapel", fx=["set:b_chapel", "add:built:1"]),
    ch("The Wall — a curtain of dwarf-cut stone around the shelf.", "c6_found", req="!b_wall", fx=["set:b_wall", "add:built:1"]),
    ch("The Bell-Mount — a tower to carry the Bell and the Skull.", "c6_found", req="!b_bellmount", fx=["set:b_bellmount", "add:built:1"]),
    ch("The Sky-Farms — terraced fields cut into the cliff.", "c6_found", req="!b_skyfarm", fx=["set:b_skyfarm", "add:built:1"]),
], redirect=[{"if": "built>=3", "goto": "c6_year"}], chapter=C)

sc("c6_year", "A Year", """
A winter passes. Then a spring. Then a harvest.

The works go up. The Wall rises, or doesn't. The grain comes in, or doesn't. Your people stop looking over their shoulders at every sound, and begin, cautiously, to look at each other.

By the next autumn there are children playing in the courtyard. By the autumn after that, a baby is born in the royal chambers: a frail, red-haired, green-eyed boy who does not cry as loud as he should.
""", [
    ch("Hold the child. Name him.", "c6_heir", req="queen_saoirse"),
    ch("Continue.", "c6_feast", req="!queen_saoirse"),
], enter=["add:hp:18", "add:xp:1"], chapter=C)

sc("c6_heir", "The Heir", """
He is light as a loaf. His breathing is a small, steady rasp. Ambrose says what he can: sun, care, patience. Ferrand says the same, more carefully.

Saoirse watches you hold your son with something unreadable in her face.

"He will live," she says, "because I have decided it."

You are not at all sure that it is up to her.
""", [ch("Continue.", "c6_feast")], enter=["set:heir_frail"], chapter=C)

sc("c6_feast", "The Feast of the First Harvest", """
A great table runs the length of the courtyard. Dwarf-brewed ale, fen-smoked eel, orchard apples from Ashgrove. The Red Hand brothers sing hymns with their shirts undone. Halbrecht, who still doesn't call you Majesty, stands to toast "the man who didn't die."

It is the first night in two years that no one keeps watch from the wall.

At the end of the table, Lady Isobel sits straight as a rod, glaring at Durgan, who is trying very hard not to look at her.
""", [
    rk("Play the matchmaker. Pair the widows of the column with the bachelor dwarves.", "CHA", "c6_match_hit", "c6_match_mixed", "c6_match_miss"),
    ch("Let them find their own way. Enjoy the night.", "c6_levy", fx=["add:hp:4"]),
], chapter=C)

sc("c6_match_hit", "Marriages", """
By the end of the night there are six pairs at the table, and one pair, Lady Isobel and Durgan the Stone-Warden, that has stopped pretending not to be. She marries him the next spring, in the Chapel, with a dwarven crown-of-iron in her hair.

A generation of children will be born of this table: half-height, strong-willed, and, you suspect, impossible.
""", [ch("Raise the levy.", "c6_levy")], enter=["set:isobel_durgan", "add:xp:1", "add:gambit:1"], chapter=C)

sc("c6_match_mixed", "A Few Matches", """
Some pairs take. Some do not. Isobel, however, stands up from her chair and informs Durgan, in front of everyone, that if he is going to stare at her he may as well ask. He does.
""", [ch("Raise the levy.", "c6_levy")], enter=["set:isobel_durgan", "add:xp:1"], chapter=C)

sc("c6_match_miss", "Awkward", """
It is a disaster. Three widows storm off. A dwarf proposes to a goat. Isobel looks at you with a flat, tired expression that says: *this is exactly why I hate you.*
""", [ch("Raise the levy.", "c6_levy")], chapter=C)

sc("c6_levy", "The Levy", """
In the spring the scouts return with the same report: the dead are massing again in the lowlands. Malgareth is not a lich who forgets.

Aldric, now sixteen, is the obvious choice for Captain of the Levy. He is stiff with pride and terrified in the right ways.

"How many men do I need?"
""", [
    ch("\"All of them. Every adult with legs.\"", "c6_levy_all", fx=["set:levy_big"]),
    ch("\"Eight hundred. The best. The rest hold the wall.\"", "c6_levy_elite", fx=["set:levy_elite"]),
], chapter=C)

sc("c6_levy_all", "Everyone", """
Aldric nods, pale. "Everyone, then."

By midsummer there are two thousand people under arms and no one in the fields. It is the kind of army that wins by exhausting itself on the enemy.
""", [ch("Send Sam to the fen for reinforcements.", "c6_sam")], chapter=C)

sc("c6_levy_elite", "Eight Hundred", """
Eight hundred men trained by dwarf and Red Hand, led by a sixteen-year-old with his father's sword. They are not a horde. They are a blade.
""", [ch("Send Sam to the fen for reinforcements.", "c6_sam")], chapter=C)

sc("c6_sam", "The Squire's Errand", """
Sam is twenty now, no longer a boy, and still serves as your squire out of pure stubbornness. You hand him a letter, a seal, and a fen-boat.

"Go to the Fenmarch. Bring me the warriors the queen has promised."

He grins. "And if she's in a mood?"

"Bring your charm."
""", [ch("A scout rides in. The Abbot wants to see you. At once.", "c7_library")], enter=["set:sam_to_fen"], chapter=C)
