# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

# my answer:
alien_color = 'green'
if alien_color == 'green':
    print("You won 5 points")
  

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

# my answer:
alien_color = 'green'
if alien_color == 'red':
    print("You won 5 points")
else:
    print("You won 10 points")


# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

# my answer:
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print("You won 5 points")
    elif i == 'red':
        print("You won 15 points")
    else:
        print("You won 10 points")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

# my answer:
while True:
    pizza_topping = input("Enter the topping: ")
    if pizza_topping == 'quit':
        print("Finished adding toppings.")
        break
    else:
        print(f"Your topping {pizza_topping} is added.")
  

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""

# my answer:
number = input("Enter the number: ")
sum_all_digits = 0

for digit in number:
    sum_all_digits += int(digit)

print(f"The sum of the digit of the number {number} is {sum_all_digits} ")


# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

# my answer:
sum = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
      break
    else:
        sum += number

print("The sum of the numbers is: ",sum)


# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""

# my answer:
import random
secret_number = random.randint(1, 5)
guesses = 0
max_guesses = 5
for guesses in  range(max_guesses):
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("You guess is too small.")
    elif guess > secret_number:
        print("You guess is too big.")
    else:
        print(f"You guessed the number in { guess } attempts")


# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

# my answer
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == 'orange':
        continue
    print(fruit, end = ' ')


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""

# my answer:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num ** 2 for num in numbers if num % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
