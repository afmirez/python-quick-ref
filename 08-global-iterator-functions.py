from functools import reduce

# Global Iterator Functions
# built-in higher-order functions that operate on iterables such as lists, 
# tuples, sets, dictionaries, strings, or any custom object that implements 
# the iterator protocol (__iter__ and __next__).

# In Python 3, map() and filter() return lazy iterators, not collections.
# To see results, consume them with list(), tuple(), set(), or a for-loop.

#------------------------------------------------------------------------------#
# Map
# Applies a given function to each element of an iterable and returns a map object.
def double_bounty(val):
    return val * 2
bounties = [100, 200, 300, 400]    
res = list(map(double_bounty, bounties))

# Using lambda
res_lbd = list(map(lambda x : x * 2, bounties))

#------------------------------------------------------------------------------#
# Reduce
# Applies a function cumulatively to an iterable, returning a single value.
# Common uses: sum, product, max/min, string concat, list flattening.
# Provided by functools, so it must be imported first.
def add_power(x, y):
    return x + y
luffys_crew_power = [1, 2, 3, 4, 5]
res = list(reduce(add_power, crew_power))
print(f"Total Straw Hat crew power: {res}")

# Using lambda
res_lbd = list(reduce(lambda x, y: x + y, luffys_crew_power))

# Using a initializer
res_lbd_plus_ten = list(reduce(lambda x, y: x + y, luffys_crew_power, 10))

#------------------------------------------------------------------------------#
# Filter
# Extract elements from an iterable (like a list, tuple or set) that satisfy 
# a given condition. 
def starts_with_z(name):
    return name.startswith("Z")
crew = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Zunesha"]
res = list(filter(starts_with_z, crew))

# Using lambda
res_lbd = list(filter(lambda x : x.startswith("Z"), crew))