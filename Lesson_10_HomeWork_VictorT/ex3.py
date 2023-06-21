"""Given two dictionaries representing students' grades:

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

Write a program that prints out a new dictionary containing the average grades for each student."""

math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

average_grades = {}


for student in math_grades:
    average = (math_grades[student] + science_grades[student]) / 2
    average_grades[student] = average

print("Average grades are:", average_grades)
