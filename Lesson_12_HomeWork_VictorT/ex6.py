"""Exercise 6: Palindrome Checker

Write a Python function called is_palindrome that checks whether a given string is a palindrome.
The function should take one argument: text (string) representing the text to be checked.
The function should return a boolean value indicating whether the text is a palindrome.

Hint: A palindrome is a word, phrase, number, or other sequence of characters
that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.

Write a program that uses the is_palindrome function to do the following:

    Prompt the user to enter a text.
    Call the is_palindrome function with the provided input.
    Print whether the text is a palindrome or not.

Example Output:

Enter a text: radar
Palindrome: True

Enter a text: Hello
Palindrome: False

Note: The palindrome checker can be customized to ignore or consider spaces, punctuation,
or capitalization based on your preference."""

def is_palindrome(text):
    cleaned_text = "".join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


text = input("Enter a text: ")

palindrome = is_palindrome(text)

print("Palindrome:", palindrome)