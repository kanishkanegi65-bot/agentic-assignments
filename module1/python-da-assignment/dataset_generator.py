import numpy as np


def generate_dataset(num_samples, num_features):
    """
    Generate a random dataset using NumPy
    """
    np.random.seed(42)  # Reproducibility
    data = np.random.rand(num_samples, num_features)
    return data


def normalize_dataset(data):
    """
    Compute mean, std and normalize using broadcasting
    """
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    normalized = (data - mean) / std
    return normalized, mean, std


def split_dataset(normalized_data):
    """
    Split dataset into training (80%) and test (20%)
    """
    num_samples = normalized_data.shape[0]
    split_index = int(0.8 * num_samples)

    train_data = normalized_data[:split_index]
    test_data = normalized_data[split_index:]

    return train_data, test_data


def demonstrate_view_behavior(normalized_data, train_data):
    """
    Modify slice and show it affects original array
    """
    print("\nBefore modification:")
    print("Original[0,0]:", normalized_data[0, 0])
    print("Train[0,0]:", train_data[0, 0])

    # Modify training slice
    train_data[0, 0] = 999

    print("\nAfter modification:")
    print("Original[0,0]:", normalized_data[0, 0])
    print("Train[0,0]:", train_data[0, 0])

    print("\nNote: Modifying the slice affected the original array because slicing returns a VIEW, not a copy.")


def main():
    num_samples = 100
    num_features = 3

    # Step 1: Generate data
    data = generate_dataset(num_samples, num_features)

    # Step 2: Normalize
    normalized_data, mean, std = normalize_dataset(data)

    # Step 3: Split
    train_data, test_data = split_dataset(normalized_data)

    # Step 4: Print shapes
    print("Original data shape:", data.shape)
    print("Mean shape:", mean.shape)
    print("Standard deviation shape:", std.shape)
    print("Training data shape:", train_data.shape)
    print("Test data shape:", test_data.shape)

    # Step 5: Demonstrate view behavior
    demonstrate_view_behavior(normalized_data, train_data)


if __name__ == "__main__":
    main()