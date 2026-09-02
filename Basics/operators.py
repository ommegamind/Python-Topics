# Arithmetic Operators--------
# Used for mathematical operations.

# Operator	Meaning	Example
# +	Addition	10 + 5
# -	Subtraction	10 - 5
# *	Multiplication	10 * 5
# /	Division	10 / 5
# //	Floor division	10 // 3
# %	Modulus/remainder	10 % 3
# **	Exponent	2 ** 3
# Examples

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

# Important: / vs //
# 10 / 3
# gives:
# 3.3333333333333335

# while:
# 10 // 3
# gives:
# 3

# // is floor division.

# For negative numbers, "floor" means rounding toward negative infinity:
# print(-10 // 3)
# Output:
# -4



# Comparison Operators---------
# Comparison operators compare values and return True or False.
# Operator	Meaning

# ==	Equal
# !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal
# <=	Less than or equal

# Very important: = vs ==
# = means assignment:
# x = 10

# == means comparison:
# x == 10


# Assignment Operators---------
# Basic assignment:
x = 10

# Python also supports compound assignment.
x += 5

# Equivalent to:
x = x + 5


# Logical Operators--------
# Used to combine conditions.
# Python has:

# and
# or
# not


# and
# Both conditions must be true.

# or
# At least one condition must be true.

# not
# Reverses a boolean result.


# Membership Operators---------
# Used to check whether a value exists inside a collection.
# Operators:
# in
# not in

# Example:
languages = ["Python", "Java", "JavaScript"]

print("Python" in languages)

print("C++" not in languages)

# Strings also support membership:

text = "Hello Python"

print("Python" in text)



# Identity Operators----------

# Python has:

# is
# is not

# They check whether two variables refer to the same object,
# rather than merely containing equal values.

# Example:

a = [1, 2, 3]
b = a

print(a is b)
# Output:
# True

# Both variables refer to the same list object.

# Compare that with:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
# Output:
# True
# False

# Important rule

# Use:
# is None
# rather than:
# == None

# Example:

# if result is None:



# Bitwise Operators---------

# These operate on individual binary bits.

# Operator	Meaning
# &	AND
# |	OR
# ^	XOR
# ~	NOT
# <<	Left shift
# >>	Right shift

a = 5
b = 3

print(a & b)

# Binary:
# 5 = 101
# 3 = 011

# 101
# 011
# ---
# 001 = 1


# operator precedence
# ()
# **
# *, /, //, %
# +, -
# comparisons
# not
# and
# or