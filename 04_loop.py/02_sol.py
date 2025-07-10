# its for total count of even nums
n = int(input("Enter n for sum:"))
sum_even = 0

for i in range(1, n+1):
    if (i%2 == 0):
        sum_even += 1
          
print(f"Total Sum of {n} even nums is: {sum_even}") 


# this is for total sum of that nums

# n = int(input("Enter n for sum:"))
# final_out = n*(n+1)       
# print(f"Total Sum of {n} even nums is: {final_out}") 