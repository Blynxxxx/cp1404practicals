"""
CP1404/CP5632 - Practical
Menu
"""
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 50
EXCELLENT_SCORE = 90
DEFAULT_SCORE = -1


def main():
    """Get score, display result and asterisks."""
    score = DEFAULT_SCORE
    print(MENU)
    choice = input("input your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
        elif choice == "P":
            if score == DEFAULT_SCORE:
                score = get_valid_score("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
            print(determine_result(score))
        elif choice == "S":
            if score == DEFAULT_SCORE:
                score = get_valid_score("Enter score: ", MINIMUM_SCORE, MAXIMUM_SCORE)
            display_asterisks(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("input your choice: ").upper()
    print("farewell")


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


def display_asterisks(score):
    """Display the number of asterisks based on score."""
    print("*" * int(score))


main()
