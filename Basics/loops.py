# Loops

# A loop allows you to execute code repeatedly.

# Python mainly provides:
# for loop
# while loop


# A for loop is generally used when you want to iterate over a
# sequence/iterable.

# Example:

numbers = [10, 20, 30, 40]
for number in numbers:
    print(number)

# for Loop with Strings
# Strings are iterable too.

name = "Python"
for character in name:
    print(character)


# range()
# range() is extremely important with for loops.
# Generally:
# range(start, stop, step)
# stop is not inclusive



# while Loop
# A while loop repeats as long as a condition remains true.

# count = 1
# while count <= 5:
#     print(count)
#     count += 1



# break
# break immediately terminates a loop.

# continue
# continue skips the current iteration and moves to the next one.

# pass
# pass does nothing.
# It's essentially a placeholder.

# Unlike continue, pass does not skip the iteration.
# It simply means:
# Do nothing here.
# Useful when you want to leave a block empty temporarily.



# else with Loops
# Python has a slightly unusual feature: loops can have an else.

# With for
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Output:

# 0
# 1
# 2
# 3
# 4
# Loop completed

# The loop's else executes when the loop finishes normally.



# What happens with break? in loop to else.

for i in range(5):
    if i == 3:
        break

    print(i)
else:
    print("Loop completed")

# Output:

# 0
# 1
# 2

# The else does not execute because the loop
#  was terminated using break.


# Nested Loops
# A loop can contain another loop.
for i in range(3):
    for j in range(2):
        print(i, j)

