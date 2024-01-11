import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent a UnreliableCar object which is inherited from Car class."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable Car instance, based on parent Car class."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        if random.uniform(0, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
