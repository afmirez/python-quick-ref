# Operators are used to perform operations on values and variables.

#------------------------------------------------------------------------------#
# Arithmetic Operators
# Used to perform basic mathematical operations like addition, subtraction, 
# multiplication and division.

a = 15
b = 4

# Addition:
print("Addition:", a + b)  
# Subtraction:
print("Subtraction:", a - b) 
# Multiplication:
print("Multiplication:", a * b)  
# Division:
print("Division:", a / b) 
# Floor Division:
print("Floor Division:", a // b)  
# Modulus:
print("Modulus:", a % b) 
# Exponentiation:
print("Exponentiation:", a ** b)

#------------------------------------------------------------------------------#
# Comparison Operators
# Compare values. It either returns True or False according 
# to the condition.

a = 13
b = 33

# Greater Than:
print(a > b)
# Less Than:
print(a < b)
# Equals to:
print(a == b)
# NOT equals to:
print(a != b)
# Greater OR equals to:
print(a >= b)
# Less OR equals to:
print(a <= b)

#------------------------------------------------------------------------------#
# Logical Operators
# Used to combine conditional statements. Precendece:
#   1. Logical not
#   2. Logical and
#   3. Logical or

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#------------------------------------------------------------------------------#
# Assignment Operators
# This operator is used to assign the value of the right side  of the expression 
# to the left side operand.
a = 10
b = a

print(b)

# Adds 'a' to 'b' and assigns the result to 'b' → b = b + a
b += a
print(b)
# Subtracts 'a' from 'b' → b = b - a
b -= a
print(b)
# Multiplies 'b' by 'a' → b = b * a
b *= a
print(b)
# Left shifts the bits of 'b' by 'a' positions → b = b << a
b <<= a
print(b)

#------------------------------------------------------------------------------#
# Indentity Operators
# is and is not are the identity operators both are used to check if two values 
# are located on the same part of the memory. 
# Two variables that are equal do not imply that they are identical. 

a = 1000
b = 2000
c = a

print(a is not b) # True if the operands are not identical 
print(a is c) # True if the operands are identical 

#------------------------------------------------------------------------------#
# Membership Operators
# in and not in are the membership operators that are used to test whether a value
# or variable is in a sequence.

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#------------------------------------------------------------------------------#
# Ternery Operator
# One-line conditional expression that returns one value if a condition is true 
# and another if it's false.
adult = True 
isAdult = True if a else False