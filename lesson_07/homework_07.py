# task 1
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
        # десь тут помила, а може не одна
        if result > 25:
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
def sum_numbers(a, b):
    return a + b

print(sum_numbers(2, 7))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calc_average(*args):
    return sum(args) / len(args)

print(calc_average(1, 2, 3, 7, 8))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_order(string_to_reverse):
    return string_to_reverse[::-1]

print(reverse_order("Ще не вмерла Украіни ні слава ні воля"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(*args):
    max_length = 0
    max_length_word = ""
    for arg in args:
        word_length = len(arg)
        if word_length > max_length:
            max_length = word_length
            max_length_word = arg
    return max_length_word

print(longest_word("banana", "fox", "apple", "wolf", "tree"))

#Також зробила це завдання за допомогою функції max:

def longest_word_2(*args):
    return max(args, key = lambda arg: len(arg))

print(longest_word_2("banana", "fox", "apple", "wolf", "tree"))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
#1)
#def find_substring(str1, str2):
#    return str1.find(str2)
#2)

def find_substring(str1, str2):
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if i + j > len(str1) or str1[i + j] != str2[j]:
                break
            elif j == len(str2) - 1:
                return i
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
pay_per_month = 1179
months_tp_pay = 18

def full_price_in_installments(price_per_month, months_to_pay):
    """Calculates the full price of the product."""
    return price_per_month * months_to_pay

print(f"Вартість комп'ютера становить: {full_price_in_installments(pay_per_month, months_tp_pay)}")
    
# task 8

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_num = 232
max_page_photo = 8

def calc_min_pages(photo_num, max_page_photo):
    """Calculates the minimum amount of pages needed to put the specified amount of photos."""
    page_num = photo_num // max_page_photo
    if photo_num % max_page_photo > 0:
        page_num = page_num + 1

    return page_num

print(f"{calc_min_pages(photo_num, max_page_photo)} сторінок знадобиться Ігорю, щоб вклеїти всі фото")

# task 9

""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
def calc_words_uppercase(string_to_count_in):
    """Calculates the amount of words starting with the uppercase letter."""
    uppercase_letters_amount = 0
    for i in string_to_count_in:
        if i.isupper():
            uppercase_letters_amount = uppercase_letters_amount + 1

    return uppercase_letters_amount

my_text = """Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним."""
print(f'{calc_words_uppercase(my_text)} слів починається з великої літери' )


# task 10

# task 3. Перевірте, чи є в списку big_list дублікати

def has_duplicates (list_to_check):
    """Returns True if list has duplicates."""
    list_to_check_set = set(list_to_check)
    return len(list_to_check) == len(list_to_check_set)

list_01 = [1, 4, 8, 13, 25, 36, 124]
if has_duplicates(list_01):
    print("В списку нема дублікатів.")
else:
    print("В списку є дублікати.")




"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
