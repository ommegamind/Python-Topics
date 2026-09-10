# What is vectorization?
# AI and ML 
# Vectorization means converting data, code operations, 
# or graphics into a numerical or geometric format that 
# computers can process more efficiently

# Code vectorization
# Running a single instruction on multiple data items
#  at the exact same time instead of looping through items one by one.


import numpy as np
# NumPy makes mathematical operations much easier.

numbers= np.array([10,20,30,40])
print(numbers)
print(numbers*2)
# With a normal Python list, numbers * 2 
# would repeat the list rather than multiply each number.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)
# This becomes very important when working with Pandas, 
# data science, and machine learning.

print(arr.ndim)
print(arr.shape)
print(arr.size)

# ndim → number of dimensions → 1D
# shape → size of each dimension → 4 elements
# size → total number of elements → 4

print(arr.dtype)
# dtype means data type.
# It tells you what kind of data is stored inside a NumPy array.

# NumPy dtype	Meaning	     Example
# int64	       Integer	       10
# float64	Decimal number	   10.5
# bool	      True/False	   True
# str/Unicode	Text	       "Hello"

arr = np.array([1, 2, 3, 4], dtype=float)

print(arr)
print(arr.dtype)
# "Store these numbers as floating-point numbers."

# Why does dtype matter?
# Different data types use different amounts of memory 
# and have different numerical ranges.

np.array([1, 2, 3], dtype=np.int32)

# uses 32-bit integers, while:

np.array([1, 2, 3], dtype=np.int64)

# uses 64-bit integers.

# One important thing
# NumPy arrays generally prefer to have one consistent dtype.

# If you mix types:

arr = np.array([1, 2.5, 3])

# NumPy will generally convert the integers to floats

arr = np.array(["abc", 2])
print(arr)

# converts all to str 


# Indexing & Slicing in NumPy
# These are used to access specific elements or parts of an array.
# Slicing with a step
# Syntax:

# arr[start:stop:step]

# for 1D its the same as normal python list 

# for 2D array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0,0])



# Boolean masking means using True and False to filter an array.

arr = np.array([10, 20, 30, 40, 50])
mask = arr>20

print(mask)
print(arr[mask])
# That's boolean masking.

# also
print(arr[arr>20])
print(arr[arr==10])
print(arr[arr != 30])

print(arr[(arr > 20) & (arr < 50)])

# Important: with NumPy, use:
# & → AND
# | → OR
# ~ → NOT
# Don't use and / or for element-by-element NumPy conditions.


# Reshaping means changing the structure/dimensions of an array
# without changing its data.
# reshape() changes the dimensions of an array.

arr = np.array([1, 2, 3, 4, 5, 6])

arr=arr.reshape(2,3)

print(arr)

# Important rule
# The total number of elements must remain the same.
# arr=arr.reshape(2,3) wouldn't work

arr= arr.ravel()
# same for flatten()

print(arr)
# ravel gives a view, editing it, edits the original copy 
# whereas flatten return a copy to be used separately


# np.arange()
# Think: "Give me numbers with this step size."

ten= np.arange(1,11,2)
# end is excluded
print(ten)

# eg
np.arange(5)
# [0 1 2 3 4]

np.arange(2, 10)
# [2 3 4 5 6 7 8 9]

np.arange(0, 1, 0.2)
# [0.  0.2 0.4 0.6 0.8]


# np.linspace()
# Think: "Give me exactly this many numbers between two points."

four=np.linspace(0, 10, 5)
print(four)
# Here stop IS included by default.

# np.zeros()
# Creates an array where every value is 0.
zero= np.zeros(5)
print(zero)

# For a 2D array:
np.zeros((2, 3))

# np.ones()
# Same idea, but fills everything with 1.
one=np.ones(5)
print(one)

# np.full()
# Creates an array where every value is whatever you specify.
any=np.full(5,7)
print(any)

# 2D:
np.full((2, 3), 10)
# You can use strings too:
np.full(4, "Hello")

# np.random is used to generate random numbers. 
# It's useful in data science 
# for things like sampling, simulations, testing,
# and creating dummy data.

print(np.random.rand(5).round(2))
# .round(2) is for easy view
# 2D:
np.random.rand(2, 3)
# → 2 rows × 3 columns.

# np.random.randint()
# Generates random integers.
print(np.random.randint(1,10))
# generates single number
# Important: 10 is excluded.

print(np.random.randint(1,10,5))
# generates an array

print(np.random.randn(5))
# np.random.randn()
# Generates random numbers from a standard normal distribution.
# “Standard normal distribution” simply means:
# Most numbers will be close to 0, while some will be farther away from 0.

# np.random.choice()
# Randomly selects values from an array.

arr = np.array([10, 20, 30, 40, 50])
# np.random.choice(arr)
print(np.random.choice(arr, 3))

# The important thing is that NumPy performs the operation
# element by element:
# a = [10, 20, 30]
# b = [ 2,  4,  5]
# a + b
#     ↓
# [10+2, 20+4, 30+5]
#     ↓
# [12, 24, 35]


# You can also do math with a single number
# a + 5
# # [15 25 35]
# a * 2
# # [20 40 60]
# a - 3
# # [7 17 27]
# a / 10
# # [1. 2. 3.]
# a ** 2    # square each value
# a % 3     # remainder

# Remember
# NumPy arrays let you perform arithmetic on the
# whole array without writing a loop.

# Brodcasting
# NumPy treats it like:
# [10, 20, 30]
# + [ 5,  5,  5]
# --------------
# [15, 25, 35]
# The 5 is broadcast to every element.


# median()
# Finds the middle value after sorting.
# np.median(arr)

# mean()
# Finds the average.
# np.mean(arr)

# std()
# std() means standard deviation.
# It tells you roughly how spread out the values are from the mean.
# arr = np.array([10, 20, 30, 40, 50])
# np.std(arr)
# Output is approximately:
# 14.14
# Simple idea:
# Small std  → values are close together
# Large std  → values are more spread out

# var()
# var() means variance.
# It also measures how spread out the data is.
# np.var(arr)
# For [10, 20, 30, 40, 50]:
# 200.0
# Important relationship:
# variance = (standard deviation)²


# axis in NumPy
# axis tells NumPy which direction to perform an operation 
# on a multi-dimensional array.
# The key thing to memorize
# axis=0 → columns
# axis=1 → rows

arr= np.array([[10,20,30],[40,50,60]])
print(arr.sum(axis=1))

# np.where() is mainly used to find positions where a condition
# is True or choose values based on a condition.
print(np.where(arr>20))

# also used to choose between 2 values
print(np.where(arr%20==0, "even", "odd"))


# np.where() vs Boolean Masking
# You already learned masking:
# arr[arr > 25]
# This returns the actual values:
# [30 40]

# Whereas:
# np.where(arr > 25)
# returns their indices/positions:
# [2 4]

# np.concatenate()
# concatenate() joins arrays along an existing axis.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a,b)))
# With 2D arrays
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
# axis=0 → add rows
print(np.concatenate((a, b), axis=1))


# np.stack()
# stack() combines arrays by creating a new axis.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.stack((a, b),axis=1))

# With 2D arrays
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
print("new: ",np.stack((a,b),axis=1))
# stack() increases the number of dimensions.

# np.dot()
# dot() multiplies values and adds the results.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a,b))

# Matrix Multiplication
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
# We can multiply them using:
# np.matmul(A, B)
# or:
# A @ B
print(A@B)
# [1,2] and [5,7] and so on

# * is NOT matrix multiplication