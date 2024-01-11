class Band:
    """Represent a band object."""

    def __init__(self, name):
        """Construct a band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Display a string representation of a band."""
        return f"{self.name} ({','.join([str(musician) for musician in self.musicians])})"

    def play(self):
        """Display a string showing the band playing with its musicians."""
        if not self.musicians:
            return f"{self.name} has no members!"
        return '\n'.join([musician.play() for musician in self.musicians])

    def add(self, musician):
        """Add a musician to band's musicians."""
        self.musicians.append(musician)
