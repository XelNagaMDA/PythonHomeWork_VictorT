"""
Create a class that describes a pet.

A pet should have the following properties:

    A name - string
    A type (cat/dog/bird) - string
    A favourite food - string

All the properties above should be initialized in the constructor function, by arguments to the constructor.

When a pet object is printed it should output something like this:

Cat called Garfield that loves lasagna or Dog called Kuzea that loves bones
"""


class Pet:
    def __init__(self, name, type_of_pet, food):
        self.name = name
        self.type_of_pet = type_of_pet
        self.food = food

    def __str__(self):
        return f"{self.type_of_pet} called {self.name} that loves {self.food}"


cat = Pet("Tom", "Cat", "chicken heads")
print(cat)
