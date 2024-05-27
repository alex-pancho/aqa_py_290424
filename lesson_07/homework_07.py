# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
           break
        print(f"{number} * {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1
number = int(input("Щоб надрукувати табличку множення на задане число, введіть число: "))
multiplication_table(number)

#multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers(a, b):
    """
    Функція обчислює суму двох чисел.

    Параметри:
    a (int, float): Перше число.
    b (int, float): Друге число.

    Повертає:
    int, float: Сума двох чисел.
    """
    return a + b

num1 = float(input("Знайдемо суму двох чисел. Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
result = sum_two_numbers(num1, num2)
print(f"Сума {num1} і {num2} дорівнює {result}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(numbers):
    """
    Функція розраховує середнє арифметичне списку чисел.

    Параметри:
    numbers (list): Список чисел (int або float).

    Повертає:
    float: Середнє арифметичне чисел у списку.
    """
    if len(numbers) == 0:
        return 0  # Повертати 0, якщо список порожній для уникнення ділення на нуль

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

numbers_list = [1, 2, 3, 4, 5]
average = calculate_average(numbers_list)
print(f"Середнє арифметичне списку {numbers_list} дорівнює {average}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(input_string):
    """
    Функція приймає рядок та повертає його у зворотному порядку.

    Параметри:
    input_string (str): Рядок, який потрібно перевернути.

    Повертає:
    str: Перевернутий рядок.
    """
    return input_string[::-1]

user_input = input("Щоб повернути рядок у зворотньому порядку, введіть його: ")
reversed_string = reverse_string(user_input)
print(f"Перевернутий рядок: {reversed_string}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(words_list):
    """
    Функція приймає список слів та повертає найдовше слово у списку.

    Параметри:
    words_list (list): Список слів.

    Повертає:
    str: Найдовше слово у списку.
    """
    if not words_list:  # перевірка на порожній список
        return ""

    longest_word = max(words_list, key=len)
    return longest_word

user_input = input("Введіть список слів через кому: ")
words_list = [word.strip() for word in user_input.split(',')]
longest_word = find_longest_word(words_list)
print(f"Найдовше слово у списку: {longest_word}")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    """
    Функція приймає два рядки та повертає індекс першого входження другого рядка у перший рядок.

    Параметри:
    str1 (str): Основний рядок.
    str2 (str): Рядок, який шукаємо.

    Повертає:
    int: Індекс першого входження другого рядка у перший рядок, або -1, якщо другого рядка немає в першому рядку.
    """
    return str1.find(str2)

str1 = input("Введіть основний рядок: ")
str2 = input("Введіть рядок, який шукаємо: ")
index = find_substring(str1, str2)
print(f"Індекс першого входження рядка '{str2}' у рядок '{str1}': {index}")

print("****")

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def find_unique_elements(input_list):
    """
    Функція приймає список та повертає всі унікальні елементи у списку.

    Параметри:
    input_list (list): Вхідний список.

    Повертає:
    list: Список унікальних елементів.
    """
    unique_elements = list(set(input_list))
    return unique_elements

# Приклад
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_elements_in_small_list = find_unique_elements(small_list)
print(f"Унікальні елементи у списку small_list: {unique_elements_in_small_list}")

# task 8

def has_duplicates(input_list):
    """
    Функція приймає список та перевіряє, чи є в ньому дублікати.

    Параметри:
    input_list (list): Вхідний список.

    Повертає:
    bool: True, якщо дублікати є, і False, якщо їх немає.
    """
    return len(input_list) != len(set(input_list))

# Приклад
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
duplicates_exist = has_duplicates(big_list)
print(f"Чи є в списку big_list дублікати: {duplicates_exist}")

# task 9

def sum_of_non_common_elements(set1, set2):
    """
    Функція обчислює суму елементів двох множин, які не є спільними.

    Параметри:
    set1 (set): Перша множина.
    set2 (set): Друга множина.

    Повертає:
    int: Сума елементів, які не є спільними в обох множинах.
    """
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    return sum(unique_to_set1) + sum(unique_to_set2)

# Приклад
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
result = sum_of_non_common_elements(set_1, set_2)
print(f"Сума елементів, які не є спільними: {result}")

# task 10

def check_alien_color(alien_color):
    if alien_color == 'green':
        return "Гравець щойно заробив 5 балів."
    else:
        return "Гравець не заробив балів."

# Приклади
print(check_alien_color('green'))  # Гравець щойно заробив 5 балів.
print(check_alien_color('yellow'))  # Гравець не заробив балів.
print(check_alien_color('red'))  # Гравець не заробив балів.

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""