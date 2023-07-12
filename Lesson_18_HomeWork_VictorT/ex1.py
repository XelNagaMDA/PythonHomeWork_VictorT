"""
Write a Python program to find palindromes in a given list of strings using Lambda.
Orginal list of strings: ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa'] List of palindromes: ['php', 'aaa'].

Note: You can use the filter function in python to filer a list using a function.
"""

list_of_strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

is_palindrome = lambda x: x == x[::-1]

palindrome_list = list(filter(is_palindrome, list_of_strings))

print(palindrome_list)