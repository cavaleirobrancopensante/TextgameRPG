from dsl import *
import dsl
C = "Chapter VI — Stone Upon Stone"

def event(id, title, text, options):
    """options: list of (label, result_text, fx, req)"""
    choices = []
    for n, (label, result, fx, req) in enumerate(options):
        rid = f"{id}_r{n}"
        sc(rid, title, result, [ch("The season turns.", "c6_season")], enter=fx, chapter=C)
        choices.append(ch(label, rid, req=req))
    sc(id, title, text, choices, chapter=C)

EVENTS = ["c6_ev_famine", "c6_ev_plague", "c6_ev_brawl", "c6_ev_emissary", "c6_ev_caravan", "c6_ev_wedding",
          "c6_ev_rockfall", "c6_ev_bandits", "c6_ev_omen", "c6_ev_fen", "c6_ev_pilgrims"]

sc("c6_season", "The Turning Year", """
The seasons turn on the mountain. Wood-smoke and snow. Mud. Bees in the kitchen-garden. Every few weeks, something new asks for your attention.
""", [
    rnd("Winter comes down.", EVENTS),
    rnd("Spring comes up.", EVENTS),
    rnd("Summer burns.", EVENTS),
], enter=["add:season:1"], reenter=["add:season:1"], redirect=[{"if": "season>=5", "goto": "c6_year"}], chapter=C)

