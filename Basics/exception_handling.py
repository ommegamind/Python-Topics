# Exception handling is the mechanism Python provides to detect and 
# handle runtime errors without abruptly terminating the program.

#compile time error: 
#What it is: Violating the basic grammar rules of Python.Examples: 
# Forgetting a colon (:) at the end of an if statement,
# or mixing up your spacing (indentation).

#runtime errors:
#  Trying to divide a number by zero (10 / 0), 
# or trying to open a file that doesn't exist on your computer.


# Because Python must read and translate your entire file into 
# instructions before running it, a compile-time error stops everything 
# immediately. Python refuses to start the engine, so it never
# reaches the try...except box.You can only catch a runtime exception 
# because the engine is already running when it hits the bump.


# What is an Exception?
# An exception is an error that occurs while a Python
# program is running.
# Example:

a = 10
b = 0
result = a / b

# Python raises:
# ZeroDivisionError: division by zero

numbers = [10, 20, 30]

print(numbers[5])

# There is no index 5, so Python raises:
# IndexError: list index out of range


# Syntax error
# The Python code itself is invalid.

# if True
#     print("Hello")

# Python can't understand the syntax.

# Exception
# The syntax is valid, but something goes wrong during execution.

x = 10 / 0

# The code is syntactically valid, but execution produces 
# ZeroDivisionError.

# try and except
# The basic exception-handling structure is:

# try:
#     # code that might fail
# except:
#     # code to handle the error


# Catching a Specific Exception
# You should generally catch specific exceptions instead of using 
# a completely generic except.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# This is better because you're explicitly saying what
# problem you expect.
# Another example:

numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Invalid index")


# Multiple Exceptions
# You can handle different exceptions separately.

try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")


# Multiple Exceptions With One except
# If you want the same handling for multiple exceptions:

try:
    pass
except (ValueError, TypeError):
    print("Invalid data")

# else-----------
# Python also provides else with exception handling.

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division failed")

else:
    print("Division successful")

# Output:
# Division successful
# When does else execute?
# else executes only when the try block succeeds without an exception.

# finally
# finally executes regardless of whether an exception occurs or not.

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Error occurred")

finally:
    print("Execution completed")

# Why finally Is Useful
# finally is commonly used for cleanup operations.
# closing an opened file 

# raise
# Sometimes you want to manually generate an exception.
# Python provides raise.

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# Getting the Exception Message
# You can store the exception in a variable using as.

try:
    number = int("abc")

except ValueError as error:
    print(error)

# You can also inspect its type:

try:
    number = int("abc")

except Exception as error:
    print(type(error))
    print(error)

#good
try:
    pass

except ValueError:
    print("Value error")

except Exception:
    print("Some other error")

# The specific exception should come before the general one.

# Bad:

# try:
#     pass

# except Exception:
#     print("General error")

# except ValueError:
#     print("Value error")

# The ValueError handler becomes unreachable 
# for a ValueError, because Exception catches it first.


# Custom Exceptions
# You can create your own exception class.

class LoginFailedError(Exception):
    pass

# Then:

raise LoginFailedError("Login failed")

# Context Managers: with
# You'll often see:

with open("data.txt", "r") as file:
    data = file.read()

# Instead of manually doing:

file = open("data.txt", "r")

try:
    data = file.read()

finally:
    file.close()

# The with statement automatically handles resource cleanup.
# This isn't exactly exception handling itself, 
# but it is closely related and useful to know.


# The basic pattern:

# try:
#     # risky code

# except SpecificException as error:
#     # handle error

# else:
#     # executes if no exception

# finally:
#     # always executes


# BaseException is the top-level/base class for Python's exceptions.
# It includes things like:

# SystemExit → program is being exited
# KeyboardInterrupt → you press Ctrl+C
# GeneratorExit
# Exception → normal application/runtime errors

# You generally don't catch BaseException yourself.
# If you press Ctrl+C, Python normally stops the program.
# But except BaseException can catch that Ctrl+C and run:

# print("Error!")

# So you're basically saying:
# "Even if the user tries to stop the program, catch that too."
# That's usually not what you want.

# So remember:
# except Exception:
# "Catch normal errors."

# except BaseException:
# "Catch basically EVERYTHING, "
# "including signals that are supposed to stop the program."


# Exception is the base class for normal runtime
#  errors that applications generally want to handle.
# you're basically saying:
# "Catch almost any normal runtime exception."

#with raise
try:
    login()

except Exception as error:
    print(f"Login failed: {error}")
    raise

# "I caught this exception, but I don't want to swallow it."
# "Raise the same exception again."
# This is called re-raising the exception.