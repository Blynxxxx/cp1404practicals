"""
CP1404/CP5632 Practical
Programming Language class.
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise a programming language instance with given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Display programming language details."""
        return f"{self.name}, {self.typing}, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine whether programming language is dynamic or not."""
        return self.typing == "Dynamic"
