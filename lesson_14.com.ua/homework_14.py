

# import csv
#
# def read_csv_file(file_path):
#    with open(file_path, newline='', encoding='utf-8') as csvfile:
#        reader = csv.reader(csvfile)
#        data = [tuple(row) for row in reader]
#    return data
#
# def write_csv_file(file_path, data):
#    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
#        writer = csv.writer(csvfile)
#        writer.writerows(data)
#
# def remove_duplicates(file1, file2, result_file):
#
#    data1 = read_csv_file(file1)
#    data2 = read_csv_file(file2)
#
#    set1 = set(data1)
#    set2 = set(data2)
#
#
#    unique_data = list(set1.symmetric_difference(set2))
#
#    write_csv_file(result_file, unique_data)
#
# file1 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_csv/random.csv'
# file2 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_csv/rmc.csv'
# result_file = 'result_tesliuk.csv'
#
# remove_duplicates(file1, file2, result_file)
#
# print(f"Результат збережено у файл {result_file}")



# import json
# import os
#
# def validate_json(file_path):
#
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             json.load(file)
#         return True
#     except json.JSONDecodeError as e:
#         return str(e)
#
# def validate_all_json_files(file_paths, log_file):
#
#     with open(log_file, 'w', encoding='utf-8') as log:
#         for file_path in file_paths:
#             result = validate_json(file_path)
#             if result is not True:
#                 message = f"Файл {file_path} не є валідним JSON: {result}"
#                 print(message)
#                 log.write(message + '\n')
#
#
# file1 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_json/localizations_en.json'
# file2 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_json/localizations_ru.json'
# file3 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_json/login.json'
# file4 = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_json/swagger.json'
# log_file = 'json__tesliuk.log'
#
# file_paths = [file1, file2, file3, file4]
#
# validate_all_json_files(file_paths, log_file)


import xml.etree.ElementTree as ET

def find_incoming_value(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall(".//group"):
            number = group.find('number')
            if number is not None and number.text == group_number:
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        return incoming.text
        return f"Група з номером {group_number} не знайдена або не має елемента incoming."
    except ET.parseError as e:
        return f"Помилка парсингу XML: {e}"

file_path = r'C:\Users\влад\PycharmProjects\aqa_py_290424/ideas_for_test/work_with_xml/groups.xml'
group_number = '5'
incoming_value = find_incoming_value(file_path, group_number)
print(f"Значення timingExbytes/incoming для групи {group_number}: {incoming_value}")