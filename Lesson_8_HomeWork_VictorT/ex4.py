"""Write a program that takes a list of strings as input.
The program should print each string on a separate line.
However, if a string starts with the letter 'A',
the program should skip that string and move on to the next one using the continue statement."""

strings = input("Enter a list of strings (separated by spaces): ").split()

for string in strings:
    if string[0] == 'A' or string[0] == 'a':
        continue
    print(string)