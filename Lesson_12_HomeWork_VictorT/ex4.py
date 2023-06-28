"""Exercise 4: Prime Number Checker

Write a Python function called is_prime that checks whether a given number is prime or not.
The function should take one argument: number (integer) representing the number to be checked.
The function should return a boolean value indicating whether the number is prime.

Hint: A prime number is a number greater than 1 that has no divisors other than 1 and itself.

Write a program that uses the is_prime function to do the following:

    Prompt the user to enter a number.
    Call the is_prime function with the provided input.
    Print whether the number is prime or not.

Example Output:

Enter a number: 17
Prime number: True

Enter a number: 8
Prime number: False
"""

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

prime = is_prime(number)

print("Prime number:", prime)