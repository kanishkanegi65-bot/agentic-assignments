def read_numbers(file_name):
    numbers_list = []
    
    with open(file_name, 'r') as file:
        print("File opened successfully")
        
        for line in file:
            clean_line = line.strip()
            if clean_line:  # Ignore empty lines
                numbers_list.append(int(clean_line))
    
    print("Data loaded")
    return numbers_list


def compute_values(numbers_list):
    total_count = len(numbers_list)
    total_sum = sum(numbers_list)
    average_value = total_sum / total_count if total_count > 0 else 0

    print("Computation completed")
    return total_count, total_sum, average_value


def write_logs(log_file, count, total_sum, average):
    with open(log_file, 'a') as file:
        file.write("File opened successfully\n")
        file.write(f"Read {count} numbers\n")
        file.write(f"Sum: {total_sum}\n")
        file.write(f"Average: {average}\n")
        file.write("Processing completed\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"

    numbers = read_numbers(input_file)
    count, total_sum, average = compute_values(numbers)
    write_logs(log_file, count, total_sum, average)


if __name__ == "__main__":
    main()