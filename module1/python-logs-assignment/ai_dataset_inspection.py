# AI Dataset Inspection Pipeline
# This program simulates the first stage of an AI data workflow using Pandas

import pandas as pd

# -----------------------------------------------------
# STEP 1: Create a sample dataset and save as CSV
# -----------------------------------------------------

data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan", "Priya", "Vikas", "Neha", "Arjun", "Pooja"],
    "Age": [21, 22, 20, 23, 24, 21, 22, 20, 23, 24],
    "Score": [78, 85, 90, 67, 88, 92, 75, 81, 95, 70],
    "Label": ["Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass", "Fail"]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sample_ai_dataset.csv", index=False)

print("CSV file created successfully.\n")


# -----------------------------------------------------
# STEP 2: Load dataset using pd.read_csv()
# -----------------------------------------------------

dataset = pd.read_csv("sample_ai_dataset.csv")

print("Dataset loaded successfully.\n")


# -----------------------------------------------------
# STEP 3: Display first 5 rows
# -----------------------------------------------------

print("First 5 rows:")
print(dataset.head())
print("\n")


# -----------------------------------------------------
# STEP 4: Display last 5 rows
# -----------------------------------------------------

print("Last 5 rows:")
print(dataset.tail())
print("\n")


# -----------------------------------------------------
# STEP 5: Display dataset information
# -----------------------------------------------------

print("Dataset Info:")
print(dataset.info())
print("\n")


# -----------------------------------------------------
# STEP 6: Display summary statistics
# -----------------------------------------------------

print("Summary Statistics:")
print(dataset.describe())
print("\n")


# -----------------------------------------------------
# STEP 7: Select a single column
# -----------------------------------------------------

age_column = dataset["Age"]

print("Single Column (Age):")
print(age_column)
print("\n")


# -----------------------------------------------------
# STEP 8: Select multiple columns
# -----------------------------------------------------

selected_columns = dataset[["Name", "Score"]]

print("Multiple Columns (Name and Score):")
print(selected_columns)
print("\n")


# -----------------------------------------------------
# STEP 9: Filter rows based on a numerical condition
# -----------------------------------------------------

filtered_data = dataset[dataset["Score"] > 80]

print("Filtered rows (Score > 80):")
print(filtered_data)
print("\n")
