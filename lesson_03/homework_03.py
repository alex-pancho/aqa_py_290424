print("Task 01-03")
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                      '"That depends a good deal on where you want to get to," said the Cat.\n' \
                      '"I don\'t much care where ——" said Alice.\n' \
                      '"Then it doesn\'t matter which way you go," said the Cat.\n' \
                      '"— so long as I get somewhere," Alice added as an explanation.\n' \
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
print("\n", "Task 04")
black_sea = 436402
azov_sea = 37800
both_seas = black_sea + azov_sea
print("\n", "black sea -", black_sea, "km2",
      "\n", "azov sea -", azov_sea, "km2", 
      "\n", "both seas - ?", "\n")

print("1)", black_sea, "+", azov_sea, "=", both_seas, "km2", "(area of ​​both seas)")
print("Answer: the area of ​​both seas is", both_seas, "km2.", "\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\n", "Task 05")
all_warehouses = 375291
warehouse_1_2 = 250449
warehouse_2_3 = 222950
warehouse_1 = all_warehouses - warehouse_2_3
warehouse_3 = all_warehouses - warehouse_1_2
warehouse_1_3 = warehouse_1 + warehouse_3
warehouse_2 = all_warehouses - warehouse_1_3 
print("\n", "all warehouses -", all_warehouses, "products", 
      "\n", "first and second warehouse -", warehouse_1_2, "products", 
      "\n", "second and third warehouse -", warehouse_2_3, "products", 
      "\n", "first warehouse - ?",
      "\n", "second warehouse - ?",
      "\n", "third warehouse - ?")
print("\n", "1)", all_warehouses, "-", warehouse_2_3, "=", warehouse_1, "(products in the first warehouse)",
      "\n", "2)", all_warehouses, "-", warehouse_1_2, "=", warehouse_3, "(products in the third warehouse)",
      "\n", "3)", warehouse_1, "+", warehouse_3, "=", warehouse_1_3, "(products in the first and third warehouse)",
      "\n", "4)", all_warehouses, "-", warehouse_1_3, "=", warehouse_2, "(products in the second warehouse)")
print("Answer: products in the first warehouse -", warehouse_1, 
      "\n", "products in the second warehouse -", warehouse_2, 
      "\n", "products in the third warehouse -", warehouse_3, "\n")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("\n", "Task 06")
month_1 = 1179
year_and_half = 18
cost_of_the_computer = month_1 * year_and_half
print("\n", "payment of one month -", month_1, "UAH", 
      "\n", "year and a half -", year_and_half, "months")
