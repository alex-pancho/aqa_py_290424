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
        # Якщо результат більше за 25, припинити виконання
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
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
    """Функція обчислює суму двох чисел."""
    return a + b


print(sum_two_numbers(3, 5))  # Виведе 8
print(sum_two_numbers(-1, 6))  # Виведе 5


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_of_list(numbers):
    """Функція розраховує середнє арифметичне списку чисел."""
    return sum(numbers) / len(numbers)


print(average_of_list([1, 2, 3, 4, 5]))  # Виведе 3.0
print(average_of_list([10, 20, 30]))  # Виведе 20.0


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(s):
    """Функція приймає рядок та повертає його у зворотному порядку."""
    return s[::-1]


print(reverse_string("hello"))  # Виведе "olleh"
print(reverse_string("World"))  # Виведе "dlroW"


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words):
    """Функція приймає список слів та повертає найдовше слово у списку."""
    return max(words, key=len)


print(longest_word(["apple", "banana", "plum", "grape"]))  # Виведе "banana"
print(longest_word(["cat", "elephant", "dog"]))  # Виведе "elephant"


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str_1, str_2):
    """Функція приймає два рядки та повертає індекс першого входження другого рядка у перший рядок."""
    return str_1.find(str_2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# task 7
def calculate_pages_needed(total_photos, photos_per_page):
    """Функція обчислює кількість сторінок, необхідних для вклеювання фотографій."""
    return (total_photos + photos_per_page - 1) // photos_per_page


print(calculate_pages_needed(232, 8))  # Виведе 29


# task 8
def calculate_computer_cost(monthly_payment, months):
    """Функція обчислює загальну вартість комп'ютера."""
    return monthly_payment * months


print(calculate_computer_cost(1179, 18))


# task 9
def has_duplicates(lst):
    """Функція перевіряє, чи є в списку дублікати."""
    return len(lst) != len(set(lst))


print(has_duplicates([3, 5, -2, -1, -3, 0, 1, 4, 5, 2]))  # Виведе True
print(has_duplicates([1, 2, 3, 4, 5]))  # Виведе False


# task 10
def unique_elements(lst):
    """Функція повертає унікальні елементи зі списку."""
    return list(set(lst))


print(unique_elements([3, 1, 4, 5, 2, 5, 3]))  # Виведе [1, 2, 3, 4, 5]

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""