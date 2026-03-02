# Simple Accuracy Reporter

accuracy_input = input("Enter model accuracy: ")

try:
    # explicit type conversion
    accuracy = float(accuracy_input)
    print(f"Model accuracy is {accuracy}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")