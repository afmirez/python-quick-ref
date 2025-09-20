# A variable is a name bound to a value (i.e., an object reference).
# Python is dynamically typed: types are inferred at runtime and variables can change types during execution.

earthAge = "4.54 billion years old"  # String
earthAge = 45000000000000            # Later reassigned as int

#------------------------------------------------------------------------------#
# Variable Naming Rules:
#   Must begin with a letter (A–Z, a–z) or an underscore _
#   Can contain letters, digits (0–9), and underscores
#   Case-sensitive (Age and age are different)
#   Avoid Python keywords (if, class, def, etc.)

#------------------------------------------------------------------------------#
# Multiple Assignments
# Assigning the same value to multiple variables:
a = b = c = 100
# Assigning different values in one line:
x, y, z = 1, 2.5, "Python"


#------------------------------------------------------------------------------#
# Type Casting: Converting one type to another using built-in functions
s = "10"
n = int(s)      # str → int

cnt = 5
f = float(cnt)  # int → float

age = 25
s2 = str(age)   # int → str

#------------------------------------------------------------------------------#
# Getting the Type of a Variable
print(type(earthAge))  # Shows current type of earthAge

#------------------------------------------------------------------------------#
# Object References in Python
# Variables reference objects, they don’t hold the actual value.
# Reassigning one variable doesn't affect another referencing the same value:
one = 1
two = one     # both point to same object initially
one = 5       # 'one' now points to a new object
print("one:", one, "two:", two)  # two is still 1

#------------------------------------------------------------------------------#
# Deleting a Variable
del one
# print(one) → NameError if used after deletion

#------------------------------------------------------------------------------#
# Swapping Two Variables@
a, b = 5, 10
a, b = b, a  # Swap values
