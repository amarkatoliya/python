chai_types = {
    "Masala": "spicy",
    "Sugar": "Sweet",
    "Green": "Mild",
}    
print(chai_types)

chai_types["Masala"] == "Fresh"

print(chai_types)

for chai in chai_types:
    print(chai,end="--")

for chai in chai_types:
    print(chai_types[chai])

for key,value in chai_types.items():
    print(key,value)
    
if "Masala" in chai_types:
    print("Yes")     
    
print(len(chai_types))    

chai_types["Ginger"] = "Xyz"

chai_types.pop("Masala")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types["Green"]
print(chai_types)

chai_types_copy = chai_types.copy()
print(chai_types_copy)

tea_shop = {
    "chai": {
        "Masala": "spicy",
        "Sugar": "Sweet",
    },
    "Tea": {
        "Black": "Strong",
        "Green": "Mild",
    }
}
print(tea_shop)
print(tea_shop["Tea"]["Green"])

sqar_num = { x: x**2 for x in range(5) }
print(sqar_num)
sqar_num.clear() 

keys = {"one", "two", "three"}
defaults_val = "test"
new_dist = dict.fromkeys(keys, keys) # if we give keys as key then all val of key is given to all keys elements
print(new_dist)