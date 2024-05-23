small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_elements = list(set(small_list))
print(f'Всі унікальні елементи в списку small_list -> {unique_elements}')
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = sum(small_list) / len(small_list)
print(f'Середнє арифмитичне елементів у small_list -> {average}')
# task 3. Перевірте, чи є в списку big_list дублікати
big_list_without_duplicates = list(set(big_list))
has_duplicates = big_list != big_list_without_duplicates
print(f'Чи є в списку big_list дублікати? -> {has_duplicates}')

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_key = max(add_dict, key=add_dict.get)
print(f'Ключ з максимальним значенням у add_dict -> {max_key}')
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {}
for key, value in base_dict.items():
    new_dict[value] = key
print(f'Новий словник, в якому ключі та значення замінені місцями -> {new_dict}')
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
print(f"Об'єднаний словник -> {sum_dict}")
# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_values = tuple(line) # Якщо просто розбити лайн посимвольно з дублікатами
new_values2 = set(line) # Якщо розбити лайн посимвольно тільки з унікальних значень
# Про всяк випадок виведу і так, і так
print(new_values)
print(new_values2)
# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum = sum(set_1 ^ set_2)
print(f'Сума елементів двох множин, які не є спільними -> {sum}')
# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
set_3 = {1, 2, 4, 5, 7, 9, 12, 14, 15, 21}
set_4 = {1, 2, 14, 9, 41, 22, 35, 36, 37, 42}
unique_set = set_3.union(set_4)
print(f'Елементи з обох списків,  які зустрічаються тільки один раз -> {unique_set}')

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_ranges = {'10-19': [], '20-29': [], '30-39': [], '40-49': [], '50+': []}

for name, age in person_list:
    if age >= 10 and age <= 19:
        age_range = '10-19'
    elif age >= 20 and age <= 29:
        age_range = '20-29'
    elif age >= 30 and age <= 39:
        age_range = '30-39'
    elif age >= 40 and age <= 49:
        age_range = '40-49'
    else:
        age_range = '50+'

    age_ranges[age_range].append(name)
print(f"Словник з іменами за віковими діапазонами -> {age_ranges}")

