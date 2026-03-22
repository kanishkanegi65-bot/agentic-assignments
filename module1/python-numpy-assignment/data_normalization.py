import numpy as np

# Step 1: Create data
data = np.array([10, 20, 30, 40, 50, 60])

# Step 2: Compute mean and std
mean = np.mean(data)
std = np.std(data)

# Step 3: Normalize
normalized = (data - mean) / std

# Step 4: Reshape (AFTER normalization)
reshaped = normalized.reshape(2, 3)

# Step 5: Print
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized data:", normalized)
print("Reshaped data:\n", reshaped)
print("Shape:", reshaped.shape)