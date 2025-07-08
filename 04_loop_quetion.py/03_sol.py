number = int(input("Enter n for fot table:"))

for i in range(1,11):
    if i ==5:
        continue  # continue skip that condition
    print(number, 'x', i, '=', number*i)