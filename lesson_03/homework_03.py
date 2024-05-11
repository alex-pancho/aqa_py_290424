alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n \
"That depends a good deal on where you want to get to," said the Cat.\n \
"I don\'t much care where ——" said Alice.\n "Then it doesn\'t matter which way you go," said the Cat.\n \
"—— so long as I get somewhere," Alice added as an explanation.\n \
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського моря становить 37 800 км2. 
Яку площу займають Чорне та Азовське моря разом?
"""
black_sea = 436_402
azov_sea = 37_800
total_sea_sum = black_sea + azov_sea
print(f'\nTotal square of black and azov sea is equal {total_sea_sum}')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено 375 291 товар. 
На першому та другому складах перебуває 250 449 товарів. 
На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_count = 375_291
first_second_count = 250_449
second_third_count = 222_950

first_stock_count = total_count - second_third_count
third_stock_count = total_count - first_second_count
second_stock_count = total_count - first_stock_count - third_stock_count

print(f'\nFirst stock has {first_stock_count} goods in stock')
print(f'Second stock has {second_stock_count} goods in stock')
print(f'Third stock has {third_stock_count} goods in stock')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами». 
Відомо, що сплачувати необхідно буде півтора року по 1179 грн/місяць. 
Обчисліть вартість комп’ютера.
"""
months_to_pay = int(1.5 * 12)
month_payment = 1179
computer_price = month_payment * months_to_pay

print(f'\nComputer costs {computer_price} UAH in common')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f'\nRemainder of the division 8019 : 8 is equal {8019 % 8}')
print(f'Remainder of the division 9907 : 9 is equal {9907 % 9}')
print(f'Remainder of the division 2789 : 5 is equal {2789 % 5}')
print(f'Remainder of the division 7248 : 6 is equal {7248 % 6}')
print(f'Remainder of the division 7128 : 5 is equal {7128 % 5}')
print(f'Remainder of the division 19224 : 9 is equal {19224 % 9}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того, що їй потрібно замовити. 
Обчисліть, скільки грошей знадобиться для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 274
pizza_middle = 218
juice = 35
cake = 350
water = 21
total_birthday_price = (pizza_big * 4) + (pizza_middle * 2) + (juice * 4) + cake + (water * 3)

print(f'\nIra should pay {total_birthday_price} UAH in common for her birthday')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232 фотографії та вклеїти в альбом. 
На одній сторінці може бути розміщено щонайбільше 8 фото. 
Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото?
"""
total_photo_count = 232
max_photo_per_side = 8
sides_for_all_photo = total_photo_count // max_photo_per_side

print(f'\nIhor should use {sides_for_all_photo} lists for all his photos')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Будапешт. 
Відстань між цими містами становить 1600 км. 
Відомо, що на кожні 100 км необхідно 9 літрів бензину. 
Місткість баку становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак?
"""
distance = 1600
tanks_volume = 48
total_liters_for_trip = (distance // 100) * 9
needs_to_added_petrol = total_liters_for_trip // tanks_volume

print(f'\nFamily should use {total_liters_for_trip} liters of a petrol for a trip')
print(f'Family should add petrol like minimum {needs_to_added_petrol} times while a trip')
