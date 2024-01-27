submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 1
common_students = [student for student in submitted if student in attended]
print("Common Students:", common_students)

# Task 2
are_identical = sorted(submitted) == sorted(attended)
print("Are Identical:", are_identical)

# Task 3
attended = [student for student in attended if student in submitted]
print("Filtered Attended List:", attended)
