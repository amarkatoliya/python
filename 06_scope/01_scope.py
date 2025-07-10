username = "xyz"

def fun():
    # username = "abc"
    print(username)

print(username)
fun()


x = 100

def fun2(y):
    z = x+y  # x is global 
    return z

res = fun2(5)
print(res)

# def fun3():
#     global x # global make that variable value global 
#     x = 88  # global override old value
    
# fun3()    

def f1():
    x = 90
    def f2():
        print(x)
    return f2
    
myRes = f1()
myRes()
# print(x)   

def one(num):  # closure
    def two(x):
        return x ** num
    return two

Res = one(2)
Res2 = one(3)

print(Res(3)) # 3*3
print(Res2(3)) # 3*3*3
