# Масив зі строками
array_with_strings = ["7,7,7,7", "1hi,5,6,7", "1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def sum_of_numbers_in_string(string):
    try:
        # Розділити рядок на окремі елементи за комами
        numbers = string.split(',')
        # Перетворити кожен елемент на ціле число і обчислити суму
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        # Якщо елемент не є числом, зловити виключення та повернути повідомлення
        return "Не можу це зробити!"

# Вивести результати для кожного елементу списку
for string in array_with_strings:
    result = sum_of_numbers_in_string(string)
    print(result)
