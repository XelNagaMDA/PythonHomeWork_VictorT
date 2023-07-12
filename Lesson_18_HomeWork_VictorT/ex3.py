"""
Create a decorator that will count the time that it took for a function to complete.

The decorator should be called benchmark_time and should show at the end of every function call
of the function that it decorates, the amount in seconds of the time it took to complete.

Bonus points if you can also print the name of the function being called (decorated).
"""
import time


def benchmark_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        time_for_function = end_time - start_time

        print(f" Function {function.__name__} took {time_for_function:.8f} time to execute")

        return result

    return wrapper


@benchmark_time
def function_multiplication(x,y):
    return x * (x + y) * (x ** y) * x * (x + 2 * y)


print(function_multiplication(12, 15))
