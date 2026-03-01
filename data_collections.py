# ---Saraksti---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)
numbers.pop(0)
total = 0
for number in numbers:
    total += number

count = 0
for number in numbers:
    count += 1
average = total / count

print("#---Saraksti--- ")
print(f"Summa: {total}, Vidējā vērtība: {average}")

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(f"Pāra skaitļi: {even_numbers}")

first_three_numbers = numbers[:3]
last_two_numbers = numbers[-2:]
print(f"Pirmie trīs skaitļi: {first_three_numbers}, Pēdējie divi skaitļi: {last_two_numbers}")

#---Vārdnīcas---
students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95,
    "Pēteris": 78,
}

students["Jānis"] = 88 

print("---Vārdnīcas--- ")
for student, grade in students.items():
    print(f"{student}: {grade}")

best_name = None
best_grade = -1
for student, grade in students.items():
    if grade > best_grade:
        best_grade = grade
        best_name = student
print(f"Labākais students: {best_name} ({best_grade})")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 88},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 78}
]

top_students = []
for student in student_list:
    if student["grade"] >= 80:
        top_students.append(student["name"])

print(f"#---Studenti ar atzīmi >= 80 ---")
for name in enumerate(top_students, start=1):
    print(f"{name[0]}. {name[1]}")
