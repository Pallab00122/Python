# Write a decorator that measures the time function takes to execute

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)

example_function(2)

# Create a decorator to print the function name and the values of its arguments every time the function is called

# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value=', '.join(str(arg) for arg in args)
#         kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
#         print(f"Calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args,**kwargs)
#     return wrapper

# @debug
# def greet(name,greeting='Hell'):
#     print(f"{greeting} , {name}")
# greet("Chai", greeting="Hello")

# Implement a decorator that caches the return values of a function , so that when its called with the same arguments,
# the cache value returns instead of re-executing the function


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        # cache_value[args]=result
        return result
    return wrapper


@cache
def long(a, b):
    time.sleep(1)
    return a+b


print(long(2, 3))
print(long(3, 4))


# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)