event("c6_ev_famine", "A Lean Winter", """
The snow comes early and stays late. By midwinter the granary is two-thirds empty, and the children have learned to play at being hungry.
""", [
    ("Open the sealed stores. Spend the reserve.", "The reserve carries you through. By spring the stores are empty and the people are alive.", ["add:coin:-40", "add:renown:1"], None),
    ("Trust Isobel's ledger. She has been right so far.", "Isobel's rationing is merciless and exact. No one starves. A few people hate her for it. She is entirely unrepentant.", ["add:xp:1", "add:renown:1"], "isobel_empowered"),
    ("Send hunting parties to the lowlands, past the dead.", "Half the party returns. They bring venison, deer-hides and a grim reluctance to speak of what they saw.", ["add:hp:-3", "add:xp:1"], None),
    ("Eat the carp. All of it.", "The stew-ponds, thank God, were stocked. By spring you will never eat fish again.", ["add:xp:1"], "carp_plan"),
])
event("c6_ev_plague", "The Cough", """
A wasting cough runs through the lower huts. Brom suspects the water. Ferrand, if he were alive, would suspect something worse.
""", [
    ("Boil all water; quarantine the sick in the old chapel.", "It costs a week, and eleven lives, but the cough burns out.", ["add:hp:-2", "add:xp:1"], None),
    ("Ask Brom to brew a deep-cap tonic.", "Brom's tonic is vile and works. The cough fades, and Brom drinks the leftovers himself, 'to be safe'.", ["add:xp:1", "add:renown:1"], "brom_ally"),
    ("Pray. Let the monks lead.", "Ambrose and his three hundred chant for nine days. Whether it was the prayers or the weather, the cough lifts.", ["add:xp:1"], None),
])
event("c6_ev_brawl", "Dwarf and Man", """
A tavern argument escalates. A dwarf and a Red Hand brother, a dispute over a seat, and then a table. By evening it is thirty men, and someone has drawn a knife.
""", [
    ("Stand between them. Make them break it up.", "You end up with a black eye and two grudging apologies.", ["add:hp:-2", "add:renown:1"], None),
    ("Have Bruni and Vance sort it. They respect each other.", "Bruni and Vance share a bench for a week, glaring and drinking. It does more for unity than your whole speech.", ["add:xp:1", "add:renown:1"], "bruni_ally"),
    ("Hang the first man to draw steel.", "The brawl ends instantly. So does something else.", ["add:renown:-1"], None),
])
event("c6_ev_emissary", "A Grey Emissary", """
A skeletal rider approaches the mountain gate under a white flag. It carries a scroll, written in a hand you recognise: the lich's own.

The scroll is an invitation to treat. It says Malgareth will pay for the Skull in any coin you name.
""", [
    ("Burn the scroll. Burn the rider.", "The rider crumbles. The scroll curls. Malgareth's invitation goes unanswered.", ["add:xp:1"], None),
    ("Read it aloud to the whole mountain. Let them hear the offer.", "The mountain listens. The mountain laughs. The rider rides home with a hundred insults. It is the best morale you've had in months.", ["add:renown:2"], None),
    ("Send an answer through Alcuin's channel.", "Alcuin's reply is a masterpiece of deception. The lich will believe whatever he is told for a month.", ["add:gambit:2", "add:xp:1"], "alcuin_double"),
    ("Entertain the offer. Ask for terms.", "He names a price. It is a good price. You tell yourself you are only listening.", ["add:corruption:1", "add:coin:120"], None),
])
event("c6_ev_caravan", "Caravan from the Lowlands", """
A caravan of eight wagons toils up the mountain road, led by a woman who claims to be Bael's cousin. They are carrying cloth, nails, salt, and a rumour that the dead are thinning in the southern vales.
""", [
    ("Trade fairly. Buy salt and nails.", "The mountain smells of salt for a month. The smiths hammer all night.", ["add:coin:-30", "add:renown:1", "add:xp:1"], None),
    ("Tax them. A king is owed his due.", "The merchants pay, sullenly. They do not come back.", ["add:coin:60", "add:renown:-1"], None),
    ("Offer them a place. A market, a street, a guildhall.", "Half the caravan stays. By autumn there is a market street. Bael weeps with joy.", ["add:renown:2", "add:xp:1"], None),
])
event("c6_ev_wedding", "A Wedding in the Chapel", """
Two of the column marry in the new chapel: a Red Hand brother and a widow from Tollmere. Ambrose officiates. The dwarves bring a barrel of something terrible.

You are asked to give a toast.
""", [
    ("Give a short, true toast.", "It is the shortest speech you have ever made and the one most remembered.", ["add:renown:1", "add:hp:3"], None),
    ("Give a long, rambling toast. Let the wine speak.", "It is a disaster. It is also the best night of the year.", ["add:hp:5", "add:xp:1"], "drive_pleasure"),
    ("Announce your own betrothal to the Fen-Queen.", "The room erupts. Saoirse's eyebrow rises, then her smile.", ["add:renown:2", "add:xp:1"], "queen_saoirse"),
])
event("c6_ev_rockfall", "Rockfall", """
After a winter thaw, the east face of the new Wall slumps. Boulders block the road, and three dwarf masons are trapped under a collapsed scaffold.
""", [
    ("Dig them out yourself, with the labour gang.", "You dig for six hours. The masons live. You do not feel your hands for a day.", ["add:hp:-3", "add:renown:2", "add:xp:1"], None),
    ("Send for Durgan.", "Durgan arrives with a hammer and a profane vocabulary. In an hour the rubble is a road.", ["add:xp:1"], "durgan_sworn"),
    ("Let the masons go. The Wall matters more.", "Three dwarf masons die. Every dwarf on the mountain remembers.", ["add:renown:-2"], None),
])
event("c6_ev_bandits", "Lowland Bandits", """
A band of thirty men, the remains of some defeated lord's levy, has taken the lower road and is robbing pilgrims.
""", [
    ("Send Corbin and her veterans.", "Corbin brings back eleven heads, three prisoners, and a very poor mood.", ["add:xp:1", "add:renown:1"], "deserters_recruited"),
    ("Offer them land and pardon. Recruit them.", "Twenty-two accept. Eight vanish in the night. The rest become good farmers.", ["add:renown:2", "add:xp:1"], None),
    ("Hunt them down yourself with the knights.", "It's a hard week. Roland takes an arrow in the shoulder. The bandits are no more.", ["add:hp:-4", "add:xp:1"], None),
])
event("c6_ev_omen", "Anselm's Vision", """
Anselm comes to your door at midnight, white-faced, hands trembling.

"The Skull spoke," he says. "Not in words. I saw a throne of coins, and a thing on it, and a door. I saw you, and I saw the door open."
""", [
    ("Press him: what did he see behind the door?", "He does not know. He says only: the thing is waiting, and has been waiting a very long time, and is *patient.*", ["set:omen_seen", "add:xp:1", "add:gambit:1"], None),
    ("Calm him. Visions are not orders.", "He nods, shaky, and leaves. You do not sleep.", ["add:hp:-1"], None),
    ("Take the Skull to Ferrand's crypt. See what the eye does.", "The dead man's eye opens, wet and white, and for a long moment it looks at the Skull. Then it closes. Something in the mountain exhales.", ["set:omen_seen", "set:ferrand_eye", "add:xp:2"], "ferrand_dead"),
])
event("c6_ev_fen", "A Fen Delegation", """
Six reed-boats arrive at the mountain's foot with a delegation from the Fenmarch: elders in woven cloaks, a choir of children, a ceremonial eel.
""", [
    ("Receive them in the Great Hall with full honours.", "The fen-folk are astonished and delighted. A treaty is signed that evening.", ["add:renown:2", "add:xp:1"], "fen_allied"),
    ("Ask for their warriors, as promised.", "They have two hundred, and send half. The rest will come at harvest.", ["add:xp:1"], "fen_allied"),
    ("Offer a gift of dwarf-steel.", "The elders bow so low their cloaks sweep the dust.", ["add:coin:-30", "add:renown:1"], "fen_allied"),
    ("Send them away empty-handed: the mountain has nothing to give.", "They leave in silence. You have the unpleasant feeling you made a mistake.", ["add:renown:-1"], None),
])
event("c6_ev_pilgrims", "Pilgrims", """
They come up the mountain road on foot, a hundred strong: the last faithful of Saint Gregory's pilgrim-orders, drawn by the rumour of a king who carries the Skull.

They kneel in the snow, and refuse to rise until you bless them.
""", [
    ("Bless them as a king and a pilgrim.", "They weep. They stay. The Chapel will need a second altar.", ["add:renown:2", "add:xp:1"], None),
    ("Refuse. You are no priest.", "Anselm blesses them instead, with a quiet look at you.", ["add:xp:1"], None),
    ("Recruit the strongest as the Skull's honour-guard.", "Thirty of them take the oath. They will die for it, gladly.", ["set:skull_guard", "add:xp:1"], None),
])

