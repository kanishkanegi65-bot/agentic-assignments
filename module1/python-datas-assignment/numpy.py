import numpy as np


def generate_dataset(num_samples, num_features):
    np.random.seed(42)  # Reproducibility
    data = np.random.randint(1, 100, size=(num_samples, num_features))
    return data


def compute_statistics(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return mean, std


def normalize_data(data, mean, std):
    normalized_data = (data - mean) / std  # Broadcasting
    return normalized_data


def split_dataset(normalized_data):
    split_index = int(0.8 * normalized_data.shape[0])
    
    training_data = normalized_data[:split_index]
    test_data = normalized_data[split_index:]
    
    return training_data, test_data


def demonstrate_view_behavior(training_data, normalized_data):
    # Modify a value in the training set
    original_value = normalized_data[0, 0]
    training_data[0, 0] = 999

    if normalized_data[0, 0] == 999:
        message = "Note: Modifying the slice affected the original array (view behavior confirmed)"
    else:
        message = "Note: Slice did not affect original array (copy behavior)"

    return original_value, normalized_data[0, 0], message


def main():
    num_samples = 100
    num_features = 3

    data = generate_dataset(num_samples, num_features)
    mean, std = compute_statistics(data)
    normalized_data = normalize_data(data, mean, std)

    training_data, test_data = split_dataset(normalized_data)

    original_val, modified_val, message = demonstrate_view_behavior(training_data, normalized_data)

    print("Original data shape:", data.shape)
    print("Mean shape:", mean.shape)
    print("Standard deviation shape:", std.shape)
    print("Training data shape:", training_data.shape)
    print("Test data shape:", test_data.shape)
    print(message)


if __name__ == "__main__":
    main()