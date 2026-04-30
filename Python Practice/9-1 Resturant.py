class Resturant:
    """Initialize attributes about a resturant"""

    def __init__(self, name, cuisine):
        """ Initialize name and cuisine attributes"""
        self.name = name 
        self.cuisine = cuisine
    
    def describe_resturant(self):
        """Print a summary of the resturant"""
        print(f"{self.name} serves {self.cuisine} cuisine.")
    
    def open_resturant(self):
        """Print a message indicating that the resturant is open"""
        print(f"{self.name} is now open!")  

my_resturant = Resturant('The Great Wall', 'Chinese')

my_resturant.describe_resturant()
my_resturant.open_resturant()
