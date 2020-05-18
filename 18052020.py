user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Access all keys in users_ids dict and save it to variable
users = user_ids.keys()

# Access all keys in num_exercises dict and save it to variable 
lessons = num_exercises.keys()

#print(users)

#print(lessons)

#.values()- returns a dict_values object that lists all the values from a dictionary
#values = user_ids.values()

total_exercises = 0

# iterate through every value and add it total exercises variable
for num in num_exercises.values():
    total_exercises += num

print(total_exercises)

#