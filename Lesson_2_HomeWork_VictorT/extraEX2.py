#Scrie un program care preia două numere ca intrare și efectuează următoarele operații:
#
#    Adună cele două numere și afișează rezultatul.
#    Scade al doilea număr din primul număr și afișează rezultatul.
#    Înmulțește cele două numere și afișează rezultatul.
#    Împarte primul număr la al doilea număr și afișează rezultatul.

num1 = int(input("Please input the first number: "))
num2 = int(input("Please input the second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum}")
subtraction = num1 - num2
print(f"The subtraction of {num1} and {num2} is: {subtraction}")
mult = num1 * num2
print(f"The multiplication of {num1} and {num2} is: {mult}")
division = num1 / num2
print(f"The division of {num1} and {num2} is: {division}")
