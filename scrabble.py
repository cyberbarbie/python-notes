# create two lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# create a dict comprehension that transforms the 2 lists into key value pairs
# letters - keys
# points - vales
letter_to_points = {letter:point for letter, point in zip(letters, points)}

# update dict with a single key value 
letter_to_points[" "] = 0

# looped through each letter in word (argument) and updated point total with the value of the key in letters to point duct
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

# create a variable that is set the value of score_word() function
brownie_points = score_word("TAELUR")

#print(brownie_points)

# create a dictionary where the keys are strings and the values are lists
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
#print(player_to_words.values())

# create an empty dict
player_to_points = {}

# create a for loop that loops through the players to words dictionary (player = key, word = value)
for player, words in player_to_words.items():
    player_points = 0
    # create a nested for loop that loops through every elemnent in list value
    for word in words:
        # update player points with the value of score_word input
        player_points += score_word(word)
        # update the player_to_points dictionary to have player as key and player_points as value 
    player_to_points[player] = player_points

print(player_to_points)

    #print(f"Player {player} has {player_points} points")


#player_points += player_to_words.get(player)

#print(player_to_words.items())

        
    