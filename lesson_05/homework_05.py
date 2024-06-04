small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
new_list = []
for i in set(small_list):
    if small_list.count(i) == 1:
        new_list.append(i)
print(f"Унікальні елементи списку small_list: {new_list}")


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
#Вирішення 1
avg_value = sum(small_list)/len(small_list)
print("Середнє арифметичне всіх елементів у списку small_list:", round(avg_value, 1))
#Вирішення 2
counter = 0
for i in small_list:
    counter = counter + i
    avg = counter / len(small_list)
print("Середнє арифметичне всіх елементів у списку small_list:",round(avg, 1))

# task 3. Перевірте, чи є в списку big_list дублікати

list_set = set(big_list)
if len(big_list) == len(list_set):
    print("У списку всі елементи унікальні")
else:
    print("У списку є дублікати")



base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
#Вирішення 1
max_key = max(add_dict, key=add_dict.get)
print(f"Ключ з максимальним значенням в словнику: {max_key}, зі значенням {add_dict.get(max_key)}")

#Вирішення 2
for k, v in add_dict.items():
    new_dict = max(add_dict, key=add_dict.get)
print(f"Ключ з максимальним значенням в словнику: {new_dict}, зі значенням {v}")

#Вирішення 3
counter = 0
for k, v in add_dict.items():
    if v > counter:
        counter = v
print(f"Ключ з максимальним значенням в словнику:{k}, зі значенням {counter}")


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

new_dict = {}
for k, v in add_dict.items():
    new_dict[v] = k
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

#Вирішення 1
sum_dict = base_dict.copy()
print(base_dict)
print(add_dict)
print(sum_dict)
for k in add_dict:
    if k in sum_dict:
        sum_dict[k] = str(add_dict[k]) + str(sum_dict[k])
    else:
        sum_dict[k] = add_dict[k]
print(sum_dict)

#Вирішення 2
sum_dict = base_dict|add_dict
for k in base_dict:
    if k in add_dict:
        sum_dict[k] = str(sum_dict[k])+str(base_dict[k])
print(sum_dict)


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
list_line = list(line)
print(list_line)
new_line = set(list_line)
print(new_line)


# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_elements = set_1.symmetric_difference(set_2)
print(unique_elements)
new_set = sum(unique_elements)
print("Сума елементів двох множин, які не є спільними:", new_set)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
set_one = set(list_1)
set_two = set(list_2)
returned_set = set_one.symmetric_difference(set_two)
print(returned_set)



person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

comp_dict = {}
for k, v in person_list:
    start_age = (v // 10) * 10
    end_age = start_age + 9
    age_range = f"{start_age}-{end_age}"
    if age_range in comp_dict:
        comp_dict[age_range].append(k)
    else:
        comp_dict[age_range] = [k]
print(comp_dict)


