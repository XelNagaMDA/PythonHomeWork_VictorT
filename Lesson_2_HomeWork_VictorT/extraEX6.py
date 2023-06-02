# Scrie un program care preia numărul de minute ca intrare și îl convertește în ore și minute.
# Afișează orele și minutele convertite.

minutes = int(input(" Please input minutes value:"))

hours = minutes / 60
result = (minutes % 60)
print(f"Your time in hh:mm is: {str(int(hours))}:{result}")