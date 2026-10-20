from dsl import *
C = "Chapter II — Aldermont"

# ---- additional hub options are patched into c2_town in build step (see patches.py) ----

sc("c2_spy", "A Grey Thread", """
Brother Ferrand finds it first: a length of grey thread, knotted in a pattern he has never seen, tied around a pigeon's leg. The pigeon was trying to leave Aldermont from the roof of the Guild Hall.

"Someone is talking to the enemy," he says. "Someone inside our wall."

Roland's hand drops to his sword. The room goes still.
""", [
    rk("Set a trap. Feed the column a false piece of news and see who carries it.", "INT", "c2_spy_caught", "c2_spy_half", "c2_spy_warned"),
    rk("Confront the one you least trust. Look them in the eye.", "CHA", "c2_spy_caught", "c2_spy_half", "c2_spy_warned"),
    ch("Say nothing. Burn the thread. A hunt will frighten the column more than a spy will.", "c2_town", fx=["set:spy_ignored"]),
], enter=["set:spy_active", "set:spy_started", "if:!bond_alcuin?set:alcuin_spy"], chapter=C)

sc("c2_spy_half", "A Half-Truth", """
The trap catches something, but the thing it catches is a shadow. You know *who* now, but not *why*, and the spy knows you know.
""", [ch("Move quickly, before the spy flees.", "c2_spy_caught")], enter=["add:hp:-1"], chapter=C)

sc("c2_spy_warned", "The Bird Flies", """
You were too slow, or too obvious. By morning there is a second pigeon, and this one is gone.

Whatever Aldermont knew, the lich now knows.
""", [ch("Go back to the Hall. You will find the spy later.", "c2_town")], enter=["set:spy_warned", "add:renown:-1"], chapter=C)

sc("c2_spy_caught", "Caught", """
It's over before dawn.
""", [ch("Face them.", "c2_caught_alcuin")], redirect=[{"if": "!alcuin_spy", "goto": "c2_caught_pell"}], chapter=C)

sc("c2_caught_alcuin", "Alcuin Confesses", """
Alcuin does not even try to lie. He is on his knees in the doorway of the chapel, with the thread still in his hands, weeping without noise.

"He has my sister," he says. "A village near the Ford. He sends me a lock of her hair every month. I tell him what he asks. Small things. Where the grain is. How many men."

He looks up. "I would have told him about the Skull. I promise you I would have told him about the Skull. I have been lucky not to know."

Roland waits for your order.
""", [
    ch("Turn him. Alcuin will write to the lich what you want read.", "c2_alcuin_double", fx=["set:alcuin_double", "set:spy_done", "add:xp:2"]),
    ch("Forgive him, and keep him by your side where you can see him.", "c2_alcuin_forgiven", fx=["set:alcuin_forgiven", "set:spy_done", "add:renown:1", "add:xp:1"]),
    ch("Exile him. He leaves with one blanket and a day's food.", "c2_alcuin_exile", fx=["set:alcuin_exiled", "set:spy_done", "court:-Alcuin"]),
    ch("Hang him. The column must see what treason costs.", "c2_alcuin_dead", fx=["set:alcuin_dead", "set:spy_done", "court:-Alcuin", "add:renown:-1"]),
], chapter=C)

sc("c2_alcuin_double", "A Double Voice", """
It is Alcuin's own idea, in the end. He writes his reports in a clear, unhurried hand, and you read each one before it flies.

"I am a very good liar," he says. "I have always been. It is only now that I have a use for it."
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_alcuin_forgiven", "Forgiven", """
He kisses your ring and then, to his own surprise, your hand. "I will not be forgiven by God," he says. "But I will be useful to a king."

It is the first honest thing he has said to you.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_alcuin_exile", "Out Through the Gate", """
He walks out into the grey morning, and nobody says a word. You will not see him again for a long time, if ever.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_alcuin_dead", "The Rope", """
It is done at dawn, in the courtyard, in front of the column. The silence is worse than the screaming would have been.

Roland does not look at you for the rest of the day.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_caught_pell", "The Clerk Pell", """
It is not a knight or an envoy. It is Pell, Corvin Bael's second clerk, a mild man with ink-stained fingers and a cough.

"I don't know what he is," he says of the lich. "He wrote me, in my own handwriting, a letter I had no memory of writing. I thought I was losing my mind. It said: *do this and your daughter will wake.* She has been asleep since the Ford."

Bael, white-faced, stands behind him.
""", [
    ch("Banish him to the infirmary under guard. He may see his daughter before the end.", "c2_pell_mercy", fx=["set:spy_done", "set:pell_mercy", "add:renown:1"]),
    ch("Hang him. A spy is a spy.", "c2_pell_dead", fx=["set:spy_done", "add:renown:-1"]),
    ch("Use him: let him write what you want written.", "c2_pell_double", fx=["set:spy_done", "set:pell_double", "add:xp:1"]),
], chapter=C)

sc("c2_pell_mercy", "A Daughter's Bed", """
Pell is allowed to sit beside the sleeping girl each night. Ferrand records her breathing in his ledger. Pell no longer writes to anyone.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_pell_dead", "The Cost of a Letter", """
The column watches. Bael looks as though he will be sick. Nobody argues. Nobody speaks.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

sc("c2_pell_double", "A Quill For a King", """
Pell's letters to the lich are works of art. They are all true in every detail, and they all mislead.
""", [ch("Back to the Hall.", "c2_town")], chapter=C)

# --- Isobel, wine cellar, standard ---
sc("c2_isobel", "The Steward's Ledger", """
Lady Isobel's ledger is the cleanest document you have ever seen. Every barrel, every sack, every head of livestock, every sick man's name.

"I will give you a number," she says. "Eight hundred and twelve days of food, if we are exact. Fewer, if you are generous. I want authority over the grain. Not you, not Bael, not the Red Hand."
""", [
    ch("Give her full authority. A steward who counts is worth three kings.", "c2_town", fx=["set:isobel_empowered", "set:did_isobel", "add:renown:1", "add:xp:1"]),
    ch("Keep the keys. She advises; you decide.", "c2_town", fx=["set:did_isobel", "set:isobel_cold"]),
], chapter=C)

sc("c2_cellar", "The Dead Lord's Cellar", """
Aldermont's late lord had one weakness, and it is racked in the cellar: thirty casks of a very good red from the Western Slopes. Vance finds you there at midnight, and does not remark on it.

"He would have wanted it drunk," the Brother-Captain says. "Not left for the dead."
""", [
    ch("Share a cup with Vance. A quiet hour.", "c2_cellar_share", fx=["set:did_cellar"]),
    ch("Order the casks loaded for the barges. Wine is currency.", "c2_town", fx=["add:coin:60", "set:did_cellar"]),
], chapter=C)

sc("c2_cellar_share", "A Cup With the Red Hand", """
Vance takes off his gauntlets for the first time. His hands are scarred, burned and raw.

"I did not want this," he says. "I wanted a quiet life and a vow. Do you know what it is like to burn a friend?"

You say you do. You talk until the candle is gone.
""", [ch("Back to the Hall.", "c2_town")], enter=["set:vance_friend", "add:hp:4", "if:drive_pleasure?add:xp:2", "if:drive_pleasure?add:gambit:1"], chapter=C)

sc("c2_standard", "The Standard on the Keep", """
You have Roland raise the standard on the keep of Aldermont. It is a small act. The wind catches the banner, and from the wall the Red Hand brothers cheer, ragged and loud.

For a moment it is not a lost kingdom, only a king.
""", [ch("Back to the Hall.", "c2_town")], enter=["set:did_standard", "add:xp:1", "add:renown:1"], chapter=C)
