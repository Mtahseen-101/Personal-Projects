# text based games that provides user with a series of options and descriptions asking what they want to do next
# if their answer is not from the options provided they lose

print("Welcome to this text based adventure game.")
name = input("To start please name your character: ") # variable to store players name
print(name, name, name, "... You wake up by the side of the road, not knowing how you ended up here.You get up and walk"
                        "towards a crossroad.")
# series of nested if statements to take the user to a different response based on what they decide to do in the scenario
answer = input("You have the option to go left or right which do you choose?(left/right): ")
if answer == "left":
    answer = input("You go left at the crossroads. After walking for what seems like an enternity you arrive at a "
                   "river, do you wish to cross it? (y/n): ")
    if answer == "y":
        answer = input("You decide to cross the river, as you start swimming a crocodile appears. You lose.")
        quit()
    elif answer == "n":
        print("You decide not to cross, you realise it was a wise decision when you see a crocodile swim by")
        answer = input("do you wish to turn back?(y/n)")
        if answer == "n":
            print(
                "You decide not to turn back, you stare at the river as hours go by and pass out due to hunger. "
                "You lose.")
            quit()
        elif answer == "y":
            print(
                "You decide to turn back, as you were walking back to the crossroads. A giant snake approaches you "
                "and bites you, you pass out from the poison that has entered your body. You lose.")
            quit()
        else:
            print("Incorrect option, you lose")
            quit()
    else:
        answer = input("Incorrect option, you lose")
        quit()
elif answer == "right":
    print("You decide to go right at the crossroad. You walk for a few minutes before arriving at a forest")
    answer = input("do you wish to enter the forest?(y/n)")
    if answer == "y":
        answer = input("You enter the forest and realise this was a mistake, You hear wolves howling as everything "
                       "goes black. You lose.")
        quit()
    elif answer == "n":
        print("You decide not to enter the forest, you realise it was a wise decision as you hear wolves howling.")
        answer = input("do you wish to turn back?(y/n)")
        if answer == "n":
            print(
                "You decide not to turn back, you stare at the forest as hours go by and pass out due to hunger. "
                "You lose.")
            quit()
        elif answer == "y":
            print(
                "You decide to turn back, as you were walking back to the crossroads. A giant snake approaches you "
                "and bites you, you pass out from the poison that has entered your body. You lose.")
            quit()
        else:
            print("Incorrect option, you lose")
            quit()
else:
    print("Incorrect option, you lose")
    quit()
