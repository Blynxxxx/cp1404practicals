"""
1. Sales Bonus
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15
SALES_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_THRESHOLD:
        bonus_rate = LOW_BONUS_RATE
    else:
        bonus_rate = HIGH_BONUS_RATE
    bonus = sales * bonus_rate
    print(f"Bonus: {bonus}")
    sales = float(input("Enter sales: $"))
