# mutable 

# list
# set
# dictionary

# -------------------

# immutable

# tuple
# string
# number
# boolean


h1 = [1,2,3]
h2 = h1

print(h1)
print(h2)

h1[0] = 100   # here list is mutable 

print(h1)
print(h2)

import copy

h1 = [5,6,7]
h2 = copy.copy(h1)  # we acn create deep and shalow copy as well

print(h1)
print(h2)

h1[0] = 100   # here list is mutable 

print(h1)
print(h2)
