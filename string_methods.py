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
new_stuff = greatest_guitarist.split('n')

print(new_stuff)