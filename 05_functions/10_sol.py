# recursion factorial example

fact = int(input("Enter number for finding factorial of given number:"))
def factorial(fact):
    if fact == 0:
        return 1
    else:
        return fact * factorial(int(fact)-1)
    
    
# for num in factorial(fact):
print(factorial(fact))