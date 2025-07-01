String = "Amar_katodita"
print(String)
print(type(String))

# print(String[0])
# print(String[-1])

print(String[0:5])

# print(String('a'))
# print(String('"a"'))
# print(String("a"))

first_letter = String[0]
print(first_letter)

slice_name = String[0:4] # slice is not inclusive
print(slice_name)

num_list = "0123456789"
print(num_list[2:6])
print(num_list[:6])
print(num_list[2:])

print(String.lower())
print(String.capitalize())
print(String.upper())
print(String.title())

# str ="      vhyg    aygi ajsh      "
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())

print(String.replace("a", "A"))
print(String.replace("a", "A", 1))

chai = "Lemon, Ginger, Mint"
# print(chai.split())
print(chai.split(", "))

test = "Amar_Katodita"
print(test.find("t"))

test2 = "one one one one one oen"
print(test2.count("one"))

test_type = "masala"
quantity = 2
order ="I want {} cups of {} tea"
print(order.format(quantity, test_type))


chai_var = ["Lemon", "Ginger", "Mint"]

print(", ".join(chai_var)) # list to string

print(len(String))

for letter in String:
    print(letter)  # for loop
    
path = "He said, \"all person is good\""
print(path)

h1 = r"Hello\nWorld" # raw string 
print(h1)
h2 = "Hello\nWorld"
print(h2)