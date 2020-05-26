# Class- An object that provides a set of information
class TwitchStreamer:
    # class variables - variables defined instance of a class
    name = "Tae'lur"
    user_name = "Cyberbarbie"
    age = 23
    location = "Georgia"

    # method()- a function defined inside of a class that can take multiple args
    # self- the first argument; reference to whatever object it is called in
    def bio(self):
        # prints a string with variables
        print(f"Hello my name is {self.name}, also known as {self.user_name} and I am {self.age}. I live in {self.location}.")
# create an instance of an object
cyberbarbie = TwitchStreamer()
cyberbarbie.bio()

#hasttr()- 

# Access and change the properties on the instance (object)
jyrone = TwitchStreamer()
jyrone.name = "Jyrone"
jyrone.user_name = "mastashake08"
jyrone.age = 28
jyrone.location = "Kentucky"
jyrone.bio()

# Access and change the properties on the instance (create another object)
joe = TwitchStreamer()
joe.name = "Joe"
joe.user_name = "lafiosca"
joe.age = 41
joe.location = "Georgia"
joe.bio()