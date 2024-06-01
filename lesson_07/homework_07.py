# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(4)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_digits(a,b):
    """Обчислює суму двох чисел"""
    sum_of_digits = a + b
    print(f'Сума двох чисел дорівнює -> {sum_of_digits}')

sum_digits(10, 12)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(*args):
    """Обчислює середнє арифмитичне списку чисел"""
    average_digits = sum(args)/len(args)
    print(f'Середнє арифмитичне списку чисел -> {average_digits}')

average(10,20,30)
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(input_string):
    """Приймає рядок та повертає його у зворотньому порядку"""
    return input_string[::-1]

print(reverse_string('Hello, world!'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(word_list):
    if not word_list:
        return None

    longest = word_list[0]

    for word in word_list:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word(['test1', 'test2', 'test333', 'test55555']))
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def square_number_in_list(*args):
    """Дана функція підносить всі числа у списку до другого степеня"""
    result = [num * num for num in args]
    return result
print(square_number_in_list(1,2,3,4,8))

# task 8
def unique_elements_in_list(list1):
    """Повертає виключно унікальні значення з заданого списку"""
    unique = list(set(list1))
    return unique

print(unique_elements_in_list([1,2,3,4,5,5,6,6,7,7,8,8,8]))

# task 9
# Оскільки домашек трохи менше робив в цій групі, вирішив використати домашки з минулої групи в якості написання функцій :) Сподіваюсь, це ок
def is_palindrome(string):
    """Перевіряє, чи є стрінга паліндромом"""
    return string == string[::-1]

string = 'level'
if is_palindrome(string):
    print(f'Рядок "{string}" є паліндромом')
else:
    print(f'Рядок "{string}" не є паліндромом')

# task 10

def is_even(number):
    """Перевіряє, чи є число парним"""
    statement = number % 2 == 0
    return statement

num = 11
if is_even(num):
    print(f"Число {num} є парним.")
else:
    print(f"Число {num} не є парним.")
