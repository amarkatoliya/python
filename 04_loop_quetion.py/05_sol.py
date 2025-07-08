# find n non repeatable char in string

input_str = input("Enter your desired char: ")

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Answer is: ",char) # here loop full 
        # break