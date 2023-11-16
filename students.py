import csv
from cs50 import SQL

def create_house(house, houses, head):
    count = 0
    for h in houses:
        if h["house"] == house:
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})

def create_student(name, students):
    students.append({"student_name": name})

def create_relationships(name, house, relationships):
    relationships.append({"student_name": name, "house": house})

db = SQL("sqlite:///roster.db")


students = []
houses = []
relationships = []

with open('students.csv', "r") as StudentsFile:
    students_reader = csv.DictReader(StudentsFile)
    for row in students_reader:
        name = row["student_name"]
        house = row["house"]
        head = row["head"]

        create_house(house, houses, head)
        create_student(name, students)
        create_relationships(name, house, relationships)

for student in students:
    db.execute("INSERT INTO new_students (student_name) VALUES (?)", student["student_name"])

for relation in relationships:
    db.execute("INSERT INTO relationships (student_name, house) VALUES (?,?)", relation["student_name"], relation["house"])

for house in houses:
    db.execute("INSERT INTO houses (house, head) VALUES (?,?)", house["house"], house["head"])

