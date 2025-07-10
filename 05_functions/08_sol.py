# fun **kwargs examples
def print_name(**kwargs):
    for key,value in kwargs.items():  #here item is neccessary
        print(f"{key}: {value}")

print_name(name="Amar", power ="Fly")
print_name(name="Lalu", )
print_name(name="Hitman", power ="Jump", enemy="Aaj tak paida nahi huaa")
