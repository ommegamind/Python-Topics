# Inheritance is an OOP concept where a child class 
# gets properties and methods from a parent class.
# The main purpose is code reuse and creating a relationship
# between classes.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()   # inherited from Animal
dog.bark()  # defined in Dog

# Parent = common functionality
# Child = common functionality + its own functionality

# Inheritance with __init__
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")

dog = Dog("Bruno")
dog.eat()
dog.bark()
# Dog doesn't have its own __init__.
# Therefore, Python uses the inherited Animal.__init__().

# super() allows the child class to access the parent class's methods.
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Method overriding
# A child class can replace/redefine a method inherited from the parent.
class Animal:
    def make_sound(self):
        print("Some animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

# Now:
animal = Animal()
dog = Dog()
animal.make_sound()
dog.make_sound()

# Inheritance
#     ↓
# Child gets functionality from Parent
#     ↓
# Child can override parent's methods
#     ↓
# Method overriding


# Types of inheritance in Python (5)

# Single inheritance
# One parent → one child.

# Multilevel inheritance
# Parent → Child → Grandchild.

# Multiple inheritance
# One child has multiple parents.
# Father      Mother
#    \          /
#     \        /
#       Child

# Hierarchical inheritance
# One parent → multiple children.
#        Animal
#        /    \
#      Dog    Cat

# Hybrid inheritance
# A combination of two or more inheritance types.


# Python follows MRO — Method Resolution Order.
# suppose
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass

# You can see it using:
print(D.mro())
# It will follow an order similar to:
# D → B → C → A → object

# MRO determines the order in which 
# Python searches parent classes for methods and attributes.

# Every normal Python class ultimately inherits from:
# object
# For example:
class Animal:
    pass

# is effectively part of:
# Animal
#    ↓
# object

# You can check:
print(Animal.mro())

# You'll get something like:
# [<class '__main__.Animal'>, <class 'object'>]
# This is also why every class ultimately gets certain
#  built-in behavior from object.