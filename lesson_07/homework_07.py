# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити/доповнити.
"""


def multiplication_table(number):
    multiplier = 1
    while multiplier:
        result = number * multiplier
        if result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def get_sum_numbers(*, first_number: int, second_number: int) -> int:
    return first_number + second_number


print(get_sum_numbers(first_number=3, second_number=7))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def calculate_average(numbers_list) -> int:
    total = sum(numbers_list)
    count = len(numbers_list)
    average = total // count
    return average


numbers = [1, 2, 3, 6]
print(calculate_average(numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def get_reverse_string(input_string) -> str:
    return input_string[::-1]


print(get_reverse_string('Alex'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(list_words) -> str:
    longest_word = ''
    for word in list_words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


words = ['JavaScript', 'Python', 'Java', 'Go', 'C++']
print(find_longest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(string_first, string_second):
    return string_first.find(string_second)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
"""
Знайдіть всі унікальні елементи в списку small_list
"""


def find_unique_elements(list_elements):
    return set(list_elements)


small_list = [3, 1, 4, 5, 2, 5, 3]
print(find_unique_elements(small_list))

# task 8
"""
Перевірте, чи є в списку big_list дублікати
"""


def find_duplicate(list_elements):
    original_big_list_length = len(list_elements)
    unique_big_list_length = len(set(list_elements))

    if original_big_list_length == unique_big_list_length:
        return f'\nThere are a unique values in a list \'big_list\''
    else:
        return '\nThere are a duplicates in a list \'big_list\''


big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
print(find_duplicate(big_list))

# task 9
"""
Знайдіть ключ з максимальним значенням у словнику add_dict
"""


def find_key_with_max_value(dictionary):
    max_value_add_dict = 0
    max_key_add_dict = None

    for key, value in dictionary.items():
        if value > max_value_add_dict:
            max_value_add_dict = value
            max_key_add_dict = key

    return max_key_add_dict


# Приклад використання функції
add_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 25}
max_key = find_key_with_max_value(add_dict)
print(f"\nКлюч з максимальним значенням у словнику \'{add_dict}\': {max_key}")

# task 10
"""
Обчисліть суму елементів двох множин, які не є спільними
"""


def sum_of_non_common_elements(set_01, set_02):
    set_03 = set_01 ^ set_02
    total_set_3_sum = sum(set_03)
    return total_set_3_sum


# Приклад використання функції
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
result_01 = sum_of_non_common_elements(set_1, set_2)
print(f"\nСума елементів двох множин, які не є спільними: {result_01}")
