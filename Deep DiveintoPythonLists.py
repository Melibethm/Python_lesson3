students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1
combined_data = [{"name": name, "grade": grade, "activity": activity} for name, grade, activity in zip(students, grades, activities)]
print("Combined Data:", combined_data)

# Task 2
passed_students = [student for student in combined_data if student["grade"] >= 80]
print("Passed Students:", passed_students)

# Task 3
for student in passed_students:
    student["status"] = "Passed"

print("Updated Passed Students:", passed_students)
