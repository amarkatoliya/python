# find factorial of given with while
number = int(input("Enter number for factorial: "))
factorial = 1

while number > 0:
    # factorial = factorial * number
    factorial *= number # same as upper line
    number -= 1
    
print(f"Factorial value of {number} is: ",factorial)