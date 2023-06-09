"""
Creaţi lista `date_personale`.

Citiţi după aceasta de la tastatură **numele**, **prenumele**, **vârsta**,
 **înălţimea** şi **ocupaţia** utilizatorului şi adăugaţi aceste valori în lista creată.
"""
date_personale = list()
info_date = ["nume", "prenume", "varsta", "inaltime", "ocupatie"]
for el in info_date:
    info = input(f"Introduceti {el}:")
    date_personale.append(info)

print(f"Lista cu date personale completata: {date_personale}")