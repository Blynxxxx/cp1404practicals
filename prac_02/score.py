"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    """Get the user's score and display the result."""
    score = get_valid_score("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
    print(determine_result(score))

    random_score = random.uniform(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(determine_result(random_score))


def get_valid_score(prompt, low, high):
    """Validate score between low and high."""
    score = float(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = float(input(prompt))
    return score


def determine_result(score):
    """Calculate the result based on score."""
    if score < PASSABLE_SCORE:
        return "Bad"
    elif score < EXCELLENT_SCORE:
        return "Passable"
    return "Excellent"


main()
