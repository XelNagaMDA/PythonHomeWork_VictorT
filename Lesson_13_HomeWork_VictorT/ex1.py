"""
    Write a function that takes a list as input and returns the sum of its elements.
    Handle the TypeError if the input is not a list.

Task:

    Define a function that accepts one parameter.
    Check if the parameter is of type list using an if statement.
    If the parameter is a list, calculate the sum of its elements using the sum()
    function and return the result.
    If the parameter is not a list, raise a TypeError with an appropriate error message.
"""


def sum_of_elem(list_of_elem):
    if type(list_of_elem) == list:
        return sum(list_of_elem)


try:
    sum_of_elem([1, 2, "B"])
except TypeError:
    print("Unsupported operand type(s) for +: 'int' and 'str'")
