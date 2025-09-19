

import random

#  Functions
# Block of statements that does a specific task.
# The def keyword stands for define and is used to create a user-defined 
# function. 
def initExplosiveTag():
    print("💣 BOOM! Paper Bomb Activated!")
initExplosiveTag()

# Passing arguments
def initJutsu(jutsuName):
    print("🔥 Ninja unleashes:", jutsuName)
initJutsu("Fire Style: Fireball Jutsu!")

# Use 'pass' when you want to define a function but its logic is not defined yet
def initAttack():
    pass
#------------------------------------------------------------------------------#
# Functions are first-class objects. You can:

# 1. Assign a function to a variable
def rasengan():
    print("Naruto uses Rasengan!")
jutsu = rasengan  
jutsu()   

# 2. Pass a function as an argument
def useJutsu(jutsuFn):
    print("Preparing jutsu...")
    jutsuFn()
useJutsu(rasengan)

# 3. Return a function to another function
def getUltimateJutsu():
    def susanoo():
        print("Sasuke summons Susanoo!")
    return susanoo
ultimate = getUltimateJutsu()
ultimate()

# 4. Store functions in a data structure
def chidori():
    print("Sasuke uses Chidori!")
def shadowClone():
    print("Naruto uses Shadow Clone Jutsu!")
jutsus = [rasengan, chidori, shadowClone]
for j in jutsus:
    j()

#------------------------------------------------------------------------------#
# Global and Local Variables 

# Local Variables
# Exist only inside a function and are inaccessible from outside it.
def greetAnInnerBiju():
    biju = 'Kurama'
    print('Hello', biju)
# print(biju)  # Error: biju is not defined outside the function

# Global Variables
# Defined outside functions and accessible everywhere.
anime = 'Naruto Shippuden'
def printAnime():
    print('I am watching :', anime)
printAnime()
print('My favorite anime is: ', anime)

#------------------------------------------------------------------------------#
# Types of function arguments

# Default arguments
def throwKunai(target, number=3):
    print(f"🎯 Throwing {number} kunai at {target}!")
throwKunai("Enemy Ninja")

# Positional Arguments
# Values are assigned to parameters based on their order in the function call.
def ninjaIntro(name, rank):
    print(f"I am {name}, a {rank}-level shinobi.")
ninjaIntro("Kakashi", "Jonin")

# Keyword Arguments 
# values are passed by explicitly specifying the parameter names, 
# so the order doesn’t matter.
ninjaIntro(rank="Genin", name="Naruto") 

# Arbitraty Arguments
# *args and **kwargs can pass a variable number of arguments to a function using 
# special symbols.
def summonNinjas(*ninjas, **jutsus):
    print("🍥 Summoned Ninjas (*args):")
    for ninja in ninjas:
        print(f"- {ninja}")
    
    print("\n🌀 Secret Jutsus Used (**kwargs):")
    for key, jutsu in jutsus.items():
        print(f"{key} => {jutsu}")


summonNinjas(
    'Naruto', 'Sasuke', 'Sakura', 
    jutsu1='Rasengan', 
    jutsu2='Chidori', 
    jutsu3='Strength of a Hundred Seal',
    ultimateJutsu='Perfect Susanoo'
)

#------------------------------------------------------------------------------#
# Return statement
# Ends a function and sends a value back to the caller. It can return any 
# data type
def chakraAmplification(chakra_level):
    """This jutsu amplifies the chakra level 
    by squaring its power!"""
    return chakra_level ** 2
print("Amplified Chakra:", chakraAmplification(8))

#------------------------------------------------------------------------------#
# Pass by Reference and Pass by Value
# Variables are references to objects. When passed to functions:
#  - Mutable objects (lists, dictionaries): modifications inside the 
#    function affect the original object.
#  - Immutable objects (integers, strings, tuples): modifications inside 
#    the function do not affect the original object.
def boostFirstChakra(chakra_levels):
    chakra_levels[0] = 20 
team_chakra = [10, 11, 12, 13]
boostFirstChakra(team_chakra) # List is modified

def boostSingleChakra(chakra):
    chakra = 20
naruto_chakra = 10
boostSingleChakra(naruto_chakra) # Value is not modified

#------------------------------------------------------------------------------#
# Nested and Anonymous Functions

# Function whiting functions
enemies = ["Orochimaru", "Madara Uchiha", "Pain"]
def figthRandomEnemy():
    randomIndex = random.randint(0, len(enemies) - 1)
    selectedEnemy = enemies[randomIndex]
    def printFight():
        print("You will figth with: ", selectedEnemy)
    printFight()
figthRandomEnemy()

# Anonymous Functions
# Function without a name. The lambda keyword is used to create anonymous
# functions.
chakraBoost_l = lambda power: power * power * power
print("⚡ Chakra Boost (lambda):", chakraBoost_l(7))

#------------------------------------------------------------------------------#
# Decorators
# Functions that extend or modify the behavior of other functions, methods, or classes,
# without altering their original code.
# They take a function as input, wrap it with extra functionality, and return it.
# Common uses: Logging, Auth, Rate Limiting, Caching, Retry.
def logAttack (attackFn):
    def wrapper(*args, **kwargs):
        print(f"Calling attack function: {attackFn.__name__}...")
        result = attackFn(*args, **kwargs)
        print(f"Function : {attackFn.__name__} finished...")
    return wrapper
@logAttack
def throwPunches(times):
    print(f"Throwing {times} punches")
throwPunches(5)


validRanges = ["Genin", "Chūnin", "Jōnin"]
def requires_range(allowed_ranges):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user["range"] not in allowed_ranges:
                print(f"You can not fight!")
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator
@requires_range(validRanges)
def figthEnemy(user):
    print(f"{user['name']} is fighting an enemy!")
user_valid = {
    "name": "Naruto Uzumaki",
    "range": "Genin"
}
user_invalid = {
    "name": "Konohamaru Sarutobi",
    "range": "Academy Student"
}
fightEnemy(user_valid)   
fightEnemy(user_invalid) 

# TO-DO: Consider to move this to the classes section
# Built-in decorators 
# Built-in decorators for classes that adjust method/attribute behavior:

# - @staticmethod: Defines a method bound to the class, not its instance.
class NinjaTools:
    @staticmethod
    def kunai_count(a, b):
        return a + b
res = NinjaTools.kunai_count(5, 3)

# - @classmethod: Defines a method bound to the class, receiving cls as first arg.
class Ninja:
    village = "Konoha"

    @classmethod
    def from_name(cls, name):
        return cls(name)

    def __init__(self, name):
        self.name = name
naruto = Ninja.from_name("Naruto")
print(naruto.name, naruto.village) 

# - @property: Turns a method into a read-only attribute (can add setter/deleter).
class Ninja:
    def __init__(self, name, missions):
        self.name = name
        self._missions = missions

    @property
    def rank(self):
        return "Genin" if self._missions < 10 else "Chunin"

naruto = Ninja("Naruto", 7)
print(naruto.name, naruto.rank)