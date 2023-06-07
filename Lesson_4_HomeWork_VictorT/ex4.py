"""
Scrieţi un program care verifică dacă litera "a" se află pe a 2-a poziţie într-un String citit de la tastatură.
"""
value = input("Please input a text:")
if value[1] == 'a':
    print("The second letter in your text is 'a'")
else:
    print(f"Your second letter is not 'a', but '{value[1]}'")