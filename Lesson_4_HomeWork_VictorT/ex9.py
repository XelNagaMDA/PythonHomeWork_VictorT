"""
Scrieți un program care cere utilizatorului să introducă o parolă.
Dacă parola conține cel puțin 8 caractere și include atât litere mari,
cât și litere mici, afișați mesajul „Parolă puternică”.
În caz contrar, afișați mesajul „Parolă slabă”.
"""
password = input("Please input a password:")
if len(password) >= 8 and password.isupper() == False and password.islower() == False:
    print("Strong Password")
else:
    print("Weak password")