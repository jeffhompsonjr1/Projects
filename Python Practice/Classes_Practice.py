class Car:
    """A Simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Intializes attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        """Return a neatly formatted name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
       """ Return the mileage of the car """
       print(f" There are {self.odometer_reading} miles on the car")

my_new_car = Car("Chevy", "Monte Carlo", "2002")
print(my_new_car.get_description_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
