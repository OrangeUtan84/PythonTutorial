def cheeseshop(kind, *arguments, **keywords):
    """creates a small output for the given parameters.

    First parameter is fixed, arguments and keywords can contain any information.
    """
    print("-- Haben Sie", kind, "?")
    print("-- Tut mir leid,", kind,"ist leider gerade aus")
    for arg in arguments:
        print(arg)
    print ("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw,":", keywords[kw])



cheeseshop("Limburger", "Der ist sehr flüssig, mein Herr",
           "Der ist wirklich sehr, SEHR flüssig, mein Herr",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

d = { "Der stinkt, mein Herr.", "Der stinkt GEWALTIG, mein Herr." }
e = { "shopkeeper": "Heinz", "client": "Gustav", "sketch": "Cheese Shop Sketch 2" }

cheeseshop("Harzer", *d, **e)

print(cheeseshop.__doc__)