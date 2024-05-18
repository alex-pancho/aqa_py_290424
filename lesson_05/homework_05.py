small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

print(set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

print(sum(small_list) // 7)

# task 3. Перевірте, чи є в списку big_list дублікати

big_set = set(big_list)
if big_list != big_set:
    print("The big_list list contains duplicate values")
else:
    print("The big_list list does not contain duplicate values")


base_dict = {'country': 'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

print(max(add_dict))

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_dict = base_dict.copy()
new_dict_with_swapped_places = {}
for key, value in new_dict.items():
    if isinstance(value, (str, int, float, tuple)):
        new_dict_with_swapped_places[value] = key
print(new_dict_with_swapped_places)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = base_dict | add_dict
print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
diff = set_1.symmetric_difference(set_2)
print(sum(diff))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

first_list = [1, 2, 3, 4, 5, 6]
second_list = [4, 5, 6, 7, 8, 9]
set_of_unique_values_from_lists = set(first_list).symmetric_difference(set(second_list))
print(set_of_unique_values_from_lists)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = tuple(person_list)
person_dict = {'10-19': [person_list[i] for i in [1]],
               '20-29': [person_list[i] for i in [0, 3, 4]],
               '30-39': [person_list[i] for i in [2]],
               '40-49': [person_list[i] for i in [5]]}
print(person_dict)
