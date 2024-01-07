from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            choose_taxi(taxis)
        elif choice == "D":
            drive_taxi(current_taxi)

        else:
            print("Invalid option")
        display_bill_to_date(current_taxi)
        print(MENU)
        choice = input(">>> ").upper()
    pass


def drive_taxi(current_taxi):
    if current_taxi:
        return current_taxi.drive()
    print("You need to choose a taxi before you can drive")


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def display_bill_to_date(current_taxi):
    if current_taxi:
        fare = current_taxi.get_fare()
    else:
        fare = 0
    print(f"Bill to date: ${fare :.2f}")

main()