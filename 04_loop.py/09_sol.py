items = ["apple", "banana", "orange", "apple", "mango", "watermalon","kevi","peach"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item is: ",item)
        break
    unique_item.add(item)
    