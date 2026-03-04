
def greet_student(name):
    return f"Hello, {name}"

def calculate_stats(scores):
    subjects = len(scores)
    average = sum(scores) / subjects
    return subjects, average

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Alice"
    scores = [70, 60, 65]
    
    greeting = greet_student(name)
    subjects, average = calculate_stats(scores)
    result = evaluate_result(average)
    
    print(greeting)
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", result)

# Start the program
main()