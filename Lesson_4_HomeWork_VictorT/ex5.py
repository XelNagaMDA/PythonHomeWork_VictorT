"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""
your_mark = int(input("Please input your test mark: "))
if your_mark >= 15:
    print(f"You've got {your_mark} and You've passed the test")
else:
    print(f"Sorry, you did not pass the test. You received {your_mark}. Minimal passing mark is 15.")