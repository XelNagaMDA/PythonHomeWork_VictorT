#Scrie un program care preia raza unui cerc ca intrare și calculează aria acestuia. Afișează aria calculată.

PI = 3.141592653589793
radius = int(input("Please input the radius of a circle:"))
area = PI * (radius**2)
print(f"The area of your circle is: {area}")
