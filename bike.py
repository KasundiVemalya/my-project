# bike.py
class Bike:
    def __init__(self, brand, type, gear_count):
        self.brand = brand
        self.type = type
        self.gear_count = gear_count

    def display_info(self):
        return f"{self.brand} {self.type} with {self.gear_count} gears"