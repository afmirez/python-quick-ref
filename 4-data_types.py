
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

# *** String Data Type ***
# Declared with "" or '' and are immutable. Any "change" really returns a brand new string.
message = 'Welcome to the Grand Line'

# Class type: str (the treasure chest of characters)
print(type(message))

# Accessing characters
print(message[1])  
print(message[-1])

# Muliline strings
logbook = '''
    You will see
    that new lines
    are preserved!
'''

# Slicing
print(message[1:3])   
print(message[3:])   
print(message[:3])    
print(message[::-1])  # Reverse string

# Iterating a string
for character in message:
    print(character)

# Delete a string
del logbook

#  Updating strings (actually new ones!)
new_message = "WW" + message[1:]                  
greeting = message.replace("Welcome", "Hello")  

# Concatenation
farewell = "... Bye bye"
print(message + " " + farewell)
print(message, " ", farewell)

# Repetition
print(message * 3) 

# String formatting
villain = "Crocodile"
print(f"I will fight {villain}!")                
print("I will fight {} {}!".format(villain, "tomorrow"))

# Membership testing
print("Cro" in villain) 

# Common string methods
print(len(message))        # Get length of string
new_message.upper()        # Return uppercase (original unchanged)
new_message.lower()        # Return lowercase (original unchanged)
crew_member = "  Zoro  "
crew_member.strip()        # Remove leading/trailing spaces (original unchanged)



# *** List Data Type ***
# Ordered and mutable collection of items. It allows duplicates, is index-based 
# (from 0), and can hold mixed data types.
crew = []  
fruits = ['apple', 'banana', 'cherry']  
mixed_treasure = [1, 'One Piece', 3.14, True]  
numbers = [2] * 5 # Create a list with repeated items.
strawhats = [
    ["Luffy", "Zoro", "Nami"],        
    ["Usopp", "Sanji", "Chopper"],    
    ["Robin", "Franky", "Brook", "Jinbe"]  
]

# List comprehension : one-line way to build/filter lists, useful for quick transforms
squares = [x**2 for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]

# Accesing elements
print(fruits[0])
print(mixed_treasure[-1])

# Removing elements
numbers.remove(2) # Removes the first occurrence of an element.
numbers.pop() # # Removes item at index, or last if none given
numbers.clear()  # Remove elements

# Adding elements into list
fruits.append("pear") #  Adds an element at the end of the list.
fruits.extend(['orange', 'pineapple']) # Adds multiple elements to the end of the list.
fruits.insert(1, 'grape') # Adds an element at a specific position.

# Updating elements
fruits[0] = "kiwi"

# Itearating over lists
for fruit in fruits:
    print(fruit)



# *** Tuple Data Type ***
# Tuple is an ordered collection of Python objects. Tuples are immutable.
empty_island = ()  
numbers_tuple = (1, 2, 3)  
mixed_loot = (1, "Map", 3.14, "Gold")  
repeated_crew = ("Luffy",) * 3  # Create a tuple  with repeated items.

# Deleting tuple
del empty_island

# Accesing elements
print(mixed_loot[0])

# Slicing
print(mixed_loot[1:])
print(mixed_loot[0:2])
print(mixed_loot[::-1]) # Reverse tuple

# Concanetation
mix_tuple = numbers_tuple + mixed_loot

#------------------------------------------------------------------------------#
# Boolean Data Type
# Built-in data type: True or False
print(type(True))
print(type(False))

#------------------------------------------------------------------------------#
# Set Data Type
# Set is an unordered collection (no guaranteed order when printed) of data types 
# that is iterable, mutable, and has no duplicate elements (duplicate values are removed).
islands = set()                 # Empty set
islands = set("GrandLine")      # Create from string → unique letters only
treasures = set(["Gold", "Map", "Sword", "Sword"])  # Create from list → duplicate removed

# Adding elements
treasures.add("Compass")   
treasures.update(["Log Pose", "Treasure Chest"]) # Add multiple elements

# Iteating over a set / Accessing a Set
for element in treasures:
    print(element, end= " ")

# Removing elements
treasures.remove("Map")      # Remove specific item (error if not found)
treasures.discard("Sword")   # Remove specific item (no error if not found)
treasures.pop()              # Remove a random item 
treasures.clear()            # Remove all items

#------------------------------------------------------------------------------#
# Dictionary Data Type
# Collection of data values, used to store data values like a map. We have 
# key-value pairs.
# Values can be of any type, keys cannot be repeated.
pirate_profile = {}  
pirate_profile = {
    'name': "Monkey D. Luffy",
    'age': 19,
    'bounty': 1500000000,
    1: ':)'
}

# Accessing items
print(pirate_profile['name'])
print(pirate_profile.get(1))

# Adding items
pirate_profile["brother"] = "Portgas D. Ace"

# Updating items
pirate_profile["brother"] = "Ace"

# Iterating over a dictionary
for key in pirate_profile:  # Iterate over keys
    print(key)
for value in pirate_profile.values():  # Iterate over values
    print(value)
for key, value in pirate_profile.items():  # Iterate over key-value pairs
    print(f"{key}: {value}")

# Removing elements
del pirate_profile["age"] # Remove by key
pirate_profile.pop("brother") # Remove and return value by key
pirate_profile.popitem() # Remove and return the last key-value pair
pirate_profile.clear() # Clear all items (empty dictionary)