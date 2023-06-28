"""

    Write a program that prompts the user to enter two numbers and calculates their division.
    Handle the ZeroDivisionError if the second number is zero.

Task:

    Prompt the user to enter the first number and store it in a variable.
    Prompt the user to enter the second number and store it in another variable.
    Convert both inputs to floating-point numbers using the float() function.
    Divide the first number by the second number and store the result in a variable.
    Use a try-except block to handle the ZeroDivisionError and print an appropriate error message
    if the second number is zero.
    If the division is successful, print the result.

"""
first_value = float(input("Please input first value:"))
second_value = float(input("Please input the second value:"))

try:
    division = first_value / second_value
    print("Division result:", division)
except ZeroDivisionError:
    print(" This is a division by zero")
