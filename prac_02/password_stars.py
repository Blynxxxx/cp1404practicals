"""
Password Check with Functions
"""
MINIMUM_LENGTH = 10


def main():
    """Get password and display asterisks as long as the word."""
    password = get_password("Input your password: ", MINIMUM_LENGTH)
    display_asterisks(password)


def display_asterisks(password):
    """Display the number of asterisks based on password length."""
    print("*" * len(password))


def get_password(prompt, length):
    """Get valid password based on the password length."""
    password = input(prompt)
    while len(password) < length:
        print("invalid password")
        password = input(prompt)
    return password


main()
