# Ex8: rocks, paper, scissors

gameOn = True

while gameOn:
    play1 = str(input("player 1 enter your play: "))
    play2 = str(input("player 2 enter your play: "))

    if play1 == "rock" and play2 == "scissors":
        print("player 1 is the winner (rock > scissors)")

    if play1 == "rock" and play2 == "paper":
        print("player 2 is the winner (paper > rock)")

    if play1 == "rock" and play2 == "rock":
        print("game is a draw (rock = rock)")

    if play1 == "paper" and play2 == "scissors":
        print("player 2 is the winner (scissors > paper)")

    if play1 == "paper" and play2 == "paper":
        print("game is a draw (paper = paper)")

    if play1 == "paper" and play2 == "rock":
        print("player 1 is the winner (paper > rock)")

    if play1 == "scissors" and play2 == "scissors":
        print("game is a draw (scissors = scissors)")

    if play1 == "scissors" and play2 == "paper":
        print("player 1 is the winner (scissors > paper)")

    if play1 == "scissors" and play2 == "rock":
        print("player 2 is the winner (rock > scissors)")

    repeat = input("play again? (y/n) ")
    if repeat == "n":
        break
    else:
        print("repeating game...")

print("good bye, ty for playing")
