# AI Data Query and Ranking System
# Using Pandas to simulate querying and analyzing an AI dataset

import pandas as pd

# -----------------------------------------------------
# STEP 1: Create Sample Dataset
# -----------------------------------------------------

data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan", "Priya", "Vikas", "Neha"],
    "Score": [78, 88, 92, 67, 95, 85, 90, 82],
    "Passed": [True, True, True, False, True, True, True, True],
    "Category": ["B", "A", "A", "C", "A", "B", "A", "B"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")


# -----------------------------------------------------
# STEP 2: Select Single Column
# -----------------------------------------------------

print("Single Column (Score):")
score_column = df["Score"]
print(score_column)
print("\n")


# -----------------------------------------------------
# STEP 3: Select Multiple Columns
# -----------------------------------------------------

print("Multiple Columns (Name, Score):")
selected_df = df[["Name", "Score"]]
print(selected_df)
print("\n")


# -----------------------------------------------------
# STEP 4: Use iloc (first 3 rows)
# -----------------------------------------------------

print("First 3 rows using iloc:")
print(df.iloc[:3])
print("\n")


# -----------------------------------------------------
# STEP 5: Use loc with meaningful index
# -----------------------------------------------------

df_indexed = df.set_index("Name")

print("Using loc (retrieve data for 'Aman'):")
print(df_indexed.loc["Aman"])
print("\n")


# -----------------------------------------------------
# STEP 6: Filter Score > 85
# -----------------------------------------------------

high_score = df[df["Score"] > 85]

print("Students with Score > 85:")
print(high_score)
print("\n")


# -----------------------------------------------------
# STEP 7: Filter Score > 85 AND Passed = True
# -----------------------------------------------------

high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Students with Score > 85 AND Passed:")
print(high_passed)
print("\n")


# -----------------------------------------------------
# STEP 8: Sort filtered result (descending Score)
# -----------------------------------------------------

sorted_high = high_passed.sort_values(by="Score", ascending=False)

print("Sorted High Performers (Descending Score):")
print(sorted_high)
print("\n")


# -----------------------------------------------------
# STEP 9: Chained filtering + sorting
# -----------------------------------------------------

print("Chained Operation (Score > 85 & Passed, sorted):")
chained_result = df[(df["Score"] > 85) & (df["Passed"])].sort_values(by="Score", ascending=False)
print(chained_result[["Name", "Score"]])
print("\n")
