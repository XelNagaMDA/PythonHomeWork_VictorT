"""
Also create a new class HumanWithPet:

The HumanWithPet should have the same properties as the Human in Ex 1.

Additionally, the HumanWithPet class should have a list of pets as a property.

Add two methods to the HumanWithPet class:

    Adopt new pet - Adds a new pet object to the list of pets
    Give away pet - Removes a pet from the humans list of pets

When printing a HumanWithPet object, the console should output the according to the following examples:

Marius Tricolici, age 24 with a pet: Cat called Garfield that loves lasagna - If the human has 1 pet.

Marius Tricolici, age 24 with 2 pets: Cat called Garfield that loves lasagna,
Dog called Kuzea that loves bones - If the human has 2 or more pets.
"""
import datetime

from Lesson_21_HomeWork_VictorT.Human import Human
from Lesson_21_HomeWork_VictorT.Pet import Pet


class HumanWithPet(Human):
    def __init__(self, first_name, last_name, date_of_birth):
        super().__init__(first_name, last_name, date_of_birth)
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)

    def give_pet(self, pet):
        self.pets.remove(pet)

    def __str__(self):
        human_info = super().__str__()
        pet_info = ', '.join(str(pet) for pet in self.pets)
        if len(self.pets) == 1:
            return f"{human_info} with a pet: {pet_info} "
        else:
            return f"{human_info} with {len(self.pets)} pets: {pet_info}"


john = HumanWithPet("John", "Doe", datetime.date(2000, 12, 12))
cat = Pet("Tom","Cat", "cottage cheese")
dog = Pet("Dog", "Mircea","bones")

john.adopt_pet(cat)
john.adopt_pet(dog)

print(john)

john.give_pet(dog)

print(john)



