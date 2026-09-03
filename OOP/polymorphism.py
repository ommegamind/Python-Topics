# Polymorphism literally means “many forms.”

# In OOP, polymorphism means:
# The same interface/method/operator can
# behave differently depending on the object or data type involved.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()
dog.sound()   # Bark
cat.sound()   # Meow

# Both classes have:
# sound()
# But sound() behaves differently.
# That's polymorphism.


# Method Overriding
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
# Dog and Cat override the parent's sound() method.

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# Python figures out the appropriate implementation at runtime.
# That's polymorphism.
# This is often called runtime polymorphism because 
# the appropriate method is determined at runtime.

# Polymorphism without inheritance
# This is an important Python-specific point.
# Python uses duck typing.
class Dog:
    def sound(self):
        print("Bark")

class Robot:
    def sound(self):
        print("Beep")

# There is no inheritance relationship between them.
# But:

def make_sound(obj):
    obj.sound()

make_sound(Dog())
make_sound(Robot())

# This is duck typing.
# The common phrase is:
# “If it walks like a duck and quacks like a duck, treat it like a duck.”


# Operator Overloading
# Consider:

print(10 + 20)

# You get:
# 30

# But:
print("Hello " + "World")

# gives:
# Hello World
# The same operator:
# +
# has different behavior depending on the operands.
# That's operator overloading, which is a form of polymorphism.
# Python implements many operators using special/dunder methods.

# a + b
# roughly corresponds to:
# a.__add__(b)

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

a = Number(10)
b = Number(20)
c = a + b
print(c.value)

# magic methods
# Operator	Dunder method
# +	    __add__()
# -	    __sub__()
# *	    __mul__()
# /	    __truediv__()
# ==	__eq__()
# <	    __lt__()
# >	    __gt__()
# <=	__le__()
# >=	__ge__()
# !=	__ne__()


# Python does not support traditional compile-time
# method overloading by defining multiple methods with 
# the same name but different parameter lists.

# Method overriding
# Child changes the behavior inherited from parent:
# Operator overloading
# You define how an operator behaves for your custom object:

# Python does not support traditional compile-time polymorphism 
# through method overloading like Java or C++. Python mainly achieves
# polymorphism at runtime through method overriding, duck typing, 
# and operator overloading.