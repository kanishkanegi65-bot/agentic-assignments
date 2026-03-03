# Secure Transaction Validator

balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified? (True/False): ")

# Convert string to Boolean safely
if verified_input.lower() == "true":
    verified = True
elif verified_input.lower() == "false":
    verified = False
else:
    print("Invalid verification input. Please enter True or False.")
    exit()

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")