"""
CP1404/CP5632 Practical
Programming Language tests.
17:20 - 17: 43
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Display programming languages which are dynamic."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # print(python)
    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
