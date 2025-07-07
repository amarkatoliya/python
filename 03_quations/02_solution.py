age = int(input("Enter the age:"))
day = str(input("is today Wednesday? :"))

price = 12 if age >= 18 else 8  #if age 18 then 12 else price 8

if day == "true":  
    price = price -2    # price -= 2
    
print("Ticket Price For You:",price)