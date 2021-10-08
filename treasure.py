import random


gameLength = 4

while gameLength > 0:
    gamerAnswer = input("Do you want to search for a treasure?")
    if gamerAnswer == "yes":
        print("Ok, test your luck...")
    else:
        print("Go straight...")
        continue
    gameLength = gameLength - 1

