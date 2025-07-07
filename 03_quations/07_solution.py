order_size = input("enter coffee order size: ")

extra_shot = input("is extra shot is needed ans in yes or no:")

if extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
    
else:
    coffee = order_size + " coffee"
    
print("your order is:",coffee)    