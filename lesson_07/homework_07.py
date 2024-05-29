# # task 1
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
        # десь тут помилка, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)
# # Should print:
# # 3x1=3
# # 3x2=6
# # 3x3=9
# # 3x4=12
# # 3x5=15
#
#
# # task 2
# """  Написати функцію, яка обчислює суму двох чисел.
# """
def sum_of_two_numbers(user_input_first, user_input_second):
    return user_input_first + user_input_second

user_input_first = int(input("Enter the 1st number of 2 to calculate their sum: "))
user_input_second = int(input("Enter the 2nd number of 2 to calculate their sum: "))
result = sum_of_two_numbers(user_input_first, user_input_second)
print(f"Sum of entered numbers is {result}")





# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def mean(list_of_numbers):
    total_sum = sum(list_of_numbers)
    count = len(list_of_numbers)
    return round(float(total_sum / count), 2)

list_of_numbers = [1, 4, 4, 23, 84, 15]
print(mean(list_of_numbers))


# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
# """
def invert_line(input_line):
    return input_line[::-1]
input_line = input("Enter a line: ")
print(invert_line(input_line))

# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
# """
def longest_word(input_list):
    return max(input_list, key=len)
input_list = input("Enter a list of words separated by whitespace:").split()
print(f"The longest word is {longest_word(input_list)}")

# # task 6
# """  Написати функцію, яка приймає два рядки та повертає
# індекс першого входження другого рядка у перший рядок, якщо другий рядок є підрядком першого рядка,
# та -1, якщо другий рядок не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
#
# # task 7
# # task 8
# # task 9
# # task 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """
# task 7
# old solution

# black_sea_square = 436_402
# azov_sea_square = 37_800
# print("The Black Sea and the Sea of Azov together cover " + str(black_sea_square + azov_sea_square) + " km2")

# new solution
def square(black_sea_square, azov_sea_square):
    return black_sea_square + azov_sea_square
black_sea_square = 436_402
azov_sea_square = 37_800
total_square = square(black_sea_square, azov_sea_square)
print(f"The Black Sea and the Sea of Azov together cover {total_square} km2")

# task 8
# old solution

# computer_price = 1179 * 18
# print(f"Вартість комп'ютера складає {computer_price} грн")

# # new solution
def computer_price(monthly_price, number_of_months):
    """counting total computer price based on monthly payment and the number of months"""
    return monthly_price * number_of_months
monthly_price = 1179
number_of_months = 18
total_price = computer_price(monthly_price, number_of_months)
print(f"The total computer price is {total_price} UAH")
#
# # task 9
#
# # old solution
#
# # set_1 = {1, 2, 3, 4, 5}
# # set_2 = {4, 6, 5, 10}
# # diff = set_1.symmetric_difference(set_2)
# # print(sum(diff))
#
# # new solution
def diff_between_two_sets(set_1, set_2):
    return(set_1.symmetric_difference(set_2))
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
diff = diff_between_two_sets(set_1, set_2)
formatted_diff = ', '.join(map(str, diff))
print(f"Unique numbers between 2 sets: {formatted_diff}.")
#
# # task 10
# # old solution
#
# # small_list = [3, 1, 4, 5, 2, 5, 3]
# # print(set(small_list))
#
# # new solution
def unique_values_from_list(small_list):
    return (set(small_list))
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_values_output = unique_values_from_list(small_list)
formatted_unique_values_output = ', '.join(map(str, unique_values_output))
print(f"Unique values from the small_list are: {formatted_unique_values_output}.")