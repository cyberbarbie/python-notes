# create a class 
class Circle:
    # create a class variable
    pi = 3.14
    # create a method (function defined inside of a clas) with 2 arguments
    #self is implicitly passed
    # radius is explicitly passed when we call the method
    def area(self, radius):
        # returns the class variable on the class * radius (what we explicitly pass) raised to the power of 2
        return Circle.pi * radius ** 2 

# create an instance of the class
circle = Circle()

pizza_area = circle.area(6)

print(pizza_area)

teaching_table_area = circle.area(18)

print(teaching_table_area)

round_room_area = circle.area(5730)

print(round_room_area)