# ---- Heir ----
sc("c6_heir_choice", "The Child's Breath", """
The boy's breathing worsens through the winter. Ferrand, if he lived, would counsel patience. Ambrose counsels sun and rest. Saoirse counsels nothing at all; she simply sits by the cradle with her hand on his small chest, night after night.

Anselm, softly, at your elbow: "The Skull has healed before. At a cost."
""", [
    ch("Ask Anselm to hold the Skull over the child.", "c6_heir_skull", req="skull_recovered"),
    ch("Trust sun, care, and time.", "c6_heir_wait"),
    ch("Take the boy to the sun-farms each dawn, and pray to the saint yourself.", "c6_heir_pray", req="drive_heir"),
], chapter=C)
sc("c6_heir_skull", "The Skull's Gift", """
Anselm lays the Skull on the boy's chest. It does nothing, for a long breath. Then the child coughs, wetly, and cries — a loud, furious, living wail.

Saoirse laughs and weeps together. You hold your son and cannot speak.

But Anselm, kneeling, looks at the Skull, and then at you. "It is a little less than it was," he says. "A little. I am not sure what it cost."
""", [ch("Continue.", "c6_feast")], enter=["set:heir_healed", "set:skull_dimmed", "clear:heir_frail", "add:xp:2"], chapter=C)
sc("c6_heir_wait", "Patience", """
You take the boy to the sun each morning. You warm his tiny feet. You sing him the lullabies your own nurse sang. By spring, he is thin but breathing, and by summer he has begun to grab at your beard.

He will be a quiet child, a watchful one. But he will live.
""", [ch("Continue.", "c6_feast")], enter=["set:heir_slow", "clear:heir_frail", "add:xp:1", "add:hp:-2"], chapter=C)
sc("c6_heir_pray", "A King's Vigil", """
For forty mornings you carry the boy up to the cliff-farms and hold him in the first light. You say the saint's prayer over him until the words lose meaning. Somewhere in the fortieth, you notice he is smiling.

It might be the sun. It might be the saint. It might simply be a father's stubbornness.
""", [ch("Continue.", "c6_feast")], enter=["set:heir_healed", "set:saint_favour", "clear:heir_frail", "add:xp:3"], chapter=C)

sc("c6_adopt", "An Heir Without a Queen", """
You have no wife and no child. The line of Gregory ends with you, unless you do something about it.

{{emmet_adopted|Emmet, the boy from the road, has taken to following you with his wooden horse.}}{{tom_saved|Tom, the one-legged boy you held at Aldermont, has grown into a solemn youth, and looks at you with an expression you recognise.}}
""", [
    ch("Adopt Emmet, the lost boy of the Weald.", "c6_feast", req="emmet_adopted", fx=["set:heir_adopted", "set:heir_emmet", "add:xp:2"]),
    ch("Take Tom as your ward. He has earned it.", "c6_feast", req="tom_saved", fx=["set:heir_adopted", "set:heir_tom", "add:xp:2"]),
    ch("Name young Aldric your heir. He is young enough to learn.", "c6_feast", fx=["set:heir_adopted", "set:heir_aldric", "add:xp:1"]),
    ch("Name no one. A king need not choose today.", "c6_feast"),
], chapter=C)
