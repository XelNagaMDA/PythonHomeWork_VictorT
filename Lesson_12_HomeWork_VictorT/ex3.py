"""Exercise 3: Password Strength Checker

Write a Python function called check_password_strength that checks the strength of a given password.
The function should take one argument: password (string) representing the password to be checked.
The function should return a boolean value indicating whether the password
 meets the specified strength criteria.

The password strength criteria are as follows:

    At least 8 characters long
    Contains at least one uppercase letter
    Contains at least one lowercase letter
    Contains at least one digit
    Contains at least one special character (e.g., !@#$%^&*)

Write a program that uses the check_password_strength function to do the following:

    Prompt the user to enter a password.
    Call the check_password_strength function with the provided input.
    Print whether the password meets the strength criteria or not.

Example Output:

Enter a password: MyPass123
Password strength: True (meets the criteria)

Enter a password: abcdefg
Password strength: False (does not meet the criteria)

Note: You can enhance the password strength checker by adding additional criteria
 or customizing the requirements according to your preference."""


def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character
    special_characters = "!@#$%^&*"
    if not any(char in special_characters for char in password):
        return False

    return True


password = input("Enter a password: ")

strength = check_password_strength(password)

print("Password strength:", strength, "(meets the criteria)" if strength else "(does not meet the criteria)")
