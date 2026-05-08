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
    
    def update_mileage(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
             print("You can't roll back")
    
    def increment_miles(self, miles):
        self.odometer_reading += miles
              
    def read_odometer(self):
       """ Return the mileage of the car """
       print(f" There are {self.odometer_reading} miles on the car")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 40):
        """ Initialize the Battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh Battery")

    def describe_range(self):
        if self.battery_size <= 40:
            print("The range of the car is 200 KMs")
        elif self.battery_size <= 60:
            print("The range of the car is 300 KMs")
        else:
            print("The range of the car is 300+ KMs")
            
        

class Electric_car(Car):
    """Initializes attributes to describe an electric car"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

   

        


