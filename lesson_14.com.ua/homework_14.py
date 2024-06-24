"""# Робота з файлами - Csv, json, xml

Складність:  середня

# task 1

Візміть два файли з теки
[ideas_for_test/work_with_csv](/ideas_for_test/work_with_csv)
порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv

# task 2

Провалідуйте, чи усі файли у папці
[ideas_for_test/work_with_json](/ideas_for_test/work_with_json)
є валідними json.
результат для невалідного файлу виведіть через print та у файл json__<your_second_name>.log

# task 3

Для файла [ideas_for_test/work_with_xml/groups.xml](/ideas_for_test/work_with_xml/groups.xml)
створіть функцію  пошуку по group/number і
повернення значення timingExbytes/incoming
результат виведіть у консоль через  print

# Як робити домашне завдання у Git:

## 0. ОБОВ’ЯЗКОВО створити нову гілку

1. **Виконати ДЗ у окремому файлі homework_<#lesson>.py**
2. **Закомітити створений код**
3. **Створити ПУЛ-РЕКВЕСТ у власний репозиторій У ГІЛКУ main**
4. **Назначити ревьювером викладача**
5. **Посилання на PR вставити у форму відповіді**
"""

import csv
from pathlib import Path

print("\n Task 01")
file1 = Path('ideas_for_test/work_with_csv/r-m-c.csv')
file2 = Path('ideas_for_test/work_with_csv/random-michaels.csv')

def read_file(file_path):
    with file_path.open('r', encoding='utf-8') as f:
        content = f.readlines()
    return content

def write_file(file_path, content):
    with file_path.open('w', encoding='utf-8') as f:
        f.writelines(content)
rows1 = read_file(file1)
rows2 = read_file(file2)
combined_rows = rows1 + rows2
unique_rows = list(set(combined_rows))
unique_rows.sort()
result_file = Path('result_Suduk.csv')
write_file(result_file, unique_rows)
print(f"The result is saved in the file {result_file}")

print("\n Task 02")

import os
import json

def is_json_valid(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except json.JSONDecodeError:
        return False

def validate_json_files(directory):
    log_file_path = os.path.join(directory, 'json_Suduk.log')
    json_files = [
        'localizations_en.json',
        'localizations_ru.json',
        'login.json',
        'swagger.json'
    ]

    invalid_files = []

    for filename in json_files:
        file_path = os.path.join(directory, filename)
        if not is_json_valid(file_path):
            invalid_files.append(filename)
            print(f"Invalid JSON: {filename}")

    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        for filename in invalid_files:
            log_file.write(f"Invalid JSON: {filename}\n")

if __name__ == "__main__":
    directory = 'ideas_for_test/work_with_json'
    validate_json_files(directory)



print("\n Task 03")

import xml.etree.ElementTree as ET

def find_incoming_by_group_number(file_path, group_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Шукаємо групу за номером
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == group_number:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    return incoming.text

    return None

if __name__ == "__main__":
    file_path = 'ideas_for_test/work_with_xml/groups.xml'
    group_number = '2'  
    result = find_incoming_by_group_number(file_path, group_number)
    if result:
        print(f"Incoming value for group number {group_number}: {result}")
    else:
        print(f"No incoming value found for group number {group_number}")
