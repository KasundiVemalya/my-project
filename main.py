# main.py
from car import Car
from bike import Bike
from truck import Truck

def main():
    # Creating Car object
    my_car = Car("Toyota", "Corolla", 2020)
    print(my_car.display_info())
    print(my_car.start_engine())
    print(my_car.stop_engine())

    # Creating Bike object
    my_bike = Bike("Giant", "Mountain", 18)
    print(my_bike.display_info())
    print(my_bike.ring_bell())
    print(my_bike.apply_brakes())

    # Creating Truck object
    my_truck = Truck("Ford", "F-150", 5)
    print(my_truck.display_info())
    print(my_truck.load_cargo())
    print(my_truck.unload_cargo())

if __name__ == "__main__":
    main()


