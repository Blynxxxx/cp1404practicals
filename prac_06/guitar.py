"""
CP1404/CP5632 Practical
Guitar class
"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display Guitar information."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate guitar age based on guitar year and current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether guitar is vintage or not based on guitar age."""
        return self.get_age() >= VINTAGE_AGE
