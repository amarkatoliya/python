import time

def cache(fun):
    cache_val = {}
    print(cache_val)
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result = fun(*args)
        cache_val[args] = result
        return result
    return wrapper

@cache
def long_fun(a,b):
    time.sleep(5)
    return a + b

print(long_fun(2,3))
print(long_fun(4,3))