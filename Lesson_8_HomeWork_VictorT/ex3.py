"""
Write a program that takes a list of numbers as input.
The program should calculate the product of all the numbers in the list.
However, if the product exceeds 100, the program should stop calculating
 and print a message indicating that the product is too large.
 Use a while loop and the break statement to terminate the loop when necessary.
"""

numbers = input("Enter a list of numbers (separated by spaces): ").split()
product = 1
index = 0

while index < len(numbers):
    product *= int(numbers[index])
    if product > 100:
        print("Product is too large.")
        break
    index += 1

print("Product:", product)