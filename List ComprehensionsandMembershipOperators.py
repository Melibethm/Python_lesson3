numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task 1
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers:", even_numbers)

# Task 2
greater_than_5 = [num for num in numbers if num > 5]
print("Numbers Greater Than 5:", greater_than_5)

# Task 3
is_number_7_present = 7 in numbers
print("Is 7 in the List:", is_number_7_present)
