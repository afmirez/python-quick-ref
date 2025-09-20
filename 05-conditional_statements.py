# Conditional statements
# Used to execute certain blocks of code based on specific conditions

#------------------------------------------------------------------------------#
# 'if' Conditional Statement
# Executes a block of code if the given condition is true.
power = 10
if power >= 20:
    print("This villian is powerfull!")

# Short-hand if statement allows us to write a single-line if statement.
if power <= 19: 
    print("This villian is not too powerfull!")

#------------------------------------------------------------------------------#
# 'if else' Conditional Statement
# Specify a block of code that will execute if the condition(s) associated with 
# an if or elif statement evaluates to False
if power >= 20:
    print("This villian is powerfull!")
else:
    print("This villian is not too powerfull!")

# Short-hand if-else statement allows us to write a single-line if-else statement.
isVillianPowerfull = True if power >= 20 else False

#------------------------------------------------------------------------------#
# 'elif' statement
#  It allows us to check multiple conditions, providing a way to execute different blocks 
#  of code based on which condition is true.
if power >= 20:
    print("This villian is powerfull!")
elif power < 20 and power > 12:
    print("This villian is average!")
else:
    print("This villian is not too powerfull!")
    