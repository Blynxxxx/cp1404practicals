"""
Password Check with Functions
"""
MINIMUM_LENGTH = 10


def main():
    """Get password and display asterisks as long as the word."""
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    """Display the number of asterisks based on password length."""
    print("*" * len(password))


def get_password():
    """Get valid password based on the password length."""
    password = input("Input your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("invalid password")
        password = input("Input your password: ")
    return password


main()
