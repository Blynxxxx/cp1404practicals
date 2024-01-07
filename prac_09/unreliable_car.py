import random
from prac_09.car import Car


class UnreliableCar(Car):
    """ """

    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)

        else:
            return 0
