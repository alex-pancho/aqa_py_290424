small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
#my answer:
unique_elements = list(set(small_list))
print(unique_elements)


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
# my answer:
sum_elements = sum(small_list)
number_elements = len(small_list)
average = sum_elements/number_elements
print(average)

# task 3. Перевірте, чи є в списку big_list дублікати
# my answer:
unique_elements_big_list = set(big_list)
has_dublictes = len(unique_elements_big_list) < len(big_list)
print(has_dublictes)


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
# my answer:
max_key = max(add_dict)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
# my answer:
changed_dict = {value: key for key, value in base_dict.items()}
print(changed_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict.copy()
for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value   
print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
# my answer:
all_symbols = set(line)
print(all_symbols)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
unique_set_1 = set_1 - set_2
unique_set_2 = set_2 - set_1
unique_elements = unique_set_1.union (unique_set_2)
print(sum(unique_elements))


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
# my answer:
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
set_1_2 = list_1 + list_2
unique_elements = set()
for element in set_1_2:
    if set_1_2.count(element) == 1:
        unique_elements.add(element)
print(unique_elements)            
        
      


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_dict = {'10-19':[], '20-29':[], '30-39':[], '40-49':[]}
for person in person_list:
    name, age = person
    if 10 <= age <= 19:
        person_dict['10-19'].append(name)
    elif 20 <= age <= 29:
        person_dict['20-29'].append(name)
    elif 30 <= age <= 39:
        person_dict['30-39'].append(name)
    elif 40 <= age <= 49:
        person_dict['40-49'].append(name)

print(person_dict)

        

