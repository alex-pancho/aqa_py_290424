# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
print("Task 01")
alien_color = 'green'
if alien_color == 'green':
   print("Congratulations, you got 5 points!")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
print("\n", "Task 02")
if alien_color == 'yellow':
   print("Congratulations, you got 5 points!")
else:
   print("Congratulations, you got 10 points!")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
print("\n", "Task 03 - 04")
alien_colors = ['green', 'yellow', 'red']
for alien_color in alien_colors:
    if alien_color == 'green':
        print("Congratulations, you got 5 points!")
    elif alien_color == 'yellow':
        print("Congratulations, you got 10 points!")
    elif alien_color == 'red':
        print("Congratulations, you got 15 points!")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
print("\n", "Task 05")
pizza_toppings = []  
while True:
    topping = input("Choose a pizza topping (or type 'quit' to exit): ")
    if topping == 'quit':
        break  
    pizza_toppings.append(topping)
    print("Great choice of pizza toppings!")
print("We will add this topping to your pizza:", pizza_toppings)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""
print("\n", "Task 06")
number = input("Enter a number: ")
all = 0
for digit in number:
    all += int(digit)
print(f"The sum of the digits of a number {number}: {all}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
print("\n", "Task 07")
sum = 0
while True:
     number = int(input("Enter a number (press 0 to count the numbers you entered): "))
     if number == 0:
         break
     sum += number
print("The sum of all entered numbers:", sum)

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
print("\n", "Task 08")
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Guess a number from 1 to 20 in 5 tries!")

for guesses in range(1, max_guesses + 1):
    guess = input(f"Attempt {guesses}: ")
    guess = int(guess)
    if guess < secret_number:
        print("Your number is too small.")
    elif guess > secret_number:
        print("Your number is too high.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {guesses} tries!")
        break
else:
    print(f"The attempts are over. The requested number was {secret_number}.")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
print("\n", "Task 09")
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
print("\n", "Task 10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
