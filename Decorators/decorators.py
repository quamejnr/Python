# This is a decorator function that returns the time taken for a program to run
import time


def decorator_function(original_function):

    def wrapper(*args, **kwargs):
        # wrapping the original function with this print statement before execution
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_func):

    def wrapper(*args, **kwargs):
        # time function begins
        t1 = time.time()
        result = original_func(*args, **kwargs)
        # time function ends is subtracted from start time to give time difference
        t2 = time.time() - t1
        print(f'{original_func.__name__} ran in: {t2} sec')
        return result

    return wrapper


@my_timer  # This modifies the functionality of the function
def display(name, age):
    print(f'My name is {name} and I am {age} years old')



