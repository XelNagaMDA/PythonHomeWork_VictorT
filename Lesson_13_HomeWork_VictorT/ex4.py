"""

    Create a function that calculates the factorial of a given positive integer.
    Handle the ValueError if a non-integer or negative number is provided.

Task:

    Define a function that accepts one parameter.
    Check if the parameter is an integer greater than or equal to zero using an if statement.
    If the parameter is not an integer or is negative, raise a ValueError with an appropriate error message.
    If the parameter is a valid positive integer, calculate its factorial using a loop.
    Return the factorial as the result.

"""


def factorial(n):
    if n == 0:
        return 1
    elif not isinstance(n, int) or n < 0:
        raise ValueError(" 'n' should be a positive integer")

    else:
        return n * (factorial(n - 1))



print(factorial("b"))
