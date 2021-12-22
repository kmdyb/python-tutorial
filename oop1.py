from random import randint


class User:
    privileges = []

    def __init__(self, name):   # metoda dunder "Double underscore"
        print("user created")

        self.name = name


class Rocket:
    """
    Rocket can fly upwards. Range is dependend on fuel.
    """
    def __init__(self, fuel=0):
        self.fuel = fuel
        self.pos_y = 0
        print("Rocket has been prepared.", self.fuel, "kg of fuel in tank.")

    def __str__(self):
        return "Rocket info: fuel " + str(self.fuel) + ", position " + str(self.pos_y)

    def start(self):
        """
        Start of a rocket.
        """
        print("A rocket has been launched.")
        while self.fuel:
            self.pos_y += 1
            self.fuel -= 1

    def status(self):
        print("Rocket's status: fuel ", self.fuel, ", position ", self.pos_y, sep='')


class RocketBoard:
    def __init__(self, number_of_rockets=2):
        self.rockets = [Rocket(randint(0, 50)) for _ in range(number_of_rockets)]
        for rocket in range(number_of_rockets):
            self.rockets[rocket].start()

        for rocket in range(number_of_rockets):
            self.rockets[rocket].status()
