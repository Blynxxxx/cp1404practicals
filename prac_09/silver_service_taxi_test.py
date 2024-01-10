from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    my_taxi = SilverServiceTaxi("my_taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(f"current fare ${my_taxi.get_fare():.2f}")


main()
