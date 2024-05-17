# car.py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"\n{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "The car's engine is now running."

    def stop_engine(self):
        return "The car's engine is now off."