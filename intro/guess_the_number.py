#!/usr/bin/env python3
"""
Guess the number game
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import random


def main():
    """ Main entry point of the app """
    print("Hello. What is your name?")
    name = input()

    print("Well " + name + ", I am thinking of a number between 1 and 20.")

    secretNumber = random.randint(1, 20)
    #print("DEBUG: Secret number is: " + str(secretNumber))

    for guessesTaken in range(1, 7):  # same as 6
        print("Take a guess:")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low.")
        elif guess > secretNumber:
            print("Your guess is too high.")
        else:
            break  # This condition is for the correct guess!

    if guess == secretNumber:
        print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses.")
    else:
        print("Nope. The number I was thinking of was " + str(secretNumber))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()