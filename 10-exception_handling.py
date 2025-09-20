# Exception Handling
# Mechanism to handle runtime errors gracefully without crashing the program.

# Risky code
try:
    clones = 0
    chakra = 100 / clones
# Handle specific error: division by zero.
except ZeroDivisionError:
    print("Naruto: Can't divide chakra with zero clones!")
# Handle invalid value errors.
except ValueError:
    print("Invalid value provided.")
# Catch-all for any other exception type.
except:
    print("Unexpected error occurred.")
# Executes only if no exception is raised in try block.
else:
    print("Chakra distributed successfully:", chakra)
# Always executes regardless of what happens.
finally:
    print("Training session ended.\n")

#------------------------------------------------------------------------------#
# Raising an exception
def summon_jutsu(chakra):
    if chakra < 0:
        raise ValueError("Chakra cannot be negative.")
    print(f"Jutsu summoned with {chakra} chakra points.")

try:
    summon_jutsu(-10)
except ValueError as e:
    print("Error:", e, "\n")

#------------------------------------------------------------------------------#
# Custom exceptions
# Create a new class that inherits from Python’s built-in Exception class.
class ChakraError(Exception):
    def __init__(self, value, msg="Chakra cannot be negative!"):
        self.value = value
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self):
        return f'{self.value} -> {self.msg}'

def summon_jutsu(chakra):
    if chakra < 0:
        raise ChakraError(chakra)
    print(f"Jutsu summoned with {chakra} chakra points.")

try:
    summon_jutsu(-20)
except ChakraError as e:
    print("Error:", e)

#------------------------------------------------------------------------------#
# Built-in Exceptions: https://www.w3schools.com/python/python_ref_exceptions.asp