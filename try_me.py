class TwitchStreamer:
    name = "Tae'lur"
    user_name = "Cyberbarbie"
    age = 23
    location = "Georgia"

    def bio(self):
        print(f"Hello my name is {self.name}, also known as {self.user_name} and I am {self.age}. I live in {self.location}.")

cyberbarbie = TwitchStreamer()
cyberbarbie.bio()

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