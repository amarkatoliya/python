file = open('test.txt', 'w')

try:
    file.write('Hello')
    
finally:
    file.close()
    
    
# second methode
with open('test.txt', 'w') as file:
    file.write("How are you")