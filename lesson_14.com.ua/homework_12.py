from pathlib import Path
import csv
import os
import json
import xml.etree.ElementTree as ET

current_file_path = Path(__file__)

# Task 1

file1_path = current_file_path.parent.parent / "ideas_for_test" / "work_with_csv" / "random.csv"
file2_path = current_file_path.parent.parent / "ideas_for_test" / "work_with_csv" / "random-michaels.csv"
result_file_path = current_file_path.parent / "result_Nechytailo.csv"

def read_csv(file_path):
    with open (file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

data1 = read_csv(file1_path)
data2 = read_csv(file2_path)

combined_data = data1 + data2
unique_data = []
seen = set()
for row in combined_data:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

with open(result_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(unique_data)

print(f'Результат записан в файл {result_file_path}')

# Task 2

folder_path = current_file_path.parent.parent / "ideas_for_test" / "work_with_json"
log_file_path = current_file_path.parent / "json_Nechytailo.log"

invalid_files = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith('.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json.load(file)
        except json.JSONDecodeError:
            invalid_files.append(filename)
            print(f'Invalid JSON: {filename}')


with open (log_file_path, 'w', encoding='utf-8') as log_file:
    for invalid_file in invalid_files:
        log_file.write(f"Invalid JSON: {invalid_file}\n")



# Task 3

input_file_xml = current_file_path.parent.parent / 'ideas_for_test' / 'work_with_xml' / 'groups.xml'

def group_search(number):
    try:
        tree = ET.parse(input_file_xml)
        root = tree.getroot()

        # Знаходимо всі елементи group з вказаним номером
        groups = root.findall(f".//group[number='{number}']")
        if not groups:
            print(f"Група з номером {number} не знайдена.")
            return None

        # Отримуємо значення timingExbytes/incoming першої знайденої групи
        group = groups[0]
        timing_exbytes_incoming = group.find('timingExbytes/incoming')
        if timing_exbytes_incoming is not None:
            return timing_exbytes_incoming.text
        else:
            print("Елемент 'timingExbytes/incoming' не знайдено для цієї групи.")
            return None

    except ET.ParseError as e:
        print(f"XML pasrsing error: {e}")
        return None


# Викликаємо функцію та виводимо результат
print(group_search('0'))
