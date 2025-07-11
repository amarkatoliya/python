
def debug(fun):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k,v  in kwargs.items())
        print(f"calling {fun.__name__} with args {args_value} ang kwargs is {kwargs_value}")
        return fun(*args, **kwargs)
        
    return wrapper

@debug
def hello():
    print("Hello")


# here basic decorator is just passsing all arguments to another function
@debug
def greet(name, greeting="Welcome"):
    print(f"{greeting}, {name}")
    
greet("Hello ", greeting="How are you!")
hello()