#------------------------------------------------------------------------------#
# input() – Getting User Input
# Returns string by default — always.
# Use type casting (int(), float(), etc.) when working with numeric input.
# Use .split() to handle multiple space-separated values.

# Basic input — always returns a string
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# Multiple space-separated inputs (returns a list of strings)
names = input("Enter your top-three favorite artists: ").split()
print("Names:", names)

# Unpacking split input into multiple variables
fruitA, fruitB, fruitC = input("Enter your top-three favorite fruits: ").split()
print("Favorite fruits:", fruitA, fruitB, fruitC)

# Input must be cast to use as number
age = int(input("How old are you?: "))
print("You are", age, "and will be", age + 5, "in 5 years.")
price = float(input("How much does it cost?: "))
print("This costs", price)

#------------------------------------------------------------------------------#
# print() – Displaying Output
# Can take multiple arguments, automatically separated by spaces.
# Ends with a newline by default (customizable via end=).
# Accepts any object type (calls str() internally).
print("Hello, World!")
a, b, c = 1, 2, 3
print(a, b, c)  
