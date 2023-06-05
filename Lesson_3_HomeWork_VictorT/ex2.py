"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera"""

text = str(input("Introduceti sirul de caractere:"))
print(len(text))
print(len(text) - text.count(" "))
text.lower()
vocale = (text.lower().count("a") + text.lower().count("e")
          + text.lower().count("i") + text.lower().count("o") + text.lower().count("u"))
print(vocale)
consoane = len(text) - text.count(" ") - vocale
print(consoane)