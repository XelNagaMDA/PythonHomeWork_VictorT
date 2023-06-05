"""
Verificarea unui palindrom
Scrieți un program care primește un șir de caractere ca intrare
și verifică dacă acesta este un palindrom (se citește la fel în ambele sensuri).
"""

text = str(input("Introduceti sir de caractere: "))
inceput = text[0:]
print(inceput)
sfarsit = text[-20000000:]
print(sfarsit)
if inceput == sfarsit:
    print("Acest cuvant e palindrom")