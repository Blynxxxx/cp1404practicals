"""
CP1404/CP5632 Practical
wimbledon
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Get file and display details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_records(records):
    """Create a dictionary of champions and set of countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        champion_to_count[record[INDEX_CHAMPION]] = champion_to_count.get(record[INDEX_CHAMPION], 0) + 1
        countries.add(record[INDEX_COUNTRY])
    return champion_to_count, countries


def get_records(filename):
    """Get records from a file."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
