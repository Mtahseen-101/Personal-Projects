# user vs computer rock paper scissors game
# best of 3, user can forfeit any time

import random

print("Welcome to the rock paper scissors game")
print("Best of 3")

userWins = 0
computerWins = 0

# list created with the options the computer can pick
options = ["rock", "paper", "scissors"]

# while loop that stops once the users or computers score reaches 3
while userWins <= 2 and computerWins <= 2:
    # gets users input and converts it to lower case
    pick = input("Type Rock,Paper,Scissors or F to Forfeit: ").lower()
    # stops loop if user asks to forfeit
    if pick == "f":
        print("Forfeiting")
        break
    # asks user to pick one of the specified keywords
    if pick not in options:
        print("please pick a valid option")
        continue
    # 0 = rock, 1 = paper, 2 = scissors
    randNum = random.randint(0, 2)
    # uses randon number to pick an option from the list
    computerPick = options[randNum]
    print("The computer picks", computerPick)
    # series of if statements to see who wins
    if pick == "rock" and computerPick == "scissors":
        print("You win this round!")
        userWins += 1
    elif pick == "paper" and computerPick == "rock":
        print("You Win this round!")
        userWins += 1
    elif pick == "scissors" and computerPick == "paper":
        print("You win this round!")
        userWins += 1
    elif pick == computerPick:
        print("It's a draw!")
    else:
        print("You lose this round!")
        computerWins += 1

print("Game Over!")
print("The score is", userWins, "wins for the user and", computerWins, "for the computer")

# if statements to decide if the user or computer won the game
if computerWins > userWins:
    print("The Computer Wins!")
elif computerWins < userWins:
    print("The User Wins!")

print("Game Over")
