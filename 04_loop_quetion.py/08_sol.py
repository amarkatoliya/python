number = int(input("Enter number for cheking prime or not: "))

is_prime = True

if number > 1:
    for i in range(2,number): #here is a catch we did not take number + 1 because if we are checking for prime num then num it self id divisable 
        if (number % i) == 0:     # always do good practice
            is_prime = False
            break
        
print(f" {number} prime is {is_prime}")