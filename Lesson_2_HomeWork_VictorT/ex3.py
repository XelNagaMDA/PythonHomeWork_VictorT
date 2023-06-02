# Creaza un program care va cere de la utilizator:
#
# Adresa de email
# Numele de utilizator
# Și va afisa aceasta infromatie in urmatorul format:
#
# Emailul pentru Marius a fost expediat cu succes pe adresa de email mariustricolici@hotmail.com
#
# Pentru adresa de email: mariustricolici@hotmail.com Si numele de utilizator: Marius

user_mail = input("Please write your email: ") # introducem de la consola datele, in loc sa facem o variabila cu numele si emailul
username = input("Please add your username:") # same as for user_mail
print(f"Emailul pentru {username} a fost expediat cu succes pe adresa de email {user_mail}")