"""

    Create a function that takes a list of numbers as input and calculates their geometric mean.
    Handle the ZeroDivisionError if the list contains a zero.

Task:

    Define a function that accepts one parameter (a list).
    Check if the list contains zero using an if statement.
    If the list contains zero, raise a ZeroDivisionError with an appropriate error message.
    If the list does not contain zero, calculate the product of all the numbers in the list using a loop.
    Use the math.pow() function to calculate the geometric mean by raising the product to the power of 1
    divided by the length of the list.
    Return the geometric mean as the result.
"""
import math


def geometric_mean_result(my_list):
    if 0 in my_list:
        raise ZeroDivisionError

    product = 1
    for el in my_list:
        product *= el

    geometric_mean = math.pow(product, 1 / len(my_list))
    return geometric_mean


print(geometric_mean_result([1, 2, 3, 0, 5, 6]))
