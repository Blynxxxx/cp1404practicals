"""
Project Management Program
6:00 -
"""
import datetime

from prac_07.project import Project

FILE_FIELD = "Name	Start Date	Priority	Cost Estimate	Completion Percentage\n"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects" \
       "\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = []

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            in_file = input("Input filename to load objects: ")
            get_projects(in_file, projects)
            print("Project file loaded.")
        elif choice == "S":
            out_file = input("Input filename to save objects: ")
            save_projects(out_file, projects)
            print("Project file saved.")
        elif choice == "D":
            projects.sort()
            incomplete_projects, completed_projects = create_two_groups(projects)
            print("Incomplete projects:")
            display_project(incomplete_projects, " ")
            print("Completed projects:")
            display_project(completed_projects, " ")
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy):")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = filter_projects(projects, date)
            display_project(filtered_projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def create_two_groups(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    return incomplete_projects, completed_projects


def get_projects(filename, projects):
    """Get projects from a file of project objects."""
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(parts[0], parts[1], priority, cost_estimate, completion_percentage)
            projects.append(project)


def save_projects(filename, projects):
    """Save list of project objects to a file."""
    with open(filename, "w") as out_file:
        out_file.write(FILE_FIELD)  # Add fields as the first line.
        for project in projects:
            print(project, file=out_file)


def display_project(projects, indentation=""):
    for project in projects:
        print(indentation, project, sep="")


def filter_projects(projects, date):
    filtered_projects = [project for project in projects if project.start_date >= date]
    return filtered_projects


def add_new_project(projects):
    """Ask the user for the inputs and add a new project to memory"""
    print("Let's add a new project")
    project_name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(project_name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    try:
        new_percentage = int(input("New Percentage: "))
        if new_percentage:
            projects[project_choice].completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        if new_priority:
            projects[project_choice].completion_percentage = new_priority
    except ValueError:
        pass


main()
