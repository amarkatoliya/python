n = [1,3,6]
m = n

print(n)
print(m)

print(m == n)

print(m is n) #true

# now we give explicitly
n = [1,3,6]
m = [1,3,6]

print(n)
print(m)

print(m == n)

print(m is n) #false    # because is comparing the memory location
