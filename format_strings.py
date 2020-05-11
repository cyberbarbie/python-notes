def poem_title_card(poet, title):
     poem_description = "The poem {} is written by {}".format(title, poet)
     return poem_description

# print(poem_title_card("Annabel Lee", "Edgar Allan Poe"))

# example of using keywords in the format method 
def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# create a function with multiple arguments (aka placeholder variables)
def poem_description(publishing_date, author, title, original_work):
    # use format method to specify the placement of the variables in the string
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

# define the variables
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)