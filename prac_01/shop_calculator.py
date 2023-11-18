"""
Shop Calculator
"""
DISCOUNT_RATE = 0.1
TOTAL_PRICE_THRESHOLD = 100

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for item in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > TOTAL_PRICE_THRESHOLD:
    total_price = total_price * (1 - DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price: .2f}")
