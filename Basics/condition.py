# Conditions

# A condition evaluates to either:
# True
# or:
# False



# if Statement

# The simplest conditional statement is if.
# Syntax
# if condition:
#     # code to execute

# Example:
age = 22
if age >= 18:
    print("Adult")

# Notice the : after the condition.
# Also notice the indentation.
# Python uses indentation to determine which statements
# belong to the if block.



# if-else

# Sometimes you want one block to execute when the condition
# is true and another when it's false.

age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")



# if-elif-else

# When there are multiple possible conditions, use elif.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")

# Python checks the conditions from top to bottom.
# Once one condition is True,
# its block executes and the remaining elif/else blocks are skipped.



# Multiple Conditions
# You can combine conditions using:

# and
# or
# not


# and
# Both conditions must be true.

age = 22
has_id = True

if age >= 18 and has_id:
    print("Allowed")

# or
# At least one condition must be true.

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")

# not
# Reverses the condition.

is_logged_in = False

if not is_logged_in:
    print("Please log in")



# Nested Conditions
# An if statement can exist inside another if.

age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# This is called a nested if.
# However, you can often simplify it:

if age >= 18 and has_id:
    print("Entry allowed")

# Use whichever makes the logic clearer.



# Python's Truthy and Falsy Values
# Python doesn't require a condition to literally be True or False.

# These are commonly falsy:

# False
# None
# 0
# 0.0
# ""
# []
# ()
# {}
# set()


# Conditional Expression / Ternary Operator
# Python allows a short form of if-else.

age = 22

result = "Adult" if age >= 18 else "Minor"

# This is called a conditional expression.
# Use it for simple conditions. Don't cram complicated logic into it.