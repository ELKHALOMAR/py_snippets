#Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
z=0
while True:
    a = random.randint(1, 9)
    user = int(input("enter a number between 1 and 9:"))
    if a == user:
        print("exact, you guessed well")
    elif user > a:
        print('to high, The exact number is', a)
    else:
        print('to low, The exact number is', a)
    z += 1

    play = input("do you want to replay (y/n):")
    if play in ("y", "n"):
        if play == "y":
            continue
        else:
            print("you gessed", z, "times")
            print("goodbye")
            break
    else:
        print("false entry")
        break




