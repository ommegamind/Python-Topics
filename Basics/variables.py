# What is a variable?
# A variable is a name used to refer to a value/object stored in memory.

name= "om"
age=22
engineer=True

# Python does not require you to declare the data type of a variable.
# Python determines the type automatically.

# You can check the type using type():
print(type(name))
print(type(age))
print(type(engineer))

# Variable convention
# Cannot start with a number.
# '-' is interpreted as subtraction.
# Can't use keywords.

# Naming conventions
# Python commonly uses snake_case:

first_name = "Om"
employee_salary = 40000
test_case_count = 10


# Constants are conventionally written in uppercase:

PI = 3.14159
MAX_RETRIES = 3

# NOTE: Python doesn't actually prevent you from changing them;
# uppercase is simply a convention.

# Multiple Variable Assignment
# You can assign several variables at once.

name, age, city = "Om", 22, "Pune"

# same variable assignment
x=y=z=100
print(x, y, z)

# swapping variable
x=10
y=20
print(x,y)

x,y=y,x
print(x,y)

# Python is dynamically typed.
# This means a variable doesn't have a permanently fixed type.

x = 10
print(type(x))

x = "Hello"
print(type(x))

x = 3.14
print(type(x))


# Python is dynamically typed, but it is also strongly typed.
# For example:

x = 10
y = "20"

print(x + y)

# This produces a TypeError.
# Python won't automatically treat "20" as the number 20.

# You would need:

print(x + int(y))