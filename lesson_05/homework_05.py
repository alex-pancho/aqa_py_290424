small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_elements = list(set(small_list))
print(f"Унікальні елементи в списку small_list: {unique_elements}")


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average_small_list = sum(small_list) / len(small_list)
print(f"Середнє арифметичне всіх елементів у списку small_list: {average_small_list}")


# task 3. Перевірте, чи є в списку big_list дублікати
has_duplicates = len(big_list) != len(set(big_list))
print(f"Чи є в списку big_list дублікати: {has_duplicates}")


base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_key = max(add_dict, key=add_dict.get)
print(f"Ключ з максимальним значенням у словнику add_dict: {max_key}")


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
flipped_add_dict = {value: key for key, value in add_dict.items()}
print(f"Словник з ключами та значеннями, поміняними місцями: {flipped_add_dict}")


# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key in set(base_dict.keys()).union(add_dict.keys()):
    if key in base_dict and key in add_dict:
        sum_dict[key] = str(base_dict[key]) + str(add_dict[key])
    elif key in base_dict:
        sum_dict[key] = base_dict[key]
    else:
        sum_dict[key] = add_dict[key]
print(f"Об'єднаний словник base_dict та add_dict: {sum_dict}")


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars_set = set(line)
print(f"Множина унікальних символів у рядку line: {unique_chars_set}")


# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_of_unique_elements = sum(set_1.symmetric_difference(set_2))
print(f"Сума елементів двох множин, які не є спільними: {sum_of_unique_elements}")


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
unique_elements_set = set(list1).symmetric_difference(set(list2))
print(f"Сет з унікальними елементами з обох списків: {unique_elements_set}")


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_ranges = {'10-19': [], '20-29': [], '30-39': [], '40-49': []}
for person in person_list:
    name, age = person
    if 10 <= age <= 19:
        age_ranges['10-19'].append(name)
    elif 20 <= age <= 29:
        age_ranges['20-29'].append(name)
    elif 30 <= age <= 39:
        age_ranges['30-39'].append(name)
    elif 40 <= age <= 49:
        age_ranges['40-49'].append(name)

print(f"Словник з іменами за віковими діапазонами: {age_ranges}")