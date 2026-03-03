# Access Control System

age = int(input("Enter your age: "))
has_id_input = input("Do you have an ID card? (True/False): ")

# Convert string to Boolean safely
if has_id_input.lower() == "true":
    has_id = True
elif has_id_input.lower() == "false":
    has_id = False
else:
    print("Invalid input for ID status. Please enter True or False.")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")