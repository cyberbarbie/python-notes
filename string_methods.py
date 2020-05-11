# .lower()- returns a string with lowercase characters

favorite_song = "SmooTH Operator"
favorite_song_lowercase = favorite_song.lower()
#print(favorite_song_lowercase)

# .upper()- returns a string with uppercase characters

favorite_song_uppercase = favorite_song.upper()
#print(favorite_song_uppercase)

# .title()- returns a string where the first letter in each word is capitalized 

favorite_song_title = favorite_song.title()
#print(favorite_song_title)

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

#print(poem_title)
#print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
#print(poem_author)
#print(poem_author_fixed)

# split()- turns a string into a list and each word becomes an element in a list
line_one = "The sky has given over"
line_one_words = line_one.split()

#print(line_one_words)

favorite_food = "My favorite food will always be enchiladas."

split_food = favorite_food.split()

#print(split_food)

favorite_quote = "The          flower that blooms in adversity is the most rare and beautiful of all"

break_down = favorite_quote.split()

#print(break_down)

# split() will turn every word in the string into its own element in a list

greatest_guitarist = "santana"
# save the method to a new variable because strings are immutable
# every encounter of that specified character/substring start a new index
new_stuff = greatest_guitarist.split('a')

# output / ['s', 'nt', 'n', '']

#print(new_stuff)

twitch_name = "cyberbarbie"
split_name = twitch_name.split('b')

#print(split_name)

favorite_food = "sushi"
new_food = favorite_food.split('s')

#print(new_food)

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')

#print(author_names)

author_last_names = []

for name in author_names:
    author_last_names.append(name.split()[-1])

# print(author_last_names)

# Escape sequences- another way to escape/split a string
# \n newline- create a line break

# use the split method to turn the string into a list
# we used the delimter \n to separate each line into its own element

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

# print(chorus_lines)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

#print(spring_storm_lines)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

#print(reapers_line_one)

# example of .join()
# add a white space between each element in a list

quote = ["I", "like", "to", "sleep", "all", "the", "time"]

combined_quote = " ".join(quote)

#print(combined_quote)

# comma separated variables - join strings with a comma

favorite_places = ["San Diego", "Toronto", "San Francisco", "Amsterdam"]

# create a common and a whitespace between each string in a list
favorite_places_csv = ', '.join(favorite_places)

#print(favorite_places_csv) 

# .join()- to combine list of strings and create a new line break between each

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

new_paragraph = '\n'.join(winter_trees_lines)

#print(new_paragraph)

# .strip()- method removes all trailing whitespace in beginning and end but preserves the middle

dirty_string = "     What are you doing    right now  "

clean_string = dirty_string.strip()

#print(clean_string)

# .strip('argument')- remove all instances of a specified argument in a string
# removes specified argument from the BEGINNING and END of a string
usernames = "@hello_goodbye cyberbarbie dsfsdfdsfds@"

just_usernames = usernames.strip('@')

# print(just_usernames)

# create a list of strings that contain lots of whitespace

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# create a new list 
love_maybe_lines_stripped = []

# loop through each string in the list to strip the whitespace
# add each new string that doesnt contain the whitespace to the empty list
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

# add a line break between each string
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

# print(love_maybe_full)

# .replace() - takes 2 arguments: what we want to replace and what we want to replace it with

dummy_string = "Lorem ipsum cupcake lorem lorem"

replace_lorem = dummy_string.replace("lorem", "hello")

# print(replace_lorem)

# another example of replace()

my_greeting = "Hello my name is Tae'lur"

replace_name = my_greeting.replace("Tae'lur", "Cyberbarbie")

# print(replace_name)

# use .replace() to replace every instance of a whitespace with a comma
with_spaces = "red blue white pink purple red"

with_commas = with_spaces.replace(" ", ", ")

# print(with_commas)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

# replace all instances of "Tomer" in the string to "Toomer" 

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

print(toomer_bio_fixed)


