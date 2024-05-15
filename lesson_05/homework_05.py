small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_elements = set(small_list)
print("Унікальні елементи в маленькому списку:", unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average = sum(small_list) / len(small_list)
print("Середнє арифметичне всіх елементів в маленькому списку:", average)

# task 3. Перевірте, чи є в списку big_list дублікати

duplicates = len(big_list) != len(set(big_list))
if duplicates:
    print("В великому списку є дублікати.")
else:
    print("У великому списку немає дублікатів.")

#dictionary
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict, key=add_dict.get)
print("Ключ з максимальним значенням у словнику add_dict:", max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

flipped_base_dict = {value: key for key, value in base_dict.items()}
flipped_add_dict = {value: key for key, value in add_dict.items()}

print("Словник, в якому ключі та значення будуть замінені місцями у base_dict:", flipped_base_dict)
print("Словник, в якому ключі та значення будуть замінені місцями у add_dict:", flipped_add_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

for key, value in base_dict.items():
    sum_dict[key] = value

for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value

print("Об'єднаний словник sum_dict:", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

line_set = set(line)
print("Множина всіх символів в line:", line_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

unique_elements = set_1 | set_2
sum_of_unique_elements = sum(unique_elements - (set_1 & set_2))
print("Сума елементів двох множин, які не є спільними:", sum_of_unique_elements)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [4, 5, 6, 7]
list_2 = [7, 8, 9, 1]
list = list_1 + list_2
unique_elements = set(list)
result_set = {x for x in unique_elements if list.count(x) == 1}
print("Сет, який містить всі елементи з обох списків, які зустрічаються тільки один раз:", result_set)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
age_ranges_dict = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}

for person, age in person_list:
    if 10 <= age <= 19:
        age_ranges_dict['10-19'].append(person)
    elif 20 <= age <= 29:
        age_ranges_dict['20-29'].append(person)
    elif 30 <= age <= 39:
        age_ranges_dict['30-39'].append(person)
    elif 40 <= age <= 49:
        age_ranges_dict['40-49'].append(person)

print("Словник з людьми у вікових діапазонах:", age_ranges_dict)