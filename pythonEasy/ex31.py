print("""You enter a dark room with two doors.
Do you go through door 1 or door 2?""")

door = input("> ")

if door == "1":
    print("""There's a giant bear here eating a cheesecake.
    What do you do?
    1. Take the cheese
    2. Scream at the bear""")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. good job!")
    elif bear == "2":
        print("the bear eats your legs off. good job!")
    else:
        print(f"well, doing {bear} is probably better")
        print("bear runs away")

elif door == "2":
    print("""You stare into the endless abyss at Cthulhu's ret
    1. blueberries
    2. yellow jacket clothespins
    3. understanding revolvers yelling melodies""")
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("""your body survives
        good job!""")
    else:
        print("""the insanity rots your eyes
        good job!""")

else:
    print("you stumble around and fall on a knife and die")
