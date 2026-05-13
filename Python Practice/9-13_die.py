from random import randint

class Die():
    """Initiate a class that rolls random dice sizes"""
    def __init__(self, sides=6):
        """There is one attribute sides"""
        self.sides = sides

    def six_sides(self):
        print(randint(1, self.sides))

    def ten_sides(self):
        self.sides = 10
        print(randint(1, self.sides))

    def twenty_sides(self):
        self.sides = 20
        print(randint(1, self.sides))

die = Die()

for num in range(40):
    die.twenty_sides()

