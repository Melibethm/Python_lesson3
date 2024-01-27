grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Task 1
sorted_grades = sorted(grades, reverse=True)
print("Sorted Grades:", sorted_grades)

#Task 2
average_grade = sum(grades) / len(grades)
print("Average Grade:", average_grade)

#Task 3
grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Modified Grades:", grades)
