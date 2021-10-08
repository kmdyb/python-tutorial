import random
from enum import Enum


# ------------------ losowość wielkości nagrody
def approximategold(value, percentrange):
    lowestvalue = value - (percentrange / 100) * value
    highestvalue = value + (percentrange / 100) * value
    return random.randint(lowestvalue, highestvalue)


# ------------------ event, wynik szukania skrzyni
Event = Enum('Event', ['Chest', 'Empty'])
eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                    }
eventTuple = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

# ----------------- rodzaj, kolor skrzyni
Colours = Enum('Colours', {'Green': 'green',
                           'Yellow': 'yellow',
                           'Purple': 'purple',
                           'Gold': 'gold'
                           }
               )
colourDictionary = {
    Colours.Green: 0.7,
    Colours.Yellow: 0.2,
    Colours.Purple: 0.07,
    Colours.Gold: 0.03
}
chestColourTuple = tuple(colourDictionary.keys())
chestColourProbability = tuple(colourDictionary.values())

# ----------------- wielkość nagrody zależna od koloru skrzyni
rewardsForChests = {
                    chestColourTuple[reward]: (reward + 1) * (reward + 1) * 1000
                    for reward in range(len(chestColourTuple))
                    }

# ----------------- główny przebieg programu
print("Hello, you have enough energy for only four searches.")
gameLength = 4
goldAcquired = 0
while gameLength > 0:
    gamerAnswer = input("Do you want to search for a treasure now?")
    if gamerAnswer == "yes":
        print("Ok, test your luck...")
        drawnEvent = random.choices(eventTuple, eventProbability)[0]
        if drawnEvent == Event.Chest:
            print("You've found a chest.")
            drawnColour = random.choices(chestColourTuple, chestColourProbability)[0]
            print("Its colour is", drawnColour.value)
            # gamerReward = rewardsForChests[drawnColour]
            gamerReward = approximategold(rewardsForChests[drawnColour], 10)
            goldAcquired = goldAcquired + gamerReward
        elif drawnEvent == Event.Empty:
            print("Nothing here.")
    else:
        print("Just do it...")
        continue
    gameLength = gameLength - 1
print("You've acquired", goldAcquired, "gold.")
