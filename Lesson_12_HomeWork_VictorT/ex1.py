"""Exercise 1: Temperature Conversion

Write a Python function called convert_temperature that converts temperature values between
Celsius and Fahrenheit. The function should take two arguments: temperature (float) and unit (string)
indicating the current temperature unit ("C" for Celsius or "F" for Fahrenheit).
The function should return the converted temperature value.

Hint: To convert Celsius to Fahrenheit, use the formula: F = (C * 9/5) + 32.
To convert Fahrenheit to Celsius, use the formula: C = (F - 32) * 5/9.

Write a program that uses the convert_temperature function to do the following:

    Prompt the user to enter a temperature value.
    Prompt the user to enter the current temperature unit ("C" or "F").
    Call the convert_temperature function with the provided inputs.
    Print the converted temperature value with the corresponding unit.

Example Output:

Enter the temperature: 25
Enter the current unit (C/F): C
Converted temperature: 77.0 F

Enter the temperature: 98.6
Enter the current unit (C/F): F
Converted temperature: 37.0 C
"""


def convert_temperature(temperature: float, unit: str):
    if unit == "C":
        converted_temperature = (temperature * 9 / 5) + 32
    elif unit == "F":
        converted_temperature = (temperature - 32) * 5 / 9
    else:
        print("Invalid value.")

    return converted_temperature


temperature = float(input("Please input the temperature: "))
unit = input("Enter the current unit (C/F):")

converted_temperature = convert_temperature(temperature, unit)