print("\n", "1)", month_1, "*", year_and_half, "=", cost_of_the_computer, "UAH", "(cost of the computer)")
print("Answer: the full price of the computer is UAH", cost_of_the_computer)


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("\n", "Task 07", "\n")
a_1 = 8019 % 8
a_2 = 8016
a_3 = 8
a_4 = 8019
a_5 = a_2 / a_3 
a_6 = a_4 - a_2
print("a)", a_2, ":", a_3, "=", a_5, ",", a_4, "-", a_2, "=", a_1, ",", "remainder =", a_1)
b_1 = 9907 % 9
b_2 = 9900
b_3 = 9
b_4 = 9907
b_5 = b_2 / b_3 
b_6 = b_4 - b_2
print("b)", b_2, ":", b_3, "=", b_5, ",", b_4, "-", b_2, "=", b_1, ",", "remainder =", b_1)
c_1 = 2789 % 5
c_2 = 2785
c_3 = 5
c_4 = 2789
c_5 = c_2 / c_3 
c_6 = c_4 - c_2
print("c)", c_2, ":", c_3, "=", c_5, ",", c_4, "-", c_2, "=", c_1, ",", "remainder =", c_1)
d_1 = 7248 % 6
d_2 = 7248
d_3 = 6
d_4 = d_2 / d_3
print("d)", d_2, ":", d_3, "=", d_4, ",", "remainder =",d_1)
e_1 = 7128 % 5
e_2 = 7125
e_3 = 5
e_4 = 7128
e_5 = e_2 / e_3 
e_6 = e_4 - e_2
print("e)", e_2, ":", e_3, "=", e_5, ",", e_4, "-", e_2, "=", e_1, ",", "remainder =", e_1)
f_1 = 19224 % 9
f_2 = 19224
f_3 = 9
f_4 = f_2 / f_3 
print("f)", f_2, ":", f_3, "=", f_4, ",", "remainder =", f_1)


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
print("\n", "Task 08")
large_pizza_1 = 274
quantity_of_large_pizza = 4
cost_large_pizzas = large_pizza_1 * quantity_of_large_pizza
average_pizza_1 = 218
quantity_of_average_pizza = 2
cost_average_pizzas = average_pizza_1 * quantity_of_average_pizza
juice = 35
quantity_of_juice = 4
cost_juices = juice * quantity_of_juice
cake = 350
water = 21
quantity_of_water = 3
cost_water = water * quantity_of_water
cost_of_everything = cost_large_pizzas + cost_average_pizzas + cost_juices + cake + cost_water
print("\n", "4 large pizzas - ?, 1 pizza", large_pizza_1, "UAH", 
      "\n", "2 average pizzas - ?, 1 pizza", average_pizza_1, "UAH", 
      "\n", "4 juices - ?, 1 juice", juice, "UAH", 
      "\n", "cake -", cake, "UAH", 
      "\n", "3 waters - ?, 1 water", water, "UAH",
      "\n", "cost of everything - ?")
print("\n", "1)", large_pizza_1, "*", quantity_of_large_pizza, "=", cost_large_pizzas, "UAH(cost of 4 large pizzas)", 
     "\n", "2)", average_pizza_1, "*", quantity_of_average_pizza, "=", cost_average_pizzas, "UAH(cost of 2 average pizzas)", 
     "\n", "3)", juice, "*", quantity_of_juice, "=", cost_juices, "UAH(cost of 4 juices)", 
     "\n", "4)", water, "*", quantity_of_water, "=", cost_water, "UAH(cost of 3 water)",
     "\n", "5)", cost_large_pizzas, "+", cost_average_pizzas, "+", cost_juices, "+", cake, "+", cost_water, "=", cost_of_everything, "UAH(cost of everything)")
print("Answer:", cost_of_everything, "UAH are required for the order.")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("\n", "Task 09")
all_photos = 232
page_1 = 8
pages = all_photos / page_1
print("\n", "all photos -", all_photos, 
      "\n", "one page can contain -", page_1, 
      "\n", "number of pages for all photos - ?")
print("\n", "1)", all_photos, ":", page_1, "=", pages, "(number of pages for all photos)")
print("Answer:", pages, "pages are required for all photos.")

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
print("\n", "Task 10")
the_whole_distance = 1600
for_100_km = 9
liters_9 = 100
the_whole_distance_for_100_km = the_whole_distance / liters_9
all_gasoline = the_whole_distance_for_100_km * for_100_km
tank_capacity = 48
visiting_a_gas_station = all_gasoline / tank_capacity
print("\n", "the whole distance -", the_whole_distance, "km", 
      "\n", "It is known - that", for_100_km, "liters of gasoline are needed for every", liters_9, "km", 
      "\n", "tank capacity -", tank_capacity, 
      "\n", "gasoline for the entire trip -?",
      "\n", "visiting a gas station -?")
print("\n", "1)", the_whole_distance, ":", liters_9, "=", the_whole_distance_for_100_km, "(16 times for 100 km)", 
      "\n", "2)", the_whole_distance_for_100_km, "*", for_100_km, "=", all_gasoline, "liters(will need gasoline)", 
      "\n", "3)", all_gasoline, ":", tank_capacity, "=", visiting_a_gas_station, "(visit to gas station)")
print("Answer: you need", all_gasoline, "liters of gasoline for the trip, you have to stop by the gas station", visiting_a_gas_station, "times.")
