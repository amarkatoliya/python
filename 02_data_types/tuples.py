# here list is same as tuple but list is mutable and tuple is immutable

tea_types = ("Green", "Black", "Oolong")
print(tea_types)

# here all basic  operations are same as list

tea_types[0]
tea_types[-1]

# tea_types[0] = "hello" # tuple is immutable so error is given

more_tea = ("herbal", "ok", "moana", "red")

all = tea_types + more_tea
print(all)
if "Green" in tea_types:
    print("Yes")
    
(one,two,three) = tea_types   
print(one)
print(two)
print(three)

print(type(tea_types))

# neesting is also done in  all data types