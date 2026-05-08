from car import Car

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

   

        


