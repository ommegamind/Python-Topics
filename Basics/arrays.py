# One important thing first: Python doesn't have a built-in
# array type that is normally used like arrays in C/Java. 
# In Python, when people say "array," they usually mean a list.

# What is a list?
# A list is an ordered, mutable collection of values.

numbers = [10, 20, 30, 40]

# Here:
# Index:     0    1    2    3
# Value:    10   20   30   40

# Python lists can contain different data types:

data = [10, "hello", True, 3.14]

# 2. Creating Lists
numbers = [1, 2, 3, 4, 5]

names = ["Om", "Rahul", "Amit"]

empty_list = []

# Using list():

numbers = list((1, 2, 3))

# You can also create a list from a string:

letters = list("Python")

print(letters)

# Index:      0        1       2
#             ↓        ↓       ↓
#           Python   Java     C++

# Negative:  -3       -2      -1

# Lists are mutable, meaning their contents can be changed.
# This is one major difference between list and tuple.


# Adding Elements
# append()
# Adds one element to the end.


# insert()
# Adds an element at a specific position.

numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)

#list.insert(index, value)


# extend()
# Adds multiple elements.

numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)


# append() vs extend()
numbers = [1, 2]
numbers.append([3, 4])
print(numbers)

# Result:
# [1, 2, [3, 4]]

# Whereas:

numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)

# Result:
# [1, 2, 3, 4]

# append() adds one object.
# extend() adds elements from an iterable.


# Removing Elements
# remove()
# Removes a specific value.

numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)

# Output:
# [10, 30]
# If the value doesn't exist, remove() raises an error.


# pop()
# Removes an element using its index and returns that element.
# Python does not have a built-in push() method for lists

numbers = [10, 20, 30]
x = numbers.pop(1)

print(x)
print(numbers)

# Output:
# 20
# [10, 30]
# Without an index:
# numbers.pop()
# removes the last element.


# del
# You can also delete using del:

numbers = [10, 20, 30]
del numbers[1]
print(numbers)

# Result:
# [10, 30]


# clear()
# Removes everything:

numbers = [1, 2, 3]
numbers.clear()
print(numbers)



# List Slicing
# Slicing is extremely important in Python.
# Syntax:
# list[start:stop:step]
# Example:

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:
# [20, 30, 40]
# Remember: stop is excluded.


numbers[:3]
# First three elements.

numbers[2:]
# From index 2 to the end.

numbers[:]
# Entire list.

numbers[::2]
# Every second element.

numbers[::-1]
# Reverse the list.


# Length of a List
# Use len():



# Useful List Methods

# Method	Purpose
# append()	Add one element
# extend()	Add multiple elements
# insert()	Insert at position
# remove()	Remove by value
# pop()	Remove by index
# clear()	Remove everything
# sort()	Sort list
# reverse()	Reverse list
# index()	Find index of value
# count()	Count occurrences
# copy()	Copy list



# You can also get indexes:
test_cases = ["Login", "Logout", "Search"]
for index, test in enumerate(test_cases):
    print(index, test)

# Output:
# 0 Login
# 1 Logout
# 2 Search
# enumerate() is worth knowing.


# Using list comprehension:

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

# With a condition:

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)