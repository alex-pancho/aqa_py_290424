import csv
import os

# Определяем пути к файлам
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
csv_folder = os.path.join(base_path, 'ideas_for_test', 'work_with_csv')
file1_path = os.path.join(csv_folder, 'r-m-c.csv')
file2_path = os.path.join(csv_folder, 'rmc.csv')
output_file_path = os.path.join(os.path.dirname(__file__), 'result_kotsar.csv')


# Функция чтения CSV файла и возврата списка строка
def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Функция записи списка строк в CSV файл
def write_csv(file_path, rows):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


# Читаем данные из обоих файлов
rows1 = read_csv(file1_path)
rows2 = read_csv(file2_path)

# Преобразуем строки в множества для поиска уникальных значений
set1 = set(tuple(row) for row in rows1)
set2 = set(tuple(row) for row in rows2)

# Найдём уникальные строки
unique_rows = set1.union(set2)

# Преобразуем обратно в список списков
unique_rows_list = [list(row) for row in unique_rows]

# Запишем результат в новый CSV файл
write_csv(output_file_path, unique_rows_list)

print(f'Результаты записаны в файл {output_file_path}')
