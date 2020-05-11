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

#print(author_last_names)

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

#print(chorus_lines)

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

print(reapers_line_one)

