small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
#unique_small_list = set(small_list)
print("Task 1: Знайдіть всі унікальні елементи в списку small_list")
print(set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print('', "Task 2: Знайдіть середнє арифметичне всіх елементів у списку small_list", sep="\n")
print(sum(small_list)/len(small_list))

# task 3. Перевірте, чи є в списку big_list дублікати
print('', "Task 3: Перевірте, чи є в списку big_list дублікати", sep="\n")

new_big_list = set(big_list)
if len(new_big_list) == len(big_list):
    print("Дублікатів в списку немає")
else:
    print("В списку big_list присутні дублікати")
    my_list = big_list
    for i in set(big_list):
        my_list.remove(i)
    print("Значення що повторюються в списку big_list:", my_list)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print('', "Task 4: Знайдіть ключ з максимальним значенням у словнику add_dict", sep="\n")
for key, value in add_dict.items():
    if value == max(add_dict.values()):
        print(f"Ключ з максимальним значенням у словнику add_dict: {key} зі значенням {value}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print('', "Task 5: Створіть новий словник, в якому ключі та значення будуть замінені місцями у заданому словнику", sep="\n")
new_dict_1 = dict(zip(add_dict.values(), add_dict.keys()))
new_base_dict = dict(zip(base_dict.values(), base_dict.keys()))
print(new_dict_1, new_base_dict, sep="\n")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print('', "Task 6: Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict", sep="\n")

sum_dict = base_dict.copy()
sum_dict.update(add_dict)
#print(sum_dict)
for key_1, value_1 in base_dict.items():
    for key_2, value_2 in add_dict.items():
        if key_1 == key_2:
            change_key = key_1
            change_text = str(value_2) + str(value_1)
            #print(f"{change_key}:{change_text}")
sum_dict[change_key] = change_text
print(sum_dict)

# task 7.
print('', "Task 7: Створіть множину всіх символів, які входять у заданий рядок", sep="\n")
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_line = set(line)
print(set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print('', "Task 8: Обчисліть суму елементів двох множин, які не є спільними", sep="\n")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print(sum(set_1.symmetric_difference(set_2)))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print('', "Task 9: Створіть два списки та обробіть їх так, щоб отримати сет...", sep="\n")
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

set_1_list = set(list_1)
set_2_list = set(list_2)
result_list = set_1_list.symmetric_difference(set_2_list)
print(result_list)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print('', "Task 10: Обробіть список кортежів person_list, що містять ім'я та вік людей, так, щоб отримати словник", sep="\n")

person_dict = dict(person_list)
#print(person_dict)
sort_person_dict= {'10-19': [], '20-29': [], '30-39': [], '40-49': []}

list_10_19 = []
list_20_29 = []
list_30_39 = []
list_40_49 = []

for key, value in person_dict.items():
    if (value >=10 and value <= 19):
        list_10_19.append(key)
    elif (value >=20 and value <= 29):
        list_20_29.append(key)
    elif (value >= 30 and value <= 39):
        list_30_39.append(key)
    elif (value >= 40 and value <= 49):
        list_40_49.append(key)

sort_person_dict['10-19'] = list_10_19
sort_person_dict['20-29'] = list_20_29
sort_person_dict['30-39'] = list_30_39
sort_person_dict['40-49'] = list_40_49

print(sort_person_dict)