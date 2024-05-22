# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

alien_color = "green"
if alien_color == "green":
    print("Player gained 5 points")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

alien_color = "green"
alien_color = "yellow"
if alien_color == "green":
    print("Player gained 5 points")
elif alien_color != "green":
    print("Player gained 10 points")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("Player gained 5 points")
    elif color == "red":
        print("Player gained 15 points")
    else:
        print("Player gained 10 points")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

while True:
    pizza_topping = input("Введіть начинку для піци: ")
    if pizza_topping == "quit":
        break
    else:
        print("Начинку до вашої піци додано!")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""

sum = 0
while True:
    user_input = input("Введіть ціле число: ")
    if user_input.isdigit():
        sum += int(user_input)
    else:
        print("Будь ласка введіть ціле число")
    print(f"Сума введених чисел: {sum}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

user_input = 0
total = 0
while True:
    user_input = input("Введіть будь-яке ціле число. Введіть 0 щоб вивести суму чисел і закінчити програму: ")
    user_input = int(user_input)
    if user_input != 0:
        total += user_input
        print(f"Сума введених чисел: {total}") # в тасці сказано що результат має показатись виключно після введення 0
    elif user_input == 0:
        print(f"Сума введених чисел: {total}. Програму завершено.")
        break

# task 8
"""  З використанням циклу FOR реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""

import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
for i in range(5):
    guessed_number = int(input("Enter the number: "))
    if guessed_number == secret_number:
        print(f"Congratulations, you guessed it! The correct number is {secret_number}.")
        break
    elif guessed_number > secret_number:
        print("The number you entered is too high! Try to guess again.")
    elif guessed_number < secret_number:
        print("The number you entered is too low! Try to guess again.")
if guessed_number != secret_number:
    print(f"All attempts used. The correct number was {secret_number}")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    else:
        print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #не вийшло знайти рішення в один рядок :(
for i in range(10):
    if i % 2 == 0:
        print(i ** 2)
