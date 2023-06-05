"""Scrieţi un program care citeşte de la tastatură de 3 ori timpul în care un sportiv aleargă
 proba de 100 metri (numărul de secunde).
Apoi afişaţi la ecran timpul mediu (media aritmetică a celor 3 încercări) în secunde."""

time1 = int(input("Primul timp la 100 de metri alergare: "))
time2 = int(input("Al doilea timp la 100 de metri alergare: "))
time3 = int(input("Al treilea la 100 de metri alergare: "))

timpul_mediu = (time1 + time2 +time3) / 3
print(timpul_mediu)