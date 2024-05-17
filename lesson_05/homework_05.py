small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print(f'\nUnique elements in a list \'small_list\' are: {set(small_list)}')

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average_small_list = sum(small_list) / len(small_list)
print(f'\nAverage value of a list \'small_list\' is: {average_small_list}')

# task 3. Перевірте, чи є в списку big_list дублікати
original_big_list_length = len(big_list)
unique_big_list_length = len(set(big_list))

if original_big_list_length == unique_big_list_length:
    print('\nThere are a unique values in a list \'big_list\'')
else:
    print('\nThere are a duplicates in a list \'big_list\'')

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_value_add_dict = 0
max_key_add_dict = None

for key, value in add_dict.items():
    if value > max_value_add_dict:
        max_value_add_dict = value
        max_key_add_dict = key

print(f'\nKey with a max value in a dict \'add_dict\' is: {max_key_add_dict}')

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
my_own_dict = {'name': 'Serhii', 'age': 29, 'gender': 'male'}
flipped_dict = dict(zip(my_own_dict.values(), my_own_dict.keys()))
print(f'\nOriginal dict is: {my_own_dict}')
print(f'Vice verses dict is: {flipped_dict}')

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict | add_dict

for key in sum_dict:
    base_value = base_dict.get(key, '')
    add_value = add_dict.get(key, '')

    sum_dict[key] = str(base_value) + str(add_value)

print(f'\nTwo dict in one: {sum_dict}')

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
unique_chars = set(line)

print(f'\nUnique chars in a line: {unique_chars}')

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_3 = list(set_1 ^ set_2)
total_set_3_sum = 0

for el in set_3:
    total_set_3_sum += el

print(f'\nThe sum of the elements of two sets that are not common is: {total_set_3_sum}')

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
first_list = [1, 2, 3, 4]
second_list = [3, 4, 5, 6]
third_list = []
third_list_intersection = list(set(first_list) & set(second_list))
third_list_union = list(set(first_list) | set(second_list))

for el in third_list_union:
    third_list.append(el)
    if el in third_list_intersection:
        third_list.remove(el)

print(f'\nList with no repeating elements: {third_list}')

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
age_ranges = {}

for name, age in person_list:
    age_range = (age // 10) * 10
    age_range_label = f'{age_range}-{age_range+9}'

    if age_range_label not in age_ranges:
        age_ranges[age_range_label] = [name]
    else:
        age_ranges[age_range_label].append(name)

print(f'\nNew dictionary: {age_ranges}')
