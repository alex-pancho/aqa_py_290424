# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = "green"
if alien_color == "green":
    print("You've just received 5 points! Good job!")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

alien_color = "red"
if alien_color == "green":
    print("You've just received 5 points! Good job!")
else:
    print("You've just received 10 points! Awesome!")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ["green", "red", "yellow"]
for color in alien_color:
    if color == "green":
        print("You've just received 5 points! Good job!")
    elif color == "red":
        print("You've just received 15 points! Wow!")
    else:
        print("You've just received 10 points! Awesome!")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
while True:
    pizza_topping = input("Choose toping to add: ")
    if pizza_topping == "quit":
        break
    print(f"The {pizza_topping} will be added to your pizza")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""

number = input("Type a number: ")
sum = 0
for digital in number:
    sum = sum + int(digital)

print(sum)

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

sum = 0
while True:
    number = input("Type a number (Type 0 to quit): ")
    if number == "0":
        break

    sum = sum + int(number)
    print(sum)

print(f"The result is {sum}")

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for guesses in range(0, max_guesses):
    number = input("Введіть число від 1 до 20: ")
    if int(number) > secret_number:
        print("Ваше припущення було занадто великим!")
    elif int(number) < secret_number:
        print("Ваше припущення було занадто малим!")
    else:
        print("Ви вгадали! Візьміть печиво :)")
        break

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number**2 for number in numbers if number % 2 == 0]
print(result)

#temp_result = []
#for number in numbers:
#    if number % 2 == 0:
#        temp_result.append(number**2)
#print(temp_result)

