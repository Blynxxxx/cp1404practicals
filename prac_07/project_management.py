"""
Project Management Program
estimate time = 2 hours
actual time = 5 hours
"""
import datetime
from prac_07.project import Project


FILE_FIELD = "Name  Start Date  Priority    Cost Estimate   Completion Percentage\n"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects" \
       "\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Project management program."""
    projects = []

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            get_valid_projects(projects)
        elif choice == "S":
            validate_projects(projects)
            save_projects(projects)
        elif choice == "D":
            validate_projects(projects)
            projects.sort()
            incomplete_projects, completed_projects = divide_projects(projects)
            print("Incomplete projects:")
            display_project(incomplete_projects, " ")
            print("Completed projects:")
            display_project(completed_projects, " ")
        elif choice == "F":
            validate_projects(projects)
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = filter_projects(projects, date)
            display_project(filtered_projects)
        elif choice == "A":
            add_new_valid_project(projects)
        elif choice == "U":
            validate_projects(projects)
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def validate_projects(projects):
    """Check whether a list of projects exit or not."""
    if not projects:
        print("No projects yet.")
        get_valid_projects(projects)


def divide_projects(projects):
    """Divide a list of projects to incomplete and completed projects."""
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    return incomplete_projects, completed_projects


def get_valid_projects(projects):
    """Get projects from a valid file of project objects."""
    is_finished = True
    while is_finished:
        try:
            filename = input("Input filename to load objects: ")
            with open(filename, "r") as in_file:
                in_file.readline()
                for line in in_file:
                    parts = line.strip().split("\t")
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    project = Project(parts[0], parts[1], priority, cost_estimate, completion_percentage)
                    projects.append(project)
            print("Project file loaded.")
            is_finished = False
        except FileNotFoundError:
            print(f"File not found.")


def save_projects(projects):
    """Save list of project objects to a file."""
    filename = input("Input filename to save objects: ")
    with open(filename, "w") as out_file:
        out_file.write(FILE_FIELD)  # Add fields as the first line.
        for project in projects:
            print(project, file=out_file)
    print("Project file saved.")


def display_project(projects, indentation=""):
    """Display project in projects."""
    for project in projects:
        print(indentation, project, sep="")


def filter_projects(projects, date):
    """Sort projects by start date."""
    return [project for project in projects if project.start_date >= date]


def add_new_valid_project(projects):
    """Ask the user for the valid inputs and add a new project to memory"""
    print("Let's add a new project")
    is_finished = True
    while is_finished:
        try:
            project_name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            new_project = Project(project_name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(new_project)
            is_finished = False
        except ValueError:
            print("Invalid input")


def update_project(projects):
    """Choose a project, then modify the completion % and/or priority - leave blank to retain existing values."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    is_finished = True
    while is_finished:
        try:
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            is_finished = False
        except ValueError:
            print("Invalid choice.")
        except IndexError:
            print("Invalid choice.")
    try:
        new_percentage = int(input("New Percentage: "))
        projects[project_choice].completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        projects[project_choice].priority = new_priority
    except ValueError:
        pass


main()
