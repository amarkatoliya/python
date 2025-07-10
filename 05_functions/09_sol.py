# fun with the yeild

value = int(input("Enter num: "))
def even_generator(value):
    for i in range(2, int(value) + 1, 2):
        yield i    # yield insted of return
    
    
# print(even_generator(10))  it's not gone work here

for num in even_generator(value):
    print(num)