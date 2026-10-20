from dsl import *
C = "Prologue — Who You Were"

sc("c0_prologue", "Before the Ford", """
Before the Ford, before the dead, you were a king. You were good at some things and bad at others, and you have had a long night on the south road to think about which.

Three questions will decide who you are when the morning comes. The first is the simplest: what do you *want*?
""", [
    ch("To take back what was mine. The standard will fly over the capital again.", "c0_fall", fx=["set:drive_reclaim"]),
    ch("To leave an heir. A line that outlasts me, whatever happens to me.", "c0_fall", fx=["set:drive_heir"]),
    ch("To taste life while there is still life to taste. Wine, company, one good night.", "c0_fall", fx=["set:drive_pleasure"]),
], chapter=C)

sc("c0_fall", "How the Ford Fell", """
You have told the story of the Ford a hundred times already, and each time it has come out a little different. Which version do you believe?
""", [
    ch("I was betrayed. A lord of my own council opened the river-gate to the enemy.", "c0_bond", fx=["set:fall_betrayed"]),
    ch("I was proud. I offered battle where I should have retreated, and men died for my vanity.", "c0_bond", fx=["set:fall_pride", "add:renown:-1"]),
    ch("I was warned. The scouts said the dead were rising; the council laughed; so did I.", "c0_bond", fx=["set:fall_warned", "add:gambit:1"]),
], chapter=C)

sc("c0_bond", "The One You Trust", """
In every court there is one voice that tells the king the truth. Whom did you keep close?
""", [
    ch("Sir Roland, who carried the standard when no one else could stand.", "c1_ford", fx=["set:bond_roland", "add:hp:2"]),
    ch("Alcuin, the envoy — clever, honeyed, and not a man you would trust with a purse.", "c1_ford", fx=["set:bond_alcuin", "add:coin:20"]),
    ch("Sir Aymer of the Ford, who held your flank when others ran.", "c1_ford", fx=["set:bond_aymer", "add:xp:1"]),
], chapter=C)
