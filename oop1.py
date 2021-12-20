import random


class User:
    privileges = []

    def __init__(self, name):
        print("user created")

        self.name = name


class Rocket:
    def __init__(self, fuel):
        self.fuel = fuel
        self.pos_y = 0
        print("Rocket has been prepared.", self.fuel, "kg of fuel in tank.")

    def start(self):
        print("A rocket has been launched.")
        while self.fuel:
            self.pos_y += 1
            self.fuel -= 1

    def status(self):
        print("Fuel ", self.fuel, ", position ", self.pos_y, sep='')


"""
test = 2
rockets = []
for i in range(test):
    newRocket = Rocket(random.randint(1, 50))
    rockets.append(newRocket)
for i in range(test):
    rockets[i].fly_y()
for i in range(test):
    rockets[i].status()
"""

number_of_rockets = 5
rockets = [Rocket(random.randint(0, 50)) for _ in range(number_of_rockets)]
for i in range(number_of_rockets):
    rockets[i].start()

for i in range(number_of_rockets):
    rockets[i].status()
