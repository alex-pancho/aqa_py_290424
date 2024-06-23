import os
import json

# Определяем путь к папке с JSON файлами
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
json_folder = os.path.join(base_path, 'ideas_for_test', 'work_with_json')
log_file_path = os.path.join(os.path.dirname(__file__), 'json_kotsar.log')


# Функция для проверки валидности JSON
def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)


# Список для хранения информации о невалидных файлах
invalid_files = []

# Проверка каждого файла в папке
for filename in os.listdir(json_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(json_folder, filename)
        is_valid, error_message = validate_json(file_path)
        if not is_valid:
            invalid_files.append({'file': filename, 'error': error_message})
            print(f"Invalid JSON file: {filename}, Error: {error_message}")


# Запись результата в лог файл
with open(log_file_path, 'w', encoding='utf-8') as log_file:
    for entry in invalid_files:
        log_file.write(f"Invalid JSON file: {entry['file']}, Error: {entry['error']}\n")
