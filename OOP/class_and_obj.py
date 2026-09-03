# OOP (Object-Oriented Programming) is a way of organizing code 
# around objects.

# The two basic concepts are:
# Class = blueprint
# Object = actual thing created from that blueprint


# Class
# A class defines what an object will have and what it can do.

class Car:

# __init__() is called automatically when you create an object.

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# self refers to each instance of object separately
# each instance has its own self and that is how it stores
# its unique values within it, also self is the first Value
# passed to any fucntion inside a class

    def drive(self):
        print("Car is driving")


# Object
# An object is an actual instance of the class.

car1 = Car("Toyota", "Red")
#in both init is automatically called on creation
car2 = Car("BMW", "Black")

# We can access their data:
print(car1.brand)  # Toyota
print(car2.brand)  # BMW

# And call their methods:
car1.drive()

# __init__ is a magic method also called a dunder method