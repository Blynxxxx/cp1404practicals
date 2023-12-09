"""
CP1404/CP5632 Practical
Guitar program.
"""

from prac_06.guitar import Guitar


def main():
    """Get guitar information and display if guitar is vintage."""
    guitars = []
    print("My guitars!")

    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $ "))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        guitar_name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        maximum_name_length = max(len(guitar.name) for guitar in guitars)
        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print(f'Guitar {i}: {guitar.name:>{maximum_name_length}} '
                  f'({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}')
    else:
        print("There is no guitar.")


main()
