"""
Numărarea caracterelor
Scrieți un program care
 primește un șir de caractere ca intrare
 și numără de câte ori apare un caracter specific (introdus in consola).

 Numarul de caractere trebuie sa fie considerat indiferent daca e majuscula sau minuscula
"""

text = str(input("Introduceti sirul de caractere:"))
caracter_verificare = str(input("Introduceti un caracter de verificare:"))
print(f"Caracterul de verificare se gaseste de {text.lower().count(caracter_verificare)} ori in sirul de caractere introdus.")