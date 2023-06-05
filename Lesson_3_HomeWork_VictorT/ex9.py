"""
Eliminați semnele de punctuație
Scrieți un program care primește o propoziție ca intrare (din consola) și
 elimină toate caracterele de punctuație (de exemplu, .,?!) din ea.
"""
text = str(input("Introduceti sirul de caractere:"))
print(text.replace("?","").replace("!","").replace(".","").replace(",",""))
