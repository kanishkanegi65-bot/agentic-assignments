# Student Marks Analyzer

marks = [78, 85, 90, 65, 88, 92, 80, 75]

print("Full list:", marks)

# Slicing
print("First 3 marks:", marks[:3])
print("Last 3 marks:", marks[-3:])

# Calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", round(average, 2))