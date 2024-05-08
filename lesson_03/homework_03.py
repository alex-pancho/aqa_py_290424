
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
    '"That depends a good deal on where you want to get to," said the Cat.\n' \
    '"I don\'t much care where ——" said Alice.\n' \
    '"Then it doesn\'t matter which way you go," said the Cat.\n' \
    '"—— so long as I get somewhere," Alice added as an explanation.\n' \
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
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
black_sea_area = 436402
azov_sea_area = 37800
print(f"Площа Чорного та Азовсього морів разом становить: {black_sea_area + azov_sea_area} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_products_num = 375291
first_and_second_products_num = 250449
second_and_third_products_num = 222950
first_products_num = all_products_num - second_and_third_products_num
third_products_num = all_products_num - first_and_second_products_num
second_products_num = all_products_num - (first_products_num + third_products_num)
print(f"Кількість товарів на першому складі: {first_products_num}\n" \
    f"Кількість товарів на другому складі: {second_products_num}\n" \
    f"Кількість товарів на третьому складі: {third_products_num}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
pay_per_month = 1179
months_tp_pay = 18
computer_price = pay_per_month * months_tp_pay
print(f"Вартість комп'ютера становить: {computer_price}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"Залишок від ділення 8019 : 8 становить: {8019 % 8} ")
print(f"Залишок від ділення 9907 : 9 становить: {9907 % 9} ")
print(f"Залишок від ділення 2789 : 5 становить: {2789 % 5} ")
print(f"Залишок від ділення 7248 : 6 становить: {7248 % 6} ")
print(f"Залишок від ділення 7128 : 5 становить: {7128 % 5} ")
print(f"Залишок від ділення 19224 : 9 становить: {19224 % 9} ")

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
grocery_list_amount = [4, 2, 4, 1, 3]
grocery_list_price = [274, 218, 35, 350, 21]
full_price = 0
for i in range(0, 5):
    full_price += grocery_list_amount[i] * grocery_list_price[i]

print(f"Для замовлення Іринки знадобиться: {full_price} грн")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_num = 232
max_page_photo = 8
page_num = photo_num // max_page_photo
if photo_num % max_page_photo > 0:
    page_num = page_num + 1

print(f"{page_num} сторінок знадобиться Ігорю, щоб вклеїти всі фото")

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

travel_distance = 1600
gas_volume_per_100km = 9
gas_storage_volume = 48
gas_amount_for_trip = (travel_distance / 100) * gas_volume_per_100km
min_amount_of_stops = int(gas_amount_for_trip // gas_storage_volume)
if gas_amount_for_trip % gas_storage_volume > 0:
    min_amount_of_stops = min_amount_of_stops + 1
print(f"Для подорожі з Харкова в Будапешт на машині знадобиться: {gas_amount_for_trip} л")
print(f"{min_amount_of_stops} разів щонайменше необхіжно буде родині заїхати на заправку")