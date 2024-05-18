# truck.py
class Truck:
    def __init__(self, make, model, capacity):
        self.make = make
        self.model = model
        self.capacity = capacity

    def display_info(self):
        return f"{self.make} {self.model} with a capacity of {self.capacity} tons"

    def load_cargo(self):
        return "The truck is loading cargo."

    def unload_cargo(self):
        return "The truck is unloading cargo."
