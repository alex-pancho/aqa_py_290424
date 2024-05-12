alice_in_wonderland = (" Would you tell me, please, which way I ought to go from here?\n"
"\"That depends a good deal on where you want to get to,\" said the Cat.\n"
"\"I don't much care where ——\" said Alice.\n"
"\"Then it doesn't matter which way you go,\" said the Cat.\n"
"\"—— so long as I get somewhere,\" Alice added as an explanation.\n"
"\"Oh, you're sure to do that,\" said the Cat,\"if you only walk long enough.")

alice_in_wonderland = alice_in_wonderland.replace("'", "\\'")
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
black_sea_area = 436402 #км²
azov_sea_area = 37800 #км²

total_area = black_sea_area + azov_sea_area
print("Загальна площа морів:", total_area, "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
first_second_sum = 250449
second_third_sum = 222950
total = 375291
x = total - second_third_sum
y = first_second_sum - x
z = second_third_sum - y

print("товари на першому складі:", x)
print("товари на другому складі:", y)
print("товари на третьому складі:", z)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 18
monthsly_payment = 1179
total_payment = months * monthsly_payment

print(total_payment)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
resalt_a = 8019 % 8
print(resalt_a)

resalt_b = 9907 % 8
print(resalt_b)

resalt_c = 2789 % 8
print(resalt_c)

resalt_d = 19224 % 8
print(resalt_d)

resalt_e = 19128 % 8
print(resalt_e)

resalt_f = 19128 % 8
print(resalt_f)

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
pizza_large_price = 4 * 274
pizza_medium_price = 2 * 218
juce_price = 4 * 35
cake_price = 350
water_price = 3 * 21

total_price = pizza_large_price + juce_price + cake_price + water_price + pizza_medium_price
print(total_price)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
import math
total_photo = 232
photos_per_page = 8
total_pages = math.ceil(total_photo / photos_per_page)

print(total_pages)

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
total_range = 1600
liters_per_100_km = 9
tank_capacity = 48
required_liters = (total_range / 100) * liters_per_100_km
required_gas_stop = required_liters / tank_capacity
required_gas_stop = round(required_gas_stop + 0.5)

print(required_gas_stop)
print(required_liters)