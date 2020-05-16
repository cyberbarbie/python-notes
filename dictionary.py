# Dictionary - An unordered set of key:value pairs
# To map pieces of data to each other 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

#print(sensors)

user_ages = {"Tae'lur": 23, "Daniel": 23, "Kyrah": 14}

# dictionaries can contain any data type
# in this example, the variable students_in_classes are set to a dictionary
# that contains keys that equal lists
students_in_classes = {
"software design": ["Aaron", "Delila", "Samson"], 
"cartography": ["Christopher", "Juan", "Marco"], 
"philosophy": ["Frederica", "Manuel"]
}

# keys can only be strings or numbers
# values can be any of the data types like lists, strings, numbers, or booleans

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

my_empty_dictionary = {}

# To add a single key:value pair to a dictionary
# my_dict["new_key"] = "new_value"

# Add a key value pair to the empty dictionary
my_empty_dictionary["Tae'lur"] = 23

#print(my_empty_dictionary)

animals_in_zoo = {}

animals_in_zoo["zebras"]= 8

animals_in_zoo["monkeys"] = 12

animals_in_zoo["dinosaurs"] = 0

#print(animals_in_zoo)

# .update()- update a dictionary with multiple key value pairs

animals_in_zoo.update({"gorillas": 21, "tigers": 23, "lions": 45})

#print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

#print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

#print(oscar_winners)

coffee_drinks = {"Mocha": 3, "Caramel machiato": 5, "Caramel frappuccino": 20}

coffee_drinks.update({"strawberrry mocha": 6, "spiced coffee": 3})

#print(coffee_drinks)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks= zip(drinks, caffeine)


# Create a dictionary that utilizes a list comprehension to create key value pairs and zip command to combine lists
#drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}

# create a dictionary that uses a 
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song, playcount in zip(songs, playcounts)}

#print(plays)

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

#print(library)

# create a dictionary that contains a tuple as a key with a string as a value 
example = {("name", "age", "occupation"): ["Tae'lur", "23", "frontend dev"]}

#print(example)

artists_ranking = {"Nicki Minaj": 10, "Jhene Aiko": 2, "Young MA": 1, "Summer Walker": 3}

#print(artists_ranking["Nicki Minaj"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

#print(zodiac_elements["earth"])

#print(zodiac_elements["fire"])

key_to_check = "water"

# To avoid a KeyError
# run a conditional to check for a key, if it exists then it will print the values correlated to that key
# if it is false, it will still not break your code. nothing happens

#if key_to_check in zodiac_elements:
 #   print(zodiac_elements["water"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}

#print(zodiac_elements["energy"])

# Error handling with Try/Except
key_to_check = "jhene"

try:
    print(zodiac_elements[key_to_check])
except KeyError:
    print("That key doesn't exist!")

