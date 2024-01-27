temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1
second_week_temperatures = temperatures[7:14]
print("Second Week Temperatures:", second_week_temperatures)

# Task 2
above_100_temperatures = [temp for temp in temperatures if temp > 100]
print("Temperatures Above 100:", above_100_temperatures)

# Task 3
reversed_temperatures = temperatures[::-1]
reversed_slice = reversed_temperatures[4:10]
print("Reversed Slice:", reversed_slice)
