# Encapsulation means keeping an object's data and 
# the code that works with that data together, 
# while controlling how that data is accessed or changed.
# TO PROTECT

# Encapsulation: control access
# We can make the internal variable private-ish:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

# The __ tells Python that this is intended to be an 
# internal/private attribute.

# we provide methods to control access:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


# Python commonly uses three naming conventions:

# Public
# self.name
# Anyone can access it:

# Protected
# self._name
# A single _ means:
# "This is intended for internal/subclass use."
# "Please don't access it directly."
# But Python does not strictly prevent access.
# It's mainly a convention.

# Private
# self.__name
# Double underscore triggers name mangling,
# making direct access harder.
# Python internally changes the name roughly to:
# _Person__name
# This is called name mangling


# The actual idea of encapsulation is:
# Hide/protect internal implementation and 
# provide controlled ways to interact with it.
# The class hides the implementation details and 
# exposes useful methods.

# Encapsulation VS Abstraction
# Encapsulation → Protect/control the internals
# Abstraction   → Hide complexity