import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_LINE = 6


def main():
    """Get and display sets of random numbers."""
    number_of_quick_picks = validate_quick_picks()

    for i in range(number_of_quick_picks):
        numbers = []
        for j in range(NUMBER_PER_LINE):
            random_number = validate_number(numbers)
            numbers.append(random_number)
            numbers.sort()
        print(" ".join(f"{number:2}" for number in numbers))


def validate_quick_picks():
    """Validate the number of quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number of quick picks.")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


def validate_number(numbers):
    """Check whether a list of numbers contain any repeated number."""
    random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    while random_number in numbers:
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    return random_number


main()
