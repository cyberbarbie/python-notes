# create a class
class Store:
    # pass keyword- placeholder for when information is updated to class
  pass

# create an instance of a class
#alternative_rocks = Store()
#isabelles_ices = Store()
# instance variables
#alternative_rocks.store_name = "Alternative Rocks"
#isabelles_ices.store_name = "Isabelle's Ices"

# hasattr()- returns true or false if attribute in instance or class exists

# getattr()- first argument (instance or class), what attribute we are looking for, default valuie 

#print(hasattr(alternative_rocks, "store_name"))
#print(getattr(alternative_rocks, "store_name", "doesnt exist"))

#print(getattr(isabelles_ices, "store_opening", "Attribute does not exist"))

#class Circle:
  #pi = 3.14

 # def __init__(self, diameter):
 #     print(f"New circle with diameter: {diameter}")

#teaching_table = Circle(36)

#example_two = Circle(85)

class Twitch_Streamer:

    def __init__ (self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def bio(self):
       print(f"My name is {self.name} and I am {self.age} years old. I am a {self.occupation}")

cyberbarbie = Twitch_Streamer("Tae'lur", 23, "webdev")
leedah = Twitch_Streamer("Leedah", 23, "student")
mani = Twitch_Streamer("Mani", 22, "student")

cyberbarbie.bio()
print()
leedah.bio()
print()
mani.bio()

