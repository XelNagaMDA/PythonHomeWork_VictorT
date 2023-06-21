"""
    Ask the user to input a large text with many words. Ignoring punctuation.
    Calculate how many times each word (regardless the case) was used.

Hints: Use str.split(' ') to break down the text into a list

Example:
Input:
how much wood would a woodchuck chuck if a woodchuck could chuck wood
Output:
Word "how" was used 1 times.
Word "much" was used 1 times.
Word "wood" was used 2 times.
Word "would" was used 1 times.
Word "a" was used 2 times.
Word "woodchuck" was used 2 times.
Word "chuck" was used 2 times.
Word "if" was used 1 times.
Word "could" was used 1 times.
"""
import string

text = input("Please input text: ")

# Removing punctuation
for punct in list(string.punctuation) + list(string.digits):
    text = text.replace(punct, "")

# Transforming all letters to lower and splitting them into a list
total_words = text.lower().split()

# Initialization of a dictionary
word_numbers = {}

# For every word in the string list, if it's not  present(else statement) in the dictionary,
# then it receives one (1) encounter. If it is already present in the dictionary, we add 1 new encounter
for word in total_words:
    if word in word_numbers:
        word_numbers[word] += 1
    else:
        word_numbers[word] = 1

# We access the key-value pairs in the dictionary, using .items()
for word, number in word_numbers.items():
    print(f"Word {word} was used {number} times.")
