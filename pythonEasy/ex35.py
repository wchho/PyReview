from sys import exit

def gold_room():
    print("this room is full of gold, how much will you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice: #does this break the choice string into char?
    # yes, looks for a 0 or 1 in the input, so 1, 11, 12, etc.
        how_much = int(choice) #converts choice into int value?
    else:
        dead("man learn to type a number")

    if how_much < 50:
        print("nice, you're not greedy")
        exit(0)
    else:
        dead("you greedy bastard")

def bear_room():
    print("""There is a bear here.
The bear has honey
The far bear is in front of another door
How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you and slaps you")
        elif choice == "taunt bear" and not bear_moved:
            print("""the bear has moved from the door
now you can go through it""")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("bear chews your leg")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("idk what that means")

def cthulhu_room():
    print("""Here you see great evil cthulhu
he, it, whatever stares at you and you go insane
do you flee or eat your head?""")

    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("yum that was tasty")
    else:
        cthulhu_room() #recursive?

def dead(why):
    print(why, "good job")
    exit(0)

def start():
    print("""you are in a dark room
there is a door to your right and left
which one do you take?""")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve")

start()
