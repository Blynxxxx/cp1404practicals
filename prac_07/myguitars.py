from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitar file, display, get new guitars and save."""
    guitars = []
    load_guitar_file(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $ "))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        guitar_name = input("Name: ")

    save_guitar_file(guitars)


def save_guitar_file(guitars):
    """Save list of guitars to file."""
    with open(FILENAME, "a") as out_file:
        for guitar in guitars:
            print(guitar, file=out_file)


def load_guitar_file(guitars):
    """Load guitar file."""
    with open(FILENAME, "r") as in_file:
        for row in in_file:
            # print(row)
            parts = row.strip().split(",")
            year = parts[1]
            cost = float(parts[2])
            guitars.append(Guitar(parts[0], year, cost))


main()
