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
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

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
def sum_numbers(number_1, number_2):
    return number_1 + number_2
print("Сума двох чисел:", sum_numbers(3, 10))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_list(list_numbers):
    counter = 0
    for i in list_numbers:
        counter = counter + i
    average = counter / len(list_numbers)
    return average
print(avg_list([12, 35, 44, 38]))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
#Вирішення 1
def reverse_row(row):
    rev_text = ""
    for i in row:
        rev_text = i + rev_text
    return rev_text
print(reverse_row("Hello, word!"))

#Вирішення 2
def reversed_row(row):
    return "".join(reversed(row))
print(reversed_row("Hello, word!"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
#Вирішення 1
def longest_word(word_list):
    sorted_list = sorted(word_list, key=len)
    return sorted_list[-1]
print("Найдовше слово у списку:", longest_word(["Alice", "Cat", "Benisimmo", "Uve"]))

#Вирішення 2
def longest_word_2(word_list):
    longest = ""
    for i in word_list:
        if len(i) > len(longest):
            longest = i
    return longest
print("Найдовше слово у списку:", longest_word_2(["Alice", "Cat", "Benisimmo", "Uve"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 not in str1:
        return -1
    else:
        word_index = str1.index(str2)
        return word_index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#1 з попередніх домашок
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
def show_list(fruit_list):
    """показує елементи списку"""
    for i in fruit_list:
        if i == 'orange':
            continue
        print(i)

fruits = ["apple", "banana", "orange", "grape", "mango"]
print(show_list(fruits))

#2 з попередніх домашок
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_list_of_squares(result):
    """шукає список квадратів парних чисел зі списку"""
    result = [i ** 2 for i in numbers if i % 2 ==0]
    return result
print(find_list_of_squares(numbers))

#3 з попередніх домашок
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

def find_sea_area(azov_sea, black_sea):
    """шукає загальну площу морів"""
    return azov_sea + black_sea
print("Загальна площа морів:", find_sea_area(436_402, 37_800))

#4 з попередніх домашок
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def credit_calculator(month_payment, amount_of_months):
    """розраховує вартість компютера"""
    return month_payment * amount_of_months
print(f"Вартість компютера: {credit_calculator(1179, 18)} гривень")








