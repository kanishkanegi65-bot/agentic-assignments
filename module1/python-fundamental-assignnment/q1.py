# User Age Calculator

birth_year = input("Enter your birth year: ")

# explicit type conversion
birth_year = int(birth_year)

current_year = 2026
age = current_year - birth_year

print(f"You are {age} years old.")