"""
Project Management Program
22:40 - 2:00
"""
COMPLETION_NUMBER = 100

class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Display Project information."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}," \
               f" estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == COMPLETION_NUMBER
