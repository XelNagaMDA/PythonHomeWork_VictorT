"""
Create a class that describes a human.

Human object should have the following properties:

    First Name - string
    Last Name - string
    Date of Birth - datetime.date

All the properties above should be initialized in the constructor function, by arguments to the constructor.

And the following methods:

    A method to get the full name of the human
    A method to get the age of the human

When printing the human object the console should output something like example below:

Marius Tricolici, age 24
"""
import datetime


class Human:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = datetime.date.today()
        age = today - self.date_of_birth
        return age.days // 365

    def __str__(self):
        return f"{self.get_full_name()}, age {self.get_age()}"


john = Human("John", "Doe", datetime.date(2000, 12, 12))

print(john)
