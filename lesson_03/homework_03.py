alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
# my answer:
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\
"That depends a good deal on where you want to get to," said the Cat.\
"I don\'t much care where ——" said Alice.\
"Then it doesn\'t matter which way you go," said the Cat.\
"—— so long as I get somewhere," Alice added as an explanation.\
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'  
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# my answer:
black_sea_area_km2 = 436402
azov_sea_area_km2 = 37800
total_area_km2 = black_sea_area_km2 + azov_sea_area_km2
print("Let's calculate the total area: Area of the Black Sea in km2 + Area of the Azov Sea in km2 = " + str(total_area_km2) + " km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
# my answer:
total_amount = 375291
stores_1_2 = 250449
stores_2_3 = 222950
store_1 = total_amount - stores_2_3
store_2 = stores_1_2 - store_1
store_3 = stores_2_3 - store_2
print(f'''If total_amount = {total_amount}
stores_1_2 = 250449
stores_2_3 = 222950,
then quantity of goods in store 1(total_amount - stores_2_3) = {store_1};
quantity of goods in store 2(stores_1_2 - store_1) = {store_2};
quantity of goods in store 3(stores_2_3 - store_2) = {store_3}.''')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# my answer:
payment_per_month = 1179
quantity_of_month_in_year = 12
months_of_payment = quantity_of_month_in_year * 1.5
print("Let's count what is the price of the computer:payment_per_month X months_of_payment =", months_of_payment * payment_per_month)



# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# my answer:
dividend_a = 8019
divisor_a = 8
remainder_a = dividend_a % divisor_a
dividend_b = 9907
divisor_b = 9
remainder_b = dividend_b % divisor_b
dividend_c = 2789
divisor_c = 5
remainder_c = dividend_c % divisor_c
dividend_d = 7248
divisor_d = 6
remainder_d = dividend_d % divisor_d
dividend_e = 7128
divisor_e = 5
remainder_e = dividend_e % divisor_e
dividend_f = 19224
divisor_f = 9
remainder_f = dividend_f % divisor_f
print(f'''The remainder of dividing {dividend_a} by {divisor_a} is {remainder_a}
The remainder of dividing {dividend_b} by {divisor_b} is {remainder_b}
The remainder of dividing {dividend_c} by {divisor_c} is {remainder_c}
The remainder of dividing {dividend_d} by {divisor_d} is {remainder_d}
The remainder of dividing {dividend_e} by {divisor_e} is {remainder_e}
The remainder of dividing {dividend_f} by {divisor_f} is {remainder_f}''')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# my answer:
big_piza_price = 274
medium_piza_price = 218
juice_price = 35
cake_price = 350
water_price = 21
print(f'''Let's calculate how much money she needs :
big_piza_price X 4 + medium_piza_price X 2 + juice_pric X 4 + cake_price X 1 + water_price X 3
total to pay: {big_piza_price * 4 + medium_piza_price * 2 + juice_price * 4 + cake_price * 1 + water_price * 3}''')
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# my answer:
number_of_fotos = 232
max_fotos_on_page = 8
print(f"How many pages for all fotos: 232/8%8 = {232//8 + 232//8%8}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# my answer:
distance = 1600
liters_per_100_km = 9
tank_capacity = 48
print(f'''1) How many liters of gas we need:1600/100 * 9  = {distance/100 * 9};
2) How many stops at gas station:(1600/100 * 9)/48 = {(distance/100 * 9)/48}''')

