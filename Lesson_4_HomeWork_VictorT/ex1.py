"""
Ce vor afişa următoarele expresii? (Încercaţi mai întâi fără a implementa codul,
 apoi implementaţi codul şi verificaţi răspunsurile):
* not (True and True)
* True or False   # True
* not (False and True)
* False and False
* True and True
* False and True
* 1 == 1 and 2 == 1
* "test" == "test"
* 1 == 1 or 2 != 1
* True and 1 == 1
* False and 0 != 0
* 1 != 0 and 2 == 1
* False and 0 != 0
* True or 1 == 1
* "test" == 1
* not (True and False)
* not (1 == 1 and 0 != 1)
* not (10 == 1 or 1000 == 1000)
* not (1 != 10 or 3 == 4)
* not ("testing" == "testing" and "Zed" == "Cool Guy")
* 1 == 1 and not ("testing" == 1 or 1 == 0)
* "chunky" == "bacon" and not (3 == 4 or 3 == 3)

"""
x1 = not (True and True)  # False
print(f"x1 e: {x1}")

x2 = True or False   # True
print(f"x2 e: {x2}")

x3 = not (False and True)  # True
print(f"x3 e: {x3}")

x4 = False and False  # False
print(f"x4 e: {x4}")

x5 = True and True  # True
print(f"x5 e: {x5}")

x6 = False and True  # False
print(f"x6 e: {x6}")

x7 = (1 == 1 and 2 == 1)  # False
print(f"x7 e: {x7}")

x8 = ("test" == "test")  # True
print(f"x8 e: {x8}")

x9 = (1 == 1 or 2 != 1)  # True
print(f"x9 e: {x9}")

x10 = (True and 1 == 1)  # True
print(f"x10 e: {x10}")

x11 = (False and 0 != 0)  # False
print(f"x11 e: {x11}")

x12 = (1 != 0 and 2 == 1)  # False
print(f"x12 e: {x12}")

x13 = (False and 0 != 0)  # False
print(f"x13 e: {x13}")

x14 = (True or 1 == 1)  # True
print(f"x14 e: {x14}")

x15 = ("test" == 1)  # False
print(f"x15 e: {x15}")

x16 = (not (True and False))  # True
print(f"x16 e: {x16}")

x17 = (not (1 == 1 and 0 != 1))  # False
print(f"x17 e: {x17}")

x18 = (not (10 == 1 or 1000 == 1000))  # False
print(f"x18 e: {x18}")

x19 = (not (1 != 10 or 3 == 4))  # False
print(f"x19 e: {x19}")

x20 = (not ("testing" == "testing" and "Zed" == "Cool Guy"))  # True
print(f"x20 e: {x20}")

x21 = (1 == 1 and not ("testing" == 1 or 1 == 0))  # True
print(f"x21 e: {x21}")

x22 = ("chunky" == "bacon" and not (3 == 4 or 3 == 3))  # False
print(f"x22 e: {x22}")