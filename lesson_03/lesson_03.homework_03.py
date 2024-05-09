#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# #Task 01 - 03
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
#task 04
black_sea_square = 436_402
azov_sea_square = 37_800
sum_square = black_sea_square + azov_sea_square
print(f"Загальна площа Чорного та Азовського морів -  {sum_square} км2. ")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.

"""
# # task 05
all_products = 375_291
warehouse_3 = all_products - 250_449
warehouse_1 = all_products - 222_950
warehouse_2 = all_products - (warehouse_3 + warehouse_1)
print(f"На першому складі розміщено {warehouse_1} товарів, на другому складі - {warehouse_2},"
      f" на третьому - {warehouse_3}.")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# # task 06
monthly_pay = 1179
period = 18
comp_cost = monthly_pay * period
print(f"Вартість комп\'ютера {comp_cost} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# # task 07
print(f"Залишок від ділення:\n"
      f"в прикладі а - {8019 % 7}\n"
      f"в прикладі b - {9907 % 7}\n"
      f"в прикладі с - {2789 % 5}\n"
      f"в прикладі d - {7248 % 6}\n"
      f"в прикладі e - {7128 % 5}\n"
      f"в прикладі f - {19224 % 9}")

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
# # task 08
big_pizza = 274 * 4
middle_pizza = 218 * 2
juice = 35 * 4
cake = 350
water = 21 * 3
all_money = big_pizza + middle_pizza + juice + cake + water
print(f"Вартість замовлення складає всього {all_money} грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# task 09
all_photos = 232
pages = all_photos//8
print(f"Ігорю знадобиться {pages} сторінок, щоб вклеїти всі фото")


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
# task 10
general_distance = 1600
tank_size = 48
petrol_needs = 9 / 100
print(f"Для подорожі необхідно {general_distance*petrol_needs} літрів бензину.\n"
      f"На заправку необхідно заїхати щонайменше {1600/(tank_size/petrol_needs)} рази.")