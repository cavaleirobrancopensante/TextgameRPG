from dsl import *
C = "Chapter IV — The Deepholt"

sc("c4_hub", "The Halls of the Deepholt", """
The Deepholt is not a dwarven city so much as a dwarven *argument* with stone, a thousand years old and not finished. Corridors lit with phosphor-moss. Forges banked low. A hall of benches built for a population five times the size of the one that remains.

The column is housed. The wounded are being tended. And Durgan, hands clasped behind him, asks the question that is all courtesy and all test: "What would the king see, while he is our guest?"
""", [
    ch("The Council of Thanes — I should hear who opposes me.", "c4_council", req="!did_council"),
    ch("Durgan's forge — I will need arms for what comes.", "c4_forge", req="!did_forge4"),
    ch("The upper stairs. Let me see what the dwarves fear.", "c4_testdelve", req="!did_test"),
    ch("The Hall of Benches — a feast, with the folk who remain.", "c4_feast", req="!did_feast4"),
    ch("Go down to the First Hall, to the standing dead.", "c4_theodore"),
], chapter=C)

# ---- council ----
sc("c4_council", "The Council of Thanes", """
Seven thanes sit on a half-circle of stone chairs. Six look at you with the expressions of people calculating the weight of a stranger. The seventh, Thane Bruni, a one-eyed dwarf with a beard shaved to a grey stubble, does not look at you at all.

"We take in men," Bruni says, to the roof, "and men bring the dead. Men woke what we sealed. Why is the first thing we do in our hour of need to open the gate to the cause of it?"

Several of the thanes shift. The question has weight.
""", [
    rk("Answer him. Plainly, with respect.", "CHA", "c4_council_hit", "c4_council_mixed", "c4_council_miss"),
    ch("Offer him a duel of honour, if that is how dwarves settle this.", "c4_council_duel", req="hp>=10"),
    ch("Concede his point. Offer to pay for every week we remain. (50 coin)", "c4_council_pay", req="coin>=50", fx=["add:coin:-50"]),
], chapter=C)
sc("c4_council_hit", "Bruni Is Answered", """
"You are right," you say. "The dead are my fault. Not the Ford, perhaps; not the gate; but I am the king of those who failed, and I will not hide behind the failure. I came to you because I have nowhere else, and because you have the only walls that can withstand them. Let me earn the stone."

Bruni stares at you for a long time. Then he laughs, and it is a surprisingly warm sound. "Aye. Let you earn it, then."
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_ally", "add:renown:1", "add:xp:1"], chapter=C)
sc("c4_council_mixed", "A Wary Majority", """
It's enough to carry four of the seven. Bruni does not smile, but he nods once and sits back. He will watch you from now on.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_wary"], chapter=C)
sc("c4_council_miss", "Bruni Walks Out", """
You hear yourself saying the wrong things. Bruni leaves before you've finished. Two others follow. By night, twelve dwarves have quit the Deepholt for the lower farms, muttering that no king is worth the gate.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_enemy", "add:renown:-1"], chapter=C)
sc("c4_council_duel", "Honour in the Pit", """
Dwarvish duels are fought in a stone ring, bare hands and a single hammer between them. Bruni takes the hammer. You take the pit.

The thanes shout bets in a language you half know.
""", [rk("Fight him.", "STR", "c4_duel_hit", "c4_duel_mixed", "c4_duel_miss")], chapter=C)
sc("c4_duel_hit", "A King Who Fights", """
You hold the hammer for exactly three heartbeats. In the fourth Bruni's wrist pops, and he drops it, laughing. "Aye! A king, by the rock! I thought you would run."

He kneels in the dust, in the dwarf fashion, and offers his beard to be pulled. You pull it.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_ally", "set:bruni_friend", "add:xp:2", "add:renown:2", "add:hp:-2"], chapter=C)
sc("c4_duel_mixed", "A Draw", """
You both end up on your backs, panting. The thanes declare it a draw and stand to clap. It is not quite respect, but it is its cousin.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_wary", "add:hp:-4", "add:xp:1"], chapter=C)
sc("c4_duel_miss", "Pounded Into the Stone", """
You wake with a doctor's thumb in your mouth. Bruni, grudgingly, has cleaned the blood from your face. "Not a fighter," he allows. "But not a coward either."
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_wary", "add:hp:-8"], chapter=C)
sc("c4_council_pay", "Coin on the Table", """
You pile the coin on the stone. Bruni looks at it, then at you. "It is not enough," he says. "It is the right kind of not-enough." He pockets it. The thanes breathe out.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_council", "set:bruni_wary", "add:renown:1"], chapter=C)

# ---- forge ----
sc("c4_forge", "The Forge of the Deepholt", """
Durgan's forge is a cavern of black anvils, quenching troughs, and a bellows the size of a boat. A dozen dwarf-smiths work the iron with the patient rhythm of men who have all the time in the world and none of it to waste.

"Choose one," Durgan says. "A gift for a friend. I'll not forge for a stranger twice."
""", [
    ch("Dwarf-forged mail, light as cloth. (+4 max HP)", "c4_forge_done", fx=["set:dwarf_mail", "add:max_hp:4", "add:hp:4"]),
    ch("A dwarf-steel blade, with a rune of binding. (Helps in the final fight.)", "c4_forge_done", fx=["set:rune_blade"]),
    ch("A delvers' lantern, whose light does not fail. (Will slow the clocks below.)", "c4_forge_done", fx=["set:delver_lantern"]),
    ch("A coil of dwarf-rope and stone-pitons. (Opens shortcuts below.)", "c4_forge_done", fx=["set:delver_rope"]),
], chapter=C)
sc("c4_forge_done", "A Dwarf's Gift", """
Durgan hands it to you with both hands and a grunt. "Don't die in it," he says gruffly. "I hate having to melt it down."
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_forge4", "add:xp:1"], chapter=C)

# ---- upper stairs test delve ----
sc("c4_testdelve", "The Upper Stairs", """
Hetta leads you with a lantern and three dwarves down the first flight of the great stair. The stone gets colder. The moss gets thinner. At the first landing a door stands open: the Hall of Maps, abandoned in a hurry.

Hetta stops. "Something moved," she says.
""", [
    rk("Go in carefully. Look for what the dwarves left behind.", "INT", "c4_test_hit", "c4_test_mixed", "c4_test_miss"),
    ch("Turn back. Hetta's instincts are better than yours.", "c4_hub", fx=["set:did_test", "add:xp:1"]),
], chapter=C)
sc("c4_test_hit", "A Map of the Deep", """
In a niche behind a fallen cabinet: a scroll, rolled in oilcloth, the lower levels sketched in an old dwarf hand. Six levels. The Hoard. The Barracks. The Market. The Cistern. The Door.

The map is incomplete. The last room is marked only by a skull in a circle, and a single word: *DON'T*.
""", [ch("Take the map and return.", "c4_hub")], enter=["set:did_test", "set:deep_map", "add:xp:2", "add:gambit:1"], chapter=C)
sc("c4_test_mixed", "A Fragment", """
Half the map is rotted. You get the first three levels and a vague warning about the fifth.
""", [ch("Return.", "c4_hub")], enter=["set:did_test", "set:deep_map_half", "add:xp:1"], chapter=C)
sc("c4_test_miss", "Something Moved", """
It was a drowned thing, wearing a dwarven helm. Hetta puts a bolt through it, but not before it opens your shoulder.
""", [ch("Return.", "c4_hub")], enter=["set:did_test", "add:hp:-5"], chapter=C)

# ---- feast ----
sc("c4_feast", "The Hall of Benches", """
Dwarf-brewed ale in stone tankards the size of a man's head. Mushroom stew with a dozen kinds of cap. A bard with a drum sings a song in a language where every verb is a hammer.

For one evening a tired mountain feels like a home.
""", [
    ch("Drink with the dwarves. Match them, tankard for tankard.", "c4_feast_drink"),
    ch("Speak with the old women of the halls. They remember the Deepholt at its height.", "c4_feast_elders"),
    ch("Give a toast to the fallen, human and dwarf.", "c4_feast_toast"),
], chapter=C)
sc("c4_feast_drink", "Tankard for Tankard", """
{{drive_pleasure|It is the finest night of the whole retreat. You wake in a dwarf's bed (empty, thank God) with a head like an anvil and a heart like a lark.}}{{!drive_pleasure|You lose the contest, but win the hall: a king who laughs at himself is a king the dwarves can follow.}}
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_feast4", "add:renown:1", "if:drive_pleasure?add:xp:2", "if:drive_pleasure?add:hp:8", "add:hp:-2"], chapter=C)
sc("c4_feast_elders", "The Matrons", """
They tell you the history of the Deepholt, over bowls of stew. They tell you of the seventh thane who went down the stair a hundred years ago and did not return. They tell you what the dwarves heard in the stone, before.

"It sings," says the eldest, wizened as a walnut. "Always the same three notes. Like it is waiting for someone to complete the tune."
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_feast4", "set:knows_deep", "set:knows_song", "add:xp:1"], chapter=C)
sc("c4_feast_toast", "To the Fallen", """
You stand and say their names, human and dwarf, as many as you know. The hall falls silent. At the end, the old dwarves strike their tankards on the stone, three times.

It is the sound of acceptance.
""", [ch("Back to the Halls.", "c4_hub")], enter=["set:did_feast4", "add:renown:2", "add:xp:1"], chapter=C)
