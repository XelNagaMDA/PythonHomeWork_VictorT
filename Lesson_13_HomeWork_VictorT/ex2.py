"""

    Create a function that takes a string as input and checks if it is a palindrome.
     Handle the ValueError if an empty string is provided.

Task:

    Define a function that accepts one parameter.
    Check if the input string is empty using an if statement.
    If the string is empty, raise a ValueError with an appropriate error message.
    If the string is not empty, compare it to its reverse and return True if they are equal (a palindrome)
     or False if they are not.

"""


def palindrome_function(word):
    if word == "":
        raise ValueError("The text should not be empty")

    palindrome = word[::-1]
    return print(word == palindrome)


palindrome_function(input("Please input a word:"))