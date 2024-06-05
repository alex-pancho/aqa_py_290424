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
            break  # Вихід з циклу, якщо результат більше 25
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1  # Виправлення змінної для інкременту


# Тестування функції
multiplication_table(3)
# Expected output:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b

result = sum_two_numbers(5, 3)
print(result)

result = sum_two_numbers(10, 15)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(average)

numbers = []
average = calculate_average(numbers)
print(average)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]
input_string = "Python"
reverced_string = reverse_string(input_string)
print(reverced_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def finde_longest_word(word_list):
    if not word_list:
        return None
    longest_word = word_list[0]
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

words = ["Python", "is", "a", "good", "example"]
longest_word = finde_longest_word(words)
print(longest_word)

words = []
longest_word = finde_longest_word(words)
print(longest_word)


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
def print_fruits_except_orange(fruits): #виводить список фруктів пропускаючи orange
    for fruit in fruits:
        if fruit == "orange":
            continue
        print(fruit)

fruits = ["apple", "banana", "orange", "grape", "mango"]
print_fruits_except_orange(fruits)

# task 8
def get_squares_of_even_numbers(numbers):
    """
    Знаходить квадрати парних чисел зі списку
    numbers (list): Список чисел
    list: Список квадратів парних чисел
    """
    squares = [x**2 for x in numbers if x % 2 == 0]
    return squares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = get_squares_of_even_numbers(numbers)
print(result)
# task 9

def calculate_sum():
    """Обчислює суму введених чисел, поки користувач не введе 0"""
    total_sum = 0
    while True:
        number = int(input("введіть число 0 для завершення: "))
        if number == 0:
            break
        total_sum += number
    return total_sum
result = calculate_sum()
print(f"cума всіх введених чисел: {result}")

# task 10
def check_alien_color(alien_color):
    """
    Перевіряє кольор інопланетянина і визначає кількість балів
    Параметри:
    alien_color (str): Колір інопланетянина.
    Повертає:
    str: Повідомлення про кількість балів, які заробив гравець.
    """
    if alien_color == 'green':
        return "Гравець заробив 5 балів."
    else:
        return "Гравець заробив 10 балів."

result_1 = check_alien_color('green')
result_2 = check_alien_color('red')

print(result_1)
print(result_2)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""