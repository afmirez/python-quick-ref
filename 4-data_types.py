
# In Python, data types classify values and determine what operations can be 
# performed on them. Since everything in Python is an object, data types are 
# classes and variables are instances of those classes.

#------------------------------------------------------------------------------#
# Numeric Data Types

# Integers: Positive or negative whole numbers. No length limit.
a = 5
print(type(a))

# Float: It is a real number with a floating-point representation. It is specified 
# by a decimal point.
b = 5.0
print(type(b))

# Complex Numbers: It is represented by a complex class. It is specified as 
# (real part) + (imaginary part)j.
c = 2 + 4j
print(type(c))

#------------------------------------------------------------------------------#
# Sequence Data Types
# Ordered collection of items, which can be of similar or different data types. 

# String Data Type
s = 'Welcome to the Geeks World'
print(type(s)) # It is represented by str class.
print(s[1])
print(s[-1])

# List Data Type
# Ordered and mutable collection of items. Items can be of different types.
a = []
a = [1,2,3]
b = [1, "Two", 3, "Four"]
print(a[0])
print(b[-1])

# Tuple Data Type
# Tuple is an ordered collection of Python objects. Tuples are immutable.
tup1 = ()
tup2 = (1,2,3)
tup2 = (1,"two",3)
print(tup2[0])

#------------------------------------------------------------------------------#
# Boolean Data Type
# Built-in data type: True or False
print(type(True))
print(type(False))

#------------------------------------------------------------------------------#
# Set Data Type
# Set is an unordered collection (no guaranteed order when printed) of data types 
# that is iterable, mutable, and has no duplicate elements (duplicate values are removed).
s1 = set()
s1 = set("TheseAreMyNotes")
print("Set with the use of String: ", s1) 
s2 = set(["I", "Like", "Pizza", "Pizza"])
print("Set with the use of List: ", s2) 

for element in s2:
    print(element, end= " ")

print("Pizza" in s2)

#------------------------------------------------------------------------------#
# Dictionary Data Type
# Collection of data values, used to store data values like a map. We have 
# key-value pairs.
# Values can be of any type, keys cannot be repeated.
d = {}
d = {
    'name': "Monkey D' Luffy",
    'age': 19,
    'bounty': 1500000000,
    1 : ':)'
}
print(d['name'])
print(d.get(1))
