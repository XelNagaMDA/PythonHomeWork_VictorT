"""
If you take a look at the file conversion_rates.json You will see a very long list of all currencies
and their conversion rate from and to MDL.
Task

Create a program that is going to load this list into the program.

On program start-up, show the list of all possible conversions, with rates from lowest to highest.

Let the user input the name of the currency to convert to. Example: EUR or MDL

    If the input currency is MDL, then use the ask the user to input again what currency to convert to MDL.
     Example USD
        Let the user input the value of MDL to convert to that currency.
        Print the converted value with only 2 decimal points (example 92.43)
    If the input currency is not MDL, then:
        Let the user input the value of MDL to convert to that currency.



    The entire program should be object-oriented (only use classes), except for the main.py which will run
    the program
    You should create CurrencyConversion object, that will store all information about each conversion.
        Example. CurrencyConversion(from="MDL", to="EUR", rate=0.049175765442905, inverse_rate=20.335219818002,
        name=" EUR")
    In order to have the ability to sort CurrencyConversion objects, implement __lt__, __eq__ functions.
    These functions should compare the rates of the CurrencyConversion objects.
    Have a CurrencyConversionService that will manage all the currency conversion information,
    and should have at least this method below.
        convert(from_currency, to_currency, amount)

Considerations

The json contains a dict of dicts. It's not a list, so pay attention, and analyze the data you are working
with before you start.
"""


class CurrencyConversion:
    def __init__(self, from_currency, to_currency, rate, inverse_rate, name):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate
        self.inverse_rate = inverse_rate
        self.name = name

    def __lt__(self, other):
        return self.rate < other.rate

    def __eq__(self, other):
        return self.rate == other.rate
