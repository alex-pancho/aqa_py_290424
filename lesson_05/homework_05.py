small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("\n", "Task 01")
unique_elements = list(set(small_list))
print(unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list


print("\n", "Task 02")
sum_0 = sum(small_list)
elements = len(small_list)
arithmetic_mean = sum_0 / elements
print("Arithmetic mean:", arithmetic_mean)

# task 3. Перевірте, чи є в списку big_list дублікати

print("\n", "Task 03")
duplicates = len(big_list) != len(set(big_list))
if duplicates :
    print("Duplicates are present.")
else:
    print("There are no duplicates.")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("\n", "Task 04")
key_1 = max(add_dict, key=add_dict.get)
print("The key with the maximum value:", key_1)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("\n", "Task 05")
new_dict = {}
for key, value in base_dict.items():
    new_dict[value] = key
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("\n", "Task 06")
sum_dict = {}
for key, value in base_dict.items():
    sum_dict[key] = value
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print(sum_dict)

# task 7.
print("\n", "Task 07")
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_0 = set(line)
print(set_0)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("\n", "Task 08")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_set = list(set_1 ^ set_2)
sum_elements = 0
for e in set_set:
    sum_elements += e
print(f'Sum: {sum_elements}')


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

print("\n", "Task 09")
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

list_list = list_1 + list_2
elements = set(list_list)
set_10 = {a for a in elements if list_list.count(a) == 1}
print(set_10)
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
print("\n", "Task 10")
age_groups = {}
for name, age in person_list:
    start = (age // 10) * 10
    end = start + 9
    age_range = f"{start}-{end}"
    
    if age_range not in age_groups:
        age_groups[age_range] = []
    
    age_groups[age_range].append(name)

print(age_groups)
