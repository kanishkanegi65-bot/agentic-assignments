# Contact Book

contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Rahul": "9988776655"
}

print("Contact List:")
for name, number in contacts.items():
    print(name, ":", number)

search_name = input("Enter name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")
    