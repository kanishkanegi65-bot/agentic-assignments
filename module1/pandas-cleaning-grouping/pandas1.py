import pandas as pd
import numpy as np

# 🔹 Sample Data
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("🔹 Original DataFrame:\n")
print(df)

# 🔹 Detect missing values
print("\n🔹 Missing Values:\n")
print(df.isnull())

# 🔹 Fill missing Salary with mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\n🔹 DataFrame after filling missing Salary:\n")
print(df)

# 🔹 Drop Temporary_Notes column
df.drop(columns=["Temporary_Notes"], inplace=True)

# 🔹 Rename Salary to Annual_Salary
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\n🔹 Cleaned DataFrame:\n")
print(df)

# 🔹 Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\n🔹 Final Summary Table:\n")
print(summary)