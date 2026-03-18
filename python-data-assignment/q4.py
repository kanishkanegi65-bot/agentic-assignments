# User Data Processing System

def calculate_average(scores):
    return sum(scores) / len(scores)

def has_admin_access(roles):
    return "admin" in roles

def main():
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 72],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 82, 84],
            "roles": {"editor"}
        }
    ]

    for user in users:
        avg = calculate_average(user["scores"])
        admin = has_admin_access(user["roles"])

        print("\nName:", user["name"])
        print("Average Score:", round(avg, 2))
        print("Admin Access:", admin)

# Run program
if __name__ == "__main__":
    main()

    