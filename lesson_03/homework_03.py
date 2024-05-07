alice_in_wonderland =  '"Would you tell me, please, which way I ought to go from here?"\n' \
                       '"That depends a good deal on where you want to get to," said the Cat.\n' \
                       '"I don\'t much care where ——" said Alice.\n' \
                       '"Then it doesn\'t matter which way you go," said the Cat.\n \
                       "—— so long as I get somewhere," Alice added as an explanation.\n' \
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


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
black_sea_square = 436_402
azov_sea_square = 37_800
print("The Black Sea and the Sea of Azov together cover " + str(black_sea_square + azov_sea_square) + " km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
warehouse_total = 375_291
warehouse_1_2_combined = 250_449
warehouse_2_3_combined = 222_950
warehouse_1 = warehouse_total - warehouse_2_3_combined
warehouse_3 = warehouse_total - warehouse_1_2_combined
warehouse_2 = warehouse_total - warehouse_1 - warehouse_3
print(f"На першому складі розміщено {warehouse_1} товарів")
print(f"На другому складі розміщено {warehouse_2} товарів")
print(f"На третьому складі розміщено {warehouse_3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
computer_price = 1179 * 18
print(f"Вартість комп'ютера складає {computer_price} грн")

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
print(f"а) 8019 : 8, остача: {a}")
print(f"b) 9907 : 9, остача: {b}")
print(f"c) 2789 : 5, остача: {c}")
print(f"d) 7248 : 6, остача: {d}")
print(f"e) 7128 : 5, остача: {e}")
print(f"f) 19224 : 9, остача: {f}")

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
pizza_large = 274 * 4
pizza_medium = 218 * 2
juice = 35 * 4
cake = 350 * 1
water = 21 * 3
shopping_list_total = pizza_large + pizza_medium + juice + cake + water
print(f"Для оплати замовлення на свій день народження Іринці знадобиться {shopping_list_total} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_total = 232
album_page_fits = 8
album_pages_needed = round(photos_total / album_page_fits)
print(f"Ігорю знадобиться {album_pages_needed} сторінок в альбомі, щоб вклеїти всі фото")

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
distance_kharkiv_budapest = 1600
gas_tank = 48
fuel_usage_per_100km = 9
total_fuel_needed = (distance_kharkiv_budapest / 100) * fuel_usage_per_100km
distance_on_one_tank = (gas_tank / fuel_usage_per_100km) * 100
refuel_stops = round(distance_kharkiv_budapest / distance_on_one_tank)
print(f"Для такої подорожі знадобиться {total_fuel_needed} л бензину")
print(f"Родині необхідно заїхати на заправку щонайменше {refuel_stops} рази")
# якщо на початок подорожі у них був пустий бак
