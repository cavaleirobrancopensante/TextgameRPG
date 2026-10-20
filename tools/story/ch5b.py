from dsl import *
C = "Chapter V — The Bell"

sc("c5_betrayal", "The Postern Opens", """
It happens at midnight. You are on the bridge with Roland when the postern in the mill-house wall swings inward, and a man you trusted steps out into the torchlight.

{{alcuin_spy|It is Alcuin. His face is wet. "I'm sorry," he says. "I'm so sorry. He has my sister."}}{{!alcuin_spy|It is Pell, the clerk, hollow-eyed. He drew the bolts himself.}}

Behind him, in the dark of the lock-house, something grey is already moving.
""", [
    ch("Kill him. There is no time.", "c5_betrayal_kill", fx=["add:renown:-1"]),
    rk("Close the postern with your own hands.", "STR", "c5_betrayal_hit", "c5_betrayal_mixed", "c5_betrayal_miss"),
    ch("Spend a Gambit: where would the dead go next? Cut them off.", "c5_betrayal_hit", req="gambit>=1", fx=["add:gambit:-1"]),
], enter=["set:spy_done", "set:bridge_betrayed"], chapter=C)
sc("c5_betrayal_kill", "A Hurried Blow", """
The man falls. The postern still stands open. Roland slams it shut, and bars it with his own sword.
""", [ch("The host is coming. Turn to face it.", "c5_siege")], enter=["add:hp:-4", "add:coin:-30"], chapter=C)
sc("c5_betrayal_hit", "The Door Holds", """
You hit the oak door with your shoulder and drive the bar home. The thing behind scratches, then goes quiet. Alcuin, or Pell, sinks against the wall and does not run.
""", [ch("The host is coming. Turn to face it.", "c5_siege")], enter=["add:xp:1"], chapter=C)
sc("c5_betrayal_mixed", "Barely", """
You close it, but not before something grey takes a bite out of the lock-keeper's arm. Ferrand or Brom will have to deal with the rest.
""", [ch("The host is coming. Turn to face it.", "c5_siege")], enter=["add:hp:-3"], chapter=C)
sc("c5_betrayal_miss", "The Lock-House Falls", """
Five of the dead get in. By the time Roland and Corbin clear the lock-house, eight people are dead and the mill-race is blocked with bodies.
""", [ch("The host is coming. Turn to face it.", "c5_siege")], enter=["add:hp:-6", "add:renown:-1", "add:coin:-40"], chapter=C)

# ---- Fen wraiths ----
sc("c5_wraith", "The Marsh-Wraiths", """
"Before we talk of crowns," Saoirse says, "there is a thing in the reeds I need killed."

Marsh-wraiths: drowned fen-folk who walk the water at night and drag children into the mud. The Skull would end them, but the Skull is not here to be spent on a marsh. Her boatmen are afraid to go out after dark.
""", [
    rk("Lead the boats out at dusk, with torches and the standard.", "CHA", "c5_wraith_hit", "c5_wraith_mixed", "c5_wraith_miss"),
    ch("Burn the reeds. Fire is faster than courage.", "c5_wraith_burn"),
], chapter=C)
sc("c5_wraith_hit", "The Night on the Water", """
You stand in the bow of a reed-boat with the standard held high and the fen-folk behind you in silence. The wraiths come in a line, white-eyed, and you do not blink.

When it is over, the marsh is quiet. Saoirse takes your hand in the dawn light, and does not let it go.
""", [ch("Return to the fen-queen.", "c5_fenmarch_after")], enter=["set:wraiths_cleared", "set:saoirse_charmed", "add:xp:2", "add:renown:1"], chapter=C)
sc("c5_wraith_mixed", "Half a Victory", """
The wraiths are broken, but three fen-boats go under before the last one dissolves. Saoirse is grateful, and grieving.
""", [ch("Return to the fen-queen.", "c5_fenmarch_after")], enter=["set:wraiths_cleared", "add:xp:1", "add:hp:-2"], chapter=C)
sc("c5_wraith_miss", "The Reeds Take Them", """
The boats are surrounded. You lose a third of Saoirse's boatmen before the wraiths scatter at dawn.
""", [ch("Return to the fen-queen.", "c5_fenmarch_after")], enter=["add:hp:-5", "add:renown:-1", "set:saoirse_cold"], chapter=C)
sc("c5_wraith_burn", "A Burning Marsh", """
The reeds go up like straw. The wraiths scream. So do half the fen-folk's homes.
""", [ch("Return to the fen-queen.", "c5_fenmarch_after")], enter=["set:wraiths_cleared", "set:saoirse_cold", "add:renown:-1"], chapter=C)
sc("c5_fenmarch_after", "Terms With the Queen", """
Saoirse studies you, chin on fist.

{{saoirse_charmed|"I think," she says slowly, "that I would like you to stay."}}{{!saoirse_charmed|"A fair day's work," she says. "Now we negotiate."}}
""", [
    ch("\"Safe harbour. A wall on the river. A place for your people when the dead come.\"", "c5_saoirse_deal"),
    rk("\"A union. My crown and yours, my Court and your boats.\"", "CHA", "c5_saoirse_marry", "c5_saoirse_deal", "c5_saoirse_cold"),
    ch("\"Marry me.\"", "c5_saoirse_marry", req="saoirse_charmed"),
], chapter=C)

