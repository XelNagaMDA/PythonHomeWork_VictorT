"""
Create a decorator that checks if the result of the function it decorates is always a number

The decorator should be called "validate_numeric" and should raise ValueError when the result
of function it decorates is not numeric.
"""


def validate_numeric(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError("Function is not numeric")
        return result

    return wrapper()
