# Ex9: guessing game

import random

#generating randomInt 1-9 incl.
answer = random.randint(1,9)
numGuess = 0

while True:
    guess = input("what is your guess? (1-9) or exit to quit: ")
    if guess == "exit":
        print("Good bye!")
        break
    else:
        numGuess = numGuess + 1;
        if int(guess) < answer:
            print("Your guess is too small")
        elif int(guess) > answer:
            print("Your guess is too large")
        elif int(guess) == answer:
            print("Your guess is exact")
            break
        else:
            print("Invalid guess, please guess again")

print(f"You made {numGuess} guesses!")
