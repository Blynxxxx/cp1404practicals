"""
Exceptions Demo

CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? type(numerator) != int  or type(denominator) != int
2. When will a ZeroDivisionError occur? denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, using if-else statement
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
