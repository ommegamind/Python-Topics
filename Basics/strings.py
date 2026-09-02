# A string is a sequence of characters.

name = "Python"

# You can use:

# "Python"
# 'Python'

# String Indexing
# Just like lists, strings use zero-based indexing.

# String Slicing
# Strings support slicing too.

text = "Python"

print(text[0:3])


# Strings Are Immutable
# This is extremely important.
# You cannot directly change an individual character.

text = "Python"
text[0] = "J"

# This causes:
# TypeError


# So:

# List → mutable

x = [1, 2, 3]
x[0] = 100

# String → immutable

x = "abc"
x[0] = "x"  # Error


#string methods-------

#string.lower()
#string.upper()

# strip()
# Removes whitespace from the beginning and end.

# replace()
# text = "Hello World"
# text = text.replace("World", "Python")
# print(text)

# split()
# Converts a string into a list.

text = "Python Java C++"
languages = text.split()
print(languages)

# Output:
# ['Python', 'Java', 'C++']

# You can specify a separator:
text = "Python,Java,C++"
languages = text.split(",")
print(languages)

# join()
# Does the opposite: combines strings from an iterable.

languages = ["Python", "Java", "C++"]
result = ", ".join(languages)
print(result)


# Searching in Strings
# in

message = "Login successful"

if "successful" in message:
    print("Test passed")


# find() 

text = "Hello Python"
print(text.find("Python"))

# Output:
# 6

# If it doesn't find the substring:
text.find("Java")
# returns:
# -1


# count()
text = "banana"
print(text.count("a"))



# String Validation Methods


text.isalpha()
# Checks whether all characters are alphabetic.
text.isdigit()
# Checks whether all characters are digits.
text.isalnum()
# Checks whether characters are letters/numbers.
text.startswith("Py")
text.endswith("on")


# f-strings
# The preferred/simple approach:

username = "Om"
status = 200
message = f"User {username} received status {status}"


# Comparing Strings
username = "admin"

if username == "admin":
    print("Valid user")

# Python string comparison is case-sensitive: