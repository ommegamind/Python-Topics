# Data Types

# int
# Represents whole numbers.

age = 22
count = -10
population = 1000000

# Python integers can become very large:

x = 999999999999999999999999999999

# No fixed 32-bit/64-bit limitation like you might encounter 
# with primitive integer types in some languages.

# float
# Represents decimal/floating-point numbers.

price = 99.99
temperature = 36.5
percentage = 85.5

# You can perform arithmetic:

x = 10.5
y = 2.5

print(x + y)


# complex
# Used for complex numbers.

z = 2 + 3J

print(z.real)
print(z.imag)

# Python uses j or J as the suffix for the imaginary unit (where j² = -1).
# You write a complex number by combining a real number and 
# an imaginary number (for example, 3 + 4j).
# Capital J works the exact same way (for example, 3 + 4J).


# bool 
# has only two values:

is_logged_in = True
is_admin = False

# Python treats:
# True
# as equivalent to 1, and:

# False
# as equivalent to 0 in numeric contexts.

print(True + True)
print(True + False)

# Strings
# A string represents text.

name = "Om"
language = 'Python'

# Both single and double quotes work:

# Multi-line strings
message = """Hello
Welcome to Python
Good luck!"""

message='''hie
whatcha
doin'''

# Strings are sequences, so individual characters
# can be accessed using indexes.

name = "Python"

print(name[0])
print(name[1])

# Negative indexing works too:

print(name[-1])


# Lists
# A list stores multiple values.
numbers = [10, 20, 30, 40]

# Lists can contain different types:
data = ["Om", 22, 85.5, True]

# Lists are mutable, meaning you can modify them.
numbers = [10, 20, 30]
numbers[0] = 100

print(numbers)


# Tuples
# A tuple is similar to a list but is immutable.

coordinates = (10, 20)

# You cannot do:

coordinates[0] = 100

# That produces an error.
# Tuples are useful when the collection should not be modified.


# Sets
# A set stores unique values.

numbers = {1, 2, 3, 3, 4}
print(numbers)

# The duplicate 3 is removed.
# Sets are useful when you care about membership and uniqueness.

skills = {"Python", "Selenium", "SQL"}

print("Python" in skills)


# Dictionaries
# A dictionary stores data as key-value pairs.

student = {
    "name": "Om",
    "age": 22,
    "branch": "CS"
}

# Access values using their keys:
print(student["name"])

# You can modify values:
student["age"] = 23


# None
# None represents the absence of a value.

result = None

# It is different from:

# 0
# and:
# ""
# and:
# False

# You commonly see it when a value 
# hasn't been assigned yet or a function doesn't 
# return anything useful.

# Correct way to check it:
# if result is None:
#     print("No result")


# Checking for type/class instance
# Use type():
x = 100

print(type(x))

# You can also use isinstance():

x = 100

print(isinstance(x, int))

# isinstance() is generally more useful when checking whether 
# something belongs to a particular type/class.



# Type Conversion
# Python allows you to convert between compatible types.
# String → Integer
age = "22"

age = int(age)

print(age)
print(type(age))

# Integer → String
age = 22

age = str(age)

# Integer → Float
x = 10

y = float(x)

print(y)

# Float → Integer
x = 10.9

print(int(x))

# Notice that it doesn't round. It truncates the decimal part.