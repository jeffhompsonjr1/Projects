class Resturant:
    """Initialize attributes about a resturant"""

    def __init__(self, name, cuisine):
        """ Initialize name and cuisine attributes"""
        self.name = name 
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_resturant(self):
        """Print a summary of the resturant"""
        print(f"{self.name} serves {self.cuisine} cuisine.")
    
    def open_resturant(self):
        """Print a message indicating that the resturant is open"""
        print(f"{self.name} is now open!")  

    def set_number_served(self, number):
        """Set the number of customers that have been served"""
        self.number_served = number
        print(f"Number of customers served: {self.number_served}")

    def increment_number_served(self, number):
        """Increment the number of customers served"""
        self.number_served += number
        print(f"Number of customers served: {self.number_served}")


my_resturant = Resturant('The Great Wall', 'Chinese')
my_new_resturant = Resturant('La Bella Italia', 'Italian')
my_new_favorite_resturant = Resturant('Sushi World', 'Japanese')

my_resturant.describe_resturant()
my_new_resturant.describe_resturant()
my_new_favorite_resturant.describe_resturant()

my_new_resturant.number_served = 25
print(my_new_resturant.number_served)

my_new_favorite_resturant.set_number_served(50)
my_resturant.increment_number_served(10)
my_resturant.increment_number_served(5) 
my_resturant.increment_number_served(7)