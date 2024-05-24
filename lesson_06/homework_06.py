import random
# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'green'
if alien_color == 'green':
    print('You have got 5 points')

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'yellow'
if alien_color == 'green':
    print('You have got 5 points')
else:
    print('You have got 10 points')

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print('You have got 5 points')
    elif color == 'red':
        print('You have got 15 points')
    else:
        print('You have got 10 points')

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = []
stop_word = 'quit'

while isinstance(pizza_topping, list):
    topping = input('\nChoose a topping for your pizza (\'quit\' is your stop word): ').lower()
    if topping == stop_word:
        print(f'Your pizza will have these toppings: {pizza_topping}')
        break
    else:
        print(f'I will add \'{topping}\' for you pizza')
        pizza_topping.append(topping)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""
users_number = input('Print your number here: ')
user_number_list = list(users_number)
total_count = 0

for number in user_number_list:
    int_type_number = int(number)
    total_count += int_type_number

print(f'\nSum of digits of a number {users_number}: {total_count}')

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
users_numbers_list = []
total_sum = 0

while isinstance(users_numbers_list, list):
    number = int(input('\nPrint your number here (choose \'0\' to stop): '))
    if number == 0:
        print(f'\nSum of digits: {total_sum}')
        break
    else:
        total_sum += number

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("\nGuess a number from 1 to 20 in 5 tries!")

for guess in range(max_guesses + 1):
    if guess != max_guesses:
        guesses += 1
        user_guess = int(input('Print your number: '))
        if user_guess == secret_number:
            print('You win this game')
            break
        else:
            if user_guess > secret_number:
                print('Your number is greater than mine')
            elif user_guess < secret_number:
                print('My number is greater than yours')
    else:
        print('It was your last try. You lose this game')

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit == 'orange':
        continue
    else:
        print(fruit)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i % 2 == 0]
print(result)
