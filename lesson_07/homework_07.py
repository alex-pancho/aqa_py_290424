# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# my answer:
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
# my answer:
def suma(a, b):
    a = int(a)
    b = int(b)
    return (a + b)
c = suma(1,'3')
print(c)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
# my answer:
def average_of(numbers):
    return sum(numbers)/len(numbers)
list = [1,2,3,4]
a = average_of(list)
print(a)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
# my answer:
def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string
s = reverse("Hello  world") 
print(s) 

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# my answer:
def longest_word_searching(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            return longest_word
list = ['apple', 'milk', 'cucumber']
result = longest_word_searching(list)
print(result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    if index != -1:
     return index
    else:
        return -1

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
# my answer_1:
def check_alien_color(alien_color):
    """
    Checks alien's color and returns amount of points won.
    Parameters: alien_color(str).
    Returnes: points won(int).
    """
    if alien_color == 'red':
        return 5
    else:
        return 10
alien_color = 'green'   
point = check_alien_color(alien_color)
print(f" You won {point} points")

# my answer_2:
def summa(a, b):
    return a + b
"""
    Calculates the sum of two numbers.
    Parameters: first number (int or float)
                second number  (int or float).
    Returnes: sum of numbers
"""  
result = summa(122.4, 22)
print("Your summa is", + result)

# my answer_3:
def average(numbers):
    """
    Calculates the arithmetic mean of a list of numbers
    Parameters:numbers (list).
    Returns: arithmetic average of the numbers in the list(float).
    """
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)
result = average([1, 2, 3, 4, 5])
print(result)

# my answer_4
def find_substring(str1, str2):
        return str1.find(str2)
result = find_substring('Hello world', 'world')#Returns the index of the first occurrence of the second string in the first string.
print(result)

result = find_substring('The quick brown fox jumps over the lazy dog', 'cat')#Returns -1 if the second string is not a substring of the first string.
print(result)