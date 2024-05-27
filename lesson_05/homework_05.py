# small_list = [3, 1, 4, 5, 2, 5, 3]
# big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

# task 1. Знайдіть всі унікальні елементи в списку small_list

small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements = list(set(small_list))
print("Унікальні елeменти:", unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average = sum(small_list) / len(small_list)
print("Середнє аріфм:", average)

# task 3. Перевірте, чи є в списку big_list дублікати

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
has_duplicates = len(big_list) == len(set(big_list))
print(has_duplicates)

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_key = max(add_dict, key=add_dict.get)
print("Ключ з максимальним значенням:", max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

reversed_dict = {value: key for key, value in add_dict.items()}
print("Новий словник зі зміненими ключами та значеннями:", reversed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
sum_dict = {}
for key, value in base_dict.items():
    if key in add_dict:
        sum_dict[key] = str(value) + str(add_dict[key])
    else:
        sum_dict[key] = value
for key, value in add_dict.items():
    if key not in base_dict:
        sum_dict[key] = value
print("Об'єднаний словник sum_dict:", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars = set(line)
print("Множина всіх унікальних символів у рядку:", unique_chars)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_elements = set_1.symmetric_difference(set_2)
sum_of_unique_elements = sum(unique_elements)
print("Сума елементів двох множин:", sum_of_unique_elements)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

from collections import Counter

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

combined_list = list_1 + list_2
counted_elements = Counter(combined_list)
unique_elements_set = {element for element, count in counted_elements.items() if count == 1}
print("Сет:", unique_elements_set)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

age_groups = {}

for name, age in person_list:
    if 10 <= age <= 19:
        age_range = '10-19'
    elif 20 <= age <= 29:
        age_range = '20-29'
    elif 30 <= age <= 39:
        age_range = '30-39'
    elif 40 <= age <= 49:
        age_range = '40-49'
    else:
        continue

    if age_range in age_groups:
        age_groups[age_range].append(name)
    else:
        age_groups[age_range] = [name]

print("Словник вікових діапазонів:", age_groups)
