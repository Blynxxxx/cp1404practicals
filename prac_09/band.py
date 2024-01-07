class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def play(self):
        if not self.musicians:
            return f"{self.name} has no members!"
        band_play = ""
        for musician in self.musicians:
            band_play += musician.play() + "\n"
        return band_play

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)
