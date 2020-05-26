# 1. Create a new list named double_nums by multiplying each number in nums by two.
#nums = [4, 8, 15, 16, 23, 42]

#double_nums = [num * 2 for num in nums]

#print(double_nums)

# 2. You’ve been given a list of the numbers between 0 and 10. 
# We created this list using the range function! 
# Create a new list named squares that contains the square of every number in this list.
#nums = range(11)

#squares = [num ** 2 for num in nums]

#print(squares)

# 3. Create a new list named add_ten that adds ten to every element in the list nums.
#nums = [4, 8, 15, 16, 23, 42]

#add_ten = [num + 10 for num in nums]

#print(add_ten)


# 4. Create a new list named divide_by_two that contains half of every element in the list nums. 
# Make sure to divide by 2, not 2.0!
#nums = [4, 8, 15, 16, 23, 42]

#divide_by_two = [num / 2 for num in nums]

#print(divide_by_two)

# 5. Create a new list named parity that contains a 1 or a 0 for each element of nums. 
# For each element, if that element was even, the new list should contain a 0. 
# If the element was odd, the new list should contain a 1.
# HINT: You can use %2 to determine if a number is even or odd. 
# If it is even, there should be no remainder (an output of 0). 
# If it is odd, there should be a remainder of 1:

#nums = [4, 8, 15, 16, 23, 42]

#parity = [num % 2 for num in nums]

#print(parity)

#Create a new list named greetings that adds "Hello, " in front of each name in the list names.

#names = ["Elaine", "George", "Jerry", "Cosmo"]

#greetings = ["Hello, " + name for name in names]

#print(greetings)

#Create a new list named first_character that contains the first character from every name in the list names
#names = ["Elaine", "George", "Jerry", "Cosmo"]

#Create a new list named lengths that contains the size of each name in the list of names
#names = ["Elaine", "George", "Jerry", "Cosmo"]

#We can use the not operator to flip the value of a Boolean:
#a = False
#b = True

#not_a = not a
#not_b = not b
#print(not_a)
#print(not_b)

# Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
#booleans = [True, False, True]

#opposite = [not boolean for boolean in booleans]

#print(opposite)

#Create a new list called is_Jerry, 
# in which an entry at position i is True if the entry in names at position i equals "Jerry". 
# The entry should be False otherwise

#names = ["Elaine", "George", "Jerry", "Cosmo"]

#is_Jerry = [i == "Jerry" for i in names]

#print(is_Jerry)

#Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.

#nums = [5, -10, 40, 20, 0]

#greater_than_two = [num > 2 for num in nums]

#print(greater_than_two)

#When using list comprehension, sometimes the items in the list that you’re iterating through will be lists themselves! 
# In these cases, you can access multiple items in those sub-lists by using the following syntax:

#original_list = [[1, 2], [3, 4],  [5, 6]]
#new_list = [item1 + item2 for (item1, item2) in original_list]
#print(new_list)

#new_list will now contain the sum of each sub-list.
#Create a new list named product that contains the product of each sub-list of nested_lists.

#nested_lists = [[4, 8], [15, 16], [23, 42]]
#product = [sub1 * sub2 for (sub1, sub2) in nested_lists]
#print(product)

#Create a new list named greater_than that contains True 
# if the first number in the sub-list is greater than the second number in the sub-list, 
# and False otherwise.
#nested_lists = [[4, 8], [16, 15], [23, 42]]

#greater_than = [num1 > num2 for (num1, num2) in nested_lists]

#print(greater_than)

#Create a new list named first_only that contains the first element in each sub-list of nested_lists.
#nested_lists = [[4, 8], [16, 15], [23, 42]]

#first_only = [item1 for (item1, item2) in nested_lists]

#print(first_only)

# Use list comprehension and the zip function 
#In the following exercises, you will be given two lists and asked to perform operations of corresponding elements of these lists. 
# This can be done by using List Comprehension and the built-in Python function zip
# Use list comprehension and the zip function to create a new list 
#named sums that sums corresponding items in lists a and b. 
# For example, the first item in the new list should be 5 from adding 1 and 4 together.

#a = [1.0, 2.0, 3.0]
#b = [4.0, 5.0, 6.0]

#sums = [num1 + num2 for (num1, num2) in zip(a, b)]

#print(sums)


# Use list comprehension and the zip function to create a new list named quotients 
# that divides the elements in list b by those in list a . 
# For example, the second item in the new list should be 2.5 from dividing 5.0 by 2.0.

#a = [1.0, 2.0, 3.0]
#b = [4.0, 5.0, 6.0]

#quotients = [item_b / item_a for (item_a, item_b) in zip(a,b)]

#print(quotients)

# You’ve been given two lists: a list of capitals and a list of countries. 
# Create a new list named locations that contains the string "capital, country" for each item in the original lists. 
# For example, if the 5th item in the capitals list is "Lima" and the 5th item in the countries list is "Peru", 
# then the 5th item in the new list should be "Lima, Peru"

#capitals = ["Santiago", "Paris", "Copenhagen"]
#countries = ["Chile", "France", "Denmark"]

#locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]

#print(locations)


# You’ve been given two lists: a list of names and a list of ages. 
# Create a new list named users that contains the string
# "Name: name, Age: age" for each pair of elements in the original lists.
# For example, if the 5th item in the names list is "John" and the 5th item in ages is 42, 
# then the 5th item in the new list should be "Name: John, Age: 42".
# As you did in the previous exercise, concatenate

#names = ["Jon", "Arya", "Ned"]
#ages = [14, 9, 35]

#users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages)]

#print(users)

# Create a new list named greater_than that contains True or False 
# depending on whether the corresponding item in list a is greater than the one in list b. 
# For example, if the 2nd item in list a is 3, and the 2nd item in list b is 5, the 2nd item in the new list should be False.

a = [30, 42, 10]
b = [15, 16, 17]

greater_than = [item_a > item_b for (item_a, item_b) in zip(a,b)]

print(greater_than)







