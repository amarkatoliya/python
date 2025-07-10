# default parameter if not provided

def greet(name = "User"): # if value is given then default
    return "Hello, " + name + "!"

print(greet('Amar'))
print(greet())