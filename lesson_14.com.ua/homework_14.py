import csv
import os
import json
from pathlib import Path
import xml.etree.ElementTree as ET

current_file_path = Path(__file__)

#Task 1

input_file1 = current_file_path.parent.parent / 'ideas_for_test\\work_with_csv\\random.csv'
input_file2 = current_file_path.parent.parent / 'ideas_for_test\\work_with_csv\\random-michaels.csv'
output_file = current_file_path.parent / 'result_iuich_bogdana.csv'
with open(input_file1) as csv_f:
    with open(input_file2) as csv_f2:
        with open(output_file, 'w', newline='') as csv_f3:
            reader = csv.reader(csv_f)
            reader2 = csv.reader(csv_f2)
            unique = []
            for i in reader:
                if i not in reader2:
                    unique.append(i)
                csv_f2.seek(0)
            csv_f.seek(0)
            for j in reader2:
                if j not in reader:
                    unique.append(j)
                csv_f.seek(0)
            writer = csv.writer(csv_f3, delimiter=",")
            writer.writerows(unique)

#Task 2

input_json_directory = current_file_path.parent.parent / 'ideas_for_test\\work_with_json'
output_log_file = current_file_path.parent /'json_Iuich_bogdana.log'
list_of_files = os.listdir(input_json_directory)
for my_file in list_of_files:
    file_path = input_json_directory / my_file
    with open(file_path, 'r', encoding='utf-8') as json_f:
        try:
            data = json.load(json_f)
        except json.decoder.JSONDecodeError as e:
            print("Error json proccessing:", e)
            with open(output_log_file, 'w') as log_file:
                log_file.write(str(e))


#Task 3

input_file_xml = current_file_path.parent.parent / 'ideas_for_test\\work_with_xml\\groups.xml'
def group_search(number):
    v = root.findall(f".//group[number='{number}']")
    values = [x.text for x in v]
    for child in v:
        value = child.find('timingExbytes/incoming')
        if value is None:
            print("NONE")
            continue
    return value.text
tree = ET.parse(input_file_xml)
root = tree.getroot()
print(group_search(0))












