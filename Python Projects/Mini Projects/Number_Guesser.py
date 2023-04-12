# Generate random number from 0-10 and track how many times it takes the user to guess the correct number

import random

numOfGuesses = 0  # variable to track guesses user has made
maxNum = input("Please provide the max number for the number guessing game: ")  # asking user for the max number

if maxNum.isdigit():  # checks to see if value provided is a number
    maxNum = int(maxNum)  # converts it to an int if it is
    if maxNum <= 0:
        print("Please enter a number greater than 0, next time")
        quit()  # restarts application if the number is a negative or 0
    else:
        print("Ok I will pick a random number less than and including", maxNum)
        randNum = random.randint(0, maxNum)  # generates a random number within the specified range
else:
    print("Please enter a number, next time")
    quit()

while True:
    numOfGuesses += 1  # increments guesses
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please guess a number")
        continue
    # compares the guess and the actual value to see if they match, providing a suitable response
    if guess == randNum:
        print("That is correct!")
        break
    elif guess < randNum:
        print("That is incorrect, guess higher")
    elif guess > randNum:
        print("That is incorrect, guess lower")

# after user has guessed the right answer tells them how many guesses it took them
print("Well done, that took you", numOfGuesses, "guesses")
