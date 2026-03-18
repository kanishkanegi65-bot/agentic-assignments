# Employee Role Checker

employee = (101, "Amit", "IT")
roles = {"editor", "viewer", "admin"}

# Tuple data
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])

# Check admin role
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")