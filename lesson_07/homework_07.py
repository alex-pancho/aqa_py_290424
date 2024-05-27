# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("\n Task 01")
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1


    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))


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
print("\n Task 02")
def sum_2(a, b):
    return a + b
result = sum_2(9, 7)
print("Sum:", result)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\n Task 03")
def c_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
average = c_average(list_1)
print("Calculate average:", average)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\n Task 04")
def reverse_string(string_for_input):
    return string_for_input[::-1]
print(reverse_string("Home work 7"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\n Task 05")
def find_longest_word(*args):
    if not args:
        return None  
    word = max(args, key=len)
    return word
all_words = ["Home", "work", "zero", "seven", "and"]
print("The longest word in the list:", find_longest_word(*all_words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\n Task 06")
def find_substring(str1, str2):

    return str1.find(str2)

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
# task 7
""" Виведіть, скільки слів у тексті починається з Великої літери? (h_w_04)
"""
print("\n Task 07")
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;"""
def count_capitalized_words(text):
    words_in_text = text.split()
    capitalized_count = sum(1 for word in words_in_text if word[0].isupper())
    return capitalized_count
print(count_capitalized_words(adwentures_of_tom_sawer))

# task 8
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?(h_w_03)
"""
print("\n Task 08")
black_sea_area = 436402
azov_sea_area = 37800
def total_area(black_sea_area, azov_sea_area):
    return black_sea_area + azov_sea_area
combined_area = total_area(black_sea_area, azov_sea_area)
print(f"The area of ​​the Black and Azov seas together is: {combined_area} km2")

# task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера. (h_w_03)
"""
print("\n Task 09")
monthly_payment = 1179
months = 18
def calculate_computer_cost(monthly_payment, months):
    return monthly_payment * months
total_cost = calculate_computer_cost(monthly_payment, months)
print(f"The cost of the computer is: {total_cost} UAH")

# task 10
"""
Знайдіть ключ з максимальним значенням у словнику add_dict. (h_w_05)
"""
print("\n Task 10")
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
def find_key_with_max_value(d):
     return max(d, key=d.get)
key_with_max_value = find_key_with_max_value(add_dict)
print(f"Key with maximum values: {key_with_max_value}")

