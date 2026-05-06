class Car:
    """Initiate a class representing a car"""
    def __init__(self, make, model, year, color):
        """ attributes of the car """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.miles = 0

    def describe_car(self):
        """ use attributes to describe the car"""
        descriptive_name = f"{self.color} {self.year} {self.make} {self.model}"
        return descriptive_name.title()

    def get_miles(self):
        """ get the value of the car mileage"""
        print(f"The car has {self.miles}")

my_first_car = Car("Chevy", "Monte Carlo", "2002","white")
print("My very first car was a", my_first_car.describe_car())
my_first_car.get_miles()

