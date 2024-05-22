small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

print(set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

sum = 0
for i in small_list:
    sum = sum + i
average = sum / len(small_list)
print(average)


# task 3. Перевірте, чи є в списку big_list дублікати

big_list_set = set(big_list)
if len(big_list) == len(big_list_set):
    print("В списку нема дублікатів.")
else:
    print("В списку є дублікати.")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

dict_values = list(add_dict.values())
dict_values.sort()
max_value = dict_values[-1]
print(max_value)
for key in add_dict:
    if add_dict[key] == max_value:
        print(key)
        break


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_dict = {}
for key, value in base_dict.items():
    new_dict[value] = key
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = {}
all_keys_base_dict = set(base_dict.keys())
all_keys_add_dict = set(add_dict.keys())
all_keys = all_keys_base_dict | all_keys_add_dict
for i in all_keys:
    if i in base_dict and i in add_dict:
        sum_dict.update({i : str(add_dict[i]) + str(base_dict[i])})
    elif i in add_dict:
        sum_dict.update({i: add_dict[i]})
    elif i in base_dict:
        sum_dict.update({i: base_dict[i]})

print(sum_dict)


# task 7.

line = "Створіть множину всіх символів, які входять у заданий рядок"
print(set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_1 = 0
set_3 = set_1 ^ set_2
for i in set_3:
    sum_1 = sum_1 + i
print(sum_1)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_01 = [1, 2, 3, 4, 12, 25, 44]
list_02 = [3, 4, 5, 6, 12, 31, 49]

set_01 = set(list_01)
set_02 = set(list_02)
set_03 = set_01 ^ set_02
print(set_03)



# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

# for each range in range_list
# find names from person_list, which has age in this range
#    for person in person_list
#        if age is in range we dedicated then add name in the temp list
#add them to dict as values 

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
range_list = ["10-19", "20-29", "30-39", "40-49", "50-59"]
person_list_dict = {}
for range in range_list:
    temp_list = []
    for person in person_list:
        if person[1] >= int(range[0:2]) and person[1] <= int(range[3:5]):
            temp_list.append(person[0])

    person_list_dict.update({range: temp_list})

print(person_list_dict)
