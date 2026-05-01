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
        """Set the number_served"""
        self.number_served = number
        print(f"We served {self.number_served} today.")

    def increment_number_served(self, number_added):
        """Increement the number of customers who've been served"""
        self.number_served += number_added
        print(f"We've served {self.number_served} today.")


my_resturant = Resturant("Lovely Creations", "Desserts")
my_resturant.describe_resturant()
my_resturant.increment_number_served(10)
my_resturant.increment_number_served(15)

            



