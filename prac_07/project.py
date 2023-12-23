"""
Project Management Program
estimate time = 2 hours
actual time = 5 hours
"""
import datetime
COMPLETION_PERCENTAGE = 100


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Display Project information."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}," \
        f" estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare Project priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine whether Project is completed or not."""
        return self.completion_percentage == COMPLETION_PERCENTAGE
