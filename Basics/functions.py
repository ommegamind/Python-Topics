# Function → a reusable block of code that can be called independently.
# Method → a function that is associated with an object/class and 
# is called using that object.


# You can create a function:

def greet():
    print("Hello Om")

# Then call it whenever needed:

greet()


# Parameters
# A function can receive input.

def greet(name):
    print("Hello", name)

# Here name is a parameter.
# Call it:

greet("Om")

# name is the parameter and "Om" is the argument.


def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# return sends a value back to the code that called the function.



# Returning Multiple Values
# Python allows a function to return multiple values.

def get_user():
    return "Om", 22

# You can unpack them:

name, age = get_user()
print(name)
print(age)


# You can provide a default value for a parameter.

def greet(name="User"):
    print("Hello", name)

# Keyword Arguments
# You can pass arguments using parameter names.

def student(name, age):
    print(name, age)

# Instead of:
student("Om", 22)
# Normal arguments are positional.

# You can write:
student(name="Om", age=22)

# You can even change the order:
student(age=22, name="Om")


def employee(name, salary):
    print(name, salary)

employee("Om", salary=40000)

# But positional arguments generally need 
# to come before keyword arguments.

# This is invalid:
# employee(name="Om", 40000)



# *args
# Sometimes you don't know how many positional 
# arguments the function will receive.

# Use *args.

def add(*numbers):
    print(numbers)

# Now:
add(10, 20)

# Output:
# (10, 20)
# Inside the function, args is a tuple.


# **kwargs
# **kwargs allows a function to receive an arbitrary number
# of keyword arguments.

def student(**details):
    print(details)

# Call:

student(name="Om", age=22, branch="CS")

# Output:
# {'name': 'Om', 'age': 22, 'branch': 'CS'}

# Inside the function, kwargs is a dictionary.



# Scope of Variables
# Variables created inside a function are generally local variables.

# Global Variables
# A variable defined outside functions is in the global scope.


# However, modifying global variables from inside
# functions requires care and, when necessary, the global keyword.

x = 10

def change():
    global x
    x = 20

change()

print(x)



# A method is a function associated with an object or class.
# For example:

name = "Python"
name.upper()

# upper() is a string method.

numbers = [1, 2, 3]
numbers.append(4)

# append() is a list method.


# Function vs Method
# Function
len("Python")

# len() is a built-in function.

# Method
"Python".upper()

# upper() is a string method.

# User-defined Functions
# A function you create yourself is called a user-defined function.



# Lambda Functions
# Python also supports small anonymous functions using lambda.
# Syntax:

# lambda arguments: expression

# Lambdas are useful for short operations
square = lambda x: x * x
print(square(5))



# Recursive Functions
# A function can call itself.



# Are Functions Objects in Python?

# Yes.
# Functions are first-class objects in Python.
# That means you can assign a function to a variable:

def greet():
    print("Hello")

x = greet

x()


# You can also pass functions as arguments:

def execute(func):
    func()

def greet():
    print("Hello")

execute(greet)


# *args     → multiple positional arguments → tuple
# **kwargs  → multiple keyword arguments   → dictionary