# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
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

black_sea_square = 436402
azov_sea_square = 37800
sum_square = black_sea_square + azov_sea_square
print("Площа Чорного та Азовського морів разом займають:", sum_square, "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

sum_sklad1_sklad2_sklad3 = 375291
sum_sklad1_sklad2 = 250449
sum_sklad2_sklad3 = 222950
sklad_1 = sum_sklad1_sklad2_sklad3 - sum_sklad2_sklad3
sklad_2 = sum_sklad1_sklad2 - sklad_1
sklad_3 = sum_sklad2_sklad3 - sklad_2
print("Кількість товарів на першому складі:", sklad_1)
print("Кількість товарів на другому складі:", sklad_2)
print("Кількість товарів на третьому складі:", sklad_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

one_time_payment = 1179
credit_period = 18
computer_price = credit_period * one_time_payment
print("Вартість комп'ютера:", computer_price, "гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("Остача від діленя чисел 8019 і 8 =", a)
print("Остача від діленя чисел 9907 і 9 =", b)
print("Остача від діленя чисел 2789 і 5 =", c)
print("Остача від діленя чисел 7248 і 6 =", d)
print("Остача від діленя чисел 7128 і 5 =", e)
print("Остача від діленя чисел 19224 і 9 =", f)

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

large_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

large_pizza_quantity = 4
medium_pizza_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

total_price = (large_pizza_price * large_pizza_quantity) + \
              (medium_pizza_price * medium_pizza_quantity) + \
              (juice_price * juice_quantity) + \
              (cake_price * cake_quantity) + \
              (water_price * water_quantity)
print("Загальна кількість грошей, яка знадобиться, це:", total_price, "гривень.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

# task 09
all_photos = 232
photos_per_page = 8

quantity_of_pages = all_photos // photos_per_page
if all_photos % photos_per_page != 0:
    quantity_of_pages += 1

print("Ігорю знадобиться", quantity_of_pages, "сторінок, щоб вклеїти всі фото.")

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

Kharkiv_Budapest_distance = 1600
gas_consumption = 9
tank_capacity = 48

required_gas = (Kharkiv_Budapest_distance / 100) * gas_consumption #необхідна кількість бензину
required_refills = required_gas / tank_capacity #кількість заправок
if required_gas % tank_capacity != 0:
    required_refills += 1

print("Для подорожі з Харкова до Будапешта знадобиться", required_gas, "літрів бензину.")
print("Для подорожі з Харкова до Будапешта знадобиться заїхати на заправку", required_refills, "разів.")
