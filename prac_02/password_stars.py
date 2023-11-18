"""
Password Check with Functions
"""

MINIMUM_LENGTH = 10

password = input("Input your password: ")
while len(password) < MINIMUM_LENGTH:
    print("invalid password")
    password = input("Input your password: ")
print("*" * len(password))