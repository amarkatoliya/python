# number presision is very good in python
import math

print(math.floor(2.5))
print(math.ceil(2.5))

# print(math.pi)
# print(math.e)

print(math.trunc(2.5)) # toward zero
print(math.trunc(-2.5))


#octal value
print(0o10)

# hexadecimal value
print(0x10)

# binary value
print(0b10)

# print(bin(10))
# print(oct(10))
# print(hex(10))

print(int('400', 8)) #octal
print(int('400', 16)) #hex
# print(int('4', 2)) #binary error

square = 2 ** 2
print(square)

root = 4 ** 0.5
print(root)

import random

print(random.random())

print(random.randint(1, 10))

li = ['lemon', 'apple', 'banana']
print(random.choice(li))

suffled_list = random.sample(li, 2)
print(suffled_list)

print((0.1 + 0.1 + 0.1) - 0.3) # known problem
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

import fractions

print(fractions.Fraction(1, 3) + fractions.Fraction(1, 3) + fractions.Fraction(1, 3) - fractions.Fraction(1, 3))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 | set2) #union
print(set1 & set2) #intersection

print(set1 - {1,2,3,4,5}) # set() == empty set

print(set1 ^ set2)

# boolean
print(type(True))
print(type(False))

print(True is 1)