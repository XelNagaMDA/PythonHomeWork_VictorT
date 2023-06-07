"""
Scrieți un program pentru a citi temperatura de la utilizator și pentru a afișa un mesaj adecvat în funcție
 de starea temperaturii de mai jos.
Temp -40-(-10) atunci 'Vremea extrem de rece'
Temp -10-0 atunci 'Vremea foarte rece'
Temp 0-10 atunci 'Vreme rece'
Temp 10-20 atunci 'Vreme normala'
Temp 20-30 atunci 'Vreme calda'
Temp 30-40 atunci 'Este foarte cald'
Temp >=40 atunci 'Este extrem de cald'
"""
temperature = float(input("Please input the temperature:"))
if temperature < -10:
    print(f"Vremea extrem de rece la temperatura de {temperature}")
elif -10 <= temperature < 0:
     print(f"Vremea e foarte rece la temperatura de {temperature}")
elif 0 <= temperature < 10:
     print(f"Vremea e rece la temperatura de {temperature}")
elif 10 <= temperature < 20:
     print(f"Vremea e normala la temperatura de {temperature}")
elif 20 <= temperature < 30:
     print(f"Vremea e calda la temperatura de {temperature}")
elif 30 <= temperature < 40:
     print(f"Vremea e foarte calda la temperatura de {temperature}")
else:
     print(f"Vremea este extrem de calda la temperatura de {temperature}")