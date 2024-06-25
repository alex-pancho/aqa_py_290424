import csv
import os
import json

# task 1
def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def remove_duplicates(data1, data2):
    combined_data = data1 + data2
    unique_data = []
    seen = set()

    for row in combined_data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)

    return unique_data

file1_path = '../ideas_for_test/work_with_csv/rmc.csv'
file2_path = '../ideas_for_test/work_with_csv/r-m-c.csv'
result_file_path = 'result_Tashchi.csv'

# Прочитання даних з файлів
data1 = read_csv(file1_path)
data2 = read_csv(file2_path)

# Видалення дублікатів
unique_data = remove_duplicates(data1, data2)

# Запис унікальних даних у новий файл
write_csv(result_file_path, unique_data)

print(f"Унікальні рядки записані у файл {result_file_path}")

#task2


def is_valid_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except (json.JSONDecodeError, IOError) as e:
        return False, str(e)

def validate_json_files(directory):
    log_file_path = 'json_Tashchi.log'
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                is_valid, error_message = is_valid_json(file_path)
                if not is_valid:
                    print(f"File {filename} is not a valid JSON: {error_message}")
                    log_file.write(f"File {filename} is not a valid JSON: {error_message}\n")

directory_path = '../ideas_for_test/work_with_json'
validate_json_files(directory_path)
