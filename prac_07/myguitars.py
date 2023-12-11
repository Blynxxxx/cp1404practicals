from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for row in in_file:
            # print(row)
            parts = row.strip().split(",")
            year = parts[1]
            cost = float(parts[2])
            guitars.append(Guitar(parts[0], year, cost))
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    print()
    for guitar in guitars:
        print(guitar)

main()
