import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}

eventTuple = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

Colours = Enum('Colours', {'Green': 'green',
                           'Yellow': 'yellow',
                           'Purple': 'purple',
                           'Gold': 'gold'
                           }
               )

chestColoursDictionary = {
    Colours.Green: 0.7,
    Colours.Yellow: 0.2,
    Colours.Purple: 0.07,
    Colours.Gold: 0.03
}

chestColourTuple = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
    chestColourTuple[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(chestColourTuple))
}

gameLength = 4
goldAcquired = 0
print("Hi, you have enough energy for only four searches.")
while gameLength > 0:
    gamerAnswer = input("Do you want to search for a treasure?")
    if gamerAnswer == "yes":
        print("Ok, test your luck...")
        drawnEvent = random.choices(eventTuple, eventProbability)[0]
        if drawnEvent == Event.Chest:
            print("You've found a chest.")
            drawnColour = random.choices(chestColourTuple, chestColourProbability)[0]
            print("Its colour is", drawnColour.value)
            gamerReward = rewardsForChests[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif drawnEvent == Event.Empty:
            print("Nothing here.")
    else:
        print("Just do it...")
        continue
    gameLength = gameLength - 1
print("You've acquired", goldAcquired, "gold.")
