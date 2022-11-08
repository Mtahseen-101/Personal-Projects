# Simple Quiz game
# 5 questions if the user gets the answer right they get a point
# make one of the questions a random maths question
# output different comments based on what the user scores


import random

score = int(0) # variable to monitor score

question1 = input("What is the capital of England?") #question for the user
answer1 = "London" # correct answer
if question1 == answer1: # determine if the answer was correct
    print("Correct")
    score += 1 # add to the score if correct
else:
    print("Incorrect")

question2 = input("What is your favourite programming language?")
answer2 = "Python"
if question2 == answer2:
    print("Correct")
    score += 1
else:
    print("Incorrect")

# generate 2 random numbers between 1 and 10 to get the user to add together
x = random.randint(1, 11)
y = random.randint(1, 11)
question3 = "What is {0} + {1} = ?(Please input a number)".format(x, y)
userInput = int(input(question3))
answer3 = int(x+y)
if userInput == answer3:
    print("Correct")
    score += 1
else:
    print("Incorrect")

question4 = input("Name an orange fruit.")
answer4 = "Orange"
if question4 == answer4:
    print("Correct")
    score += 1
else:
    print("Incorrect")

question5 = input("Is this statement true or false. Coffee is better than tea.")
answer5 = "True"
if question5 == answer5:
    print("Correct")
    score += 1
else:
    print("Incorrect")


# output appropriate message depending on the score the user got
if score == 0:
    print("End of quiz. You scored", score, "Did you even try?")
elif 1 <= score <= 3:
    print("End of quiz. You scored", score, "Nice attempt im sure you will do better next time.")
elif 4 <= score:
    print("End of quiz. You scored", score, "You did very well, I hope you didn't cheat.")

