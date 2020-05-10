# to run script in terminal type python3 strings.py 

# Strings are zero-indexed, each character in a string has a position and it starts from zero

#favorite_word = "fml"

# select specific character in a string using [] and save it to a new variable
#first_element = favorite_word[0]

# use print() to output text to the terminal
#print(favorite_word)

#print(first_element)

#my_name = "Cyberbarbie"

#first_initial = my_name[0]

# slicing string_name[first_index:last_index]
# starts at and INCLUDES first index
# ends at but EXCLUDES last index

# select first 3 letters of name / output is Cyb
#start_of_name = my_name[:3]
# print(start_of_name)

# select last 3 letters of name / output is bie
#last_of_name = my_name[-3:]
# print(last_of_name)

#first_name = "Rodrigo"
#last_name = "Villanueva"

# slice first 5 letters of 
#new_account = last_name[:5]
#print(new_account)

# slice 3-6 letters in last name
 #temp_password = last_name[2:6]

#def account_generator(first_name, last_name):
    #account_name = first_name[:3] + last_name[:3]
    #return account_name

#new_account = account_generator("Tae'lur", "Alexis")

#print(new_account)

# len(string_name)- check the length of a string
# string_name[-1] - find the last character in a string 

# To slice last 4 characters of a string using len()
# string_name[length:-4]



# write a function that returns a string that concatenates the last 3 characters of first name and last name
# def password_generator(first_name,last_name):
  #combined_name = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  #return combined_name

#print(password_generator("Cyber", "Barbie"))

#company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

#second_to_last = company_motto[-2]

#final_word = company_motto[-4:]

#print(final_word)

# concatenate "R" with a slice of first_name that includes 
# everything but the first character and save it to a new string
# called fixed first_nme
#fixed_first_name = "R" + first_name[1:]

#password = "theycallme\"crazy\"91"
# print(password)

# loop through a string 
#def print_each_letter(word):
 #   for letter in word:
  #      print(letter)
#print(print_each_letter("Hello"))

def get_length(word):
        return len(word)

#print(get_length("Taelur"))

# loop through character in a string 
def get_length_alt(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

#print(get_length_alt("Taelur"))

favorite_fruit = "pineapple"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1
#print(counter)


#def letter_check(word, letter):
 #   for character in word:
  ##         return True
   # return False

#print(letter_check("Amsterdam", "A"))

def contains(big_string, little_string):
    return little_string in big_string

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if(letter in string_two) and not (letter in common):
            common.append(letter)
    return common

print(common_letters("banana", "cream"))

# to run script in terminal type python3 strings.py 

# Strings are zero-indexed, each character in a string has a position and it starts from zero

#favorite_word = "fml"

# select specific character in a string using [] and save it to a new variable
#first_element = favorite_word[0]

# use print() to output text to the terminal
#print(favorite_word)

#print(first_element)

#my_name = "Cyberbarbie"

#first_initial = my_name[0]

# slicing string_name[first_index:last_index]
# starts at and INCLUDES first index
# ends at but EXCLUDES last index

# select first 3 letters of name / output is Cyb
#start_of_name = my_name[:3]
# print(start_of_name)

# select last 3 letters of name / output is bie
#last_of_name = my_name[-3:]
# print(last_of_name)

#first_name = "Rodrigo"
#last_name = "Villanueva"

# slice first 5 letters of 
#new_account = last_name[:5]
#print(new_account)

# slice 3-6 letters in last name
 #temp_password = last_name[2:6]

#def account_generator(first_name, last_name):
    #account_name = first_name[:3] + last_name[:3]
    #return account_name

#new_account = account_generator("Tae'lur", "Alexis")

#print(new_account)

# len(string_name)- check the length of a string
# string_name[-1] - find the last character in a string 

# To slice last 4 characters of a string using len()
# string_name[length:-4]



# write a function that returns a string that concatenates the last 3 characters of first name and last name
# def password_generator(first_name,last_name):
  #combined_name = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  #return combined_name

#print(password_generator("Cyber", "Barbie"))

#company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

#second_to_last = company_motto[-2]

#final_word = company_motto[-4:]

#print(final_word)

# concatenate "R" with a slice of first_name that includes 
# everything but the first character and save it to a new string
# called fixed first_nme
#fixed_first_name = "R" + first_name[1:]

#password = "theycallme\"crazy\"91"
# print(password)

# loop through a string 
#def print_each_letter(word):
 #   for letter in word:
  #      print(letter)
#print(print_each_letter("Hello"))

def get_length(word):
        return len(word)

#print(get_length("Taelur"))

# loop through character in a string 
def get_length_alt(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

#print(get_length_alt("Taelur"))

favorite_fruit = "pineapple"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1
#print(counter)


#def letter_check(word, letter):
 #   for character in word:
  ##         return True
   # return False

#print(letter_check("Amsterdam", "A"))


















