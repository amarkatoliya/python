password = input("Enter the password: ")

if len(password) < 6:
    strangth = "weak"
elif len(password) <= 8:
    strangth = "medium"
else:
    strangth = "strong"    

print(f"The password is {strangth}")