"""
CP1404/CP5632 Practical
Emails
"""
email_to_name = {}
email = input("Email: ")
while email != "":
    name = " ".join(email[:email.find("@")].split(".")).title()
    check_name_question = input(f"Is your name {name}? (Y/n) ").upper()
    if check_name_question != "Y" and check_name_question != "":
        name = input("Name: ").title()
    email_to_name[email] = name
    email = input("Email: ")
print()
for email,name in email_to_name.items():
    print(f"{name} ({email})")


