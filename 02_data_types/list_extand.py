tea_var = ["Green tea", "Black tea", "Oolong tea"]

print(tea_var)
print(tea_var[1:2])

tea_var[2] = "Masala tea"
print(tea_var)

tea_var[1:2] = "Lemon tea"
print(tea_var)

tea_var[1:2] = ["Lemon tea"]
print(tea_var)

tea_var[0:2] = ["1 tea", "2 tea"]
print(tea_var)

# print(tea_var[1:1])  # empty

# tea_var[1:1] = [" tea", " tea"]

tea_var[1:3] = [] #if empty assign then delete done

print(tea_var)

for tea in tea_var:
    print(tea,end="--")

if "Green tea" in  tea_var:
    print("Yes")

tea_var.append("Masala tea")    
print(tea_var)

tea_var.pop()  # remove last element also use remove


tea_var.insert(1,"Masala tea")

tea_var_copy = tea_var.copy() # create new list with diif memory location
print(tea_var_copy == tea_var)

square_nums = [x**2 for x in range(10)]
print(square_nums)
print(tea_var)

cube_num = [x**3 for x in range(5)]
print(cube_num)              