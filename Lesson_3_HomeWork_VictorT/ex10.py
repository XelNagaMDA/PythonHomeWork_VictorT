"""
Înlocuiți un subșir de caractere
Scrieți un program care primește o propoziție, un subșir de caractere țintă
și un subșir de caractere de înlocuire ca intrare (din consola)
și înlocuiește toate aparițiile subșirului de caractere țintă cu subșirul de caractere de înlocuire.
"""
text = input("Text: ")
subtext_target = input("Tinta: ")
subtext_replace = input("Inlocuire: ")
print(text.replace(subtext_target, subtext_replace))

