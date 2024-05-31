list_of_strings = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
]


def sum_of_numbers_in_string(string):
    try:
        # Розділяємо рядок за комами і перетворюємо на числа
        numbers = [int(num) for num in string.split(',')]
        return sum(numbers)
    except ValueError:
        # Якщо знайдено нечисловий символ, повертаємо повідомлення про помилку
        return 'Не можу це зробити!'


# # Для кожного елемента в масиві, обчислюємо суму чисел або виводимо повідомлення про помилку
results = [sum_of_numbers_in_string(string) for string in list_of_strings]

# Виведення результатів
for result in results:
    print(result)
