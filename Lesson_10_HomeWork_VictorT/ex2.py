"""Create a program that will register a list of guests and food for a restaurant.

The user has to input how many guests will be coming

To register each guest, the user will input the name of the guest and two (2) dishes.

At the end, print out the list of the guests and what they ordered.
And the total number of each dish the restaurant will have to prepare.

Use dict
Example:

Input:
3

Marius
Ravioli
Caesar Salad

Ana
Pepper steak
Caesar Salad

Gheorghe
Greek salad
Lentil Soup

Output:
The guests will be: [Marius, Ana, Gheorghe]

Marius ordered Ravioli and Caesar Salad
Ana ordered Pepper steak and Caesar Salad
Gheorghe ordered Greek salad and Lentil Soup

You will have to prepare:
Ravioli x 1
Caesar Salad x 2
Pepper steak x 1
Greek salad x 1
Lentil Soup x 1
"""

guest_number = int(input("Please input how many guests will attend: "))

guest_list = {}
food_dishes = {}


for guest in range(guest_number):
    guest_name = input(" Enter the guest's name: ")
    dish1 = input("What will be the first meal: ")
    dish2 = input("What will be the second meal: ")

    guest_list[guest_name] = [dish1, dish2]
    food_dishes[dish1] = food_dishes.get(dish1, 0) + 1
    food_dishes[dish2] = food_dishes.get(dish2, 0) + 1

print("The guests will be:", list(guest_list.keys()))

for guest, order in guest_list.items():
    print(f"{guest} ordered {order[0]} and {order[1]}")

print("You will have to prepare:")

for dish, count in food_dishes.items():
    print(f"{dish} x {count}")

