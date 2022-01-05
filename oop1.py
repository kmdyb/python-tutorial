from random import randint
from math import sqrt


class Rocket:
    """
    Rocket can fly upwards. Range is dependend on fuel.
    """
    def __init__(self, fuel: float = 0, x: float = 0, y: float = 0):
        self.fuel = fuel
        self.pos_y = y
        self.pos_x = x
        print("Rocket has been prepared.", self.fuel, "kg of fuel in tank.")

    def __str__(self):
        return "Rocket info: fuel " + str(self.fuel) + ", position " + str(self.pos_y)

    def start(self):
        """
        Start of a rocket.
        """
        print("A rocket has started.")
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

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].fuel = value

    @staticmethod
    def get_distance(obj1: Rocket, obj2: Rocket) -> float:
        ab = obj1.pos_y - obj2.pos_y
        bc = obj1.pos_x - obj2.pos_x
        return sqrt(ab**2 + bc**2)

    def get_amount_of_rockets(self):
        return len(self.rockets)

    def __len__(self):
        return self.get_amount_of_rockets()
