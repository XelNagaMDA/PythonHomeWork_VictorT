#Scrie un program care preia o temperatură în grade Celsius ca intrare
# și o convertește în grade Fahrenheit. Formula de conversie este: Fahrenheit = Celsius * 9/5 + 32.
# Afișează temperatura convertită.

celsius_value = int(input("Please input your Celsius value: "))
fahrenheit_value = (celsius_value * 9) / 5 + 32
print(f"Your Celsius value converted in Fahrenheit value is: {fahrenheit_value}")