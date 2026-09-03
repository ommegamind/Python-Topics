# Abstraction means hiding unnecessary implementation details
# and showing only what the user needs to use.
# Encapsulation → protect the internal data
# Abstraction → hide the complicated implementation
# TO HIDE

class Car:

    def start(self):
        self.__check_engine()
        self.__inject_fuel()
        self.__ignite_engine()
        print("Car started")

    def __check_engine(self):
        print("Checking engine...")

    def __inject_fuel(self):
        print("Injecting fuel...")

    def __ignite_engine(self):
        print("Igniting engine...")

# The user simply does:
car = Car()
car.start()

# They don't need to know:
# __check_engine()
# __inject_fuel()
# __ignite_engine()
# The complicated implementation is hidden.
# The user only gets:

car.start()


# Python provides the abc module for formal abstraction.
# ABC = Abstract Base Class

from abc import ABC, abstractmethod

class Animal(ABC):
# "This method is required,"
# " but the parent class isn't providing the actual implementation."
    @abstractmethod
    def make_sound(self):
        pass

# here Animal is an abstract base class or an abstract class
# it says any class implementing Animal must implement make_sound
# method but idc how

# abstract classes can't be implemented

# Abstraction
# Focuses on:
# Hiding unnecessary complexity and exposing only what is needed.

# Vehicle
#    ↑
#    │
#   Car  ← ABC
#    ↑
#    │
# SportsCar

# Car is both:
# A subclass of Vehicle
# An Abstract Base Class