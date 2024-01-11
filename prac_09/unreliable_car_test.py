from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""

    # create cars with different reliabilities
    my_car = UnreliableCar("My Car", 100, 90)
    limo = UnreliableCar("Limo", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 11):
        print(f"Attempting to drive {i}km:")
        print(f"{my_car.name} drove {my_car.drive(i)}km")
        print(f"{limo.name} drove {limo.drive(i)}km")

    # print the final states of the cars
    print(my_car)
    print(limo)


main()