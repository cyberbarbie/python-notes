class UserInfo:
    name = "CyberBarbie"
    age = 23
    occupation = "content creator and whatever else they pay me to do"

    def bio(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old. I work as a {self.occupation}")

another_inst = UserInfo()
another_inst.bio()

another_attempt = UserInfo()
another_attempt.name = "Joe"
another_attempt.bio()

third_attempt = UserInfo()
third_attempt.name = "Britney"
third_attempt.bio()


another_inst.bio()

another_inst.name = "Lindsey"
another_inst.bio()

# create a class called DistanceConverter
class DistanceConverter:
    #create a class variable
  kms_in_a_mile = 1.609
  # create a method that takes 2 arguments- self which references the instance that the method is called in
  # the other argument is the only one who explicitly pass
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

# creates an instance of a class and sets it to the variable name "converter"
converter = DistanceConverter()
# explicitly pass in the miles argument
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)




