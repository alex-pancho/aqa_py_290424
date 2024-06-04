""" Сюди підготовані ф-ції вставити
"""

#
#Task1
def sum_numbers(number_1, number_2):
    return number_1 + number_2

#
# #Task2
def avg_list(list_numbers):
    counter = 0
    for i in list_numbers:
        counter = counter + i
    average = counter / len(list_numbers)
    return average

#
# #Task3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_list_of_squares(n_list):
    """шукає список квадратів парних чисел зі списку"""
    result = [i ** 2 for i in n_list if i % 2 == 0]
    return result
# print(find_list_of_squares(numbers))

#Task5
def longest_word(word_list):
    sorted_list = sorted(word_list, key=len)
    return sorted_list[-1]
# print("Найдовше слово у списку:", longest_word(['Anna', 'Bennissimo']))
#
# #Task4
number_list = ["1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"]
def find_sum_numbers3(some_string):
    try:
        return sum(list(int(item) for item in some_string.split(',')))
    except ValueError:
        return "Не можу це зробити!"

for element in number_list:
    print(find_sum_numbers3(element))