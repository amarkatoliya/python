# fun with *args
def sum_all(*args):
    # print(args)   (1, 2, 3, 4, 5)
    print(*args)     # 1 2 3 4 5
    return sum(args)

print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,5,8,9,4,3,5,89))
print(sum_all(1,2,3,4,5,6,7,8,45,0,77,67))