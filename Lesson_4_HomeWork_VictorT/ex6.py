"""
Scrieţi un program care citeşte de la tastatură numele unei persoane.
Dacă numele nu începe cu literă mare,
atunci programul transformă valoarea citită în numele persoanei scris cu literă mare.
După aceasta, afişează la ecran `"Salut, <numele citit de la tastatura care începe cu litera mare>!"`.
"""
name = input("Please input your name:")
# if name != name.capitalize():
# if name[0] != name[0].upper():
#    print(f"Salut {name[0].upper()}")
# else:
#    print(f"Salut {name}")
print(f"Salut {name.capitalize()}")  # fara IF

