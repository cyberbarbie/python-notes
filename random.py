# import and use random
import random

#random.randint()- takes 2 numbers as arguments and generates a random number between the two 

# create a variable and set it equal to a list comprehension
# the list comprehension contains an operation that loops through the range (a list of numbers from 0-100)
random_list = [random.randint(1, 100) for i in range(101)]

# Print a random number from the list of numbers
randomer_number = random.choice(random_list)

print(randomer_number)

# prints a random list of numbers from 1-100
print(random_list)