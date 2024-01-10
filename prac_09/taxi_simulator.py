from prac_06.car import Car
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Create taxi simulator program which user can choose taxis, how far they want to drive,
    display the trip cost and total bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost: .2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        display_total_bill(total_bill)
        print(MENU)
        menu_choice = input(">>> ").lower()
    display_total_bill(total_bill)
    print("Taxis are now:")
    display_taxis(taxis)


def display_total_bill(total_bill):
    """Display total bill."""
    print(f"Bill to date: ${total_bill:.2f}")


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Get valid taxi choice."""
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
        return current_taxi
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Taxi choice should be number")


main()
