"""

    Write a program that asks the user to enter their age and handles the AgeError
     if the age is less than 0 or greater than 150.
     Define a custom exception class called AgeError for this purpose.

Task:

    Define a custom exception class called AgeError that inherits from the base Exception class.
    Define a function that prompts the user to enter their age and returns the age as an integer.
    Use a try-except block to handle potential exceptions.
    Within the try block, convert the user's input to an integer and store it in a variable.
    Use an if statement to check if the age is less than 0 or greater than 150.
    If the age is invalid, raise an AgeError with an appropriate error message.
    If the age is valid, return it.

"""


class AgeError(Exception):
    pass


def age_prompt():
    input_age = int(input("input age:"))
    if input_age < 0 or input_age > 150:
        raise AgeError
    return print("Your age is: ", input_age)


age_prompt()
