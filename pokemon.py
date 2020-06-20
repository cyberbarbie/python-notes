class Pokemon:
    def __init__(self, name, type, level = 5):
        self.name = name
        self.type = type
        self.level = level
        self.maximum_health = level * 10
        self.current_health = level * 10
        self.knocked_out = False
    
    # determine the pokemon level, health and type
    def __repr__(self):
        return f"{self.name}'s is currently at level {self.level}. Their type is {self.type}. Their current health is at {self.current_health}.'"

    # this is for when the character's health has been regained!
    def regain_health(self):
        self.knocked_out =  False
        if self.current_health = 0:
            self.current_health = 1
        print(f"{self.name}'s health has been regained!'")

    # attack method- takes another pokemon as an argument and deals damage to another
    # types- fire, water, normal

    def attack(self, opponent):
        
        # check if the character is knocked

        if self.knocked_out:
            print(f"This {self.name} can't attack because it's knocked out!")

        # check if the character has a disadvantage, if it does then it only deals damage == half its opponents level
        if (self.type == "Water" and opponent.type == "Fire") or (self.type == "Water" and opponent.type == "Normal") or (self.type == "Fire" and self.type == "Normal"):
            print(f"{self.name} has attacked {opponent.name} with {")


    # determines if pokemon is knocked out and damage dealt
    def knock_out(self):
        self.knocked_out = True
        if self.health != 0
            self.health = 0
        print(f"{self.name} was knocked out.")

    # method- lost health
    def lose_health(self, health_amount):
        self.current_health -= health_amount
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print(f"{self.name} lost health! Now they're currently at {self.current_health} points.")


    # method - Acquiring more health 
    def gaining_health(self, health_amount):
        if self.current_health == 0:
            regain_health()
        self.current_health += health_amount
        
        if self.current_health >= maximum_health:
            self.current_health = self.maximum_health
        print(f"{self.name} currently has {self.current_health} health points now.")















    # create subclasses for different pokemons- inherits the name and level
    class Charmander(Pokemon):
        def __init__(self, level = 10):
            super().__init__("Charmander", "Fire", level)

    class Pikachu(Pokemon):
        def __init__(self, level):
            super().__init__("Pikachu", "Water", level)
    
    class Squirtle(Pokemon):
        def __init__(self, level):
            super().__init__("Squirtle", "Normal", level)

    class Bulbasaur(Pokemon):
        def __init__(self, level):
            super().__init__("Bulbasaur", "Water", level)

    class Eevee(Pokemon):
        def __init__(self, level):
            super().__init__("Eevee", "Fire", level)

    class Geodude(Pokemon):
        def __init__(self, level):
            super().__init__("Geodude", "Fire", level)

    class Jigglypuff(Pokemon):
        def __init__(self, level):
            super().__init__("Jigglypuff", "Normal", level)

# Trainer class- has a name list of pokemon, number of potions
# currently active pokemon- rep as a number

class Trainer:
    def __init__