# ---- Three days of Malgareth ----
sc("c5_three_days", "The Third Day", """
Three days. You have spent them well, or you have spent them badly. On the evening of the third, a white flag rises on the far bank, and Malgareth's voice, patient as a physician's, comes across the water.

"King Gregory. The courtesy is expended. Your answer?"
""", [
    rk("Feint. Offer a decoy box to be handed over at the river's centre.", "INT", "c5_feint_hit", "c5_feint_mixed", "c5_feint_miss"),
    ch("Use the Alcuin channel: the false reports have set the trap.", "c5_feint_hit", req="alcuin_double"),
    ch("Refuse. Raise the standard.", "c5_refuse"),
    ch("Accept a winter truce. Pay in coin, not relics. (100 coin)", "c5_truce", req="coin>=100", fx=["add:coin:-100", "add:corruption:1"]),
], chapter=C)
sc("c5_feint_hit", "The Decoy Takes", """
Malgareth's hand closes around a wooden box. The lid lifts. Inside is a bundle of straw, a splinter of oak from the Aldermont gate, and one of Brom's more pungent mushrooms.

The silence stretches. When he lifts his head, he is — almost — laughing. "I do admire a good lie," says the lich. "It will cost you a winter."

The host withdraws a week's march. The river sleeps.
""", [ch("Use the time well.", "c5_prep")], enter=["set:lich_fooled", "add:xp:2", "add:gambit:2"], chapter=C)
sc("c5_feint_mixed", "Suspicion", """
He doesn't open the box. He weighs it in his hand, and smiles. "Light," he says, "for such a weighty thing."

He steps back across the river and the host stirs.
""", [ch("Make your preparations.", "c5_prep")], chapter=C)
sc("c5_feint_miss", "A Poor Liar", """
The lid lifts, and the straw inside is the last thing you see before the front rank begins to move.
""", [ch("Make your preparations. Quickly.", "c5_prep")], enter=["add:hp:-3"], chapter=C)
sc("c5_truce", "The Winter Truce", """
Malgareth takes the coin, and his word, and the word is good as lich-words go. The host withdraws a day's march. The river sleeps. The king has bought a winter with purse and conscience.

It is a poor victory, but it is a victory of the kind that leaves people alive.
""", [ch("Find a home in the hills.", "c6_found")], enter=["set:winter_truce", "set:evacuated"], chapter=C)

# ---- extra siege plans ----
sc("c5_champion", "The Champion at the Bridge", """
A figure steps onto the far end of the bridge: armoured, tall, bareheaded, with a face you know.

{{knows_varric|It is Lord Varric of the Western March, whom the Ford made undead. The lich has raised him to hold the bridge.}}{{!knows_varric|He wears the colours of a lord of your own kingdom. His eyes are milk.}}

He raises a sword, and waits.
""", [
    rk("Cross the bridge. Meet him in single combat.", "STR", "c5_champ_hit", "c5_champ_mixed", "c5_champ_miss"),
    ch("Send Theodore. The undying cannot be killed.", "c5_champ_hit", req="court:Theodore"),
], enter=["set:champion_done"], chapter=C)
sc("c5_champ_hit", "A Sword Through the Dead", """
{{knows_varric|You have waited for this. Varric's sword is quick, but your hatred is quicker. He falls on the bridge boards, and his helm rolls into the river. The dead are silent. You have taken their lord.}}{{!knows_varric|The champion falls, and the host sags. For a moment you can feel their purpose waver.}}
""", [ch("Return to your preparations.", "c5_prep")], enter=["add:xp:2", "add:renown:2", "set:champion_won", "if:knows_varric?set:varric_dead"], chapter=C)
sc("c5_champ_mixed", "A Hard-Won Blow", """
You lose a hand's width of skin from your forearm, but the champion falls. The host recoils.
""", [ch("Return to your preparations.", "c5_prep")], enter=["add:xp:1", "add:hp:-5", "set:champion_won"], chapter=C)
sc("c5_champ_miss", "Beaten Back", """
The champion's sword goes through your shoulder before Roland drags you away. You live. Hartmann holds the bridge until the wound can be bound.
""", [ch("Return to your preparations.", "c5_prep")], enter=["add:hp:-8", "add:renown:-1"], chapter=C)
sc("c5_bridge_hold", "Hold the Bridge", """
You do not have the Skull armed, and you do not have the fire-rafts ready, but you have a stone bridge, a chain, and a line of pikes.

The dead come across in files of six. Roland and Corbin hold the right. Hartmann holds the left. You hold the centre.
""", [
    rk("Hold until dawn.", "CON", "c5_hold_hit", "c5_hold_mixed", "c5_hold_miss"),
], chapter=C)
sc("c5_hold_hit", "The Bridge Holds", """
By dawn the bridge is a drift of broken things, and you are still standing. The host withdraws, bleeding, and the Bell on the mountain tolls the last of them down.
""", [ch("Count the cost.", "c5_victory")], enter=["add:xp:2", "add:hp:-3", "add:renown:2"], chapter=C)
sc("c5_hold_mixed", "Barely", """
You hold it, barely. Three of the pikemen are dead, and Corbin has lost two fingers. But the dawn comes.
""", [ch("Count the cost.", "c5_victory")], enter=["add:xp:1", "add:hp:-6"], chapter=C)
sc("c5_hold_miss", "The Line Breaks", """
The right flank gives at midnight. You fall back across the bridge into the lock-house with a dozen survivors, and slam the door.
""", [ch("Evacuate.", "c5_evac_first")], enter=["add:hp:-8", "add:renown:-1"], chapter=C)
