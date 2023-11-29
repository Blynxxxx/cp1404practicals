"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = get_data()
    # print(subjects)
    display_subjects(subjects)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(",")
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display subject details."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
