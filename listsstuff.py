# zip - combine 2 lists and create an object of pairs 

# create 2 lists 
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# combine into an object
names_and_dogs_names = zip(names, dogs_names)

# transform into an object list of tuples
list_of_names_and_dogs_names = list(names_and_dogs_names)

# .append() - add one item lista list
names.append(1)
dogs_names.append(2)

#print(list_of_names_and_dogs_names)

# add multiple items to a list- must combine lists 
# To update list with multiple items- save to new list
# can only concatenate lists, so must save data type in a list
desserts = ['cake', 'cookie', 'bread']
updated_desserts = desserts + [1]
#print(updated_desserts)

# Range- create a consecutive list of numbers
# range(#)- ends at number before input
# range(10)- 0-9 / returns an object we can convert into a list
#print(list(my_range))

#range(2, 9)- 2, 3, 4, 5, 6, 7, 8
# 2 arguments- start at and ends at 

#range(1, 20, 2)- starts at, ends at 20, increments by 2

# create list of numbers 0-9 (but not inc 9)
#list(range(9))

# save object as list
#gradebook = list(zip(subjects, grades))

names = ["Tae'lur", "Joe", "Raven", "Leedah", "Mani"]

greetings = ["Good Morning, " + name for name in names]

values = [1, 2, 3, 4, 5]

multiply_by_ten = [num * 10 for num in values]

complicate_me_daddy = ["Complicate me " + str(num) + " hello" for num in values]

print(complicate_me_daddy)

print(multiply_by_ten)

print(greetings)

temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_F = [(9.0/5.0)*temp + 32 for temp in temperatures]

# return square value of each number in range(11) 0-10
nums = range(11)

squares = [num ** 2 for num in range(11)]

print(squares)

nums = [4, 8, 15, 16, 23, 42]

add_ten = [num + 10 for num in nums]

nums = [4, 8, 15, 16, 23, 42]

divide_by_two = [num/2 for num in nums]

#num % 2 == 0 - even
#num % 2 == 1 - odd

# Create a new list named parity 
# that contains a 1 or a 0 for each element of nums. 
# For each element, if that element was even, 
# the new list should contain a 0. If the element was odd, 
# the new list should contain a 1.

nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]

print(parity)

names = ["Elaine", "George", "Jerry", "Cosmo"]

greetings = ["Hello, " + name for name in names]

# Get first character from each string in a list
names = ["Elaine", "George", "Jerry", "Cosmo"]

first_character = [name[0] for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]

# Return the length of each element in a list
lengths = [len(name) for name in names]

booleans = [True, False, True]

opposite = [not boolean for boolean in booleans ]

print(opposite)

a = True
b = False 

not_a = not a # False
not_b = not b # True

#Create a new list called is_Jerry
#in which an entry at position i is True 
#if the entry in names at position i equals 
#"Jerry". The entry should be False otherwise



names = ["Elaine", "George", "Jerry", "Cosmo"]

is_Jerry = [name == "Jerry" for name in names]

#Create a new list called greater_than_two
#in which an entry at position i is True 
#if the entry in nums at position i is greater than 2.
nums = [5, -10, 40, 20, 0]

greater_than_two = [num > 2 for num in nums]

nested_lists = [[4, 8], [15, 16], [23, 42]]

#iterate through lists in a list (sublist)

product = [item1 * item2 for (item1, item2) in nested_lists]

#Create a new list named greater_than 
#that contains True if the first number 
#in the sub-list is greater than the second 
#number in the sub-list, and False otherwise.


nested_lists = [[4, 8], [16, 15], [23, 42]]

greater_than = [num1 > num2 for (num1, num2) in nested_lists]

# Create a new list named first_only 
# that contains the first element 
# in each sub-list of nested_lists.


first_only = [item1 for (item1, item2) in nested_lists]


# Use list comprehension and the zip function 
# to create a new list named sums 
# that sums corresponding items in lists a and b.
# For example, the first item in the new list 
# should be 5 from adding 1 and 4 together.
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

combo = zip(a, b)

sums = [num1 + num2 for (num1, num2) in combo]

# or 

sums = [item1 + item2 for (item1, item2) in zip(a, b)]


a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

quotients = [item2 / item1 for (item1, item2) in zip(a,b)]

# To concatenate a string and integer
# use str() to convert the int into a string
#You’ve been given two lists: 
#a list of names and a list of ages. 
# Create a new list named users that 
# contains the string "Name: name, Age: age" 
# for each pair of elements in the original 
# lists. For example, if the 5th item in 
# the names list is "John" and the 5th item 
# in ages is 42, then the 5th item in the
#  new list should be "Name: John, Age: 42".
names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]

users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]

#Create a new list named 
#greater_than that contains True or False 
#depending on whether the corresponding item 
#in list a is greater than the one in list b. For example, 
#if the 2nd item in list a is 3, and the 2nd item in list b is 5, 
#the 2nd item in the new list should be False.

a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [item_a > item_b for (item_a, item_b) in zip(a,b)]
