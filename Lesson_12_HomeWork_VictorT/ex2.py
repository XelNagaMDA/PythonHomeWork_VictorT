"""Exercise 2: Fibonacci Sequence

Write a Python function called generate_fibonacci that generates the Fibonacci sequence
 up to a given number of terms.
 The function should take one argument: terms (integer) indicating
 the number of Fibonacci terms to generate.
 The function should return a list containing the Fibonacci sequence.

Hint: The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum
of the two preceding numbers.

Write a program that uses the generate_fibonacci function to do the following:

    Prompt the user to enter the number of Fibonacci terms to generate.
    Call the generate_fibonacci function with the provided input.
    Print the generated Fibonacci sequence.

Example Output:

Enter the number of Fibonacci terms to generate: 8
Generated Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13]

Enter the number of Fibonacci terms to generate: 5
Generated Fibonacci sequence: [0, 1, 1, 2, 3]
"""


def generate_fibonacci(terms):
    fibonacci_sequence = [0, 1]

    if terms <= 2:
        return fibonacci_sequence[:terms]

    while len(fibonacci_sequence) < terms:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


terms = int(input("Enter the number of Fibonacci terms to generate: "))

fibonacci_sequence = generate_fibonacci(terms)

print("Generated Fibonacci sequence:", fibonacci_sequence)
