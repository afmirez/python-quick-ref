# Loops
# Used to repeat actions efficiently.

#------------------------------------------------------------------------------#
# 'for' loop
# Iterate over a sequence such as a list, tuple, string or range
times = 5
for i in range(0,times):
    print('i is: ', i)

favoriteAnimes = ['One Piece', 'Hunter X Hunter', 'Fullmetal Alchemist']
for anime in favoriteAnimes:
    print('One of my favorite anime is: ', anime)

for index in range(len(favoriteAnimes)):
    print('One of my favorite anime is: ', favoriteAnimes[index], ', and its index is: ', index)

#------------------------------------------------------------------------------#
# 'while' loop
#  Execute a block of statements repeatedly until a given condition is satisfied
eatenTacos = 0
while (eatenTacos < 5):
    print('I am still hungry')
    eatenTacos+=1
else:
    print("I am done!")

# Infinite Loop
# Use the condition 'True' to run the block code until you break out using 'break' or
# some other logic
# while (True):
#     print("Uncomment this if you want to see an infinite loop!")

#------------------------------------------------------------------------------#
# Nested Loops
# Loop inside another loop 
arrayOfPowerArrays = [
    ["Gomu Gomu no Pistol", "Gear Second", "Gear Third"],
    ["Haki Observation", "Haki Armament", "Haki Conqueror"],
    ["Gear Fourth: Boundman", "Gear Fourth: Snakeman", "Gear Fifth: Nika"]
]

for i, array in enumerate(arrayOfPowerArrays, start=1):
    print(f"Power Set {i}:")
    for element in array:
        print(f"  - {element}")
    print()  # Empty line between sets

#------------------------------------------------------------------------------#
# Loop Control Statements
# Change execution from their normal sequence.
# When execution leaves a scope, all automatic objects that were created in that 
# scope are destroyed.

characters = [
    "Monkey D. Luffy",   # Hero
    "Roronoa Zoro",      # Hero
    "Donquixote Doflamingo",  # Villain
    "Crocodile"               # Villain
]

# 'continue' returns the control to the beginning of the loop.
for character in characters:
    if (character == "Monkey D. Luffy" or character == "Roronoa Zoro"):
        continue
    print("This is a villian: ", character)

# 'break' brings control out of the loop.
for character in characters:
    if (character == "Monkey D. Luffy" or character == "Roronoa Zoro"):
        break
    print("This is a villian: ", character) # We will not see anything printed

# 'pass' is used when a statement is syntactically required but no action is needed
for character in characters:
    if character == "Crocodile":
        pass  # Placeholder for future logic, does nothing now
    else:
        print("Processing character:", character)
        