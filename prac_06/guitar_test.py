"""
CP1404/CP5632 Practical
Guitar class
"""

from prac_06.guitar import Guitar


def run_test():
    """Test for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    gibson = Guitar(name, year, cost)
    print(gibson)
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")

    another_guitar = Guitar("Another Guitar", 2020, 100)
    print(another_guitar)
    print(f"{another_guitar.name} get_age() - Expected 3. Got {another_guitar.get_age()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


run_test()
