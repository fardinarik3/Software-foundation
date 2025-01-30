import sys
import csv


def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores)


def assign_grade(average):
    """Assign a grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def determine_pass_or_fail(average):
    """Determine if the student passed or failed."""
    return "Pass" if average >= 50 else "Fail"


def find_min_score(scores):
    """Find the minimum score from the list."""
    return min(scores)


def find_max_score(scores):
    """Find the maximum score from the list."""
    return max(scores)


def read_csv(file_path):
    """Read data from the input CSV file."""
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header row
            data = [row for row in reader if any(row)]  # Skip empty rows
        return header, data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def process_data(data):
    """Process the student data, calculating averages, grades, and other stats."""
    processed_data = []
    for row in data:
        if len(row) >= 4:  # Ensure the row has enough values
            try:
                name = row[0]
                scores = list(map(int, row[1:4]))  # Convert scores to integers
                average = calculate_average(scores)
                grade = assign_grade(average)
                min_score = find_min_score(scores)
                max_score = find_max_score(scores)
                result = determine_pass_or_fail(average)
                processed_data.append([name] + scores + [average, grade, min_score, max_score, result])
            except ValueError:
                print(f"Error: Invalid data for student {row[0]}. Skipping row.")
        else:
            print(f"Warning: Skipping incomplete row: {row}")
    return processed_data


def write_csv(file_path, header, data):
    """Write processed data to the output CSV file."""
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header + ['Average', 'Grade', 'Min Score', 'Max Score', 'Result'])  # Add new columns
            writer.writerows(data)
        print(f"Results saved to '{file_path}'")
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python Process_Data.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Process the data
    header, student_data = read_csv(input_file)
    processed_data = process_data(student_data)
    write_csv(output_file, header, processed_data)
