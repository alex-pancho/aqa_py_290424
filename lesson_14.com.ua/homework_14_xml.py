import os
import xml.etree.ElementTree as ET

# Определяем путь к файлам
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
xml_folder = os.path.join(base_path, 'ideas_for_test', 'work_with_xml')
xml_file_path = os.path.join(xml_folder, 'groups.xml')


# Функция для поиска значения timingExbytes/incoming по номеру группы
def find_incoming_by_group_number(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Проходим по всем элементам group
        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        return incoming.text

        return None

    except ET.ParseError as e:
        print(f'Error parsing XML file: {e}')
        return None


# Пример использования функции
group_number = 0
incoming_value = find_incoming_by_group_number(xml_file_path, group_number)
if incoming_value:
    print(f'Incoming value for group {group_number}: {incoming_value}')
else:
    print(f"Group {group_number} not found or no incoming value available")
