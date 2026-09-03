# Collections in Python
# Collections are data structures used to store multiple values together.
# Python's main built-in collections are:

numbers = [10, 20, 30]          # List
point = (10, 20, 30)            # Tuple
unique = {10, 20, 30}           # Set
user = {"name": "Om", "age": 22} # Dictionary

# Python's collections module
# These four are from Python's collections module. Think of them
# as specialized versions of normal Python data structures.

# You want to know how many times each number appears.
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]

count = Counter(numbers)

print(count)

# gives a dictionary with key as the elements and value as their 
# number of occurance



# With defaultdict, you can specify what to give when a key
# doesn't exist.

from collections import defaultdict
data = defaultdict(int)
print(data["count"])

# int produces 0

# Another useful example
# Suppose you want to group names by department:

from collections import defaultdict

employees = defaultdict(list)

employees["QA"].append("John")
employees["QA"].append("Sarah")
employees["Dev"].append("Mike")

print(employees)

# Output:
# {
#     "QA": ["John", "Sarah"],
#     "Dev": ["Mike"]
# }


# deque → efficient queue
# deque means double-ended queue.
# It allows you to efficiently add/remove items from both ends.

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")
queue.appendleft("Z")

print(queue)

queue.pop()
queue.popleft()

queue.extend(["1","2","3"])
queue.extendleft(["4","5","6"])


# With normal tuple you have to remember what 0, 1, 2 mean.
# With namedtuple:

from collections import namedtuple

Users=namedtuple("Users",["name","age","role"])
user = Users("om",22,"QA")
print(user.name)
print(user.age)
print(user.role)

# since it is a tuple its still immutable