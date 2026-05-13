#9-14 Lottery
"""Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters form the list and print a message saying
that any ticket matching these 4 numbers or letters wins a prize."""

#import random modules
from random import randint, choice

#create empty lists to add letters and lottery picks to
alphabet=[]
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet.append(letter)
lottery_balls=[]

#Test random number selector(This was my inital attempt before giving it to chat)
#for num in range(10):
    #print(randint(1,50))
    #lottery_balls.append(randint(1,50))
#for letter in range(4):
    #lottery_balls.append(choice(alphabet))

#Add 10 random numbers to the list
while len(lottery_balls) < 10:
    random_number = randint(1,51)

    if random_number not in lottery_balls:
        lottery_balls.append(random_number)

#Add 4 random letters to the list
while len(lottery_balls) < 14:
    random_letter = choice(alphabet)

    if random_letter not in lottery_balls:
        lottery_balls.append(random_letter)


winning_numbers=[]
while len(winning_numbers) < 4:
    choices = choice(lottery_balls)

    if choices not in winning_numbers:
        winning_numbers.append(choices)

print(f"Any ticket matching these winning numbers {winning_numbers} is a winner!")
    


