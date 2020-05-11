highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

# use .split() to transform a string into a list and separate into list elements by a comma
highlighted_poems_list = highlighted_poems.split(",")

# print(highlighted_poems_list)

# Create a new empty list called highlighted_poems_stripped.
highlighted_poems_stripped = []

# iterate through highlighted_poems_list using a for loop
# for each poem strip away the whitespace
for poem in highlighted_poems_list:
    # append it to your new list, highlighted_poems_stripped
  highlighted_poems_stripped.append(poem.strip())

# print(highlighted_poems_stripped)

# create an empty list
highlighted_poems_details = []

# Loop through each poem in poems and use the split method with delimeter ":"
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

# create 3 empty lists 
titles = []
poets = []
dates = []

# create a for loop that appends (aka adds) the appropriate name to variable
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

# loop through and print a string with variables using the format method
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))





