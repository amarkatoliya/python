import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start}")
        return result
    return wrapper

@timer  # if you call timed fun it take time of that fun
def example_function(n):
    time.sleep(n)
    
    
example_function(2)